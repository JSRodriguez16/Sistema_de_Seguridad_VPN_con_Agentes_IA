from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from pathlib import Path

from .common import new_output, utc_now, write_json


def command(args, timeout=8):
    return subprocess.run(args, check=True, capture_output=True, text=True, timeout=timeout).stdout


def collect_status(config):
    """Never use `wg show dump`: it includes private and preshared keys."""
    result = {"at": utc_now(), "interface": config["interface"], "peers": [], "errors": []}
    now = time.time()
    try:
        data = {}
        for field in ("latest-handshakes", "transfer", "endpoints", "allowed-ips"):
            for line in command(["wg", "show", config["interface"], field]).splitlines():
                key, *values = line.split("\t")
                data.setdefault(key, {})[field] = values
        for key, fields in data.items():
            handshake = int(fields.get("latest-handshakes", ["0"])[0])
            rx, tx = map(int, fields.get("transfer", ["0", "0"]))
            age = max(0, now - handshake) if handshake else None
            result["peers"].append({
                "public_key": key, "allowed_ips": fields.get("allowed-ips", []),
                "endpoint": fields.get("endpoints", ["(none)"])[0],
                "handshake_age_seconds": age, "rx_bytes": rx, "tx_bytes": tx,
                "state": "never" if age is None else ("recent" if age <= config["handshake_recent_seconds"] else "stale"),
            })
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        result["errors"].append(f"WireGuard: {type(exc).__name__}: {exc}")
    try:
        result["qos_classes"] = command(["tc", "-s", "class", "show", "dev", config["interface"]])
        result["qos_qdisc"] = command(["tc", "-s", "qdisc", "show", "dev", config["interface"]])
    except (OSError, subprocess.SubprocessError) as exc:
        result["errors"].append(f"QoS: {type(exc).__name__}: {exc}")
    result["limitations"] = "recent/stale/never describen el handshake, no una conexión TCP ni un registro de autenticación rechazada."
    return result


def peer_events(previous, current):
    before = {peer["public_key"]: peer for peer in previous.get("peers", [])}
    events = []
    for peer in current["peers"]:
        old = before.pop(peer["public_key"], None)
        if old is None or old["state"] != peer["state"]:
            events.append({"at": current["at"], "public_key": peer["public_key"],
                           "event": "handshake_state", "previous": old["state"] if old else "unobserved",
                           "state": peer["state"], "allowed_ips": peer["allowed_ips"]})
        if old and (peer["rx_bytes"] < old["rx_bytes"] or peer["tx_bytes"] < old["tx_bytes"]):
            events.append({"at": current["at"], "public_key": peer["public_key"], "event": "counter_reset"})
    if not current["errors"]:
        for key in before:
            events.append({"at": current["at"], "public_key": key, "event": "peer_removed"})
    return events


def doctor(config):
    return {"at": utc_now(), "platform": os.name,
            "tools": {name: shutil.which(name) for name in ("wg", "wg-quick", "tshark", "tc", "iptables", "iperf3")},
            "vpn": collect_status(config),
            "note": "VPN y QoS requieren Linux. La demo y el análisis CSV funcionan también en Windows."}


def init_vpn(endpoint, clients, output):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]*:[0-9]{1,5}", endpoint):
        raise ValueError("Use endpoint DNS-o-IPv4:puerto; este prototipo es IPv4")
    port = int(endpoint.rsplit(":", 1)[1])
    if not 1 <= port <= 65535 or not 1 <= clients <= 10:
        raise ValueError("Puerto 1..65535 y entre 1 y 10 clientes")
    if not shutil.which("wg"):
        raise ValueError("Instale wireguard-tools en Linux para generar claves con wg")
    output = new_output(output)
    if os.name == "posix":
        output.chmod(0o700)

    def keys():
        private = command(["wg", "genkey"]).strip()
        public = subprocess.run(["wg", "pubkey"], input=private + "\n", check=True,
                                capture_output=True, text=True, timeout=8).stdout.strip()
        if not all(re.fullmatch(r"[A-Za-z0-9+/]{43}=", key) for key in (private, public)):
            raise ValueError("wg devolvió una clave inválida")
        return private, public

    def secret_file(name, content):
        descriptor = os.open(output / name, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)

    server_private, server_public = keys()
    server = f"[Interface]\nAddress = 10.77.0.1/24\nListenPort = {port}\nPrivateKey = {server_private}\nMTU = 1420\n"
    inventory = {}
    for index in range(1, clients + 1):
        private, public = keys()
        address = f"10.77.0.{index + 1}"
        server += f"\n[Peer]\n# cliente-{index}\nPublicKey = {public}\nAllowedIPs = {address}/32\n"
        secret_file(f"cliente-{index}.conf", f"[Interface]\nAddress = {address}/32\nPrivateKey = {private}\nMTU = 1420\n\n[Peer]\nPublicKey = {server_public}\nEndpoint = {endpoint}\nAllowedIPs = 10.77.0.1/32\nPersistentKeepalive = 25\n")
        inventory[address] = f"cliente-{index}"
    secret_file("wg0.conf", server)
    write_json(output / "lab.json", {"interface": "wg0", "server_ip": "10.77.0.1", "peers": inventory,
                                    "window_seconds": 10, "probability_threshold": 0.65,
                                    "scan_ports_threshold": 20, "high_rate_bytes_per_second": 1000000,
                                    "handshake_recent_seconds": 180})
    return {"output": str(output), "clients": clients, "endpoint": endpoint,
            "note": "Claves generadas localmente. Configuraciones creadas; túnel todavía no activado."}
