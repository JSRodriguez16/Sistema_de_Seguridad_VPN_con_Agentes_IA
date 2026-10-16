from __future__ import annotations

import csv
import ipaddress
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False), encoding="utf-8")


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as stream:
        return list(csv.DictReader(stream))


def write_rows(path, rows, fields=None):
    rows = list(rows)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields or (list(rows[0]) if rows else []))
        writer.writeheader()
        writer.writerows(rows)


def load_config(path):
    config = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,15}", config["interface"]):
        raise ValueError("Nombre de interfaz inválido")
    ipaddress.IPv4Address(config["server_ip"])
    if not isinstance(config["peers"], dict) or not config["peers"]:
        raise ValueError("Configure al menos un peer")
    for address in config["peers"]:
        ipaddress.IPv4Address(address)
        if address == config["server_ip"]:
            raise ValueError("Un peer no puede tener la IP del servidor")
    for name in ("window_seconds", "scan_ports_threshold", "high_rate_bytes_per_second", "handshake_recent_seconds"):
        value = float(config[name])
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} debe ser positivo y finito")
    if not 0 < config["probability_threshold"] < 1:
        raise ValueError("probability_threshold debe estar entre 0 y 1")
    return config


def new_output(path):
    path = Path(path)
    if path.exists() and any(path.iterdir()):
        raise ValueError(f"El directorio {path} ya contiene archivos; use otro nombre de corrida")
    path.mkdir(parents=True, exist_ok=True)
    return path
