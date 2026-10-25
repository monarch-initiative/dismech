#!/usr/bin/env python3
"""Gate: counseling, screening, diagnostic and monitoring actions link to no node.

A treatment whose action is informational or diagnostic -- genetic counseling
above all -- does not act on a mechanism or a phenotype, so it may not carry
``target_mechanisms`` or ``target_phenotypes``: those render as treatment
edges in the pathograph. The rule and the treatment terms that imply a
category are in ``src/dismech/medical_actions.py``.

The same rule runs as ``check_non_therapeutic_actions_do_not_use_treatment_targets``
in ``tests/test_data.py``, but that sweep is path-gated and never runs on a
``kb/``-only curation PR, which is the only kind that adds such a link. This
script is the ungated, whole-KB copy, for the reason ``check_entity_refs.py``
gives. No baseline: the KB was clean when it landed.

Usage
-----
    python scripts/check_non_therapeutic_actions.py
    python scripts/check_non_therapeutic_actions.py kb/disorders/Asthma.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.medical_actions import (
    may_have_findings,
    non_therapeutic_action_target_errors,
)
from dismech.yaml_io import safe_load

DEFAULT_ROOTS = ("kb/disorders", "kb/modules", "kb/comorbidities")


def iter_yaml_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p) for p in paths]
    return [p for root in DEFAULT_ROOTS for p in sorted((ROOT / root).glob("*.yaml"))]


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="KB YAML files (default: all)")
    args = parser.parse_args()

    files = iter_yaml_files(args.paths)
    findings: list[tuple[Path, str]] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
            if not may_have_findings(text):
                continue
            data = safe_load(text)
        except (OSError, yaml.YAMLError) as exc:
            print(f"{_display(path)}: could not read ({exc})", file=sys.stderr)
            return 1
        if isinstance(data, dict):
            findings.extend(
                (path, e) for e in non_therapeutic_action_target_errors(data)
            )

    if findings:
        print("Non-therapeutic action(s) linked into the pathograph.\n")
        print("Counseling, screening, diagnosis and monitoring do not act on a")
        print("mechanism or phenotype. Drop the target_mechanisms /")
        print("target_phenotypes links and keep the evidence on the treatment. If")
        print("the treatment bundles a real intervention, set")
        print("`action_category: THERAPEUTIC` instead. See 'Non-therapeutic")
        print("actions link to no node' in CLAUDE.md.\n")
        for path, error in findings:
            print(f"{_display(path)}: {error}")
        print(f"\n{len(findings)} finding(s) across {len(files)} file(s).")
        return 1

    print(f"OK: no non-therapeutic action links a node in {len(files)} KB file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
