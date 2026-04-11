"""Semantic validation for ``phenotype_term`` usage across disorder files.

Background (issue #817): The ``PhenotypeTerm`` enum in ``dismech.yaml`` allows
both HP terms and MONDO terms (under ``MONDO:0000001``) so that legitimate
disease-as-feature patterns can be represented (post-infectious sequelae,
hereditary-syndrome cancer risks, surgical complications, etc.). The
``linkml-term-validator`` checks that an ID is reachable and that the label
is correct, but it does not check whether the term is *semantically
appropriate* for the slot.

This module fills that QC gap with two cheap, deterministic checks:

1. A disorder must never list its **own** ``disease_term`` id as a
   ``phenotype_term`` -- a disease cannot be a phenotype of itself.
2. The set of MONDO terms used as ``phenotype_term`` is pinned to a frozen
   allowlist. New MONDO usages must be added to the allowlist explicitly,
   forcing a curator to acknowledge the design intent and preventing
   accidental drift back into the patterns that motivated issue #817.

The module exposes a CLI that mirrors ``dismech.graph``:

    uv run python -m dismech.validate_phenotype_terms --validate kb/disorders
    uv run python -m dismech.validate_phenotype_terms --file kb/disorders/Foo.yaml

It is wired into ``just validate`` (per-file) and ``just validate-all`` so
that the check runs as part of ``just qc`` and in CI on every changed
disorder file, not only in the ``pytest`` test matrix.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import yaml


# Frozen allowlist of MONDO IDs intentionally used in ``phenotype_term`` slots.
# Each entry has been reviewed and represents a legitimate disease-as-feature
# pattern (sequela, hereditary-syndrome cancer risk, organ complication, ...).
# Adding to this set should be a deliberate curation decision -- not a default.
ALLOWED_MONDO_PHENOTYPE_TERMS: frozenset[str] = frozenset(
    {
        "MONDO:0002375",  # sebaceous adenoma (Lynch / Muir-Torre variant)
        "MONDO:0004235",  # diverticulitis (Meckel diverticulum complication)
        "MONDO:0005052",  # irritable bowel syndrome (post-infectious sequela)
        "MONDO:0005081",  # preeclampsia (antiphospholipid syndrome obstetric)
        "MONDO:0005140",  # ovarian carcinoma (Lynch cancer risk)
        "MONDO:0005575",  # colorectal cancer (Lynch cancer risk)
        "MONDO:0005851",  # Miller Fisher syndrome (Campylobacter sequela)
        "MONDO:0006807",  # intestinal perforation (Meckel complication)
        "MONDO:0007835",  # intussusception (Meckel complication)
        "MONDO:0011962",  # endometrial cancer (Lynch cancer risk)
        "MONDO:0016218",  # Guillain-Barre syndrome (Campylobacter sequela)
        "MONDO:0017376",  # reactive arthritis (Campylobacter sequela)
        "MONDO:0020654",  # renal pelvis/ureter urothelial carcinoma (Lynch)
    }
)


def iter_phenotype_terms(node: object) -> Iterator[tuple[str, str]]:
    """Yield ``(curie, preferred_term)`` for every ``phenotype_term`` block
    found anywhere in ``node``.
    """
    if isinstance(node, dict):
        pt = node.get("phenotype_term")
        if isinstance(pt, dict):
            term = pt.get("term") or {}
            tid = term.get("id") if isinstance(term, dict) else None
            if isinstance(tid, str):
                yield tid, pt.get("preferred_term") or ""
        for value in node.values():
            yield from iter_phenotype_terms(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_phenotype_terms(item)


def disease_term_id(data: dict) -> str | None:
    """Return the disorder's own ontology CURIE (from ``disease_term``)."""
    dt = data.get("disease_term")
    if isinstance(dt, dict):
        term = dt.get("term")
        if isinstance(term, dict):
            tid = term.get("id")
            if isinstance(tid, str):
                return tid
    return None


