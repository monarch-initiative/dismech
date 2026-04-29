"""Shared helpers for source-vs-dismech comparison modules."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def normalize_hp_id(term_id: str | None) -> str | None:
    """Normalize HPO identifiers to uppercase CURIE form."""
    if not term_id:
        return None
    tid = str(term_id).strip()
    if not tid or ":" not in tid:
        return None
    prefix, local = tid.split(":", 1)
    if prefix.casefold() != "hp":
        return None
    local = local.strip()
    if not local:
        return None
    return f"HP:{local}"


def default_kb_dir() -> Path:
    return Path(__file__).resolve().parents[3] / "kb" / "disorders"


def iter_disease_files(kb_dir: Path) -> list[Path]:
    return sorted(
        p for p in kb_dir.glob("*.yaml") if not p.name.endswith(".history.yaml")
    )


def load_yaml_object(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as stream:
        data = yaml.safe_load(stream)
    if not isinstance(data, dict):
        raise ValueError(f"YAML at {path} must be an object")
    return data


def get_disease_term_id(disease_data: dict[str, Any]) -> str | None:
    disease_term = disease_data.get("disease_term")
    if not isinstance(disease_term, dict):
        return None
    term = disease_term.get("term")
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id else None
