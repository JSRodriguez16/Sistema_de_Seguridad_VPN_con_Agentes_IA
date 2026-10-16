from __future__ import annotations

import csv
import json
import math
import os
import queue
import shutil
import subprocess
import threading
import time
import uuid
from dataclasses import asdict

import psutil

from .common import utc_now, write_json
from .features import Aggregator, FEATURES, META, PACKET_FIELDS, Packet
from .model import predict
from .report import PREDICTION_FIELDS, build_report
from .wireguard import collect_status, peer_events

TSHARK_FIELDS = ["frame.time_epoch", "ip.src", "ip.dst", "tcp.srcport", "tcp.dstport",
                 "udp.srcport", "udp.dstport", "ip.len", "tcp.flags.syn", "tcp.flags.ack",
                 "tcp.flags.reset", "ip.proto"]


def parse_tshark(line):
    fields = next(csv.reader([line]))
    if len(fields) != len(TSHARK_FIELDS):
        raise ValueError("Número de campos tshark inesperado")
    timestamp, src, dst, ts, td, us, ud, length, syn, ack, rst, proto = fields
    return Packet.from_row(dict(zip(PACKET_FIELDS, [timestamp, src, dst, ts or us or 0, td or ud or 0,
                                                    length, int(syn == "1" and ack != "1"), int(rst == "1"), proto])))


