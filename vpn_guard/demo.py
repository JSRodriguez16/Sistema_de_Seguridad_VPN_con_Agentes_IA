from dataclasses import asdict
import random

from .common import write_rows
from .features import Packet, extract


def generate(config, output, seed=42):
    rng = random.Random(seed)
    peers = list(config["peers"])
    server = config["server_ip"]
    seconds = config["window_seconds"]
    base = 1800000000 // seconds * seconds  # Deliberately fixed, not a real capture date.
    train_rows, test_rows, example_packets = [], [], []
    scenarios = [("navegacion", "normal"), ("transferencia_legitima", "normal"),
                 ("escaneo", "anomaly"), ("escaneo_lento", "anomaly")]
    for run in range(16):
        for scenario_index, (scenario, label) in enumerate(scenarios):
            run_id = f"demo-{seed}-{run:02d}-{scenario}"
            packets = []
            for w in range(8):
                peer = peers[(run + w) % len(peers)]
                start = base + (run * 40 + scenario_index * 8 + w) * seconds
                if scenario == "navegacion":
                    count, port_count = rng.randint(15, 120), rng.randint(1, 5)
                elif scenario == "transferencia_legitima":
                    count, port_count = rng.randint(150, 450), rng.randint(1, 3)
                elif scenario == "escaneo":
                    count, port_count = rng.randint(30, 140), rng.randint(22, 100)
                else:
                    # Sparse probes mixed with normal activity challenge short windows.
                    count, port_count = rng.randint(30, 120), rng.randint(2, 8)
                for p in range(count):
                    probe = label == "anomaly" and (scenario != "escaneo_lento" or p == 0 or rng.random() < 0.15)
                    outbound = True if probe and p == 0 else rng.random() < (0.65 if probe else 0.45)
                    port = 1024 + p % port_count if probe else [443, 80, 22, 53, 8080][p % min(port_count, 5)]
                    length = rng.randint(40, 250) if probe else rng.randint(60, 1420)
                    packet = Packet(start + 0.05 + p * (seconds - 0.1) / count,
                                    peer if outbound else server, server if outbound else peer,
                                    45000 if outbound else port, port if outbound else 45000,
                                    length, int(outbound and rng.random() < (0.85 if probe else 0.08)),
                                    int(not outbound and rng.random() < (0.6 if probe else 0.02)))
                    packets.append(packet)
            rows = extract(packets, config, run_id, "synthetic", label, scenario)
            (train_rows if run < 12 else test_rows).extend(rows)
            if run == 15:
                example_packets.extend(asdict(p) for p in packets)
    write_rows(output / "entrenamiento.csv", train_rows)
    write_rows(output / "prueba.csv", test_rows)
    write_rows(output / "paquetes_ejemplo.csv", example_packets)
    return train_rows, test_rows
