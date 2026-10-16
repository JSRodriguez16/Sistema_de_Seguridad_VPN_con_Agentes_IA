from __future__ import annotations

from collections import Counter
from html import escape
from pathlib import Path
import json
import statistics

from .common import utc_now, write_json, write_rows
from .features import FEATURES, META
from .model import metrics

PREDICTION_FIELDS = META + FEATURES + ["probability", "ml_alert", "rule_alert", "alert", "reasons", "inference_ms"]


def build_report(rows, output, config, artifact=None, diagnostics=None, evaluation="observacion"):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    alerts = [row for row in rows if int(row["alert"])]
    errors = [row for row in rows if row.get("label") in ("normal", "anomaly")
              and int(row["alert"]) != int(row["label"] == "anomaly")]
    times = sorted(float(row["inference_ms"]) for row in rows)
    source = sorted({row["source"] for row in rows})
    summary = {
        "generated_at": utc_now(), "source": source, "evaluation": evaluation,
        "synthetic_warning": "Datos simulados; no validan seguridad, cifrado, QoS ni precisión real." if "synthetic" in source else None,
        "windows": len(rows), "alerts": len(alerts), "errors": len(errors),
        "config": config, "detector": "RandomForest + reglas" if artifact else "Solo reglas; sin modelo IA",
        "model_training_sources": artifact["train_sources"] if artifact else [],
        "model_identity": {key: artifact[key] for key in ("created_at", "train_features_sha256", "versions")} if artifact else None,
        "metrics_combined": metrics(rows), "metrics_rules": metrics(rows, "rule_alert"),
        "metrics_ml": metrics(rows, "ml_alert") if artifact else None,
        "inference_ms_mean": statistics.mean(times) if times else None,
        "inference_ms_p95": times[min(len(times) - 1, int(0.95 * len(times)))] if times else None,
        "scenarios": {s: metrics([r for r in rows if r.get("scenario", "") == s])
                      for s in sorted({r.get("scenario", "") for r in rows})},
        "peer_windows": dict(Counter(row["peer_name"] for row in rows)),
        "diagnostics": diagnostics or {},
    }
    write_json(output / "metricas.json", summary)
    write_rows(output / "predicciones.csv", rows, PREDICTION_FIELDS)
    write_rows(output / "errores.csv", errors, PREDICTION_FIELDS)
    with (output / "alertas.jsonl").open("w", encoding="utf-8") as stream:
        for row in alerts:
            stream.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + "\n")
    def fmt(value):
        return "No calculable" if value is None else f"{value:.3f}"
    def e(value):
        return escape(str(value))
    m = summary["metrics_combined"]
    cards = "".join(f'<div class="card"><small>{name}</small><strong>{value}</strong></div>' for name, value in [
        ("Ventanas", len(rows)), ("Alertas", len(alerts)), ("F1 combinado", fmt(m["f1"])),
        ("Falsas alarmas / normales", fmt(m["false_positive_rate"])),
        ("Inferencia p95 (ms)", fmt(summary["inference_ms_p95"]))])
    metric_rows = "".join(f'<tr><th>{name}</th>' + "".join(f'<td>{fmt(item[key])}</td>' for key in ("accuracy", "precision", "recall", "f1", "false_positive_rate")) + '</tr>'
                          for name, item in [("IA", summary["metrics_ml"]), ("Reglas", summary["metrics_rules"]), ("IA o reglas", m)] if item)
    cm = m["confusion_matrix"]
    confusion = (f'<table><tr><th>Real / Predicción</th><th>Normal</th><th>Alerta</th></tr><tr><th>Normal</th><td>TN {cm["TN"]}</td><td>FP {cm["FP"]}</td></tr><tr><th>Anomalía</th><td>FN {cm["FN"]}</td><td>TP {cm["TP"]}</td></tr></table>'
                 if cm else '<p>Sin etiquetas verificadas: no se calculan métricas de clasificación.</p>')
    sample = errors[:30] if errors else alerts[:30]
    sample_rows = "".join('<tr>' + ''.join(f'<td>{e(row.get(key, ""))}</td>' for key in ["peer_name", "window_start", "label", "alert", "reasons"]) + '</tr>' for row in sample)
    # Standalone SVG: no external services, scripts, libraries or fonts.
    bins = {}
    for row in rows:
        start = float(row["window_start"])
        bins.setdefault(start, [0, 0])
        bins[start][0] += 1
        bins[start][1] += int(row["alert"])
    points = sorted(bins.items())
    bars = []
    for i, (_, (total, flagged)) in enumerate(points):
        width = 880 / max(1, len(points))
        height = 130 * flagged / total
        bars.append(f'<rect x="{30 + i * width:.2f}" y="{150-height:.2f}" width="{max(.2,width-.5):.2f}" height="{height:.2f}" fill="#ffb86b"/>')
    chart = '<svg viewBox="0 0 940 185" role="img" aria-label="Proporción de alertas por ventana temporal"><text x="30" y="15" fill="#c9d4e4">100%</text><path d="M30 150 H915" stroke="#62748d"/>' + ''.join(bars) + '<text x="30" y="175" fill="#c9d4e4">Ventanas en orden temporal →</text></svg>'
    warning = summary["synthetic_warning"] or "Captura real. Una alerta indica un patrón sospechoso; su etiqueta debe confirmarse en el experimento."
    if not rows:
        warning = "Sin ventanas completas para analizar. Revise tráfico, interfaz, duración y errores de captura; no hay evidencia para evaluar detección."
    if artifact and "synthetic" in artifact["train_sources"] and "synthetic" not in source:
        warning += " ATENCIÓN: modelo entrenado con datos sintéticos; resultados exploratorios."
    page = f'''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diagnóstico VPN</title><style>
:root{{color-scheme:dark}}*{{box-sizing:border-box}}body{{margin:0;background:#0d1522;color:#edf3fc;font:16px/1.5 system-ui,sans-serif}}main{{max-width:1180px;margin:auto;padding:38px 24px}}h1{{font-size:36px;margin:8px 0}}h2{{font-size:22px;margin-top:32px}}p,small{{color:#b9c7da}}.tag{{color:#80e1ce;letter-spacing:.12em;font-size:12px}}.notice{{border-left:4px solid #ffb86b;padding:14px 20px;background:#242333}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:12px;margin:24px 0}}.card{{padding:18px;background:#172437;border-radius:10px}}strong{{display:block;font-size:28px;color:#80e1ce}}table{{width:100%;border-collapse:collapse}}td,th{{text-align:left;padding:12px;border-bottom:1px solid #304056}}th{{color:#91a9c7}}.scroll{{overflow:auto}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;background:#172437;padding:20px}}a{{color:#80e1ce}}svg{{width:100%;background:#172437;border-radius:10px}}footer{{margin-top:36px;color:#91a9c7}}
</style><main><div class="tag">WIREGUARD / LABORATORIO SOHO</div><h1>Diagnóstico de seguridad VPN</h1>
<p>{e(summary['detector'])} · {e(evaluation)} · {e(summary['generated_at'])}</p><div class="notice">{e(warning)}</div>{cards}
<h2>Calidad de detección</h2><p>Unidad de evaluación: un dispositivo en una ventana de {e(config['window_seconds'])} segundos. Clase positiva: anomalía. Las probabilidades del bosque no están calibradas.</p>
<div class="scroll"><table><tr><th>Detector</th><th>Accuracy</th><th>Precision</th><th>Recall</th><th>F1</th><th>FPR</th></tr>{metric_rows}</table></div>
<h2>Matriz de confusión del sistema combinado</h2>{confusion}<h2>Alertas en el tiempo</h2>{chart}
<h2>{'Errores para revisar' if errors else 'Muestra de alertas'}</h2><p>Hasta 30 registros. Los CSV contienen todos los registros.</p><div class="scroll"><table><tr><th>Dispositivo</th><th>Inicio Unix</th><th>Etiqueta real</th><th>Alerta</th><th>Evidencia</th></tr>{sample_rows}</table></div>
<h2>Diagnóstico operativo</h2><pre>{e(json.dumps(diagnostics or {}, indent=2, ensure_ascii=False))}</pre>
<h2>Cómo interpretar</h2><p>FP: actividad normal marcada. FN: anomalía que pasó sin alerta. Si no hay anomalías etiquetadas, Recall no es calculable. Un volumen alto también puede ser una transferencia legítima. Los motivos describen reglas y la decisión del modelo, no prueban un ataque.</p>
<p>La latencia de inferencia excluye el tiempo de acumular la ventana. El handshake indica actividad criptográfica reciente; no certifica una sesión conectada. Este reporte no mide por sí solo cifrado, rendimiento del túnel ni efectividad de QoS.</p>
<footer><a href="metricas.json">Métricas JSON</a> · <a href="predicciones.csv">Todas las predicciones</a> · <a href="errores.csv">Errores CSV</a> · <a href="alertas.jsonl">Alertas JSONL</a></footer></main></html>'''
    (output / "reporte.html").write_text(page, encoding="utf-8")
    return summary
