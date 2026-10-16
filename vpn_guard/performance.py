import json
import statistics
from pathlib import Path

from .common import write_json, write_rows


def summarize(paths, output):
    rows = []
    for name in paths:
        path = Path(name)
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        if data.get("error"):
            raise ValueError(f"iperf3 falló en {path}: {data['error']}")
        received = data.get("end", {}).get("sum_received") or data.get("end", {}).get("sum")
        if not received or "bits_per_second" not in received:
            raise ValueError(f"No hay resultado de recepción completo en {path}")
        sent = data["end"].get("sum_sent", {})
        rows.append({"run": path.parent.name, "stream": path.stem,
                     "mbps": received["bits_per_second"] / 1e6,
                     "seconds": received.get("seconds", ""),
                     "bytes": received.get("bytes", ""),
                     "retransmits": sent.get("retransmits", ""),
                     "jitter_ms": received.get("jitter_ms", ""),
                     "lost_percent": received.get("lost_percent", ""),
                     "input": str(path)})
    if not rows:
        raise ValueError("Proporcione archivos JSON de iperf3")
    write_rows(output / "rendimiento.csv", rows)
    summary = {"source": "mediciones iperf3 importadas", "samples": len(rows),
               "streams": {stream: {"n": len(values), "mean_mbps": statistics.mean(values),
                                     "std_mbps": statistics.stdev(values) if len(values) > 1 else None}
                           for stream in sorted({r["stream"] for r in rows})
                           for values in [[r["mbps"] for r in rows if r["stream"] == stream]]},
               "note": "Compare resúmenes separados sin/con QoS; revise ping.txt y contadores tc. Un solo ensayo no prueba mejora."}
    write_json(output / "rendimiento.json", summary)
    return summary
