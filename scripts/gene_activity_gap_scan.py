#!/usr/bin/env python3
"""Find pathograph edges that jump from a gene straight to a process node.

The pathograph draws an edge from a ``genetic:`` node to a ``pathophysiology``
node whenever the two share a gene (``src/dismech/graph.py``,
``pathophysiology_by_gene_key``). GO's own structure names three levels on that
path — **gene -> molecular function -> biological process** — and the
node-classification design
(``docs/superpowers/specs/2026-08-16-pathograph-node-classification-brainstorm.md``)
found the middle one, ACTIVITY, to be a real tier that curators had already
improvised without a slot to put it in.

This scan measures where that middle level is missing: a gene node whose first
mechanism node carries ``biological_processes:`` but no ``molecular_functions:``
is a **process jump** — the graph goes from the lesion to what the cell can no
longer do, skipping what the *protein* can no longer do.

Not every jump is a defect. Three things separate a fixable gap from a node that
is correctly process-level, and the scan reports all three rather than collapsing
them into a score:

* **How many genes the landing node carries.** One gene means the molecular
  function is unambiguous. Twenty-one genes (``Primary_Ciliary_Dyskinesia`` /
  "Ciliary Dysfunction") means the node bundles dynein ATPases, radial-spoke
  structural constituents and axonemal rulers, and *no* single MF term is
  correct — that is a debundle target, not an annotation gap.
* **Whether the activity claim is already in the prose.** Many landing nodes
  assert the molecular function in ``name`` or ``description`` and simply do not
  carry the term ("SLC25A20 transporter molecular function deficiency", whose
  description says "reduce ... carnitine-acylcarnitine translocase activity",
  annotated only with ``GO:0015879 carnitine transport``). Nothing new has to be
  established for those; the claim is curated, just unstructured.
* **How far the jump lands**, read off the GO seed table
  (``docs/superpowers/pathograph_node_class_go_seed.tsv``). Landing on an
  ACTIVITY-class BP term is barely a jump; landing on CELLULAR or TISSUE skips
  two or three tiers.

The ``verdict`` column is **advisory**, in the same sense as
``environmental-term-audit``'s reuse suggestions: it reads slot presence and
curator-written prose, never biology. A node can be legitimately process-level
with one gene — ``Autosomal_Recessive_Non-Syndromic_Intellectual_Disability``'s
"Loss of a Gene-Specific Molecular Function Required by Developing Neurons" says
in its own description that the class has no shared molecular function, which is
the finding, not a gap. Read the node before curating it.

Usage::

    uv run python scripts/gene_activity_gap_scan.py
    uv run python scripts/gene_activity_gap_scan.py --format tsv --out gaps.tsv
    uv run python scripts/gene_activity_gap_scan.py --verdict ANNOTATE_MF --format list
    uv run python scripts/gene_activity_gap_scan.py --format json --out gaps.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from dismech.graph import build_causal_graph  # noqa: E402
from dismech.yaml_io import safe_load  # noqa: E402

DEFAULT_KB_DIRS = ("kb/disorders", "kb/modules")
SEED_TABLE = Path("docs/superpowers/pathograph_node_class_go_seed.tsv")

#: Words that assert a molecular activity. Matched against the landing node's
#: name and description to find claims that are curated but unstructured.
ACTIVITY_PROSE = re.compile(
    r"\b(activity|catalytic|catalys\w*|catalyz\w*|enzymatic|enzyme|kinase|phosphatase|"
    r"protease|peptidase|hydrolase|transferase|dehydrogenase|synthase|synthetase|"
    r"carboxylase|oxidase|reductase|isomerase|ligase|channel|transporter|translocase|"
    r"permease|receptor|motor|ATPase|GTPase|helicase|conductance|turnover)\b",
    re.IGNORECASE,
)

#: Seed classes that sit at or below the activity tier -- landing on one of
#: these is a short jump, so the fix is a term on the existing node.
NEAR_MOLECULAR_CLASSES = frozenset({"ACTIVITY", "SUBSTANCE", "GENOMIC"})

VERDICTS = ("DEBUNDLE_FIRST", "ANNOTATE_MF", "INSERT_CHAIN", "INSERT_ACTIVITY_NODE")


@dataclass
class Jump:
    """One gene node -> process-only pathophysiology node landing."""

    entry: str
    path: str
    node: str
    genes: list[str] = field(default_factory=list)
    gene_nodes: list[str] = field(default_factory=list)
    bp_terms: list[str] = field(default_factory=list)
    landing_classes: list[str] = field(default_factory=list)
    activity_prose: bool = False
    activity_in_name: bool = False
    verdict: str = ""

    @property
    def n_genes(self) -> int:
        return len(self.genes)


def load_seed(path: Path) -> dict[str, str]:
    """Read the GO BP term -> node-class seed table, if it is present."""
    seed: dict[str, str] = {}
    if not path.exists():
        return seed
    for line in path.read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 5 or parts[0] == "go_id":
            continue
        seed[parts[0]] = parts[2]
    return seed


def _descriptor_terms(descriptors: Any) -> list[tuple[str | None, str | None]]:
    out: list[tuple[str | None, str | None]] = []
    for item in descriptors or []:
        if not isinstance(item, dict):
            continue
        term = item.get("term") if isinstance(item.get("term"), dict) else {}
        out.append((term.get("id"), term.get("label") or item.get("preferred_term")))
    return out


def _node_genes(node: dict[str, Any]) -> list[str]:
    """Gene symbols annotated on a pathophysiology node, deduplicated."""
    descriptors = list(node.get("genes") or [])
    if isinstance(node.get("gene"), dict):
        descriptors.append(node["gene"])
    symbols: list[str] = []
    for _curie, label in _descriptor_terms(descriptors):
        if label and label not in symbols:
            symbols.append(label)
    return symbols


def decide(jump: Jump) -> str:
    """Assign an advisory verdict. Order matters; the first rule that fits wins."""
    if jump.n_genes >= 2:
        # No single MF term is correct for a node carrying several unrelated
        # gene products. Splitting the node comes before annotating it.
        return "DEBUNDLE_FIRST"
    if set(jump.landing_classes) & NEAR_MOLECULAR_CLASSES or jump.activity_prose:
        # The activity is either already asserted in prose or barely a tier away:
        # add molecular_functions: to the node that exists. No topology change.
        return "ANNOTATE_MF"
    if "PATHWAY" in jump.landing_classes:
        # A signalling cascade drawn as one node. The fix is a chain of steps,
        # not a single term.
        return "INSERT_CHAIN"
    return "INSERT_ACTIVITY_NODE"


def scan_entry(path: Path, seed: dict[str, str]) -> tuple[list[Jump], Counter]:
    """Classify every gene -> pathophysiology landing in one KB entry."""
    counts: Counter = Counter()
    jumps: dict[str, Jump] = {}

    data = safe_load(path.read_text())
    if not isinstance(data, dict):
        return [], counts

    nodes = {
        item["name"]: item
        for item in data.get("pathophysiology") or []
        if isinstance(item, dict) and item.get("name")
    }
    graph = build_causal_graph(data)

    for edge in graph.edges:
        if edge.source_type != "genetic" or edge.target not in nodes:
            continue
        node = nodes[edge.target]
        counts["gene_to_mechanism_edges"] += 1

        if node.get("molecular_functions"):
            counts["ACTIVITY_BOUND"] += 1
            continue
        if not node.get("biological_processes"):
            counts[
                "PROTEIN_ONLY"
                if (node.get("gene_products") or node.get("protein_complexes"))
                else "UNGROUNDED"
            ] += 1
            continue

        counts["PROCESS_JUMP"] += 1
        jump = jumps.get(edge.target)
        if jump is None:
            bp = _descriptor_terms(node.get("biological_processes"))
            prose = f"{node.get('name') or ''} {node.get('description') or ''}"
            jump = Jump(
                entry=path.stem,
                path=str(path),
                node=edge.target,
                genes=_node_genes(node),
                bp_terms=[f"{curie} {label}" for curie, label in bp if curie],
                landing_classes=sorted(
                    {seed[curie] for curie, _ in bp if curie in seed}
                ),
                activity_prose=bool(ACTIVITY_PROSE.search(prose)),
                activity_in_name=bool(ACTIVITY_PROSE.search(node.get("name") or "")),
            )
            jump.verdict = decide(jump)
            jumps[edge.target] = jump
        if edge.source not in jump.gene_nodes:
            jump.gene_nodes.append(edge.source)

    return list(jumps.values()), counts


def render_summary(jumps: list[Jump], counts: Counter, n_entries: int) -> str:
    lines = [
        f"Scanned {n_entries} KB entries.",
        "",
        "Gene -> mechanism edges by grounding of the landing node:",
    ]
    total = counts["gene_to_mechanism_edges"] or 1
    for key in ("ACTIVITY_BOUND", "PROCESS_JUMP", "PROTEIN_ONLY", "UNGROUNDED"):
        lines.append(f"  {counts[key]:6}  {key:<16} {counts[key] / total:5.1%}")
    lines.append(f"  {counts['gene_to_mechanism_edges']:6}  total")

    entries = {jump.entry for jump in jumps}
    lines += [
        "",
        f"Process jumps: {len(jumps)} distinct landing nodes "
        f"across {len(entries)} entries.",
        "",
        "Advisory verdict:",
    ]
    verdicts = Counter(jump.verdict for jump in jumps)
    for verdict in VERDICTS:
        lines.append(f"  {verdicts[verdict]:6}  {verdict}")

    lines += ["", "Landing tier (GO seed table class of the BP term):"]
    tiers = Counter(
        "+".join(jump.landing_classes) or "(not in seed table)" for jump in jumps
    )
    for tier, n in tiers.most_common(10):
        lines.append(f"  {n:6}  {tier}")

    single = [jump for jump in jumps if jump.n_genes == 1]
    lines += [
        "",
        f"Single-gene landing nodes (MF unambiguous): {len(single)}",
        "  ...whose prose already asserts the activity: "
        f"{sum(1 for jump in single if jump.activity_prose)}",
        "  ...asserting it in the node name itself:    "
        f"{sum(1 for jump in single if jump.activity_in_name)}",
    ]
    return "\n".join(lines)


def render_tsv(jumps: list[Jump]) -> str:
    header = [
        "entry",
        "node",
        "verdict",
        "n_genes",
        "genes",
        "landing_classes",
        "activity_prose",
        "activity_in_name",
        "bp_terms",
        "gene_nodes",
    ]
    rows = ["\t".join(header)]
    for jump in jumps:
        rows.append(
            "\t".join(
                [
                    jump.entry,
                    jump.node,
                    jump.verdict,
                    str(jump.n_genes),
                    "; ".join(jump.genes),
                    "+".join(jump.landing_classes),
                    "yes" if jump.activity_prose else "no",
                    "yes" if jump.activity_in_name else "no",
                    "; ".join(jump.bp_terms),
                    "; ".join(jump.gene_nodes),
                ]
            )
        )
    return "\n".join(rows)


def render_list(jumps: list[Jump]) -> str:
    return "\n".join(
        f"{jump.verdict:<21} {jump.entry}  ::  {jump.node}"
        f"  [{'; '.join(jump.genes) or 'no gene on node'}]"
        for jump in jumps
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="KB files or directories to scan (default: kb/disorders kb/modules)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "list", "json"),
        default="summary",
        help="output format (default: summary)",
    )
    parser.add_argument(
        "--verdict",
        choices=VERDICTS,
        action="append",
        help="restrict output to these verdicts; repeatable",
    )
    parser.add_argument(
        "--single-gene-only",
        action="store_true",
        help="only landing nodes carrying exactly one gene",
    )
    parser.add_argument("--out", type=Path, help="write to this file instead of stdout")
    parser.add_argument(
        "--seed",
        type=Path,
        default=SEED_TABLE,
        help="GO BP -> node class seed table (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    targets = args.paths or [Path(d) for d in DEFAULT_KB_DIRS]
    files: list[Path] = []
    for target in targets:
        if target.is_dir():
            files.extend(sorted(target.glob("*.yaml")))
        elif target.exists():
            files.append(target)
        else:
            print(f"warning: {target} does not exist", file=sys.stderr)

    seed = load_seed(args.seed)
    if not seed:
        print(
            f"warning: no seed table at {args.seed}; landing tiers will be empty",
            file=sys.stderr,
        )

    jumps: list[Jump] = []
    counts: Counter = Counter()
    for path in files:
        entry_jumps, entry_counts = scan_entry(path, seed)
        jumps.extend(entry_jumps)
        counts.update(entry_counts)

    selected = jumps
    if args.verdict:
        selected = [jump for jump in selected if jump.verdict in set(args.verdict)]
    if args.single_gene_only:
        selected = [jump for jump in selected if jump.n_genes == 1]
    selected.sort(key=lambda jump: (jump.entry, jump.node))

    if args.format == "summary":
        text = render_summary(selected, counts, len(files))
    elif args.format == "tsv":
        text = render_tsv(selected)
    elif args.format == "list":
        text = render_list(selected)
    else:
        text = json.dumps([asdict(jump) for jump in selected], indent=1)

    if args.out:
        args.out.write_text(text + "\n")
        print(f"wrote {len(selected)} rows to {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
