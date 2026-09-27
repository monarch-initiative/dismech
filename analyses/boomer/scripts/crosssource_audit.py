"""Compare dismech's direct external-vocabulary mappings against MONDO's own xrefs.

A dismech entry can reach an external vocabulary two ways:

* **directly** -- ``mappings.icd10cm_mappings`` / ``icd11f_mappings`` /
  ``ncit_mappings`` on the entry
* **transitively** -- through its ``disease_term``, since MONDO carries its own
  ``skos:exactMatch`` and ``oio:hasDbXref`` links to OMIM, ORDO, DOID, UMLS,
  SNOMED, ICD and NCIT

Where both routes reach the *same vocabulary* but land on *different* terms, the
two assertions compete. This script reports those cases.

Prefixes are normalised before comparison because the two sources spell the same
vocabulary differently (dismech ``icd11f:`` vs MONDO ``icd11.foundation:``;
MONDO ``Orphanet:`` vs ``ORDO:``). WHO ICD-10 and ICD-10-CM remain distinct.

**Read the output with care.** Most hits are granularity differences rather than
contradictions. A broadMatch to a parent category can coexist with an exactMatch
to its child. The ``both_exact`` column flags competing exact assertions for
review; distinct identifiers alone do not prove logical inconsistency.

Usage:
    uv run python analyses/boomer/scripts/crosssource_audit.py \
        --out analyses/boomer/cross-source/disagreements.tsv
"""

from __future__ import annotations

import argparse
import csv
import glob
import sqlite3
import sys
from pathlib import Path

MONDO_DB = Path.home() / ".data/oaklib/mondo.db"
REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO / "src"))
from dismech import kb_cache

# collapse the spelling differences between the two sources
PREFIX_ALIASES = {
    "icd11f": "ICD11",
    "icd11.foundation": "ICD11",
    "ICD-10": "ICD10",
    "ICD10": "ICD10",
    "Orphanet": "ORPHA",
    "ORDO": "ORPHA",
}


FIELDNAMES = (
    "entry",
    "vocabulary",
    "dismech_term",
    "dismech_predicate",
    "mondo_term",
    "mondo_label",
    "mondo_xrefs",
    "both_exact",
)


def term_id(descriptor):
    if not isinstance(descriptor, dict):
        return None
    return (descriptor.get("term") or {}).get("id") or descriptor.get("id")


def normalise(curie):
    prefix, _, local = curie.partition(":")
    return f"{PREFIX_ALIASES.get(prefix, prefix)}:{local}"


def mondo_xrefs(con, curie):
    """Return (all_xrefs, exact_only).

    Kept separate because ``oio:hasDbXref`` is a cross-reference of unstated
    strength while ``skos:exactMatch`` is an identity claim. Unioning them and
    then calling the result "exact" would overstate the MONDO side.
    """
    exact = {
        normalise(o)
        for (o,) in con.execute(
            "select object from statements where subject=? and predicate='skos:exactMatch' "
            "and object is not null",
            (curie,),
        )
    }
    dbxref = {
        normalise(v)
        for (v,) in con.execute(
            "select value from statements where subject=? and predicate='oio:hasDbXref' "
            "and value is not null",
            (curie,),
        )
    }
    return exact | dbxref, exact


def main(argv=None):
    kb_cache.default_off()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb", default=str(REPO / "kb/disorders/*.yaml"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--db", default=str(MONDO_DB))
    args = ap.parse_args(argv)

    con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)

    def label(curie):
        row = con.execute(
            "select value from statements where subject=? and predicate='rdfs:label'",
            (curie,),
        ).fetchone()
        return row[0] if row else curie

    rows = []
    for path in sorted(glob.glob(args.kb)):
        data = kb_cache.load_document(path) or {}
        if not isinstance(data, dict):
            continue
        mondo = term_id(data.get("disease_term"))
        if not mondo or not mondo.startswith("MONDO:"):
            continue
        direct = []
        for key, items in (data.get("mappings") or {}).items():
            if key == "mondo_mappings":
                continue
            for item in items or []:
                if curie := term_id(item):
                    direct.append((curie, item.get("mapping_predicate")))
        if not direct:
            continue

        xrefs, exact_xrefs = mondo_xrefs(con, mondo)
        for curie, predicate in direct:
            vocab = normalise(curie).split(":")[0]
            mondo_side = sorted(x for x in xrefs if x.startswith(vocab + ":"))
            if not mondo_side or normalise(curie) in mondo_side:
                continue
            rows.append(
                {
                    "entry": Path(path).stem,
                    "vocabulary": vocab,
                    "dismech_term": curie,
                    "dismech_predicate": predicate,
                    "mondo_term": mondo,
                    "mondo_label": label(mondo),
                    "mondo_xrefs": ";".join(mondo_side),
                    # true only when BOTH sides claim identity: dismech exactMatch,
                    # and a MONDO skos:exactMatch (not merely an oio:hasDbXref)
                    "both_exact": str(
                        predicate == "skos:exactMatch"
                        and any(x.startswith(vocab + ":") for x in exact_xrefs)
                    ).lower(),
                }
            )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        # explicit fieldnames: deriving them from rows[0] crashes on an empty result,
        # i.e. exactly when dismech and MONDO agree everywhere
        w = csv.DictWriter(fh, fieldnames=list(FIELDNAMES), delimiter="\t")
        w.writeheader()
        w.writerows(
            sorted(rows, key=lambda r: (r["both_exact"] == "false", r["entry"]))
        )

    n_exact = sum(r["both_exact"] == "true" for r in rows)
    print(f"cross-vocabulary disagreements: {len(rows)}")
    print(f"  competing exact assertions to review: {n_exact}")
    print(
        f"  dismech side is close/narrow/broadMatch (usually granularity): {len(rows) - n_exact}"
    )
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
