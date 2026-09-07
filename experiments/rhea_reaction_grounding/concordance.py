#!/usr/bin/env python3
"""Test whether a Rhea reaction corroborates the biomarker dismech already curates.

For an inborn error of metabolism the enzyme's substrate is usually the
diagnostic biomarker. dismech records both facts independently: a
``molecular_functions`` GO term on a pathophysiology node, and a ``biochemical``
biomarker bound to ChEBI. Rhea knows the reaction's ChEBI participants. So the
two can be cross-checked without any new curation:

    does the entry's biomarker appear among the participants of the reaction
    its molecular-function term maps to?

A hit means Rhea independently corroborates a link dismech asserts through
separate curation. A miss is diagnostic rather than a failure -- the biomarker
may be genuinely downstream of the reaction, the reaction may be the wrong pick
from a many-mapped GO term, or the ChEBI binding may warrant a look.

This also yields the shortlist of "simple cases" (monogenic, real pathway
information, biomarker evidence) requested in
https://github.com/monarch-initiative/dismech/issues/973.

It reads only. It does not write to ``kb/``, the schema, or any cache.

Inputs, all pinned in the run directory's MANIFEST.yaml:
  * rhea2go.tsv              GO -> Rhea reaction (committed, small)
  * chebi_pH7_3_mapping.tsv  reconciles ChEBI protonation forms (fetched)
  * rhea.db                  OAK/semsql Rhea build, for RO:0000057 participants
                             (~1 GB; never committed -- see MANIFEST.yaml)

Usage:
    python concordance.py --out-dir 2026-09-07-biomarker-concordance
"""

from __future__ import annotations

import argparse
import csv
import glob
import os
import sqlite3
import sys
from collections import defaultdict

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from dismech.yaml_io import safe_load  # noqa: E402

PARTICIPANT_PREDICATE = "RO:0000057"  # has participant


def load_go_to_rhea(path):
    mapping = defaultdict(set)
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 4 or fields[0] == "RHEA_ID":
                continue
            mapping[fields[3]].add("RHEA:" + fields[0])
    return mapping


def load_participants(db_path):
    """reaction CURIE -> {ChEBI CURIE}, straight from the semsql statements table."""
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
    return participants


def load_ph_equivalents(path):
    """ChEBI CURIE -> {equivalent CURIEs}, both directions.

    Rhea states participants at pH 7.3, so a KB biomarker bound to the neutral
    species will not match a reaction participant bound to the zwitterion
    without this. Rhea publishes the mapping precisely because the mismatch is
    real and systematic.
    """
    forward = {}
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 2 or fields[0] == "CHEBI":
                continue
            forward["CHEBI:" + fields[0]] = "CHEBI:" + fields[1]
    reverse = defaultdict(set)
    for source, target in forward.items():
        reverse[target].add(source)

    def equivalents(curie):
        out = {curie}
        if curie in forward:
            out.add(forward[curie])
        out |= reverse.get(curie, set())
        return out

    return equivalents


def collect_entry(doc):
    """Return (molecular-function GO terms, [(biomarker name, ChEBI)], gene count)."""
    go_terms = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "molecular_functions" and isinstance(value, list):
                    for descriptor in value:
                        term = (descriptor or {}).get("term") or {}
                        if str(term.get("id", "")).startswith("GO:"):
                            go_terms.add(term["id"])
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(doc)
    biomarkers = []
    for entry in doc.get("biochemical") or []:
        term = ((entry or {}).get("biomarker_term") or {}).get("term") or {}
        if str(term.get("id", "")).startswith("CHEBI:"):
            biomarkers.append((entry.get("name"), term["id"]))
    return go_terms, biomarkers, len(doc.get("genetic") or [])


def analyse(kb_glob, go_to_rhea, participants, equivalents):
    rows = []
    for path in sorted(glob.glob(kb_glob)):
        try:
            with open(path, encoding="utf-8") as handle:
                doc = safe_load(handle.read())
        except Exception:  # noqa: BLE001 - a malformed entry is not this run's concern
            continue
        if not isinstance(doc, dict):
            continue
        go_terms, biomarkers, gene_count = collect_entry(doc)
        if not go_terms or not biomarkers:
            continue
        reactions = {r for go in go_terms for r in go_to_rhea.get(go, ())}
        if not reactions:
            continue
        reachable = set()
        for reaction in reactions:
            reachable |= participants.get(reaction, set())
        matched = [(n, c) for n, c in biomarkers if equivalents(c) & reachable]
        rows.append(
            {
                "entry": os.path.basename(path)[: -len(".yaml")],
                "genes": gene_count,
                "mf_terms": len(go_terms),
                "reactions": len(reactions),
                "biomarkers": len(biomarkers),
                "concordant": len(matched),
                "matched": "; ".join(f"{n} ({c})" for n, c in matched),
            }
        )
    return rows


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb-glob", default=os.path.join(here, "..", "..", "kb", "disorders", "*.yaml"))
    parser.add_argument("--rhea2go", default=os.path.join(here, "2026-09-07-coverage", "rhea2go.tsv"))
    parser.add_argument("--ph-map", default=os.path.join(here, "2026-09-07-biomarker-concordance", "chebi_pH7_3_mapping.tsv"))
    parser.add_argument("--rhea-db", default=os.path.expanduser("~/.data/oaklib/rhea.db"))
    parser.add_argument("--out-dir", default=os.path.join(here, "2026-09-07-biomarker-concordance"))
    args = parser.parse_args()

    go_to_rhea = load_go_to_rhea(args.rhea2go)
    participants = load_participants(args.rhea_db)
    equivalents = load_ph_equivalents(args.ph_map)
    rows = analyse(os.path.normpath(args.kb_glob), go_to_rhea, participants, equivalents)

    concordant = [r for r in rows if r["concordant"]]
    os.makedirs(args.out_dir, exist_ok=True)

    tsv_path = os.path.join(args.out_dir, "candidates.tsv")
    with open(tsv_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["entry", "genes", "mf_terms", "reactions", "biomarkers", "concordant", "matched"],
            delimiter="\t",
        )
        writer.writeheader()
        # Monogenic first, then most corroborated: the order a curator would pick from.
        for row in sorted(rows, key=lambda r: (r["genes"], -r["concordant"], r["entry"])):
            writer.writerow(row)

    lines = [
        "# Biomarker-substrate concordance",
        "",
        f"entries with a Rhea-mappable MF term AND a ChEBI-bound biomarker: {len(rows)}",
        f"  >=1 biomarker is a participant of the mapped reaction: {len(concordant)} "
        f"({100.0 * len(concordant) / len(rows):.1f}%)" if rows else "  (no entries qualified)",
        "",
        f"monogenic among concordant: {sum(1 for r in concordant if r['genes'] == 1)}",
        f"candidates written to: {os.path.basename(tsv_path)}",
    ]
    report = "\n".join(lines) + "\n"
    with open(os.path.join(args.out_dir, "metrics.txt"), "w", encoding="utf-8") as handle:
        handle.write(report)
    print(report, end="")


if __name__ == "__main__":
    main()
