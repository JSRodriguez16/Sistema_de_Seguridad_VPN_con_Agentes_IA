from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from .common import load_config, new_output, read_rows, write_json, write_rows
from .features import FEATURES, META, Packet, extract


def parser():
    root = argparse.ArgumentParser(description="Laboratorio VPN WireGuard: captura, IA y diagnóstico")
    root.add_argument("--config", default="config/lab.json", help="Configuración JSON del laboratorio")
    commands = root.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo", help="Demo reproducible sin enviar tráfico ni activar VPN")
    demo.add_argument("--output", default="resultados/demo")
    demo.add_argument("--seed", type=int, default=42)
    train = commands.add_parser("train", help="Entrenar y evaluar con corridas independientes")
    train.add_argument("--train", nargs="+", required=True, help="CSV de ventanas de entrenamiento")
    train.add_argument("--test", nargs="+", required=True, help="CSV de ventanas de prueba independientes")
    train.add_argument("--output", required=True)
    train.add_argument("--seed", type=int, default=42)
    evaluate = commands.add_parser("evaluate", help="Evaluar un modelo con capturas etiquetadas nuevas")
    evaluate.add_argument("--model", required=True)
    evaluate.add_argument("--input", nargs="+", required=True)
    evaluate.add_argument("--output", required=True)
    replay = commands.add_parser("analyze", help="Analizar ventanas CSV; etiquetas opcionales")
    replay.add_argument("--model")
    replay.add_argument("--input", nargs="+", required=True)
    replay.add_argument("--output", required=True)
    extraction = commands.add_parser("extract", help="Extraer ventanas desde CSV de metadatos de paquetes")
    extraction.add_argument("--input", required=True)
    extraction.add_argument("--output", required=True)
    extraction.add_argument("--run-id", required=True, help="Conserve el ID original si reextrae una captura")
    extraction.add_argument("--source", choices=["real", "synthetic"], required=True)
    extraction.add_argument("--label", choices=["normal", "anomaly"], default="")
    extraction.add_argument("--scenario", default="")
    monitor = commands.add_parser("monitor", help="Captura y alertas continuas en el servidor Linux")
    monitor.add_argument("--output", required=True)
    monitor.add_argument("--seconds", type=int, default=120, help="Duración máxima de esta corrida")
    monitor.add_argument("--model")
    monitor.add_argument("--label", choices=["normal", "anomaly"], default="")
    monitor.add_argument("--scenario", default="")
    monitor.add_argument("--allow-demo-model", action="store_true")
    doctor = commands.add_parser("doctor", help="Revisar herramientas, peers y contadores QoS sin modificar red")
    doctor.add_argument("--output")
    vpn = commands.add_parser("init-vpn", help="Generar configuraciones y claves con wg (no activa la red)")
    vpn.add_argument("--endpoint", required=True, help="DNS-o-IPv4:puerto alcanzable por el cliente")
    vpn.add_argument("--clients", type=int, default=2)
    vpn.add_argument("--output", default="private")
    performance = commands.add_parser("performance", help="Resumir mediciones reales de iperf3")
    performance.add_argument("--input", nargs="+", required=True)
    performance.add_argument("--output", required=True)
    return root


def combine(paths):
    return [row for path in paths for row in read_rows(path)]


def run(args):
    if args.command == "performance":
        from .performance import summarize
        return summarize(args.input, new_output(args.output))
    if args.command == "init-vpn":
        from .wireguard import init_vpn
        return init_vpn(args.endpoint, args.clients, args.output)
    config = load_config(args.config)
    if args.command == "doctor":
        from .wireguard import doctor
        result = doctor(config)
        if args.output:
            write_json(args.output, result)
        return result
    if args.command == "extract":
        if Path(args.output).exists():
            raise ValueError("El CSV de salida ya existe; use otro nombre")
        packets = [Packet.from_row(row) for row in read_rows(args.input)]
        rows = extract(packets, config, args.run_id, args.source, args.label, args.scenario)
        write_rows(args.output, rows, META + FEATURES)
        return {"windows": len(rows), "output": args.output,
                "note": "Extracción offline: ventanas de los bordes pueden ser parciales; use monitor para excluirlas."}
    from .model import check_holdout, load_model, predict, save_model, train
    from .report import build_report
    if args.command in ("demo", "train"):
        output = new_output(args.output)
        started = time.perf_counter()
        if args.command == "demo":
            from .demo import generate
            training, testing = generate(config, output, args.seed)
        else:
            training, testing = combine(args.train), combine(args.test)
        artifact = train(training, args.seed)
        check_holdout(artifact, testing)
        predictions = predict(testing, config, artifact)
        save_model(artifact, output / "modelo.joblib")
        write_json(output / "modelo_metadata.json", {k: v for k, v in artifact.items() if k != "pipeline"})
        report = build_report(predictions, output, config, artifact,
                              {"pipeline_elapsed_seconds": time.perf_counter() - started,
                               "train_windows": len(training), "test_windows": len(testing),
                               "train_runs": sorted({r["run_id"] for r in training}),
                               "test_runs": sorted({r["run_id"] for r in testing}),
                               "split": "Corridas completas independientes; normalización ajustada solo en entrenamiento"},
                              evaluation="prueba independiente")
        return {"output": str(output.resolve()), "source": report["source"],
                "windows": report["windows"], "metrics": report["metrics_combined"],
                "notice": report["synthetic_warning"]}
    artifact = load_model(args.model) if args.model else None
    if args.command == "monitor":
        from .capture import monitor
        return monitor(config, new_output(args.output), args.seconds, artifact,
                       args.label, args.scenario, args.allow_demo_model)
    rows = combine(args.input)
    if args.command == "evaluate":
        check_holdout(artifact, rows)
    output = new_output(args.output)
    report = build_report(predict(rows, config, artifact), output, config, artifact,
                          evaluation="prueba independiente" if args.command == "evaluate" else "observacion (puede incluir entrenamiento)")
    return {"output": str(output.resolve()), "windows": report["windows"], "metrics": report["metrics_combined"]}


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        result = run(args)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (ValueError, OSError, KeyError, ImportError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
