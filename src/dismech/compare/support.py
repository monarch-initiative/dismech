"""Shared helpers for source-vs-dismech comparison modules."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from dismech import kb_cache
from dismech.yaml_io import safe_load


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
    """Parse ``path`` into a fresh, private mapping."""
    with open(path, encoding="utf-8") as stream:
        data = safe_load(stream)
    return _require_mapping(data, path)


def load_shared_yaml_object(path: Path) -> dict[str, Any]:
    """Same contract as :func:`load_yaml_object`, but the document is shared.

    Backed by :mod:`dismech.kb_cache`, so repeated scans of kb/disorders/ in one
    process parse each file once. The returned mapping is the shared copy --
    treat it as read-only, and use :func:`load_yaml_object` if you need to
    annotate it.
    """
    return _require_mapping(kb_cache.load_document(path), path)


def _require_mapping(data: Any, path: Path) -> dict[str, Any]:
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
