"""Generate one boomer analysis folder per grounded dismech disorder.

For every `kb/disorders/` entry whose `disease_term` and at least one
`has_subtypes[].subtype_term` are grounded in MONDO, this assembles a single
knowledge base holding everything that bears on that entry's grounding:

* **dismech** -- each `subtype ProperSubClassOf parent` edge (hard; it is what
  `has_subtypes` means), and namespace disjointness so two distinct entries
  cannot collapse into one
* **MONDO**   -- the subsumption edges and `owl:disjointWith` axioms relating the
  entry's term to each subtype's term (hard; we test dismech against MONDO, not
  MONDO against itself)
* **mappings** -- one identity claim per grounded term, as probabilistic facts,
  each with the competing `ProperSubClassOf` readings in both directions

One KB per *disorder* rather than per pair is deliberate: an entry's subtypes all
share a parent, so solving them together lets a conflict in one subtype bear on
the others. It also matches how a curator reads the result -- "what does boomer
say about this disease".

Each folder gets:

    README.md      what was checked, per-subtype verdicts, what boomer did
    kb.yaml        the boomer input, runnable as
                   `pyboomer solve kb.yaml -t 60 -C 6`
    solution.yaml  boomer's output, machine-readable
    solution.md    boomer's output, rendered

`-C 6` is not optional in the reproduction command. The partitioning that makes
these KBs tractable is a solver setting, not something serialised into kb.yaml, so
a plain `pyboomer solve kb.yaml` runs at boomer's default and times out on
anything past a handful of subtypes. The CLI has no flag for
`partition_initial_threshold`, but `--max-pfacts-per-clique` triggers the same
partitioning and reproduces these results exactly.

Usage:
    uv run --with networkx python analyses/boomer/scripts/build_analyses.py \
        --out analyses/boomer/disorders --boomer-src ~/repos/boomer-py/src
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import glob
import io
import json
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import yaml

MONDO_DB = Path.home() / ".data/oaklib/mondo.db"
REPO = Path(__file__).resolve().parents[3]

# prior that a curated mapping means identity, and the competing readings
P_IDENTITY = 0.90
P_NARROWER = 0.07
P_BROADER = 0.03


def load_boomer(src):
    sys.path.insert(0, str(Path(src).expanduser()))
    from boomer.model import KB, SearchConfig
    from boomer.renderers.markdown_renderer import MarkdownRenderer
    from boomer.renderers.yaml_renderer import YAMLRenderer
    from boomer.search import solve

    return KB, SearchConfig, solve, MarkdownRenderer, YAMLRenderer


def term_id(descriptor):
    if not isinstance(descriptor, dict):
        return None
    return (descriptor.get("term") or {}).get("id") or descriptor.get("id")


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

    def disjoint_pairs(self, curies):
        placeholders = ",".join("?" * len(curies))
        return list(
            self.con.execute(
                f"select subject,object from statements where predicate='owl:disjointWith' "
                f"and subject in ({placeholders}) and object in ({placeholders})",
                (*curies, *curies),
            )
        )


def verdict_for(mondo, child, parent):
    if child == parent:
        return "SAME_TERM"
    if parent in mondo.ancestors(child):
        return "AGREES"
    if child in mondo.ancestors(parent):
        return "REVERSED"
    return "SILENT"


def collect(kb_glob, mondo):
    """Yield one record per disorder that has at least one grounded subtype pair."""
    for path in sorted(glob.glob(kb_glob)):
        data = yaml.safe_load(open(path)) or {}
        if not isinstance(data, dict):
            continue
        parent_term = term_id(data.get("disease_term"))
        if not parent_term or not parent_term.startswith("MONDO:"):
            continue
        pairs = []
        for subtype in data.get("has_subtypes") or []:
            child = term_id(subtype.get("subtype_term"))
            if child and child.startswith("MONDO:"):
                pairs.append(
                    {
                        "subtype": subtype.get("name"),
                        "term": child,
                        "label": mondo.label(child),
                        "verdict": verdict_for(mondo, child, parent_term),
                    }
                )
        if pairs:
            yield {
                "slug": Path(path).stem,
                "name": data.get("name") or Path(path).stem,
                "parent_term": parent_term,
                "parent_label": mondo.label(parent_term),
                "pairs": pairs,
            }


def build_kb_dict(mondo, rec):
    d_parent = f"dismech:{rec['slug']}"
    terms = {rec["parent_term"], *(p["term"] for p in rec["pairs"])}

    facts, seen = [], set()

    def add(fact):
        key = json.dumps(fact, sort_keys=True)
        if key not in seen:
            seen.add(key)
            facts.append(fact)

    add({"fact_type": "MemberOfDisjointGroup", "sub": d_parent, "group": "dismech"})
    for term in sorted(terms):
        add({"fact_type": "MemberOfDisjointGroup", "sub": term, "group": "MONDO"})

    labels = {
        d_parent: f"{rec['name']} (dismech entry)",
        rec["parent_term"]: rec["parent_label"],
    }
    pfacts = [
        {
            "fact": {
                "fact_type": "EquivalentTo",
                "sub": d_parent,
                "equivalent": rec["parent_term"],
            },
            "prob": P_IDENTITY,
        },
        {
            "fact": {
                "fact_type": "ProperSubClassOf",
                "sub": d_parent,
                "sup": rec["parent_term"],
            },
            "prob": P_NARROWER,
        },
        {
            "fact": {
                "fact_type": "ProperSubClassOf",
                "sub": rec["parent_term"],
                "sup": d_parent,
            },
            "prob": P_BROADER,
        },
    ]

    for pair in rec["pairs"]:
        d_child = f"dismech:{rec['slug']}#{pair['subtype']}"
        labels[d_child] = f"{rec['name']} / {pair['subtype']} (dismech subtype)"
        labels[pair["term"]] = pair["label"]
        add({"fact_type": "MemberOfDisjointGroup", "sub": d_child, "group": "dismech"})
        add({"fact_type": "ProperSubClassOf", "sub": d_child, "sup": d_parent})
        # MONDO's own opinion about this subtype term vs the entry's term
        for a, b in (
            (pair["term"], rec["parent_term"]),
            (rec["parent_term"], pair["term"]),
        ):
            if a != b and b in mondo.ancestors(a):
                add({"fact_type": "ProperSubClassOf", "sub": a, "sup": b})
        pfacts += [
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": d_child,
                    "equivalent": pair["term"],
                },
                "prob": P_IDENTITY,
            },
            {
                "fact": {
                    "fact_type": "ProperSubClassOf",
                    "sub": d_child,
                    "sup": pair["term"],
                },
                "prob": P_NARROWER,
            },
            {
                "fact": {
                    "fact_type": "ProperSubClassOf",
                    "sub": pair["term"],
                    "sup": d_child,
                },
                "prob": P_BROADER,
            },
        ]

    for s, o in mondo.disjoint_pairs(sorted(terms)):
        add({"fact_type": "DisjointWith", "sub": s, "sibling": o})

    return {
        "name": f"dismech-{rec['slug']}",
        "description": (
            f"Grounding check for the dismech entry {rec['name']}: its "
            f"{len(rec['pairs'])} grounded subtype(s) against MONDO's hierarchy."
        ),
        "facts": facts,
        "pfacts": pfacts,
        "labels": labels,
    }


VERDICT_NOTE = {
    "AGREES": "MONDO has this subtype's term as a descendant of the entry's term.",
    "SILENT": "MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.",
    "REVERSED": "MONDO has the entry's term as a descendant of this subtype's term - backwards from dismech.",
    "SAME_TERM": "Subtype and entry are grounded to the same MONDO term.",
}


def write_readme(folder, rec, sol, retracted, timed_out):
    counts = Counter(p["verdict"] for p in rec["pairs"])
    lines = [
        f"# {rec['name']}",
        "",
        (
            f"Boomer grounding analysis for [`kb/disorders/{rec['slug']}.yaml`]"
            f"(../../../../kb/disorders/{rec['slug']}.yaml)."
        ),
        "",
        (
            f"- **Entry term:** [`{rec['parent_term']}`]"
            f"(http://purl.obolibrary.org/obo/{rec['parent_term'].replace(':', '_')}) "
            f"{rec['parent_label']}"
        ),
        f"- **Grounded subtypes:** {len(rec['pairs'])}",
        "- **Verdicts:** " + ", ".join(f"{v} {n}" for v, n in counts.most_common()),
        "",
        "## Subtypes",
        "",
        "| Subtype | MONDO term | Label | Verdict |",
        "|---|---|---|---|",
    ]
    for pair in rec["pairs"]:
        lines.append(
            f"| {pair['subtype']} | `{pair['term']}` | {pair['label']} | `{pair['verdict']}` |"
        )

    lines += ["", "## What boomer did", ""]
    if timed_out:
        lines += [
            "The search **timed out**, so the assignment below is the best found within the",
            "budget rather than a settled result. Treat it as indicative only.",
            "",
        ]
    if retracted:
        lines += [
            "Boomer could **not** accept every mapping at once and retracted the following",
            "identity claim(s) to restore consistency:",
            "",
        ]
        lines += [f"- `{sub}` ≡ `{obj}`" for sub, obj in retracted]
        lines += [
            "",
            "A retraction means these assertions are jointly unsatisfiable, not that the",
            "retracted mapping is necessarily the wrong one. Which assertion to give up is a",
            "curation decision.",
            "",
        ]
    else:
        lines += [
            "All identity mappings were accepted together - dismech's subtype hierarchy, the",
            "mappings, and MONDO's hierarchy are jointly consistent for this entry.",
            "",
        ]
    if counts.get("SILENT"):
        lines += [
            f"{counts['SILENT']} subtype(s) are `SILENT`: MONDO asserts no path between the",
            "terms in either direction. That is consistent (nothing is violated) but",
            "uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather",
            "than a dismech error. These are candidate MONDO enrichment proposals.",
            "",
        ]

    lines += [
        "## Verdict meanings",
        "",
        *[f"- **`{k}`** - {v}" for k, v in VERDICT_NOTE.items() if counts.get(k)],
        "",
        "## Files",
        "",
        "| File | What |",
        "|---|---|",
        (
            "| [`kb.yaml`](kb.yaml) | Boomer input. Run with "
            "`pyboomer solve kb.yaml -t 60 -C 6`. |"
        ),
        "| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |",
        "| [`solution.md`](solution.md) | Boomer output, rendered. |",
        "",
        "Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).",
        "",
    ]
    (folder / "README.md").write_text("\n".join(lines))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb", default=str(REPO / "kb/disorders/*.yaml"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--db", default=str(MONDO_DB))
    ap.add_argument("--boomer-src", default="~/repos/boomer-py/src")
    ap.add_argument("--timeout", type=int, default=60)
    ap.add_argument(
        "--partition-threshold",
        type=int,
        default=6,
        help=(
            "Minimum pfacts before boomer partitions the KB into independent cliques. "
            "boomer's own default is 200, which never triggers at this scale and makes "
            "even a 12-pfact KB time out; the subtypes of one entry are largely "
            "independent, so splitting them is both sound and orders of magnitude faster."
        ),
    )
    ap.add_argument("--only", help="restrict to one slug (for debugging)")
    ap.add_argument("--index", help="TSV index to write")
    args = ap.parse_args(argv)

    KB, SearchConfig, solve, MarkdownRenderer, YAMLRenderer = load_boomer(
        args.boomer_src
    )
    mondo = Mondo(args.db)
    cfg = SearchConfig(
        timeout_seconds=args.timeout,
        partition_initial_threshold=args.partition_threshold,
    )
    out_root = Path(args.out)
    out_root.mkdir(parents=True, exist_ok=True)

    index, tally = [], Counter()
    records = [
        r for r in collect(args.kb, mondo) if not args.only or r["slug"] == args.only
    ]
    for i, rec in enumerate(records, 1):
        kb_dict = build_kb_dict(mondo, rec)
        kb = KB.model_validate(kb_dict)
        with contextlib.redirect_stdout(io.StringIO()):
            sol = solve(kb, cfg)
        # the markdown renderer titles the solution from this; unset it renders "## None"
        sol.name = kb_dict["name"]

        retracted = sorted(
            (f.sub, f.equivalent)
            for gp in (sol.solved_pfacts or [])
            if type(f := gp.pfact.fact).__name__ == "EquivalentTo"
            and not gp.truth_value
        )
        timed_out = bool(sol.timed_out)

        folder = out_root / rec["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "kb.yaml").write_text(yaml.safe_dump(kb_dict, sort_keys=False))
        (folder / "solution.yaml").write_text(YAMLRenderer().render(sol, kb))
        (folder / "solution.md").write_text(MarkdownRenderer().render(sol, kb))
        write_readme(folder, rec, sol, retracted, timed_out)

        counts = Counter(p["verdict"] for p in rec["pairs"])
        status = (
            "TIMED_OUT"
            if timed_out
            else ("RETRACTED" if retracted else "ALL_MAPPINGS_CONSISTENT")
        )
        tally[status] += 1
        for verdict, n in counts.items():
            tally[f"pair:{verdict}"] += n
        index.append(
            {
                "slug": rec["slug"],
                "name": rec["name"],
                "parent_term": rec["parent_term"],
                "n_subtypes": len(rec["pairs"]),
                "n_pfacts": len(kb.pfacts),
                "agrees": counts.get("AGREES", 0),
                "silent": counts.get("SILENT", 0),
                "reversed": counts.get("REVERSED", 0),
                "same_term": counts.get("SAME_TERM", 0),
                "status": status,
                "n_retracted": len(retracted),
            }
        )
        if i % 50 == 0:
            print(f"  {i}/{len(records)}", file=sys.stderr)

    if args.index:
        with Path(args.index).open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(index[0]), delimiter="\t")
            w.writeheader()
            w.writerows(index)

    print(f"wrote {len(index)} disorder folders -> {out_root}")
    for k, n in sorted(tally.items()):
        print(f"  {n:5d}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
