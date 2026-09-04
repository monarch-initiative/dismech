"""Audit dismech grouping membership against MONDO's hierarchy.

A ``kb/groupings/`` entry is a curated **union**: it lists member diseases that
belong together. When the grouping itself carries a MONDO mapping and its members
carry ``disease_term``s, that union becomes checkable -- if the grouping *is* the
MONDO class, every member's term should be a descendant of the grouping's term.

Only groupings whose MONDO mapping is ``skos:exactMatch`` are checked. A
``broadMatch`` grouping is explicitly narrower than its MONDO term, and a
``narrowMatch`` one explicitly wider, so neither licenses the descendant
expectation; ``closeMatch``/``relatedMatch`` are too weak to test against.

Verdicts mirror the per-disorder analysis in ``build_analyses.py``:

``AGREES``    MONDO has the member's term under the grouping's term.
``SILENT``    No path either way -- usually a missing MONDO ``is_a`` edge.
``REVERSED``  MONDO has the grouping's term under the member's. Combined with the
              identity claims this is unsatisfiable.

Usage:
    uv run python analyses/boomer/scripts/grouping_audit.py \
        --out analyses/boomer/groupings/violations.tsv
"""

from __future__ import annotations

import argparse
import csv
import glob
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml

MONDO_DB = Path.home() / ".data/oaklib/mondo.db"
REPO = Path(__file__).resolve().parents[3]

# a grouping only entails "members are under my term" when it claims identity
IDENTITY_PREDICATES = {"skos:exactMatch"}

FIELDNAMES = (
    "verdict",
    "grouping",
    "grouping_term",
    "grouping_label",
    "member",
    "member_term",
    "member_label",
)


def term_id(descriptor):
    if not isinstance(descriptor, dict):
        return None
    return (descriptor.get("term") or {}).get("id") or descriptor.get("id")


def disease_terms(kb_glob):
    """Map Disease.name -> its MONDO disease_term (members reference entries by name)."""
    out = {}
    for path in glob.glob(kb_glob):
        data = yaml.safe_load(open(path)) or {}
        if isinstance(data, dict) and data.get("name"):
            out[data["name"]] = term_id(data.get("disease_term"))
    return out


class Mondo:
    def __init__(self, db):
        self.con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        self._label: dict[str, str] = {}
        self._anc: dict[str, set[str]] = {}

    def label(self, curie):
        if curie not in self._label:
            row = self.con.execute(
                "select value from statements where subject=? and predicate='rdfs:label'",
                (curie,),
            ).fetchone()
            self._label[curie] = row[0] if row else curie
        return self._label[curie]

    def ancestors(self, curie):
        if curie not in self._anc:
            self._anc[curie] = {
                o
                for (o,) in self.con.execute(
                    "select object from entailed_edge where subject=? "
                    "and predicate='rdfs:subClassOf' and object like 'MONDO:%'",
                    (curie,),
                )
            }
        return self._anc[curie]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--groupings", default=str(REPO / "kb/groupings/*.yaml"))
    ap.add_argument("--disorders", default=str(REPO / "kb/disorders/*.yaml"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--db", default=str(MONDO_DB))
    args = ap.parse_args(argv)

    mondo = Mondo(args.db)
    terms = disease_terms(args.disorders)
    rows, tally = [], Counter()

    for path in sorted(glob.glob(args.groupings)):
        grouping = yaml.safe_load(open(path)) or {}
        identity = [
            m["term"]["id"]
            for m in (grouping.get("mappings") or {}).get("mondo_mappings") or []
            if m.get("mapping_predicate") in IDENTITY_PREDICATES
        ]
        if not identity:
            tally["grouping has no exactMatch MONDO mapping (skipped)"] += 1
            continue
        g_term = identity[0]

        for member in grouping.get("members") or []:
            if member.get("member_type") not in (None, "DISEASE", "SUBTYPE"):
                continue
            m_term = terms.get(member.get("member"))
            if not m_term or not m_term.startswith("MONDO:"):
                tally["member has no MONDO disease_term"] += 1
                continue
            if m_term == g_term:
                verdict = "SAME_TERM"
            elif g_term in mondo.ancestors(m_term):
                verdict = "AGREES"
            elif m_term in mondo.ancestors(g_term):
                verdict = "REVERSED"
            else:
                verdict = "SILENT"
            tally[verdict] += 1
            if verdict in ("SILENT", "REVERSED"):
                rows.append(
                    {
                        "verdict": verdict,
                        "grouping": grouping.get("name") or Path(path).stem,
                        "grouping_term": g_term,
                        "grouping_label": mondo.label(g_term),
                        "member": member.get("member"),
                        "member_term": m_term,
                        "member_label": mondo.label(m_term),
                    }
                )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # explicit fieldnames: deriving them from rows[0] crashes on an empty result,
    # i.e. exactly when every grouping agrees with MONDO
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(FIELDNAMES), delimiter="\t")
        w.writeheader()
        w.writerows(
            sorted(rows, key=lambda r: (r["verdict"], r["grouping"], r["member"]))
        )

    for k, n in tally.most_common():
        print(f"  {n:4d}  {k}")
    print(f"\nwrote {len(rows)} violation rows -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
