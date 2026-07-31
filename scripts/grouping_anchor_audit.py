#!/usr/bin/env python3
"""dismech#7175: Mondo-anchoring audit for kb/groupings (and a note on modules).

Groupings (Grouping class) carry an optional MONDO cross-reference in
``mappings.mondo_mappings`` -- NOT a ``disease_term`` (a grouping stands on its own
curated rationale and need not recapitulate a MONDO class). This audit reports, per
grouping: whether it maps to MONDO, validates any mapped ids via OAK (missing / obsolete
/ label drift), and lists unmapped groupings (candidate Mondo grouping-class requests, or
intentionally-standalone unions).

Modules (kb/modules) are deliberately NOT Mondo-anchored -- they model conserved
processes anchored to process ontologies (GO / OGMS / MPATH / UBERON), so they are out of
scope for the Mondo dimension and only sanity-checked for stray obsolete MONDO refs.

Usage:
    uv run python scripts/grouping_anchor_audit.py
"""
from __future__ import annotations

import glob
import os

import yaml
from oaklib import get_adapter


def main():
    a = get_adapter("sqlite:obo:mondo")
    obs = set(a.obsoletes())

    groups = sorted(glob.glob(os.path.join("kb", "groupings", "*.yaml")))
    mapped, unmapped, issues = [], [], []
    for p in groups:
        d = yaml.safe_load(open(p))
        name = d.get("name") or os.path.basename(p)[:-5]
        mm = ((d.get("mappings") or {}).get("mondo_mappings")) or []
        entries = [(e.get("term") or {}) for e in mm if (e.get("term") or {}).get("id")]
        if entries:
            mapped.append(name)
            for e in entries:
                i, stored = e.get("id"), e.get("label")
                canon = a.label(i)
                if i in obs:
                    issues.append((name, i, "OBSOLETE", stored, canon))
                elif canon is None:
                    issues.append((name, i, "MISSING", stored, None))
                elif stored and canon and stored.strip() != canon.strip():
                    issues.append((name, i, "LABEL_DRIFT", stored, canon))
        else:
            unmapped.append((name, d.get("grouping_basis")))

    print(f"# Grouping Mondo-anchoring audit (kb/groupings, n={len(groups)})\n")
    print(f"  with MONDO mapping: {len(mapped)}")
    print(f"  without MONDO mapping: {len(unmapped)}")
    print(f"\n## MONDO id issues in grouping mappings: {len(issues)}")
    for n, i, k, s, c in issues:
        print(f"  {n}: {i} {k} stored='{s}' canonical='{c}'")
    print(f"\n## Groupings with NO MONDO mapping "
          f"(candidate Mondo grouping-class request, or standalone union): {len(unmapped)}")
    for n, b in sorted(unmapped):
        print(f"  - {n}   basis={b}")


if __name__ == "__main__":
    main()
