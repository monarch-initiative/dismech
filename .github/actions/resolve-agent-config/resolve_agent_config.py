#!/usr/bin/env python3
"""Resolve the effective AI model for an agentic workflow from agent-config.yaml.

Read at run time by the ``resolve-agent-config`` composite action (issue #5218).
Two modes:

* default: print the single resolved model id for ``--workflow``.
  Resolution order: ``--override`` (if non-empty) > per-workflow ``model:`` >
  ``default_model``.
* ``--matrix``: print the workflow's ``models:`` list as a JSON array, for a job
  that fans out across models via ``strategy.matrix``.

Kept dependency-light (PyYAML only) and side-effect free so it can be unit
tested directly; the composite action does the ``$GITHUB_ENV`` / ``$GITHUB_OUTPUT``
plumbing.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml


class ConfigError(RuntimeError):
    """Raised when the config cannot satisfy the request."""


def load_config(path: Path) -> dict:
    if not path.exists():
        raise ConfigError(f"agent config not found: {path}")
    data = yaml.safe_load(path.read_text()) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"agent config must be a mapping: {path}")
    return data


def _workflow_entry(config: dict, workflow: str) -> dict:
    entry = (config.get("workflows") or {}).get(workflow)
    if entry is None:
        raise ConfigError(
            f"workflow '{workflow}' is not defined under 'workflows:' in the "
            f"agent config"
        )
    if not isinstance(entry, dict):
        raise ConfigError(f"workflow '{workflow}' entry must be a mapping")
    return entry


def resolve_model(config: dict, workflow: str, override: str | None = None) -> str:
    """Return the effective single model id for ``workflow``."""
    if override and override.strip():
        return override.strip()
    entry = _workflow_entry(config, workflow)
    model = entry.get("model")
    if model:
        return str(model)
    if entry.get("matrix"):
        raise ConfigError(
            f"workflow '{workflow}' defines a 'matrix:', not a single 'model:'; "
            f"use --matrix"
        )
    default = config.get("default_model")
    if not default:
        raise ConfigError(
            f"workflow '{workflow}' has no 'model:' and no top-level "
            f"'default_model' is set"
        )
    return str(default)


def resolve_matrix(config: dict, workflow: str) -> list[dict]:
    """Return the workflow's ``matrix:`` list (for ``strategy.matrix.include``).

    Each entry is a mapping (e.g. ``{effort, model, selector}``) and must include
    a ``model``.
    """
    entry = _workflow_entry(config, workflow)
    matrix = entry.get("matrix")
    if not matrix:
        raise ConfigError(
            f"workflow '{workflow}' has no 'matrix:' list; use single-model mode"
        )
    if not isinstance(matrix, list) or not matrix:
        raise ConfigError(f"workflow '{workflow}' 'matrix:' must be a non-empty list")
    for item in matrix:
        if not isinstance(item, dict) or not item.get("model"):
            raise ConfigError(
                f"workflow '{workflow}' matrix entries must be mappings with a "
                f"'model:'"
            )
    return matrix


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--workflow", required=True)
    parser.add_argument("--override", default="")
    parser.add_argument(
        "--matrix",
        action="store_true",
        help="print the workflow's models: list as a JSON array",
    )
    args = parser.parse_args(argv)

    try:
        config = load_config(args.config)
        if args.matrix:
            print(json.dumps(resolve_matrix(config, args.workflow)))
        else:
            print(resolve_model(config, args.workflow, args.override))
    except ConfigError as exc:
        print(f"resolve-agent-config: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
