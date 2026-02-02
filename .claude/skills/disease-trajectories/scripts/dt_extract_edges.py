#!/usr/bin/env python3
"""Extract disease-trajectory edges from JSON into a normalized TSV/CSV."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


EDGE_KEYS = (
    "edges",
    "links",
    "pairs",
    "data",
    "results",
    "trajectories",
)

A_KEYS = (
    "a",
    "source",
    "from",
    "disease_a",
    "disease_a_id",
    "disease1",
    "icd_a",
    "icd1",
)

B_KEYS = (
    "b",
    "target",
    "to",
    "disease_b",
    "disease_b_id",
    "disease2",
    "icd_b",
    "icd2",
)

PAIR_KEYS = ("pair", "pair_id", "pair_key", "edge", "edge_id")


def _get_ci(d: Dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in d:
            return d[key]
        for alt in (key.lower(), key.upper(), key.title()):
            if alt in d:
                return d[alt]
    return None


def _split_pair(pair: str) -> Tuple[Optional[str], Optional[str]]:
    if not pair or not isinstance(pair, str):
        return None, None
    for sep in ("-", "/", "|"):
        if sep in pair:
            left, right = pair.split(sep, 1)
            return left.strip(), right.strip()
    return None, None


def _normalize_sex(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value)


def _normalize_direction(record: Dict[str, Any]) -> str:
    if record.get("directionality"):
        return str(record["directionality"])
    a_before = record.get("a_before_b")
    b_before = record.get("b_before_a")
    same_time = record.get("same_time")
    try:
        a_val = float(a_before) if a_before is not None else None
        b_val = float(b_before) if b_before is not None else None
        s_val = float(same_time) if same_time is not None else None
    except (TypeError, ValueError):
        return ""
    if a_val is None and b_val is None and s_val is None:
        return ""
    if a_val is not None and b_val is not None and a_val > b_val:
        return "A_BEFORE_B"
    if a_val is not None and b_val is not None and b_val > a_val:
        return "B_BEFORE_A"
    if s_val is not None and (a_val is None or b_val is None):
        return "SAME_TIME"
    return "UNKNOWN"


def _record_from_item(item: Dict[str, Any], source_path: str) -> Dict[str, Any]:
    a_id = None
    b_id = None
    for key in A_KEYS:
        a_id = a_id or _get_ci(item, key)
    for key in B_KEYS:
        b_id = b_id or _get_ci(item, key)

    pair_val = None
    for key in PAIR_KEYS:
        pair_val = pair_val or _get_ci(item, key)
    if (a_id is None or b_id is None) and pair_val:
        pair_a, pair_b = _split_pair(str(pair_val))
        a_id = a_id or pair_a
        b_id = b_id or pair_b

    record = {
        "disease_a_id": a_id or "",
        "disease_b_id": b_id or "",
        "sex": _normalize_sex(_get_ci(item, "sex", "gender")),
        "a_before_b": _get_ci(item, "a_before_b", "A_before_B"),
        "b_before_a": _get_ci(item, "b_before_a", "B_before_A"),
        "same_time": _get_ci(item, "same_time", "SAME_TIME"),
        "p_value": _get_ci(item, "p_value", "p", "pval"),
        "fdr": _get_ci(item, "fdr", "q_value", "q"),
        "metric": _get_ci(item, "metric", "measure", "stat"),
        "count": _get_ci(item, "count", "n"),
        "directionality": _get_ci(item, "directionality", "direction"),
        "raw_pair": pair_val or "",
        "source_path": source_path,
    }
    if not record["directionality"]:
        record["directionality"] = _normalize_direction(record)
    return record


def _iter_phase_dict(phase_dict: Dict[str, Any], source_path: str) -> Iterable[Dict[str, Any]]:
    for pair_key, payload in phase_dict.items():
        if not isinstance(payload, dict):
            continue
        pair_a, pair_b = _split_pair(str(pair_key))
        sex_keys = [
            key for key in payload.keys()
            if str(key).lower() in {"male", "female", "all", "both", "unknown"}
        ]
        if sex_keys:
            for sex_key in sex_keys:
                entry = payload.get(sex_key) or {}
                if not isinstance(entry, dict):
                    entry = {"value": entry}
                entry = dict(entry)
                entry.setdefault("sex", sex_key)
                if pair_a or pair_b:
                    entry.setdefault("disease_a_id", pair_a)
                    entry.setdefault("disease_b_id", pair_b)
                entry.setdefault("pair", pair_key)
                yield _record_from_item(entry, source_path)
        else:
            entry = dict(payload)
            if pair_a or pair_b:
                entry.setdefault("disease_a_id", pair_a)
                entry.setdefault("disease_b_id", pair_b)
            entry.setdefault("pair", pair_key)
            yield _record_from_item(entry, source_path)


def _iter_records(data: Any, source_path: str) -> Iterable[Dict[str, Any]]:
    if isinstance(data, dict):
        if "phase_dict" in data and isinstance(data["phase_dict"], dict):
            yield from _iter_phase_dict(data["phase_dict"], source_path)
            return
        for key in EDGE_KEYS:
            if key in data and isinstance(data[key], list):
                for item in data[key]:
                    if isinstance(item, dict):
                        yield _record_from_item(item, source_path)
                return
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                yield _record_from_item(item, source_path)


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _write_rows(rows: List[Dict[str, Any]], output: Path | None, fmt: str) -> None:
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    if output:
        out_handle = output.open("w", newline="", encoding="utf-8")
    else:
        out_handle = sys.stdout
    try:
        if fmt == "jsonl":
            for row in rows:
                out_handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        else:
            dialect = "excel-tab" if fmt == "tsv" else "excel"
            writer = csv.DictWriter(out_handle, fieldnames=fieldnames, dialect=dialect)
            writer.writeheader()
            writer.writerows(rows)
    finally:
        if output:
            out_handle.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract DT edges from JSON to TSV/CSV/JSONL")
    parser.add_argument("input", help="Path to DT JSON file")
    parser.add_argument("--output", "-o", help="Output path (default stdout)")
    parser.add_argument("--format", "-f", choices=("tsv", "csv", "jsonl"), default="tsv")
    args = parser.parse_args()

    input_path = Path(args.input)
    data = _load_json(input_path)
    rows = list(_iter_records(data, str(input_path)))
    _write_rows(rows, Path(args.output) if args.output else None, args.format)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
