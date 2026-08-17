"""Audit dismech's subtype hierarchy against MONDO's.

A dismech entry that declares ``has_subtypes`` asserts a real subsumption:
the subtype is a kind of the parent entry. When both the parent's
``disease_term`` and the subtype's ``subtype_term`` are grounded in MONDO, that
assertion becomes checkable -- MONDO should agree that the subtype's term is a
descendant of the parent's term.

Three ways it can fail to agree:

``AGREES``      MONDO has subtype_term as a descendant of disease_term. Nothing to do.
``SILENT``      MONDO relates them in neither direction. Usually a *MONDO* gap --
                a missing ``is_a`` edge -- not a dismech error.
``REVERSED``    MONDO says the parent's term is a descendant of the subtype's term,
                i.e. exactly backwards from dismech. Combined with the two identity
                mappings this is genuinely unsatisfiable.

Usage:
    uv run python experiments/mapping-alignment/scripts/hierarchy_audit.py \
        --out experiments/mapping-alignment/<run>/conflicts.tsv
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


def term_id(descriptor):
    """Pull the CURIE out of a dismech descriptor (``{term: {id: ...}}``)."""
    if not isinstance(descriptor, dict):
        return None
    return (descriptor.get("term") or {}).get("id") or descriptor.get("id")


class Mondo:
    """Thin cached reader over the semantic-sql MONDO build."""

    def __init__(self, db=MONDO_DB):
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
        """Entailed MONDO superclasses (reflexive closure excluded)."""
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


def collect_pairs(kb_glob):
    """Yield (slug, subtype_name, subtype_term, parent_term) for grounded pairs."""
    for path in sorted(glob.glob(kb_glob)):
        data = yaml.safe_load(open(path)) or {}
        if not isinstance(data, dict):
            continue
        slug = Path(path).stem
        parent = term_id(data.get("disease_term"))
        if not parent or not parent.startswith("MONDO:"):
            continue
        for subtype in data.get("has_subtypes") or []:
            child = term_id(subtype.get("subtype_term"))
            if child and child.startswith("MONDO:"):
                yield slug, subtype.get("name"), child, parent


def classify(mondo, child, parent):
    if child == parent:
        return "SAME_TERM"
    if parent in mondo.ancestors(child):
        return "AGREES"
    if child in mondo.ancestors(parent):
        return "REVERSED"
    return "SILENT"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb", default=str(REPO / "kb/disorders/*.yaml"))
    ap.add_argument("--out", required=True, help="TSV to write")
    ap.add_argument("--db", default=str(MONDO_DB))
    args = ap.parse_args(argv)

    mondo = Mondo(args.db)
    rows, tally = [], Counter()
    for slug, name, child, parent in collect_pairs(args.kb):
        verdict = classify(mondo, child, parent)
        tally[verdict] += 1
        if verdict in ("SILENT", "REVERSED"):
            rows.append(
                {
                    "verdict": verdict,
                    "entry": slug,
                    "subtype": name,
                    "subtype_term": child,
                    "subtype_label": mondo.label(child),
                    "parent_term": parent,
                    "parent_label": mondo.label(parent),
                }
            )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(
            sorted(rows, key=lambda r: (r["verdict"], r["entry"], r["subtype"] or ""))
        )

    total = sum(tally.values())
    print(f"grounded parent/subtype pairs: {total}")
    for verdict, n in tally.most_common():
        print(f"  {n:5d}  {verdict}")
    print(f"\nwrote {len(rows)} conflict rows -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
