"""Shared helpers for dismech export modules."""

from __future__ import annotations

from pathlib import Path


def discover_disorder_files(input_dir: Path) -> list[Path]:
    """Return sorted disorder YAML files in ``input_dir``, excluding history files."""
    return [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]