def validate_file(yaml_path: Path) -> list[str]:
    """Run both semantic checks against a single disorder file.

    Returns a (possibly empty) list of issue strings.
    """
    data = yaml.safe_load(yaml_path.read_text())
    issues: list[str] = []

    # Check 1: disorder must not use its own id as a phenotype_term.
    own_id = disease_term_id(data)
    if own_id:
        for curie, label in iter_phenotype_terms(data):
            if curie == own_id:
                issues.append(
                    f"{yaml_path.name} uses its own id {own_id} as a "
                    f"phenotype_term (preferred_term={label!r}). A disease "
                    f"cannot be a phenotype of itself; move to "
                    f"differential_diagnoses, comorbidities, or remove it."
                )

    # Check 2: MONDO phenotype_terms must be on the allowlist.
    for curie, label in iter_phenotype_terms(data):
        if curie.startswith("MONDO:") and curie not in ALLOWED_MONDO_PHENOTYPE_TERMS:
            issues.append(
                f"{yaml_path.name} uses MONDO term {curie} "
                f"(preferred_term={label!r}) as a phenotype_term, but it is "
                f"not on ALLOWED_MONDO_PHENOTYPE_TERMS. If this is a "
                f"legitimate disease-as-feature pattern, add the CURIE to "
                f"src/dismech/validate_phenotype_terms.py with a one-line "
                f"justification. Otherwise replace with an HP term."
            )

    return issues


def validate_all_disorders(input_dir: Path) -> dict[str, list[str]]:
    """Validate every disorder file in ``input_dir``.

    Returns a dict mapping filename to list of issue strings (only files with
    issues are included). Also returns a synthetic ``"_stale_allowlist"`` key
    if the allowlist contains entries that are no longer used in the KB --
    this keeps the allowlist honest as files evolve.
    """
    issues: dict[str, list[str]] = {}
    used_mondo: set[str] = set()

    for yaml_path in sorted(input_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue
        file_issues = validate_file(yaml_path)
        if file_issues:
            issues[yaml_path.name] = file_issues

        # Collect used MONDO terms for the stale-allowlist check.
        data = yaml.safe_load(yaml_path.read_text())
        for curie, _ in iter_phenotype_terms(data):
            if curie.startswith("MONDO:"):
                used_mondo.add(curie)

    stale = ALLOWED_MONDO_PHENOTYPE_TERMS - used_mondo
    if stale:
        issues["_stale_allowlist"] = [
            f"ALLOWED_MONDO_PHENOTYPE_TERMS contains entries that are no "
            f"longer used as a phenotype_term anywhere in {input_dir}. Please "
            f"remove: {sorted(stale)}"
        ]

    return issues


def _print_issues(issues: dict[str, list[str]]) -> int:
    if not issues:
        return 0
    total = sum(len(v) for v in issues.values())
    print(
        f"Found {total} phenotype_term semantic issue(s) across "
        f"{len(issues)} file(s):\n"
    )
    for name, file_issues in issues.items():
        print(f"{name}:")
        for issue in file_issues:
            print(f"  - {issue}")
        print()
    return 1


def main() -> None:
    """CLI entry point for phenotype_term semantic validation."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate phenotype_term semantics (issue #817)"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--validate",
        "-v",
        metavar="DIR",
        help="Validate all disorder files in DIR",
    )
    group.add_argument(
        "--file",
        "-f",
        metavar="FILE",
        help="Validate a single disorder file",
    )

    args = parser.parse_args()

    if args.file:
        yaml_path = Path(args.file)
        file_issues = validate_file(yaml_path)
        if file_issues:
            print(f"{yaml_path.name}:")
            for issue in file_issues:
                print(f"  - {issue}")
            sys.exit(1)
        print(f"✓ {yaml_path.name}: phenotype_term semantics OK")
        return

    input_dir = Path(args.validate)
    issues = validate_all_disorders(input_dir)
    if issues:
        sys.exit(_print_issues(issues))
    print(f"✓ All disorders in {input_dir} pass phenotype_term semantic checks.")


if __name__ == "__main__":
    main()
