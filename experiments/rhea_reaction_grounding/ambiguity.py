#!/usr/bin/env python3
"""Enumerate the GO molecular-function terms that map to more than one Rhea reaction.

The coverage run found that 24.6% of Rhea-reachable MF terms map to several
reactions, so the reaction cannot be derived from the GO term alone. A raw count
does not say how bad that is: alcohol dehydrogenase mapping to 67 reactions is a
different problem from a term mapping to two reactions that differ only by
cofactor.

This script classifies each ambiguous term by whether its reactions share a
substrate core:

  SHARED_CORE  every mapped reaction has at least one non-ubiquitous participant
               in common -- the reactions are variants on one transformation, and
               a renderer could show the shared chemistry without choosing
  DISJOINT     no participant is common to all of them -- the mapped reactions are
               genuinely different chemistry, and only a curator can pick

Ubiquitous cofactors (water, protons, ATP/ADP, NAD(P)(H), O2, CO2, phosphate,
CoA, FAD) are excluded before intersecting, since they are shared by almost
every reaction and would make everything look related.

It reads only. It does not write to ``kb/``, the schema, or any cache.

Usage:
    python ambiguity.py --out-dir 2026-09-07-mapping-ambiguity
"""

from __future__ import annotations

import argparse
import csv
import glob
import os
import sqlite3
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from dismech.yaml_io import safe_load  # noqa: E402

PARTICIPANT_PREDICATE = "RO:0000057"
LABEL_PREDICATE = "rdfs:label"

# Cofactors and small molecules shared by so many reactions that including them
# would make every pair of reactions look like variants of each other.
UBIQUITOUS = {
    "CHEBI:15377",  # water
    "CHEBI:15378",  # H(+)
    "CHEBI:15379",  # O2
    "CHEBI:16526",  # CO2
    "CHEBI:16240",  # hydrogen peroxide
    "CHEBI:30616",  # ATP
    "CHEBI:456216",  # ADP
    "CHEBI:456215",  # AMP
    "CHEBI:43474",  # hydrogenphosphate
    "CHEBI:33019",  # diphosphate
    "CHEBI:57540",  # NAD(+)
    "CHEBI:57945",  # NADH
    "CHEBI:58349",  # NADP(+)
    "CHEBI:57783",  # NADPH
    "CHEBI:57692",  # FAD
    "CHEBI:58307",  # FADH2
    "CHEBI:57287",  # CoA
}


def load_go_to_rhea(path):
    mapping = defaultdict(set)
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 4 or fields[0] == "RHEA_ID":
                continue
            mapping[fields[3]].add("RHEA:" + fields[0])
    return mapping


def load_rhea(db_path):
    """Return (reaction -> {ChEBI participants}, reaction -> equation label)."""
    if not os.path.exists(db_path):
        sys.exit(
            f"Rhea database not found at {db_path}.\n"
            "It is ~1 GB and deliberately not committed. Build it with:\n"
            "  uv run runoak -i sqlite:obo:rhea info RHEA:23844\n"
            "which downloads it to ~/.data/oaklib/rhea.db, then re-run with --rhea-db."
        )
    connection = sqlite3.connect(db_path)
    participants = defaultdict(set)
    query = "select subject, object from statements where predicate = ?"
    for subject, obj in connection.execute(query, (PARTICIPANT_PREDICATE,)):
        if obj and obj.startswith("CHEBI:"):
            participants[subject].add(obj)
    labels = {}
    query = "select subject, value from statements where predicate = ? and subject like 'RHEA:%'"
    for subject, value in connection.execute(query, (LABEL_PREDICATE,)):
        if value:
            labels[subject] = value
    return participants, labels


def scan_kb_mf(kb_glob):
    """Return (GO id -> use count, GO id -> curated label, GO id -> {entry names})."""
    counts = Counter()
    labels = {}
    entries = defaultdict(set)

    def walk(node, entry):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "molecular_functions" and isinstance(value, list):
                    for descriptor in value:
                        term = (descriptor or {}).get("term") or {}
                        term_id = term.get("id")
                        if term_id and str(term_id).startswith("GO:"):
                            counts[term_id] += 1
                            entries[term_id].add(entry)
                            labels.setdefault(term_id, term.get("label") or "")
                walk(value, entry)
        elif isinstance(node, list):
            for item in node:
                walk(item, entry)

    for path in sorted(glob.glob(kb_glob, recursive=True)):
        entry = os.path.basename(path)[: -len(".yaml")]
        try:
            with open(path, encoding="utf-8") as handle:
                walk(safe_load(handle.read()), entry)
        except Exception:  # noqa: BLE001
            continue
    return counts, labels, entries


def classify(reactions, participants):
    """SHARED_CORE when a non-ubiquitous participant is common to every reaction."""
    sets = [participants.get(r, set()) - UBIQUITOUS for r in reactions]
    sets = [s for s in sets if s]
    if len(sets) < 2:
        return "UNKNOWN", set()
    core = set.intersection(*sets)
    return ("SHARED_CORE" if core else "DISJOINT"), core


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb-glob", default=os.path.join(here, "..", "..", "kb", "**", "*.yaml"))
    parser.add_argument("--rhea2go", default=os.path.join(here, "2026-09-07-coverage", "rhea2go.tsv"))
    parser.add_argument("--rhea-db", default=os.path.expanduser("~/.data/oaklib/rhea.db"))
    parser.add_argument("--out-dir", default=os.path.join(here, "2026-09-07-mapping-ambiguity"))
    args = parser.parse_args()

    go_to_rhea = load_go_to_rhea(args.rhea2go)
    participants, equations = load_rhea(args.rhea_db)
    counts, labels, entries = scan_kb_mf(os.path.normpath(args.kb_glob))

    rows = []
    for go_id, uses in counts.items():
        reactions = go_to_rhea.get(go_id, set())
        if len(reactions) < 2:
            continue
        kind, core = classify(reactions, participants)
        rows.append(
            {
                "go_id": go_id,
                "go_label": labels.get(go_id, ""),
                "reactions": len(reactions),
                "kb_uses": uses,
                "kb_entries": len(entries[go_id]),
                "ambiguity": kind,
                "shared_core": ";".join(sorted(core)),
                "entries": ";".join(sorted(entries[go_id])[:6]),
            }
        )
    rows.sort(key=lambda r: (-r["reactions"], r["go_id"]))

    os.makedirs(args.out_dir, exist_ok=True)
    tsv_path = os.path.join(args.out_dir, "ambiguous_terms.tsv")
    with open(tsv_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [], delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    by_kind = Counter(r["ambiguity"] for r in rows)
    affected_uses = sum(r["kb_uses"] for r in rows)
    lines = [
        "# GO molecular-function terms mapping to more than one Rhea reaction",
        "",
        f"ambiguous terms in use in kb/: {len(rows)}",
        f"annotation instances they account for: {affected_uses}",
        f"classification: {dict(sorted(by_kind.items()))}",
        "",
        "## reaction-count distribution",
    ]
    for size, n in sorted(Counter(r["reactions"] for r in rows).items()):
        lines.append(f"  {size} reactions: {n} terms")
    lines += ["", "## the ten most ambiguous"]
    for row in rows[:10]:
        lines.append(
            f"  {row['go_id']} {row['go_label'][:52]:52s} "
            f"{row['reactions']:>3} rxn  {row['kb_uses']:>2} uses  {row['ambiguity']}"
        )
    report = "\n".join(lines) + "\n"
    with open(os.path.join(args.out_dir, "metrics.txt"), "w", encoding="utf-8") as handle:
        handle.write(report)
    print(report, end="")


if __name__ == "__main__":
    main()
