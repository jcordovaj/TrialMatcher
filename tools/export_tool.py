import csv
import json
from typing import List, Dict, Any
from datetime import datetime, timezone


def export_results_json(results: List[Dict[str, Any]], out_path: str = None) -> str:
    if not out_path:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        out_path = f"/tmp/trialmatcher_results_{ts}.json"

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return out_path


def export_results_csv(results: List[Dict[str, Any]], out_path: str = None) -> str:
    if not out_path:
        ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        out_path = f"/tmp/trialmatcher_results_{ts}.csv"

    rows = []
    for r in results:
        rows.append({
            "patient_id": r.get("patient_id"),
            "trial_id": r.get("trial_id"),
            "overall_status": r.get("overall_status"),
            "confidence": r.get("confidence"),
            "summary": r.get("summary")
        })

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else [])
        writer.writeheader()
        writer.writerows(rows)

    return out_path