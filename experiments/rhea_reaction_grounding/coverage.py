#!/usr/bin/env python3
"""Measure how much of dismech's GO annotation Rhea could reach.

dismech carries no Rhea identifiers. The only bridge between the KB as curated
and Rhea's reaction space is ``rhea2go.tsv``, which maps Rhea reactions to GO
terms. This script asks, for a given KB tree and a pinned ``rhea2go.tsv``
snapshot, how many of the GO terms already curated in ``kb/`` sit on the far end
of that bridge -- and how ambiguous the crossing is.

It reads only. It does not write to ``kb/``, the schema, or any cache.

Usage:
    python coverage.py --kb-root kb --rhea2go 2026-09-07-coverage/rhea2go.tsv
"""

from __future__ import annotations

import argparse
import glob
import os
import sys
from collections import Counter, defaultdict

# dismech's own loader, so we parse YAML exactly as the KB tooling does.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from dismech.yaml_io import safe_load  # noqa: E402

# The two ontology-bound descriptor slots that carry GO terms. Rhea maps to GO
# molecular function and to a narrow band of metabolic process terms, so both
# are worth counting even though only one is expected to land.
GO_SLOTS = ("molecular_functions", "biological_processes")


def load_rhea2go(path):
    """Return (go_id -> {rhea_id}, direction counter).

    rhea2go rows are ``RHEA_ID  DIRECTION  MASTER_ID  ID``. DIRECTION matters:
    a mapping carried on an undirected master reaction cannot tell a curator
    which way flux runs.
    """
    go_to_rhea = defaultdict(set)
    directions = Counter()
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 4 or fields[0] == "RHEA_ID":
                continue
            rhea_id, direction, _master, go_id = fields[:4]
            go_to_rhea[go_id].add(rhea_id)
            directions[direction] += 1
    return go_to_rhea, directions


def scan_kb(kb_root):
    """Return per-slot term counters and per-file term sets.

    Walks every mapping in every KB file rather than assuming a fixed depth --
    ``molecular_functions`` appears on pathophysiology nodes, and the same slot
    name is reused at several nesting levels.
    """
    counts = {slot: Counter() for slot in GO_SLOTS}
    by_file = {slot: defaultdict(set) for slot in GO_SLOTS}

    def walk(node, path):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in GO_SLOTS and isinstance(value, list):
                    for descriptor in value:
                        term = (descriptor or {}).get("term") or {}
                        term_id = term.get("id")
                        if term_id:
                            counts[key][term_id] += 1
                            by_file[key][path].add(term_id)
                walk(value, path)
        elif isinstance(node, list):
            for item in node:
                walk(item, path)

    files = sorted(glob.glob(os.path.join(kb_root, "**", "*.yaml"), recursive=True))
    unreadable = []
    for path in files:
        try:
            with open(path, encoding="utf-8") as handle:
                walk(safe_load(handle.read()), path)
        except Exception as exc:  # noqa: BLE001 - report, never mask
            unreadable.append((path, type(exc).__name__))
    return files, counts, by_file, unreadable


def pct(numerator, denominator):
    return 100.0 * numerator / denominator if denominator else 0.0


def report(kb_root, rhea2go_path, out=sys.stdout):
    go_to_rhea, directions = load_rhea2go(rhea2go_path)
    files, counts, by_file, unreadable = scan_kb(kb_root)

    def emit(line=""):
        print(line, file=out)

    emit("# Rhea reachability of dismech GO annotation")
    emit()
    emit(f"KB root:        {kb_root}")
    emit(f"rhea2go:        {rhea2go_path}")
    emit(f"KB YAML files:  {len(files)}")
    if unreadable:
        emit(f"UNREADABLE:     {len(unreadable)} (listed at end)")
    emit()

    emit("## rhea2go snapshot")
    reactions = {r for rs in go_to_rhea.values() for r in rs}
    emit(f"distinct GO terms mapped:   {len(go_to_rhea)}")
    emit(f"distinct Rhea reactions:    {len(reactions)}")
    emit(f"direction values:           {dict(sorted(directions.items()))}")
    undirected = directions.get("UN", 0)
    emit(f"undirected (UN) share:      {pct(undirected, sum(directions.values())):.1f}%")
    emit()

    for slot in GO_SLOTS:
        terms = counts[slot]
        covered = {t for t in terms if t in go_to_rhea}
        instances_total = sum(terms.values())
        instances_covered = sum(terms[t] for t in covered)
        files_with = {f for f, s in by_file[slot].items() if s}
        files_covered = {f for f, s in by_file[slot].items() if s & covered}
        multi = {t for t in covered if len(go_to_rhea[t]) > 1}

        emit(f"## {slot}")
        emit(f"distinct terms:             {len(terms)}")
        emit(f"  with >=1 Rhea reaction:   {len(covered)} ({pct(len(covered), len(terms)):.1f}%)")
        emit(f"annotation instances:       {instances_total}")
        emit(
            f"  covered:                  {instances_covered} "
            f"({pct(instances_covered, instances_total):.1f}%)"
        )
        emit(f"files carrying the slot:    {len(files_with)}")
        emit(
            f"  with >=1 mappable term:   {len(files_covered)} "
            f"({pct(len(files_covered), len(files_with)):.1f}%)"
        )
        emit(
            f"covered terms mapping to >1 reaction: {len(multi)} "
            f"({pct(len(multi), len(covered)):.1f}% of covered)"
        )
        if multi:
            emit("  worst ambiguity (term: reactions, KB uses):")
            for term in sorted(multi, key=lambda t: (-len(go_to_rhea[t]), t))[:10]:
                emit(f"    {term}: {len(go_to_rhea[term])} reactions, used {terms[term]}x")
        emit()

    if unreadable:
        emit("## unreadable files")
        for path, exc in unreadable:
            emit(f"  {path}: {exc}")
        emit()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--kb-root",
        default=os.path.join(here, "..", "..", "kb"),
        help="KB tree to scan (default: the repo's kb/)",
    )
    parser.add_argument(
        "--rhea2go",
        default=os.path.join(here, "2026-09-07-coverage", "rhea2go.tsv"),
        help="pinned rhea2go.tsv snapshot",
    )
    args = parser.parse_args()
    report(os.path.normpath(args.kb_root), os.path.normpath(args.rhea2go))


if __name__ == "__main__":
    main()
