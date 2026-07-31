#!/usr/bin/env python3
"""dismech#7175: Mondo-anchoring audit for kb/groupings (and a kb/modules scan).

Groupings (Grouping class) carry an optional MONDO cross-reference in
``mappings.mondo_mappings`` -- NOT a ``disease_term`` (a grouping stands on its own
curated rationale and need not recapitulate a MONDO class). This audit reports, per
grouping: whether it maps to MONDO, validates any mapped ids via OAK (missing / obsolete
/ label drift), and lists unmapped groupings (candidate Mondo grouping-class requests, or
intentionally-standalone unions).

Modules (kb/modules) are deliberately NOT Mondo-anchored -- they model conserved
processes anchored to process ontologies (GO / OGMS / MPATH / UBERON), so they are out of
scope for the Mondo dimension. This script reports the module count and scans every module
for stray MONDO references (in evidence/notes), checking that none are obsolete.

Usage:
    uv run python scripts/grouping_anchor_audit.py
"""
from __future__ import annotations

import glob
import os
import re

import yaml
from oaklib import get_adapter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPINGS = os.path.join(ROOT, "kb", "groupings")
MODULES = os.path.join(ROOT, "kb", "modules")
MONDO_ID_RE = re.compile(r"MONDO:\d+")


def main():
    a = get_adapter("sqlite:obo:mondo")
    obs = set(a.obsoletes())

    groups = sorted(glob.glob(os.path.join(GROUPINGS, "*.yaml")))
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

    # Modules: process-anchored, out of Mondo scope -- only scan for stray/obsolete MONDO refs.
    modules = sorted(glob.glob(os.path.join(MODULES, "*.yaml")))
    with_disease_term, with_mondo_ref, obsolete_refs = 0, [], []
    for p in modules:
        raw = open(p).read()
        doc = yaml.safe_load(raw)
        name = os.path.basename(p)[:-5]
        if isinstance(doc, dict) and doc.get("disease_term"):
            with_disease_term += 1
        ids = set(MONDO_ID_RE.findall(raw))
        if ids:
            with_mondo_ref.append(name)
            for i in ids:
                if i in obs:
                    obsolete_refs.append((name, i))
    print(f"\n# Module scan (kb/modules, n={len(modules)}) -- out of Mondo scope, sanity only")
    print(f"  modules with a disease_term (expected 0): {with_disease_term}")
    print(f"  modules with a stray MONDO reference (evidence/notes): {len(with_mondo_ref)}")
    print(f"  obsolete MONDO references: {len(obsolete_refs)}")
    for n, i in obsolete_refs:
        print(f"     ! {n}: {i} OBSOLETE")


if __name__ == "__main__":
    main()