def monitor(config, output, seconds, artifact=None, label="", scenario="", allow_demo_model=False):
    if os.name != "posix" or not shutil.which("tshark"):
        raise ValueError("La captura real requiere Linux y tshark; use demo en Windows")
    if seconds < 2 * config["window_seconds"]:
        raise ValueError("Capture al menos dos ventanas completas")
    if artifact and artifact["window_seconds"] != config["window_seconds"]:
        raise ValueError("Ventanas del modelo y configuración incompatibles")
    if artifact and "synthetic" in artifact["train_sources"] and not allow_demo_model:
        raise ValueError("Modelo sintético: reentrene con capturas reales o use --allow-demo-model para exploración")
    run_id = str(uuid.uuid4())
    started, cpu_started = time.time(), time.process_time()
    first_full = math.ceil(started / config["window_seconds"]) * config["window_seconds"]
    manifest = {"run_id": run_id, "source": "real", "started_at": utc_now(), "requested_seconds": seconds,
                "label": label, "scenario": scenario, "config": config, "state": "running",
                "model_training_sources": artifact["train_sources"] if artifact else []}
    write_json(output / "manifest.json", manifest)
    args = ["tshark", "-l", "-n", "-i", config["interface"], "-a", f"duration:{seconds}",
            "-f", "ip and (" + " or ".join(f"host {ip}" for ip in config["peers"]) + ")",
            "-T", "fields", "-E", "separator=,", "-E", "quote=d", "-E", "occurrence=f"]
    for field in TSHARK_FIELDS:
        args.extend(["-e", field])
    pending = queue.Queue(maxsize=10000)
    overflow = [0]
    done = threading.Event()
    aggregate = Aggregator(config, run_id, "real", label, scenario)
    predictions = []
    invalid, partial = 0, 0
    rss_peak = psutil.Process().memory_info().rss
    previous = {}
    next_status = started
    interrupted = False
    failure = None
    forced_stop = False
    with (output / "captura.stderr.log").open("w", encoding="utf-8") as stderr, \
            (output / "paquetes.csv").open("w", newline="", encoding="utf-8") as raw, \
            (output / "ventanas.csv").open("w", newline="", encoding="utf-8") as features, \
            (output / "predicciones_en_vivo.csv").open("w", newline="", encoding="utf-8") as predicted, \
            (output / "alertas_en_vivo.jsonl").open("w", encoding="utf-8") as alerts, \
            (output / "estado_vpn.jsonl").open("w", encoding="utf-8") as states, \
            (output / "eventos_vpn.jsonl").open("w", encoding="utf-8") as events:
        raw_writer = csv.DictWriter(raw, fieldnames=PACKET_FIELDS)
        feature_writer = csv.DictWriter(features, fieldnames=META + FEATURES)
        pred_writer = csv.DictWriter(predicted, fieldnames=PREDICTION_FIELDS)
        for writer in (raw_writer, feature_writer, pred_writer):
            writer.writeheader()
        try:
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=stderr, text=True, bufsize=1)
        except OSError as exc:
            manifest.update(state="failed", error=str(exc), ended_at=utc_now())
            write_json(output / "manifest.json", manifest)
            raise ValueError(f"No se pudo iniciar tshark: {exc}") from exc

        def reader():
            try:
                for line in process.stdout:
                    try:
                        pending.put_nowait(line)
                    except queue.Full:
                        overflow[0] += 1
            finally:
                done.set()

        def emit(rows):
            feature_writer.writerows(rows)
            batch = predict(rows, config, artifact)
            predictions.extend(batch)
            pred_writer.writerows(batch)
            for row in batch:
                if row["alert"]:
                    alerts.write(json.dumps(row, ensure_ascii=False) + "\n")
                    print(f"ALERTA {row['peer_name']}: {row['reasons']}", flush=True)
            for stream in (raw, features, predicted, alerts):
                stream.flush()

        thread = threading.Thread(target=reader, daemon=True)
        thread.start()
        try:
            while time.time() < started + seconds + 5:
                try:
                    line = pending.get(timeout=0.2)
                    try:
                        packet = parse_tshark(line)
                        raw_writer.writerow(asdict(packet))
                        if packet.timestamp >= first_full:
                            aggregate.add(packet)
                        else:
                            partial += 1
                    except (ValueError, KeyError):
                        invalid += 1
                except queue.Empty:
                    pass
                if pending.empty():
                    emit(aggregate.flush(time.time() - 1))
                if time.time() >= next_status:
                    current = collect_status(config)
                    states.write(json.dumps(current, ensure_ascii=False) + "\n")
                    for event in peer_events(previous, current):
                        events.write(json.dumps(event, ensure_ascii=False) + "\n")
                    states.flush()
                    events.flush()
                    previous = current
                    next_status = time.time() + config["window_seconds"]
                    rss_peak = max(rss_peak, psutil.Process().memory_info().rss)
                if done.is_set() and pending.empty():
                    break
        except KeyboardInterrupt:
            interrupted = True
        except Exception as exc:
            failure = f"{type(exc).__name__}: {exc}"
        finally:
            if process.poll() is None:
                forced_stop = not interrupted and failure is None
                process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
            thread.join(timeout=2)
            process.stdout.close()
            ended = min(time.time(), started + seconds)
            emit(aggregate.flush(math.floor(ended / config["window_seconds"]) * config["window_seconds"]))
    elapsed = time.time() - started
    diagnostics = {"elapsed_seconds": elapsed, "agent_cpu_seconds": time.process_time() - cpu_started,
                   "agent_rss_peak_sampled_mb": rss_peak / 1024**2,
                   "queue_dropped_packets": overflow[0], "invalid_packets": invalid,
                   "late_packets": aggregate.late_packets, "ignored_packets": aggregate.ignored_packets,
                   "initial_partial_packets_excluded": partial, "final_partial_peer_windows_excluded": len(aggregate.windows),
                   "tshark_exit_code": process.returncode, "interrupted": interrupted,
                   "forced_stop": forced_stop, "unprocessed_queue_packets": pending.qsize(),
                   "error": failure, "last_vpn_status": previous,
                   "resource_scope": "Solo agente Python; tshark/kernel excluidos. Ver captura.stderr.log para pérdidas del capturador."}
    failed = bool(failure or forced_stop or (process.returncode != 0 and not interrupted))
    state = "failed" if failed else ("interrupted" if interrupted else ("finished" if predictions else "no_data"))
    manifest.update({"ended_at": utc_now(), "state": state,
                     "interrupted": interrupted, "diagnostics": diagnostics})
    write_json(output / "manifest.json", manifest)
    build_report(predictions, output, config, artifact, diagnostics)
    if failed:
        raise ValueError(f"Captura fallida; consulte {output / 'captura.stderr.log'} y manifest.json")
    return {"output": str(output), "run_id": run_id, "windows": len(predictions), "state": manifest["state"]}
