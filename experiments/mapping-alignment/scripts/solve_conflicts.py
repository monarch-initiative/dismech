"""Hand each hierarchy conflict to pyboomer and record what it does with it.

For every conflict row from ``hierarchy_audit.py`` we assemble the three
assertion sets that bear on it and ask boomer whether they can hold together:

* **dismech**  -- ``subtype ProperSubClassOf parent`` (hard; it is what
  ``has_subtypes`` means)
* **MONDO**    -- the subsumption edges and ``owl:disjointWith`` axioms relating
  the two grounded terms (hard; we are testing dismech against MONDO, not
  auditing MONDO against itself)
* **mappings** -- the two identity claims, as probabilistic facts, each with the
  competing ``ProperSubClassOf`` readings in both directions

``REVERSED`` rows are unsatisfiable with both identity claims accepted: chaining
subtype < parent = MONDO-parent < MONDO-subtype = subtype yields subtype <
subtype, and ProperSubClassOf is irreflexive. Boomer has to retract one claim,
and which one it retracts is the useful output.

``SILENT`` rows are satisfiable as they stand -- MONDO simply does not relate the
two terms. For those the interesting question is the reverse: if we *proposed*
the missing ``is_a`` edge to MONDO, would it be consistent with what MONDO
already asserts? We add the proposed edge as a pfact and report whether boomer
can accept it.

Usage:
    uv run python experiments/mapping-alignment/scripts/solve_conflicts.py \
        --conflicts <run>/conflicts.tsv --out <run>/verdicts.tsv \
        --boomer-src ~/repos/boomer-py/src
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import io
import sqlite3
import sys
from collections import Counter
from pathlib import Path

MONDO_DB = Path.home() / ".data/oaklib/mondo.db"


def load_boomer(src):
    sys.path.insert(0, str(Path(src).expanduser()))
    from boomer.model import KB, SearchConfig
    from boomer.search import solve

    return KB, SearchConfig, solve


def build_kb(con, row):
    """Assemble the dismech + MONDO + mapping constraint set for one conflict."""
    child, parent = row["subtype_term"], row["parent_term"]
    d_child = f"dismech:{row['entry']}#{row['subtype']}"
    d_parent = f"dismech:{row['entry']}"

    facts = [
        # what has_subtypes asserts
        {"fact_type": "ProperSubClassOf", "sub": d_child, "sup": d_parent},
        # entities of a namespace are pairwise non-identical (subsumption still allowed)
        {"fact_type": "MemberOfDisjointGroup", "sub": child, "group": "MONDO"},
        {"fact_type": "MemberOfDisjointGroup", "sub": parent, "group": "MONDO"},
        {"fact_type": "MemberOfDisjointGroup", "sub": d_child, "group": "dismech"},
        {"fact_type": "MemberOfDisjointGroup", "sub": d_parent, "group": "dismech"},
    ]

    # MONDO's own subsumption between the two grounded terms, whichever way it runs
    for a, b in ((child, parent), (parent, child)):
        hit = con.execute(
            "select 1 from entailed_edge where subject=? and object=? "
            "and predicate='rdfs:subClassOf'",
            (a, b),
        ).fetchone()
        if hit:
            facts.append({"fact_type": "ProperSubClassOf", "sub": a, "sup": b})

    # MONDO disjointness touching either term
    for s, o in con.execute(
        "select subject,object from statements where predicate='owl:disjointWith' "
        "and subject in (?,?) and object in (?,?)",
        (child, parent, child, parent),
    ):
        facts.append({"fact_type": "DisjointWith", "sub": s, "sibling": o})

    pfacts = []
    for dis, mon in ((d_child, child), (d_parent, parent)):
        pfacts += [
            {
                "fact": {"fact_type": "EquivalentTo", "sub": dis, "equivalent": mon},
                "prob": 0.90,
            },
            {
                "fact": {"fact_type": "ProperSubClassOf", "sub": dis, "sup": mon},
                "prob": 0.07,
            },
            {
                "fact": {"fact_type": "ProperSubClassOf", "sub": mon, "sup": dis},
                "prob": 0.03,
            },
        ]
    if row["verdict"] == "SILENT":
        # the edge dismech's hierarchy implies MONDO ought to have
        pfacts.append(
            {
                "fact": {"fact_type": "ProperSubClassOf", "sub": child, "sup": parent},
                "prob": 0.60,
            }
        )
    return {
        "name": f"{row['entry']}--{row['subtype']}",
        "facts": facts,
        "pfacts": pfacts,
    }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--conflicts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--boomer-src", default="~/repos/boomer-py/src")
    ap.add_argument("--db", default=str(MONDO_DB))
    ap.add_argument("--timeout", type=int, default=20)
    args = ap.parse_args(argv)

    KB, SearchConfig, solve = load_boomer(args.boomer_src)
    con = sqlite3.connect(f"file:{args.db}?mode=ro", uri=True)
    cfg = SearchConfig(timeout_seconds=args.timeout)

    rows = list(csv.DictReader(open(args.conflicts), delimiter="\t"))
    out_rows, tally = [], Counter()
    for i, row in enumerate(rows, 1):
        kb = KB.model_validate(build_kb(con, row))
        with contextlib.redirect_stdout(io.StringIO()):
            sol = solve(kb, cfg)

        accepted = {
            (f.sub, f.equivalent)
            for gp in (sol.solved_pfacts or [])
            if gp.truth_value and type(f := gp.pfact.fact).__name__ == "EquivalentTo"
        }
        d_child = f"dismech:{row['entry']}#{row['subtype']}"
        d_parent = f"dismech:{row['entry']}"
        kept_child = (d_child, row["subtype_term"]) in accepted
        kept_parent = (d_parent, row["parent_term"]) in accepted

        if row["verdict"] == "REVERSED":
            outcome = (
                "BOTH_MAPPINGS_KEPT (unexpected)"
                if kept_child and kept_parent
                else f"RETRACTED_{'PARENT' if kept_child else 'SUBTYPE'}_MAPPING"
            )
        else:
            proposed = any(
                gp.truth_value
                and type(f := gp.pfact.fact).__name__ == "ProperSubClassOf"
                and f.sub == row["subtype_term"]
                and f.sup == row["parent_term"]
                for gp in (sol.solved_pfacts or [])
            )
            outcome = (
                "PROPOSED_EDGE_CONSISTENT" if proposed else "PROPOSED_EDGE_REJECTED"
            )

        tally[outcome] += 1
        out_rows.append(
            {
                **row,
                "outcome": outcome,
                "timed_out": bool(sol.timed_out),
                "n_pfacts": len(kb.pfacts),
            }
        )
        if i % 40 == 0:
            print(f"  {i}/{len(rows)}", file=sys.stderr)

    out = Path(args.out)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)

    print(
        f"solved {len(out_rows)} conflicts (timeouts: {sum(r['timed_out'] for r in out_rows)})"
    )
    for k, n in tally.most_common():
        print(f"  {n:5d}  {k}")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
