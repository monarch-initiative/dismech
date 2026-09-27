#!/usr/bin/env python3
"""Census of how far estrogen signalling is curated in dismech.

The question this answers is "the corpus talks about estrogen constantly, but
where does it actually bind the receptor?" It is answered in six deterministic
tiers over ``kb/disorders/``, from loosest to strictest, so the shape of the gap
is visible rather than asserted:

1. ``MENTIONS_ESTROGEN`` -- some string anywhere in the entry names estrogen,
   estradiol, estrone or estriol (either spelling), or uses the ER-alpha /
   ER-beta receptor notation.
2. ``NODE_INVOKES`` -- the same test restricted to strings under
   ``pathophysiology:``, so the entry does not merely mention estrogen in a
   treatment or a quoted abstract but builds a mechanism node around it.
3. ``GO_BOUND`` -- the entry binds ``GO:0030520`` *estrogen receptor signaling
   pathway* somewhere.
4. ``RECEPTOR_NAMED`` -- the entry names the receptor in prose or in a quoted
   snippet, either by gene symbol (``ESR1`` / ``ESR2``) or by the phrase
   "estrogen receptor".
5. ``GENE_BOUND`` -- the entry binds ``hgnc:3467`` (ESR1) or ``hgnc:3468``
   (ESR2) as an ontology term anywhere, including in ``genetic:``.
6. ``GENE_ON_NODE`` -- a ``pathophysiology[]`` node carries a ``genes:``
   descriptor bound to one of those two CURIEs, so the receptor reaches the
   pathograph rather than sitting in a genetics list.

The tiers are *not* strictly nested. An entry can bind ``GO:0030520`` without
naming the receptor, and can name the receptor without binding the pathway, so
each tier is counted independently and the report shows the overlaps.

The gap this was written to measure is between tiers 3 and 6: the pathway is
annotated on a node and the receptor driving it is not. See issue #12925.

Counts move with every curation PR. The script is the deliverable; any number
in a committed report is a dated snapshot.

Usage:
    uv run python scripts/estrogen_signalling_census.py              # markdown
    uv run python scripts/estrogen_signalling_census.py --format tsv
    uv run python scripts/estrogen_signalling_census.py --json
    uv run python scripts/estrogen_signalling_census.py --out docs/reports/x.md

Offline. Reads only committed YAML; no ontology adapter and no network.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from collections.abc import Iterator
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from dismech import kb_cache

ROOT = Path(__file__).resolve().parent.parent
DISORDERS_DIR = ROOT / "kb" / "disorders"
MODULES_DIR = ROOT / "kb" / "modules"

# Tier 1. Both spellings of the hormone family, plus the ER-alpha / ER-beta
# notation papers use for the receptor proteins. Deliberately a substring test
# with no leading \w*, so "antiestrogen" and "hyperestrogenism" match while
# "sequestration" (whose "estr" is preceded by "u") does not.
ESTROGEN_RE = re.compile(r"(?i)o?estr(?:ogen|adiol|one|iol)|ER-?(?:alpha|beta)\b|ER[αβ]")

# Tier 4. The receptor named as such: gene symbol, or the phrase. \s+ rather
# than a literal space because a YAML folded scalar joins a line break into a
# space, so the phrase can be split across source lines: a line-based grep
# misses CHEK2-related_Cancer_Predisposition, the parsed document does not.
RECEPTOR_RE = re.compile(r"(?i)\bESR[12]\b|o?estrogen\s+receptor")

# Tier 3 / 5. Verified against cache/go/terms.csv and cache/hgnc/terms.csv
# rather than written from memory.
GO_ESTROGEN_SIGNALLING = "GO:0030520"  # estrogen receptor signaling pathway
ESR_CURIES = {"hgnc:3467": "ESR1", "hgnc:3468": "ESR2"}

# Counts reported in issue #12925, measured on commit 94591e52d4. These are
# fixed historical figures, not a target: they are kept so that a regenerated
# report always shows how far the corpus has moved since the gap was described.
#
# RECEPTOR_NAMED is the one tier where this script and the issue disagree about
# the same tree, by one entry. The issue's figure came from a line-based search;
# CHEK2-related_Cancer_Predisposition writes "oestrogen receptor" in a folded
# scalar that splits the phrase across two source lines, so a line-based search
# misses it and a parse of the document does not. 30 is the correct count.
BASELINE_COMMIT = "94591e52d4"
BASELINE_COUNTS = {
    "MENTIONS_ESTROGEN": 115,
    "NODE_INVOKES": 57,
    "GO_BOUND": 12,
    "RECEPTOR_NAMED": 29,
    "GENE_BOUND": 6,
    "GENE_ON_NODE": 1,
}

TIERS = (
    "MENTIONS_ESTROGEN",
    "NODE_INVOKES",
    "GO_BOUND",
    "RECEPTOR_NAMED",
    "GENE_BOUND",
    "GENE_ON_NODE",
)


@dataclass
class Entry:
    slug: str
    tiers: dict[str, bool]
    go_nodes: list[str] = field(default_factory=list)
    gene_node_symbols: list[str] = field(default_factory=list)
    gene_bound_symbols: list[str] = field(default_factory=list)

    @property
    def is_gap(self) -> bool:
        """Binds the pathway on a node but puts no receptor gene on any node."""
        return self.tiers["GO_BOUND"] and not self.tiers["GENE_ON_NODE"]


def walk_strings(node: Any) -> Iterator[str]:
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for value in node.values():
            yield from walk_strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_strings(value)


def walk_term_ids(node: Any) -> Iterator[str]:
    """Yield every ``term.id`` string below ``node``."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "term" and isinstance(value, dict):
                term_id = value.get("id")
                if isinstance(term_id, str):
                    yield term_id
            yield from walk_term_ids(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_term_ids(value)


def matches(pattern: re.Pattern[str], node: Any) -> bool:
    return any(pattern.search(text) for text in walk_strings(node))


def esr_curies_in(node: Any) -> list[str]:
    found = {
        ESR_CURIES[term_id.lower()]
        for term_id in walk_term_ids(node)
        if term_id.lower() in ESR_CURIES
    }
    return sorted(found)


def assess(slug: str, document: Any) -> Entry | None:
    if not isinstance(document, dict):
        return None
    nodes = document.get("pathophysiology") or []
    if not isinstance(nodes, list):
        nodes = []

    go_nodes = [
        str(node.get("name", "<unnamed>"))
        for node in nodes
        if isinstance(node, dict) and GO_ESTROGEN_SIGNALLING in set(walk_term_ids(node))
    ]
    go_bound_anywhere = GO_ESTROGEN_SIGNALLING in set(walk_term_ids(document))

    gene_node_symbols: set[str] = set()
    for node in nodes:
        if isinstance(node, dict):
            gene_node_symbols.update(esr_curies_in(node.get("genes") or []))

    gene_bound_symbols = esr_curies_in(document)

    return Entry(
        slug=slug,
        tiers={
            "MENTIONS_ESTROGEN": matches(ESTROGEN_RE, document),
            "NODE_INVOKES": matches(ESTROGEN_RE, nodes),
            "GO_BOUND": go_bound_anywhere,
            "RECEPTOR_NAMED": matches(RECEPTOR_RE, document),
            "GENE_BOUND": bool(gene_bound_symbols),
            "GENE_ON_NODE": bool(gene_node_symbols),
        },
        go_nodes=sorted(go_nodes),
        gene_node_symbols=sorted(gene_node_symbols),
        gene_bound_symbols=gene_bound_symbols,
    )


def collect(directory: Path) -> list[Entry]:
    entries: list[Entry] = []
    for path, document in kb_cache.iter_documents(directory):
        entry = assess(path.stem, document)
        if entry is not None:
            entries.append(entry)
    return entries


# Fields that reproduce an external source verbatim. A mention confined to
# these means the module cites a paper about the receptor; it does not mean the
# module models the receptor.
QUOTED_FIELDS = {"reference_title", "snippet"}


def strip_quoted(node: Any) -> Any:
    """Return ``node`` with every quoted-source field removed."""
    if isinstance(node, dict):
        return {k: strip_quoted(v) for k, v in node.items() if k not in QUOTED_FIELDS}
    if isinstance(node, list):
        return [strip_quoted(v) for v in node]
    return node


def module_survey() -> list[tuple[str, bool, bool, bool]]:
    """(stem, named in module prose, binds GO:0030520, binds ESR1/ESR2) per module."""
    rows = []
    for path, document in kb_cache.iter_documents(MODULES_DIR):
        if not isinstance(document, dict):
            continue
        mentions = matches(ESTROGEN_RE, document) or matches(RECEPTOR_RE, document)
        if not mentions:
            continue
        own = strip_quoted(document)
        in_prose = matches(ESTROGEN_RE, own) or matches(RECEPTOR_RE, own)
        term_ids = set(walk_term_ids(document))
        rows.append(
            (
                path.stem,
                in_prose,
                GO_ESTROGEN_SIGNALLING in term_ids,
                bool(esr_curies_in(document)),
            )
        )
    return sorted(rows)


TIER_BLURB = {
    "MENTIONS_ESTROGEN": "names estrogen/estradiol/estrone/estriol or ER-alpha/ER-beta anywhere",
    "NODE_INVOKES": "the same, restricted to `pathophysiology:`",
    "GO_BOUND": f"binds `{GO_ESTROGEN_SIGNALLING}` estrogen receptor signaling pathway",
    "RECEPTOR_NAMED": "names `ESR1`/`ESR2` or the phrase “estrogen receptor”",
    "GENE_BOUND": "binds `hgnc:3467` (ESR1) or `hgnc:3468` (ESR2) anywhere",
    "GENE_ON_NODE": "binds either gene in a `genes:` descriptor on a pathophysiology node",
}


def render_markdown(entries: list[Entry], modules: list[tuple[str, bool, bool, bool]]) -> str:
    counts = Counter()
    for entry in entries:
        for tier, hit in entry.tiers.items():
            if hit:
                counts[tier] += 1

    total = len(entries)
    gaps = sorted((e for e in entries if e.is_gap), key=lambda e: e.slug)
    genetics_only = sorted(
        (e for e in entries if e.tiers["GENE_BOUND"] and not e.tiers["GENE_ON_NODE"]),
        key=lambda e: e.slug,
    )

    out: list[str] = []
    out.append("# Estrogen signalling coverage census")
    out.append("")
    out.append(
        "Where estrogen signalling is curated in `kb/disorders/`, counted in six "
        "tiers from loosest to strictest. Regenerate with "
        "`just estrogen-census`; the counts move with every curation PR, so "
        "treat the numbers here as a dated snapshot and the script as the "
        "deliverable. Background: issue #12925."
    )
    out.append("")
    out.append(f"Entries scanned: **{total}**.")
    out.append("")
    out.append("| Tier | Test | Entries | Share |")
    out.append("| --- | --- | ---: | ---: |")
    for tier in TIERS:
        pct = (100.0 * counts[tier] / total) if total else 0.0
        out.append(f"| `{tier}` | {TIER_BLURB[tier]} | {counts[tier]} | {pct:.1f}% |")
    out.append("")
    out.append(
        "The tiers are not strictly nested. An entry can bind the pathway "
        "without naming the receptor, and can name the receptor without "
        "binding the pathway, so each row is counted independently."
    )
    out.append("")

    out.append(f"### Drift since commit `{BASELINE_COMMIT}`")
    out.append("")
    out.append(
        "The baseline column is the figure reported in issue #12925 when the gap "
        "was described. Any difference is ordinary curation drift, except as "
        "noted below the table."
    )
    out.append("")
    out.append("| Tier | Baseline | Now | Change |")
    out.append("| --- | ---: | ---: | ---: |")
    for tier in TIERS:
        base = BASELINE_COUNTS[tier]
        delta = counts[tier] - base
        out.append(f"| `{tier}` | {base} | {counts[tier]} | {delta:+d} |")
    out.append("")
    out.append(
        "One of those differences is not drift. `RECEPTOR_NAMED` was measured "
        "with a line-based search, which misses "
        "`CHEK2-related_Cancer_Predisposition`: it writes \u201coestrogen receptor\u201d "
        "in a folded scalar, so the phrase is split across two source lines and "
        "only exists once the document is parsed. Re-measuring the baseline tree "
        "with this script gives 30, not 29."
    )
    out.append("")

    out.append("## The gap this was written to measure")
    out.append("")
    out.append(
        f"{len(gaps)} entries bind `{GO_ESTROGEN_SIGNALLING}` on a node while putting no "
        "receptor gene on any node. The pathway is annotated and the receptor "
        "driving it is not."
    )
    out.append("")
    out.append("| Entry | Node(s) binding the pathway |")
    out.append("| --- | --- |")
    for entry in gaps:
        nodes = "; ".join(entry.go_nodes) if entry.go_nodes else "_(bound outside a node)_"
        out.append(f"| `{entry.slug}` | {nodes} |")
    out.append("")
    out.append(
        "Each row is a research task, not a mechanical backfill. A `genes:` "
        "descriptor asserts that this receptor drives this mechanism in this "
        "disease, and some of these nodes are loss-of-signalling or "
        "ligand-supply claims where an ESR1 binding would be wrong. Deciding "
        "not to bind, with the reason recorded in `notes`, is a closed task."
    )
    out.append("")

    out.append("## Receptor bound, but off the pathograph")
    out.append("")
    out.append(
        f"{len(genetics_only)} entries bind ESR1 or ESR2 somewhere without the gene "
        "reaching a pathophysiology node. These are typically susceptibility "
        "polymorphisms in `genetic:`, where a genotype-association paper may "
        "legitimately stop short of supporting a causal edge."
    )
    out.append("")
    out.append("| Entry | Gene(s) bound |")
    out.append("| --- | --- |")
    for entry in genetics_only:
        out.append(f"| `{entry.slug}` | {', '.join(entry.gene_bound_symbols)} |")
    out.append("")

    on_node = sorted((e for e in entries if e.tiers["GENE_ON_NODE"]), key=lambda e: e.slug)
    out.append("## Receptor on the pathograph")
    out.append("")
    if on_node:
        for entry in on_node:
            out.append(f"- `{entry.slug}` — {', '.join(entry.gene_node_symbols)}")
    else:
        out.append("_None._")
    out.append("")

    out.append("## Modules")
    out.append("")
    gene_modules = [stem for stem, _, _, gene_bound in modules if gene_bound]
    if gene_modules:
        gene_sentence = "Modules binding either gene: " + ", ".join(
            f"`{stem}`" for stem in gene_modules
        ) + "."
    else:
        gene_sentence = "No module binds either gene."
    out.append(
        "Modules that mention estrogen or the receptor, and whether they bind "
        "it. \u201cIn module prose\u201d separates a module that models the receptor "
        "from one that merely cites a paper about it: a mention confined to "
        "`reference_title` or `snippet` is quoted source metadata, not a claim "
        f"the module makes. {gene_sentence} A module node binding "
        "is a design decision rather than a backfill, because a generic "
        "receptor binding may belong only in the conforming entries."
    )
    out.append("")
    out.append("| Module | In module prose | Binds `GO:0030520` | Binds ESR1/ESR2 |")
    out.append("| --- | --- | --- | --- |")
    for stem, in_prose, go_bound, gene_bound in modules:
        out.append(
            f"| `{stem}` | {'yes' if in_prose else 'quoted sources only'} | "
            f"{'yes' if go_bound else 'no'} | {'yes' if gene_bound else 'no'} |"
        )
    out.append("")
    return "\n".join(out)


def render_tsv(entries: list[Entry]) -> str:
    header = ["slug", *TIERS, "go_nodes", "genes_on_node", "genes_bound"]
    rows = ["\t".join(header)]
    for entry in sorted(entries, key=lambda e: e.slug):
        if not any(entry.tiers.values()):
            continue
        rows.append(
            "\t".join(
                [
                    entry.slug,
                    *("1" if entry.tiers[t] else "0" for t in TIERS),
                    "; ".join(entry.go_nodes),
                    ",".join(entry.gene_node_symbols),
                    ",".join(entry.gene_bound_symbols),
                ]
            )
        )
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", help="write here instead of stdout")
    parser.add_argument(
        "--format",
        choices=("markdown", "tsv"),
        default="markdown",
        help="output format (default: markdown)",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON instead")
    args = parser.parse_args(argv)

    # One walk of the corpus, so the shared parse cache is pure cost.
    kb_cache.default_off()

    entries = collect(DISORDERS_DIR)
    if args.json:
        payload = json.dumps([asdict(e) for e in entries if any(e.tiers.values())], indent=2)
    elif args.format == "tsv":
        payload = render_tsv(entries)
    else:
        payload = render_markdown(entries, module_survey())

    if args.out:
        Path(args.out).write_text(payload + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({len(entries)} entries scanned)", file=sys.stderr)
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
