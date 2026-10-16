from __future__ import annotations

import ipaddress
import math
from dataclasses import dataclass, field

FEATURES = [
    "packets", "bytes", "packets_per_second", "bytes_per_second",
    "mean_packet_bytes", "std_packet_bytes", "mean_iat_ms", "std_iat_ms",
    "active_seconds", "unique_dst_ports", "unique_dst_ips", "syn_ratio",
    "rst_ratio", "outbound_ratio",
]
META = ["run_id", "source", "peer_ip", "peer_name", "window_start", "window_seconds", "label", "scenario"]
PACKET_FIELDS = ["timestamp", "src_ip", "dst_ip", "src_port", "dst_port", "length", "syn", "rst", "protocol"]


@dataclass(frozen=True)
class Packet:
    timestamp: float
    src_ip: str
    dst_ip: str
    src_port: int
    dst_port: int
    length: int
    syn: int = 0
    rst: int = 0
    protocol: int = 6

    @classmethod
    def from_row(cls, row):
        packet = cls(float(row["timestamp"]), row["src_ip"], row["dst_ip"],
                     int(row["src_port"] or 0), int(row["dst_port"] or 0),
                     int(row["length"]), int(row["syn"] or 0), int(row["rst"] or 0),
                     int(row["protocol"]))
        ipaddress.IPv4Address(packet.src_ip)
        ipaddress.IPv4Address(packet.dst_ip)
        if (not math.isfinite(packet.timestamp) or packet.timestamp < 0
                or not 20 <= packet.length <= 65535
                or not all(0 <= p <= 65535 for p in (packet.src_port, packet.dst_port))
                or packet.syn not in (0, 1) or packet.rst not in (0, 1)
                or not 0 <= packet.protocol <= 255):
            raise ValueError("Metadatos de paquete fuera de rango")
        return packet


@dataclass
class Moments:
    count: int = 0
    mean: float = 0
    m2: float = 0

    def add(self, value):
        self.count += 1
        delta = value - self.mean
        self.mean += delta / self.count
        self.m2 += delta * (value - self.mean)

    @property
    def std(self):
        return math.sqrt(max(0, self.m2 / self.count)) if self.count else 0


@dataclass
class Window:
    sizes: Moments = field(default_factory=Moments)
    iats: Moments = field(default_factory=Moments)
    total_bytes: int = 0
    outbound: int = 0
    syn: int = 0
    rst: int = 0
    first: float | None = None
    last: float | None = None
    ports: set = field(default_factory=set)
    targets: set = field(default_factory=set)

    def add(self, packet, outbound):
        if self.last is not None and packet.timestamp < self.last:
            raise ValueError("Paquetes fuera de orden temporal; ordene la captura antes de extraer")
        if self.first is None:
            self.first = packet.timestamp
        if self.last is not None:
            self.iats.add((packet.timestamp - self.last) * 1000)
        self.last = packet.timestamp
        self.sizes.add(packet.length)
        self.total_bytes += packet.length
        self.rst += packet.rst
        if outbound:
            self.outbound += 1
            self.syn += packet.syn
            if packet.protocol in (6, 17) and packet.dst_port:
                self.ports.add(packet.dst_port)
            # Bound memory under extreme cardinality; count saturates at 4096.
            if len(self.targets) < 4096:
                self.targets.add(packet.dst_ip)

    def features(self, seconds):
        count = self.sizes.count
        return dict(zip(FEATURES, [
            count, self.total_bytes, count / seconds, self.total_bytes / seconds,
            self.sizes.mean, self.sizes.std, self.iats.mean, self.iats.std,
            self.last - self.first, len(self.ports), len(self.targets),
            self.syn / max(self.outbound, 1), self.rst / count, self.outbound / count,
        ]))


class Aggregator:
    def __init__(self, config, run_id, source="real", label="", scenario=""):
        if label not in ("", "normal", "anomaly"):
            raise ValueError("label debe ser normal, anomaly o vacío")
        self.config, self.run_id, self.source = config, run_id, source
        self.label, self.scenario = label, scenario
        self.windows = {}
        self.ignored_packets = 0
        self.late_packets = 0
        self.closed_before = -1

    def add(self, packet):
        seconds = self.config["window_seconds"]
        start = math.floor(packet.timestamp / seconds) * seconds
        if start + seconds <= self.closed_before:
            self.late_packets += 1
            return
        peers = self.config["peers"]
        involved = [ip for ip in (packet.src_ip, packet.dst_ip) if ip in peers]
        if not involved:
            self.ignored_packets += 1
        for ip in dict.fromkeys(involved):
            self.windows.setdefault((start, ip), Window()).add(packet, ip == packet.src_ip)

    def flush(self, until=float("inf")):
        rows = []
        seconds = self.config["window_seconds"]
        for (start, peer) in sorted(list(self.windows)):
            if start + seconds <= until:
                window = self.windows.pop((start, peer))
                rows.append({"run_id": self.run_id, "source": self.source,
                             "peer_ip": peer, "peer_name": self.config["peers"][peer],
                             "window_start": start, "window_seconds": seconds,
                             "label": self.label, "scenario": self.scenario,
                             **window.features(seconds)})
        self.closed_before = max(self.closed_before, until)
        return rows


def extract(packets, config, run_id, source="real", label="", scenario=""):
    collector = Aggregator(config, run_id, source, label, scenario)
    for packet in packets:
        collector.add(packet)
    return collector.flush()
