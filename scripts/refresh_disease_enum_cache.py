#!/usr/bin/env python3
"""Refresh the MONDO membership of the disease enum caches.

The ``linkml-term-validator`` treats ``cache/enums/*.csv`` as the authoritative
whitelist of valid dynamic-enum members and errors (rather than re-deriving from
the ontology) when a referenced term is missing. Because CI only re-validates
*changed* files, a valid disease-level ``MONDO:`` term that was never in the
cache sits latent until some edit touches its entry, then fails
``just validate-terms`` for that PR. This has recurred repeatedly (Gaucher, CKD,
osteoporosis, ischemic stroke, GERD, ...).

The maintained repair tool (``dismech.enum_cache --fix``) only *prunes* invalid
rows; it does not *add* referenced-but-missing valid terms. This script closes
that gap: it walks the KB, collects the MONDO terms referenced in the slots
bound to each disease enum, keeps those genuinely reachable from the enum's
roots in MONDO, and adds any missing ones to the corresponding cache file.

Scope is MONDO only; NCIT rows and other enum caches are left untouched. Run
from the repo root:

    uv run python scripts/refresh_disease_enum_cache.py          # apply
    uv run python scripts/refresh_disease_enum_cache.py --check  # report only
"""
from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path

import yaml
from oaklib import get_adapter
from oaklib.datamodels.vocabulary import IS_A

# Enum roots, mirroring the reachable_from source_nodes in
# src/dismech/schema/dismech.yaml (DiseaseTerm / DiseaseOrSubtypeTerm).
DISEASE_TERM_ROOTS = ["MONDO:0000001", "MONDO:0020573"]
DISEASE_OR_SUBTYPE_ROOTS = ["MONDO:0000001"]

# YAML slots (parent keys) whose term.id binds to each enum.
DISEASE_TERM_SLOTS = {"disease_term", "mondo_mappings"}
SUBTYPE_SLOTS = {"subtype_term"}

CACHE_GLOBS = {
    "DiseaseTerm": "cache/enums/diseaseterm_*.csv",
    "DiseaseOrSubtypeTerm": "cache/enums/diseaseorsubtypeterm_*.csv",
}
KB_GLOBS = ["kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/groupings/*.yaml"]


def collect_refs() -> tuple[set[str], set[str]]:
    """Return (disease_term MONDO refs, subtype_term MONDO refs) across the KB."""
    dt: set[str] = set()
    dos: set[str] = set()

    def walk(obj, ctx):
        if isinstance(obj, dict):
            for key, val in obj.items():
                nctx = (
                    "DT"
                    if key in DISEASE_TERM_SLOTS
                    else "DOS"
                    if key in SUBTYPE_SLOTS
                    else ctx
                )
                if key == "id" and isinstance(val, str) and val.startswith("MONDO:"):
                    if ctx == "DT":
                        dt.add(val)
                    elif ctx == "DOS":
                        dos.add(val)
                walk(val, nctx)
        elif isinstance(obj, list):
            for item in obj:
                walk(item, ctx)

    for pattern in KB_GLOBS:
        for path in glob.glob(pattern):
            try:
                walk(yaml.safe_load(open(path)), None)
            except yaml.YAMLError:
                continue
    return dt, dos


def valid_members(roots: list[str]) -> set[str]:
    """MONDO CURIEs reachable from the given roots via is_a (subClassOf)."""
    adapter = get_adapter("sqlite:obo:mondo")
    members: set[str] = set()
    for root in roots:
        members.update(
            c for c in adapter.descendants(root, predicates=[IS_A]) if c.startswith("MONDO:")
        )
    return members


def cache_path(enum: str) -> Path:
    matches = sorted(glob.glob(CACHE_GLOBS[enum]))
    if len(matches) != 1:
        raise SystemExit(f"expected exactly one cache file for {enum}, found {matches}")
    return Path(matches[0])


def refresh(enum: str, refs: set[str], roots: list[str], apply: bool) -> int:
    path = cache_path(enum)
    lines = path.read_text().splitlines()
    header, cached = lines[0], set(lines[1:])
    valid = valid_members(roots)
    add = sorted((refs & valid) - cached)
    skipped = sorted(refs - valid)
    print(f"{enum} ({path.name}): {len(cached)} cached, +{len(add)} to add", file=sys.stderr)
    if skipped:
        print(f"  skipped {len(skipped)} unreachable ref(s): {skipped[:8]}", file=sys.stderr)
    if add and apply:
        merged = sorted(cached | set(add))
        path.write_text(header + "\n" + "\n".join(merged) + "\n")
    return len(add)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report missing terms without modifying the caches (nonzero exit if any).",
    )
    args = parser.parse_args(argv)

    dt_refs, dos_refs = collect_refs()
    total = 0
    total += refresh("DiseaseTerm", dt_refs, DISEASE_TERM_ROOTS, apply=not args.check)
    total += refresh(
        "DiseaseOrSubtypeTerm", dos_refs, DISEASE_OR_SUBTYPE_ROOTS, apply=not args.check
    )
    if args.check:
        return 1 if total else 0
    print(f"Added {total} MONDO term(s) to the disease enum caches.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
