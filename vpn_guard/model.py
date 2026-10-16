from __future__ import annotations

import hashlib
import math
import platform
import time
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from .common import utc_now
from .features import FEATURES


def matrix(rows):
    if not rows:
        raise ValueError("No hay ventanas para analizar")
    values = np.array([[float(row[key]) for key in FEATURES] for row in rows])
    if not np.isfinite(values).all() or (values < 0).any():
        raise ValueError("Las caracteristicas deben ser numericas, finitas y no negativas")
    return values


def validate_rows(rows, labeled=False):
    matrix(rows)
    seen = set()
    for row in rows:
        if not row.get("run_id") or row.get("source") not in ("real", "synthetic"):
            raise ValueError("Cada ventana requiere run_id y source (real/synthetic)")
        if row.get("label", "") not in (("normal", "anomaly") if labeled else ("", "normal", "anomaly")):
            raise ValueError("Etiquetas faltantes o invalidas: use normal/anomaly")
        if not math.isfinite(float(row["window_seconds"])) or float(row["window_seconds"]) <= 0:
            raise ValueError("Duracion de ventana invalida")
        identity = (row["run_id"], row["peer_ip"], float(row["window_start"]))
        if identity in seen:
            raise ValueError("Ventana duplicada: no incluya la misma captura mas de una vez")
        seen.add(identity)


def train(rows, seed=42):
    validate_rows(rows, labeled=True)
    if len(rows) < 20 or set(row["label"] for row in rows) != {"normal", "anomaly"}:
        raise ValueError("Entrene con al menos 20 ventanas y ambas clases normal/anomaly")
    windows = {float(row["window_seconds"]) for row in rows}
    if len(windows) != 1:
        raise ValueError("Todas las capturas deben usar la misma duracion de ventana")
    x = matrix(rows)
    y = [int(row["label"] == "anomaly") for row in rows]
    pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(
        n_estimators=100, max_depth=8, min_samples_leaf=2,
        class_weight="balanced", random_state=seed, n_jobs=1,
    ))
    pipeline.fit(x, y)
    return {
        "schema": 1, "pipeline": pipeline, "features": FEATURES,
        "window_seconds": windows.pop(), "created_at": utc_now(), "seed": seed,
        "train_run_ids": sorted({row["run_id"] for row in rows}),
        "train_sources": sorted({row["source"] for row in rows}),
        "train_windows": len(rows), "train_classes": dict(Counter(row["label"] for row in rows)),
        "train_features_sha256": hashlib.sha256(x.tobytes()).hexdigest(),
        "versions": {"python": platform.python_version(), "sklearn": sklearn.__version__, "numpy": np.__version__},
        "feature_importance": dict(zip(FEATURES, pipeline[-1].feature_importances_.tolist())),
    }


def save_model(artifact, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, path)


def load_model(path):
    artifact = joblib.load(path)
    if artifact.get("schema") != 1 or artifact.get("features") != FEATURES:
        raise ValueError("Modelo incompatible con el esquema de caracteristicas")
    if artifact["versions"]["sklearn"] != sklearn.__version__:
        raise ValueError("Version de scikit-learn distinta a entrenamiento; reinstale la version o reentrene")
    return artifact


def check_holdout(artifact, rows):
    validate_rows(rows, labeled=True)
    overlap = set(artifact["train_run_ids"]) & {row["run_id"] for row in rows}
    if overlap:
        raise ValueError(f"Fuga de datos: corridas presentes en entrenamiento y prueba: {sorted(overlap)}")


def predict(rows, config, artifact=None):
    if not rows:
        return []
    validate_rows(rows)
    expected_window = artifact["window_seconds"] if artifact else config["window_seconds"]
    if any(float(row["window_seconds"]) != expected_window for row in rows):
        raise ValueError("Ventana de captura incompatible con modelo/configuracion")
    if expected_window != config["window_seconds"]:
        raise ValueError("La duracion del modelo y la configuracion no coinciden")
    x = matrix(rows)
    predictions = []
    for index, row in enumerate(rows):
        started = time.perf_counter()
        probability = None
        ml_alert = False
        if artifact:
            pipeline = artifact["pipeline"]
            probability = float(pipeline.predict_proba(x[index:index + 1])[0, 1])
            ml_alert = probability >= config["probability_threshold"]
        rule_reasons = []
        if float(row["unique_dst_ports"]) >= config["scan_ports_threshold"]:
            rule_reasons.append("muchos_puertos_destino")
        if float(row["bytes_per_second"]) >= config["high_rate_bytes_per_second"]:
            rule_reasons.append("volumen_elevado")
        reasons = list(rule_reasons)
        if ml_alert:
            reasons.append("patron_clasificado_por_modelo")
        predictions.append({**row, "probability": probability if probability is not None else "",
                            "ml_alert": int(ml_alert), "rule_alert": int(bool(rule_reasons)),
                            "alert": int(ml_alert or bool(rule_reasons)),
                            "reasons": ";".join(reasons),
                            "inference_ms": (time.perf_counter() - started) * 1000})
    return predictions


def metrics(predictions, field="alert"):
    labeled = [row for row in predictions if row.get("label") in ("normal", "anomaly")]
    if not labeled:
        return {"labeled_windows": 0, "confusion_matrix": None,
                "accuracy": None, "precision": None, "recall": None, "f1": None,
                "false_positive_rate": None}
    tp = sum(row["label"] == "anomaly" and bool(int(row[field])) for row in labeled)
    fp = sum(row["label"] == "normal" and bool(int(row[field])) for row in labeled)
    tn = sum(row["label"] == "normal" and not int(row[field]) for row in labeled)
    fn = sum(row["label"] == "anomaly" and not int(row[field]) for row in labeled)
    def ratio(a, b):
        return a / b if b else None
    return {"labeled_windows": len(labeled), "confusion_matrix": {"TN": tn, "FP": fp, "FN": fn, "TP": tp},
            "accuracy": (tp + tn) / len(labeled), "precision": ratio(tp, tp + fp),
            "recall": ratio(tp, tp + fn), "f1": ratio(2 * tp, 2 * tp + fp + fn),
            "false_positive_rate": ratio(fp, fp + tn)}
