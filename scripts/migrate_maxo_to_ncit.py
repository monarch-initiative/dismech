#!/usr/bin/env python3
"""Migrate MAXO treatment/diagnosis terms to NCIT across the knowledge base.

Removes the Medical Action Ontology (MAXO) from dismech entirely by rewriting
every ``term.id`` / ``term.label`` bound to MAXO under a ``treatment_term`` or
``diagnosis_term`` descriptor to its NCI Thesaurus (NCIT) equivalent.

The mapping is driven by ``docs/superpowers/maxo_ncit_crosswalk.tsv`` plus a set
of reachability overrides (drug-class / substance / device nodes that are not
reachable from ``NCIT:C25218`` and would fail treatment-enum validation) and a
small BLANK set (MAXO terms with no NCIT equivalent — the ``term:`` block is
dropped, keeping the free-text ``preferred_term``).

Every MAXO ``term:`` block in the KB satisfies the invariant

    <indent>term:
    <indent+2>id: MAXO:NNNNNNN
    <indent+2>label: <label>

(verified across all 4,351 occurrences), so the rewrite is line-oriented for
minimal, reviewable diffs rather than a ruamel round-trip.

Run: ``uv run python scripts/migrate_maxo_to_ncit.py``  (edits kb/ in place)
     ``uv run python scripts/migrate_maxo_to_ncit.py --check``  (report only)
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import re
from pathlib import Path

MAP_TSV = Path("docs/superpowers/maxo_ncit_final_map.tsv")
ID_RE = re.compile(r"^(\s*)id:\s*(MAXO:\d+)\s*$")


def load_map(path: Path) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            mapping[row["maxo_id"]] = {
                "action": row["action"],
                "ncit_id": row["ncit_id"],
                "ncit_label": row["ncit_label"],
            }
    return mapping


def migrate_file(fp: Path, mapping: dict[str, dict]) -> tuple[list[str], dict]:
    lines = fp.read_text().split("\n")
    deletions: set[int] = set()
    replacements: dict[int, str] = {}
    stats = {"remap": 0, "blank": 0, "unmapped": []}

    for i, line in enumerate(lines):
        m = ID_RE.match(line)
        if not m:
            continue
        indent, maxo_id = m.group(1), m.group(2)
        entry = mapping.get(maxo_id)
        if entry is None:
            stats["unmapped"].append(maxo_id)
            continue
        label_line = lines[i + 1]
        label_indent = label_line[: len(label_line) - len(label_line.lstrip())]
        if entry["action"] == "BLANK":
            # drop the term: (i-1), id: (i), label: (i+1) lines
            deletions.update({i - 1, i, i + 1})
            stats["blank"] += 1
        else:
            replacements[i] = f"{indent}id: {entry['ncit_id']}"
            replacements[i + 1] = f"{label_indent}label: {entry['ncit_label']}"
            stats["remap"] += 1

    if not deletions and not replacements:
        return lines, stats

    out = []
    for idx, line in enumerate(lines):
        if idx in deletions:
            continue
        out.append(replacements.get(idx, line))
    return out, stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only, do not write")
    ap.add_argument("--glob", default="kb/**/*.yaml")
    args = ap.parse_args()

    mapping = load_map(MAP_TSV)
    total = {"files": 0, "remap": 0, "blank": 0}
    unmapped: dict[str, list[str]] = {}

    for fp in sorted(glob.glob(args.glob, recursive=True)):
        p = Path(fp)
        new_lines, stats = migrate_file(p, mapping)
        if stats["unmapped"]:
            unmapped[fp] = stats["unmapped"]
        if stats["remap"] or stats["blank"]:
            total["files"] += 1
            total["remap"] += stats["remap"]
            total["blank"] += stats["blank"]
            if not args.check:
                p.write_text("\n".join(new_lines))

    print(json.dumps({"summary": total, "unmapped": unmapped}, indent=2))
    return 1 if unmapped else 0


if __name__ == "__main__":
    raise SystemExit(main())
