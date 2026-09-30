#!/usr/bin/env python3
"""How far ToxCast assay endpoints reach into the dismech pathograph.

An assay endpoint declares an intended gene target. A pathophysiology node may
name a gene. Where the two name the same gene, the endpoint is a **candidate**
for that node: something a curator could consider mapping. This script counts
those candidates from three sides, which are the three breakdowns issue #12858
asks for:

* **nodes** -- how many pathophysiology nodes name a gene some endpoint targets;
* **genes** -- how many of the panel's gene targets dismech binds, and where;
* **diseases** -- how many entries carry at least one such node.

The word is *coverage*, not *mapping*, on purpose. A shared gene symbol says the
endpoint and the node are about the same gene. It does not say they agree on
direction, on the quantity measured, or on mechanism, and #12858 gives a real
example of each disagreement. Every count here is therefore an upper bound on
what could be mapped, never a count of mappings.

The join
--------
A node names a gene through ``genes[]``, ``gene``, or the ``gene``/``genes`` of
its ``genetic_context`` -- the same three places ``dismech.graph`` reads when it
links a gene to a mechanism. Only HGNC-bound descriptors count, and the key is
the descriptor's ``term.label``, which term validation holds to HGNC's approved
symbol.

On the ToxCast side the key is the gene symbol, upper-cased. Three things keep
that from being a plain string match:

* **Species.** Each gene object carries its own species, separate from the
  system the assay ran in. A target is *human* when some endpoint names the
  human gene, and *ortholog-only* when the panel names it solely through another
  species' gene (rat ``Cyp2b1``, zebrafish ``esr2a``). An ortholog-only target
  that shares a symbol with a human gene still joins, and is reported apart.
* **Superseded symbols.** ToxCast carries three symbols HGNC has since replaced;
  see :data:`SUPERSEDED_SYMBOLS`.
* **One composite.** Endpoint 1846 names ``FOS|JUN`` as a single gene object;
  it is split into its two genes.

Usage:
    uv run python scripts/toxcast_pathograph_coverage.py              # markdown
    uv run python scripts/toxcast_pathograph_coverage.py --format tsv --table targets
    uv run python scripts/toxcast_pathograph_coverage.py --json
    uv run python scripts/toxcast_pathograph_coverage.py --out docs/reports/x.md

Offline once the annotations are cached (``just toxcast-refresh``, which needs
``CTX_API_KEY``). Reads committed YAML and that cache; no ontology adapter.
Report-only: exits 0. Counts move with every curation PR and with every EPA
release, so any number in a committed report is a dated snapshot.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech import kb_cache
from dismech.toxcast_assays import (
    AnnotationsMissing,
    AnnotationSnapshot,
    AssayEndpoint,
    default_annotations,
)

ROOT = Path(__file__).resolve().parent.parent
DISORDERS_DIR = ROOT / "kb" / "disorders"
MODULES_DIR = ROOT / "kb" / "modules"

#: Symbols ToxCast still carries that HGNC has replaced. Each was resolved by
#: looking the gene object's Entrez id up among HGNC's ``ncbigene:`` xrefs, not
#: by name: 3014 is ``hgnc:4739``, 3020 is ``hgnc:4764``, 5524 is ``hgnc:9308``.
#: Without this the three would read as absent from dismech whatever it binds.
#: ``--check-symbols`` reports any further symbol that has gone the same way.
SUPERSEDED_SYMBOLS = {
    "H2AFX": "H2AX",
    "H3F3A": "H3-3A",
    "PPP2R4": "PTPA",
}

#: Where a target sits in dismech, strictest first. A target gets the first
#: tier it satisfies.
TIERS = ("ON_NODE", "GENETIC_ONLY", "ELSEWHERE_ONLY", "ABSENT")

TIER_BLURB = {
    "ON_NODE": "named by a pathophysiology node in at least one entry",
    "GENETIC_ONLY": "bound in a `genetic:` record, on no node",
    "ELSEWHERE_ONLY": "bound elsewhere in an entry (a subtype, a treatment, a biomarker), in no `genetic:` record and on no node",
    "ABSENT": "bound nowhere in `kb/disorders/`",
}

SCALES = ("MOLECULAR", "CELLULAR", "TISSUE", "ORGANISM")
UNTAGGED = "(untagged)"
NO_FAMILY = "(none given)"


# ----- ToxCast side -----


@dataclass
class Target:
    """One molecular target of the panel, keyed on its gene symbol."""

    symbol: str
    aeids: set[int] = field(default_factory=set)
    #: Endpoints naming the human gene. Empty for an ortholog-only target.
    human_aeids: set[int] = field(default_factory=set)
    #: The symbols as ToxCast wrote them, before upper-casing and aliasing.
    written_as: set[str] = field(default_factory=set)

    @property
    def human(self) -> bool:
        return bool(self.human_aeids)


def symbol_keys(symbol: str) -> list[str]:
    """The join key or keys for one ToxCast gene symbol."""
    keys = []
    for part in symbol.split("|"):
        key = part.strip().upper()
        if key:
            keys.append(SUPERSEDED_SYMBOLS.get(key, key))
    return keys


def endpoint_keys(endpoint: AssayEndpoint) -> set[str]:
    return {key for gene in endpoint.genes for key in symbol_keys(gene.symbol)}


def collect_targets(endpoints: Iterable[AssayEndpoint]) -> dict[str, Target]:
    targets: dict[str, Target] = {}
    for endpoint in endpoints:
        for gene in endpoint.genes:
            for key in symbol_keys(gene.symbol):
                target = targets.setdefault(key, Target(symbol=key))
                target.aeids.add(endpoint.aeid)
                target.written_as.add(gene.symbol)
                if gene.is_human:
                    target.human_aeids.add(endpoint.aeid)
    return targets


# ----- dismech side -----


@dataclass(frozen=True)
class Node:
    """One pathophysiology node that names at least one gene."""

    entry: str
    name: str
    scale: str
    #: True when the node carries a ``genetic_context``, i.e. it records a
    #: variant. That is the structural mark of a node naming a lesion rather
    #: than a state an assay could read.
    has_variant: bool


@dataclass
class KBIndex:
    """What one KB directory binds, gene by gene."""

    n_entries: int = 0
    n_nodes: int = 0
    gene_nodes: set[Node] = field(default_factory=set)
    nodes_by_gene: dict[str, set[Node]] = field(default_factory=dict)
    genetic_by_gene: dict[str, set[str]] = field(default_factory=dict)
    anywhere_by_gene: dict[str, set[str]] = field(default_factory=dict)
    scale_of_all_nodes: Counter = field(default_factory=Counter)


def hgnc_label(descriptor: Any) -> str | None:
    """The upper-cased HGNC label of a gene descriptor, or None if unbound."""
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if not isinstance(term, dict):
        return None
    term_id, label = term.get("id"), term.get("label")
    if not isinstance(term_id, str) or not term_id.lower().startswith("hgnc:"):
        return None
    return label.strip().upper() if isinstance(label, str) and label.strip() else None


def descriptors_in(item: Any, *keys: str) -> Iterator[Any]:
    """Descriptors under singular or list-valued ``keys`` of ``item``."""
    if not isinstance(item, dict):
        return
    for key in keys:
        value = item.get(key)
        if isinstance(value, list):
            yield from value
        elif value is not None:
            yield value


def node_gene_labels(node: dict) -> set[str]:
    """Genes a node names, read from the slots ``dismech.graph`` links on."""
    found = descriptors_in(node, "gene", "genes")
    context = descriptors_in(node.get("genetic_context"), "gene", "genes")
    return {label for d in (*found, *context) if (label := hgnc_label(d))}


def walk_hgnc_labels(node: Any) -> Iterator[str]:
    """Every HGNC-bound label below ``node``, wherever it sits."""
    if isinstance(node, dict):
        if label := hgnc_label(node):
            yield label
        for value in node.values():
            yield from walk_hgnc_labels(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_hgnc_labels(value)


def index_entry(index: KBIndex, slug: str, document: Any) -> None:
    if not isinstance(document, dict):
        return
    index.n_entries += 1

    for raw in document.get("pathophysiology") or []:
        if not isinstance(raw, dict):
            continue
        index.n_nodes += 1
        scale = raw.get("biological_scale")
        scale = scale if scale in SCALES else UNTAGGED
        index.scale_of_all_nodes[scale] += 1
        labels = node_gene_labels(raw)
        if not labels:
            continue
        node = Node(
            entry=slug,
            name=str(raw.get("name", "<unnamed>")),
            scale=scale,
            has_variant=isinstance(raw.get("genetic_context"), dict),
        )
        index.gene_nodes.add(node)
        for label in labels:
            index.nodes_by_gene.setdefault(label, set()).add(node)

    for record in document.get("genetic") or []:
        for descriptor in descriptors_in(record, "gene_term"):
            if label := hgnc_label(descriptor):
                index.genetic_by_gene.setdefault(label, set()).add(slug)

    for label in set(walk_hgnc_labels(document)):
        index.anywhere_by_gene.setdefault(label, set()).add(slug)


def index_kb(directory: Path) -> KBIndex:
    index = KBIndex()
    for path, document in kb_cache.iter_documents(directory):
        index_entry(index, path.stem, document)
    return index


# ----- the join -----


def tier_of(symbol: str, index: KBIndex) -> str:
    if symbol in index.nodes_by_gene:
        return "ON_NODE"
    if symbol in index.genetic_by_gene:
        return "GENETIC_ONLY"
    if symbol in index.anywhere_by_gene:
        return "ELSEWHERE_ONLY"
    return "ABSENT"


@dataclass
class Coverage:
    """The join of one annotation snapshot against one indexed KB directory."""

    endpoints: list[AssayEndpoint]
    targets: dict[str, Target]
    index: KBIndex
    modules: KBIndex
    retrieved: str = ""
    kb_commit: str = ""
    #: The nodes each endpoint reaches, filled on first use. Every count below
    #: is a fold over this, so it is computed once per endpoint.
    _nodes_by_aeid: dict[int, set[Node]] = field(default_factory=dict, repr=False)

    # --- genes ---

    def tier(self, symbol: str) -> str:
        return tier_of(symbol, self.index)

    def targets_in(self, tier: str) -> list[Target]:
        return [t for t in self.targets.values() if self.tier(t.symbol) == tier]

    # --- nodes ---

    def candidate_nodes(self, symbols: Iterable[str] | None = None) -> set[Node]:
        symbols = self.targets if symbols is None else symbols
        found: set[Node] = set()
        for symbol in symbols:
            found |= self.index.nodes_by_gene.get(symbol, set())
        return found

    def nodes_for(self, endpoint: AssayEndpoint) -> set[Node]:
        if endpoint.aeid not in self._nodes_by_aeid:
            self._nodes_by_aeid[endpoint.aeid] = self.candidate_nodes(
                endpoint_keys(endpoint)
            )
        return self._nodes_by_aeid[endpoint.aeid]

    # --- endpoints ---

    def with_gene(self) -> list[AssayEndpoint]:
        return [e for e in self.endpoints if e.genes]

    def candidates(self) -> list[AssayEndpoint]:
        return [e for e in self.endpoints if self.nodes_for(e)]

    def human_candidates(self) -> list[AssayEndpoint]:
        """Candidates reaching a node through the human gene, not an ortholog."""
        out = []
        for endpoint in self.endpoints:
            keys = {
                k for g in endpoint.genes if g.is_human for k in symbol_keys(g.symbol)
            }
            if self.candidate_nodes(keys):
                out.append(endpoint)
        return out

    def pair_count(self) -> int:
        return sum(len(self.nodes_for(e)) for e in self.endpoints)

    # --- diseases ---

    def candidate_entries(self) -> set[str]:
        return {node.entry for node in self.candidate_nodes()}

    def off_node_entries(self) -> set[str]:
        """Entries binding a target somewhere while no node of theirs names one."""
        bound: set[str] = set()
        for symbol in self.targets:
            bound |= self.index.anywhere_by_gene.get(symbol, set())
        return bound - self.candidate_entries()


def kb_commit(directory: Path) -> str:
    """Short hash of the last commit to touch ``directory``, or an empty string.

    Pins the content measured rather than the branch it was measured on: a
    commit that changes only this script leaves the answer where it was.
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%h", "--abbrev=10", "--", str(directory)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return result.stdout.strip()


def build(
    snapshot: AnnotationSnapshot,
    disorders_dir: Path = DISORDERS_DIR,
    modules_dir: Path = MODULES_DIR,
) -> Coverage:
    endpoints = sorted(snapshot, key=lambda e: e.aeid)
    return Coverage(
        endpoints=endpoints,
        targets=collect_targets(endpoints),
        index=index_kb(disorders_dir),
        modules=index_kb(modules_dir),
        retrieved=snapshot.retrieved,
        kb_commit=kb_commit(disorders_dir),
    )


# ----- rendering -----


def pct(part: int, whole: int) -> str:
    return f"{100.0 * part / whole:.1f}%" if whole else "n/a"


def family_rows(cov: Coverage) -> list[tuple[str, int, int, int, int, int]]:
    """(family, endpoints, with gene, candidates, nodes, entries), largest first."""
    groups: dict[str, list[AssayEndpoint]] = {}
    for endpoint in cov.endpoints:
        groups.setdefault(endpoint.target_family or NO_FAMILY, []).append(endpoint)
    rows = []
    for family, members in groups.items():
        nodes: set[Node] = set()
        n_candidates = 0
        for endpoint in members:
            reached = cov.nodes_for(endpoint)
            n_candidates += bool(reached)
            nodes |= reached
        rows.append(
            (
                family,
                len(members),
                sum(1 for e in members if e.genes),
                n_candidates,
                len(nodes),
                len({n.entry for n in nodes}),
            )
        )
    return sorted(rows, key=lambda r: (-r[1], r[0]))


def render_markdown(cov: Coverage, *, top: int = 20) -> str:
    index = cov.index
    n_endpoints = len(cov.endpoints)
    with_gene = cov.with_gene()
    candidates = cov.candidates()
    human_candidates = cov.human_candidates()
    nodes = cov.candidate_nodes()
    entries = cov.candidate_entries()
    off_node = cov.off_node_entries()
    human_targets = [t for t in cov.targets.values() if t.human]
    ortholog_targets = [t for t in cov.targets.values() if not t.human]

    out: list[str] = []
    add = out.append

    add("# ToxCast assay coverage of the dismech pathograph")
    add("")
    add(
        "How many ToxCast and Tox21 assay endpoints declare a gene target that a "
        "dismech pathophysiology node also names, counted from the side of the "
        "assays, the nodes, the genes and the diseases. Background: issue #12858; "
        "scope and interpretation: `projects/TOXCAST.md`."
    )
    add("")
    add(
        "A shared gene is a **candidate**, not a mapping. It says an endpoint and "
        "a node concern the same gene. It does not say they agree on direction, "
        "on the quantity measured, or on mechanism, so every figure below is an "
        "upper bound on what could be mapped."
    )
    add("")
    add(
        f"Assay annotations retrieved from the EPA CTX API on "
        f"**{cov.retrieved or 'an unrecorded date'}**; `kb/disorders/` as of commit "
        f"`{cov.kb_commit or 'unknown'}`. Both move, so treat the numbers as a dated "
        "snapshot and regenerate with `just toxcast-coverage`."
    )
    add("")

    # --- a) nodes, from the assay side and the node side ---
    add("## Pathograph node coverage")
    add("")
    add("### From the assay side")
    add("")
    add("| Assay endpoints | Count | Share of panel |")
    add("| --- | ---: | ---: |")
    add(f"| In the panel | {n_endpoints} | |")
    add(
        f"| Declare no usable gene target | {n_endpoints - len(with_gene)} | "
        f"{pct(n_endpoints - len(with_gene), n_endpoints)} |"
    )
    add(
        f"| Declare a gene target | {len(with_gene)} | {pct(len(with_gene), n_endpoints)} |"
    )
    add(
        f"| **Candidates: a target is named by at least one node** | "
        f"**{len(candidates)}** | **{pct(len(candidates), n_endpoints)}** |"
    )
    add(
        f"| &nbsp;&nbsp;of which through the human gene | {len(human_candidates)} | "
        f"{pct(len(human_candidates), n_endpoints)} |"
    )
    add(
        f"| &nbsp;&nbsp;of which through another species' ortholog only | "
        f"{len(candidates) - len(human_candidates)} | "
        f"{pct(len(candidates) - len(human_candidates), n_endpoints)} |"
    )
    add("")
    add(
        f"Of the endpoints that declare a gene target, {pct(len(candidates), len(with_gene))} "
        "are candidates. An endpoint with no gene target cannot be found by this "
        "join at all, which is not the same as having no node it could speak to: "
        "a cell-viability counter-screen declares no gene and may still bear on a "
        "cell-death node."
    )
    add("")
    add("By intended target family, largest first:")
    add("")
    add(
        "| Intended target family | Endpoints | With a gene target | Candidates | Nodes reached | Entries reached |"
    )
    add("| --- | ---: | ---: | ---: | ---: | ---: |")
    for family, total, genes, n_cand, n_nodes, n_entries in family_rows(cov):
        add(f"| {family} | {total} | {genes} | {n_cand} | {n_nodes} | {n_entries} |")
    add("")
    add(
        "Nodes and entries are counted once per family, so those two columns do "
        "not sum to the totals below: one node can be reached from several "
        "families."
    )
    add("")

    add("### From the node side")
    add("")
    add("| Pathophysiology nodes in `kb/disorders/` | Count | Share of all nodes |")
    add("| --- | ---: | ---: |")
    add(f"| All nodes | {index.n_nodes} | |")
    add(
        f"| Name at least one HGNC-bound gene | {len(index.gene_nodes)} | "
        f"{pct(len(index.gene_nodes), index.n_nodes)} |"
    )
    add(
        f"| **Candidates: name a gene some endpoint targets** | **{len(nodes)}** | "
        f"**{pct(len(nodes), index.n_nodes)}** |"
    )
    add("")
    add(
        f"That is {pct(len(nodes), len(index.gene_nodes))} of the nodes that name a gene. "
        f"Pairing every candidate endpoint with every node it reaches gives "
        f"**{cov.pair_count()} endpoint-node pairs**, which is the size of the job if "
        "each candidate were reviewed."
    )
    add("")
    add("Candidate nodes by `biological_scale`, against all nodes:")
    add("")
    add("| `biological_scale` | Candidate nodes | All nodes | Share of that scale |")
    add("| --- | ---: | ---: | ---: |")
    scale_counts = Counter(node.scale for node in nodes)
    for scale in (*SCALES, UNTAGGED):
        total = index.scale_of_all_nodes[scale]
        add(
            f"| {scale} | {scale_counts[scale]} | {total} | {pct(scale_counts[scale], total)} |"
        )
    add("")
    n_variant = sum(1 for node in nodes if node.has_variant)
    add(
        f"{n_variant} of the {len(nodes)} candidate nodes ({pct(n_variant, len(nodes))}) "
        "carry a `genetic_context`, meaning the node records a variant. Those are "
        "the nodes most likely to name a lesion where an assay reads a state, "
        "which is the first mismatch #12858 describes. The remainder are not "
        "thereby cleared: a node can name a lesion in prose without the slot."
    )
    add("")

    # --- b) genes ---
    add("## Gene coverage")
    add("")
    add(
        f"The panel names **{len(cov.targets)} distinct gene targets**. "
        f"{len(human_targets)} are named through the human gene by at least one "
        f"endpoint; {len(ortholog_targets)} are named only through another "
        "species' gene, and join to dismech only where the upper-cased symbol "
        "happens to be a human gene's symbol."
    )
    add("")
    add(
        "| Where the target sits in `kb/disorders/` | Human targets | Ortholog-only targets | All | Endpoints naming one |"
    )
    add("| --- | ---: | ---: | ---: | ---: |")
    for tier in TIERS:
        members = cov.targets_in(tier)
        aeids: set[int] = set()
        for target in members:
            aeids |= target.aeids
        n_human = sum(1 for t in members if t.human)
        add(
            f"| `{tier}`: {TIER_BLURB[tier]} | {n_human} | {len(members) - n_human} | "
            f"{len(members)} | {len(aeids)} |"
        )
    add("")
    multi_gene = sum(1 for e in cov.endpoints if len(endpoint_keys(e)) > 1)
    add(
        "Each target takes the first tier it satisfies. The endpoint column can "
        f"count one endpoint in two rows, because {multi_gene} endpoints name more "
        "than one gene."
    )
    add("")
    add(f"The {top} most-assayed targets, and how far each reaches:")
    add("")
    add("| Target | Endpoints | Tier | Nodes | Entries |")
    add("| --- | ---: | --- | ---: | ---: |")
    ranked = sorted(cov.targets.values(), key=lambda t: (-len(t.aeids), t.symbol))
    for target in ranked[:top]:
        reached = index.nodes_by_gene.get(target.symbol, set())
        add(
            f"| {target.symbol} | {len(target.aeids)} | `{cov.tier(target.symbol)}` | "
            f"{len(reached)} | {len({n.entry for n in reached})} |"
        )
    add("")
    once = sum(1 for t in cov.targets.values() if len(t.aeids) == 1)
    ten_plus = sum(1 for t in cov.targets.values() if len(t.aeids) >= 10)
    add(
        f"The panel is very uneven: {once} targets appear in exactly one endpoint "
        f"and {ten_plus} appear in ten or more."
    )
    add("")
    rewritten: dict[str, set[str]] = {}
    for target in cov.targets.values():
        for written in target.written_as:
            if written.upper() != target.symbol:
                rewritten.setdefault(written, set()).add(target.symbol)
    if rewritten:
        add(
            "Symbols the join rewrote, because ToxCast writes them differently "
            "from HGNC's approved symbol:"
        )
        add("")
        for written in sorted(rewritten):
            read_as = " and ".join(
                f"`{symbol}`" for symbol in sorted(rewritten[written])
            )
            add(f"- `{written}` is read as {read_as}")
        add("")

    # --- c) diseases ---
    add("## Disease coverage")
    add("")
    add("| Entries in `kb/disorders/` | Count | Share |")
    add("| --- | ---: | ---: |")
    add(f"| All entries | {index.n_entries} | |")
    add(
        f"| **Carry at least one candidate node** | **{len(entries)}** | "
        f"**{pct(len(entries), index.n_entries)}** |"
    )
    add(
        f"| Bind a target somewhere, on no node | {len(off_node)} | "
        f"{pct(len(off_node), index.n_entries)} |"
    )
    remainder = index.n_entries - len(entries) - len(off_node)
    add(f"| Bind no target | {remainder} | {pct(remainder, index.n_entries)} |")
    add("")
    add(
        "In the middle row the gene is already bound in the entry, typically in "
        "`genetic:`, and no pathophysiology node names it. Whether it belongs on "
        "a node is a curation question for each entry, not a backfill: a gene on "
        "a node asserts that the gene drives that mechanism in that disease."
    )
    add("")
    per_entry = Counter(node.entry for node in nodes)
    buckets = Counter(
        "1" if n == 1 else "2-3" if n <= 3 else "4 or more" for n in per_entry.values()
    )
    add("| Candidate nodes in the entry | Entries |")
    add("| --- | ---: |")
    for bucket in ("1", "2-3", "4 or more"):
        add(f"| {bucket} | {buckets[bucket]} |")
    add("")
    add(f"The {top} targets reaching the most entries:")
    add("")
    add("| Target | Entries | Nodes | Nodes with a `genetic_context` | Endpoints |")
    add("| --- | ---: | ---: | ---: | ---: |")
    by_reach = sorted(
        (t for t in cov.targets.values() if t.symbol in index.nodes_by_gene),
        key=lambda t: (
            -len({n.entry for n in index.nodes_by_gene[t.symbol]}),
            t.symbol,
        ),
    )
    for target in by_reach[:top]:
        reached = index.nodes_by_gene[target.symbol]
        add(
            f"| {target.symbol} | {len({n.entry for n in reached})} | {len(reached)} | "
            f"{sum(1 for n in reached if n.has_variant)} | {len(target.aeids)} |"
        )
    add("")

    # --- modules ---
    module_nodes: set[Node] = set()
    for symbol in cov.targets:
        module_nodes |= cov.modules.nodes_by_gene.get(symbol, set())
    add("## Mechanism modules")
    add("")
    add(
        f"Counted apart, because a module is not a disease. {len(module_nodes)} of "
        f"the {cov.modules.n_nodes} pathophysiology nodes in `kb/modules/` name a "
        f"gene some endpoint targets, across {len({n.entry for n in module_nodes})} "
        f"of {cov.modules.n_entries} modules."
    )
    add("")

    add("## Regenerating")
    add("")
    add("```bash")
    add(
        "just toxcast-refresh                                 # cache the annotations; needs CTX_API_KEY"
    )
    add("just toxcast-coverage                                # this report, to stdout")
    add(
        "just toxcast-coverage --format tsv --table targets   # one row per gene target"
    )
    add(
        "just toxcast-coverage --format tsv --table nodes     # one row per candidate node"
    )
    add(
        "just toxcast-coverage --format tsv --table endpoints # one row per assay endpoint"
    )
    add(
        "just toxcast-coverage --format tsv --table diseases  # one row per entry with a candidate node"
    )
    add("```")
    add("")
    return "\n".join(out)


def render_tsv(cov: Coverage, table: str) -> str:
    index = cov.index
    rows: list[list[str]] = []
    if table == "targets":
        rows.append(
            [
                "symbol",
                "human_gene",
                "tier",
                "endpoints",
                "nodes",
                "entries",
                "toxcast_symbols",
            ]
        )
        for target in sorted(cov.targets.values(), key=lambda t: t.symbol):
            reached = index.nodes_by_gene.get(target.symbol, set())
            rows.append(
                [
                    target.symbol,
                    "1" if target.human else "0",
                    cov.tier(target.symbol),
                    str(len(target.aeids)),
                    str(len(reached)),
                    str(len({n.entry for n in reached})),
                    ";".join(sorted(target.written_as)),
                ]
            )
    elif table == "nodes":
        rows.append(
            [
                "entry",
                "node",
                "biological_scale",
                "has_genetic_context",
                "targets",
                "endpoints",
            ]
        )
        by_node: dict[Node, set[str]] = {}
        for symbol in cov.targets:
            for node in index.nodes_by_gene.get(symbol, set()):
                by_node.setdefault(node, set()).add(symbol)
        for node in sorted(by_node, key=lambda n: (n.entry, n.name)):
            symbols = sorted(by_node[node])
            aeids: set[int] = set()
            for symbol in symbols:
                aeids |= cov.targets[symbol].aeids
            rows.append(
                [
                    node.entry,
                    node.name,
                    node.scale,
                    "1" if node.has_variant else "0",
                    ";".join(symbols),
                    str(len(aeids)),
                ]
            )
    elif table == "endpoints":
        rows.append(
            [
                "aeid",
                "name",
                "genes",
                "organism",
                "target_family",
                "function_type",
                "signal_direction",
                "nodes",
                "entries",
            ]
        )
        for endpoint in cov.endpoints:
            reached = cov.nodes_for(endpoint)
            rows.append(
                [
                    str(endpoint.aeid),
                    endpoint.name,
                    ";".join(endpoint.gene_symbols),
                    endpoint.organism,
                    endpoint.target_family,
                    endpoint.function_type,
                    endpoint.signal_direction,
                    str(len(reached)),
                    str(len({n.entry for n in reached})),
                ]
            )
    else:
        rows.append(["entry", "candidate_nodes", "targets", "endpoints"])
        by_entry: dict[str, tuple[set[Node], set[str]]] = {}
        for symbol in cov.targets:
            for node in index.nodes_by_gene.get(symbol, set()):
                nodes, symbols = by_entry.setdefault(node.entry, (set(), set()))
                nodes.add(node)
                symbols.add(symbol)
        for entry in sorted(by_entry):
            nodes, symbols = by_entry[entry]
            aeids = set()
            for symbol in symbols:
                aeids |= cov.targets[symbol].aeids
            rows.append(
                [entry, str(len(nodes)), ";".join(sorted(symbols)), str(len(aeids))]
            )
    return "\n".join("\t".join(row) for row in rows)


def summary(cov: Coverage) -> dict[str, Any]:
    """The headline figures, for ``--json`` and for tests."""
    nodes = cov.candidate_nodes()
    return {
        "retrieved": cov.retrieved,
        "kb_commit": cov.kb_commit,
        "endpoints": len(cov.endpoints),
        "endpoints_with_gene": len(cov.with_gene()),
        "candidate_endpoints": len(cov.candidates()),
        "candidate_endpoints_human_gene": len(cov.human_candidates()),
        "endpoint_node_pairs": cov.pair_count(),
        "targets": len(cov.targets),
        "targets_human": sum(1 for t in cov.targets.values() if t.human),
        "targets_by_tier": {tier: len(cov.targets_in(tier)) for tier in TIERS},
        "nodes": cov.index.n_nodes,
        "nodes_naming_a_gene": len(cov.index.gene_nodes),
        "candidate_nodes": len(nodes),
        "candidate_nodes_with_genetic_context": sum(1 for n in nodes if n.has_variant),
        "entries": cov.index.n_entries,
        "candidate_entries": len(cov.candidate_entries()),
        "entries_binding_a_target_off_node": len(cov.off_node_entries()),
    }


# ----- optional symbol check -----


def unapproved_human_symbols(cov: Coverage) -> list[str] | None:
    """Human target symbols that are not an HGNC approved symbol, or None.

    Returns None when the local HGNC build is absent. Asks about the file
    before opening the adapter, because opening ``sqlite:obo:hgnc`` without the
    build does not fail: it downloads it.
    """
    import sqlite3

    from dismech.oak_db import local_build_path, local_build_present

    if not local_build_present("sqlite:obo:hgnc"):
        return None
    connection = sqlite3.connect(local_build_path("hgnc"))
    try:
        approved = {
            str(value).upper()
            for (value,) in connection.execute(
                "SELECT value FROM statements WHERE predicate = 'rdfs:label'"
            )
            if value
        }
    finally:
        connection.close()
    return sorted(
        t.symbol for t in cov.targets.values() if t.human and t.symbol not in approved
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", help="write here instead of stdout")
    parser.add_argument(
        "--format",
        choices=("markdown", "tsv"),
        default="markdown",
        help="output format (default: markdown)",
    )
    parser.add_argument(
        "--table",
        choices=("targets", "nodes", "endpoints", "diseases"),
        default="targets",
        help="which table --format tsv writes (default: targets)",
    )
    parser.add_argument(
        "--json", action="store_true", help="emit the headline figures as JSON"
    )
    parser.add_argument(
        "--top", type=int, default=20, help="rows in the ranked tables (default: 20)"
    )
    parser.add_argument(
        "--check-symbols",
        action="store_true",
        help=(
            "list human target symbols that are not an HGNC approved symbol; "
            "needs the local HGNC build"
        ),
    )
    parser.add_argument(
        "--data-dir", type=Path, default=None, help="annotation cache directory"
    )
    args = parser.parse_args(argv)

    # Each directory is walked once, so the shared parse cache is pure cost.
    kb_cache.default_off()

    try:
        snapshot = default_annotations(args.data_dir).load()
    except AnnotationsMissing as error:
        print(error, file=sys.stderr)
        return 2

    cov = build(snapshot)

    if args.check_symbols:
        unapproved = unapproved_human_symbols(cov)
        if unapproved is None:
            print(
                "no local HGNC build; fetch it with:\n    just fetch-ontology-dbs hgnc",
                file=sys.stderr,
            )
            return 2
        if unapproved:
            print("human target symbols that are not an HGNC approved symbol:")
            for symbol in unapproved:
                print(f"  {symbol}")
            print("add each to SUPERSEDED_SYMBOLS after resolving it by Entrez id")
        else:
            print("every human target symbol is an HGNC approved symbol")
        return 0

    if args.json:
        payload = json.dumps(summary(cov), indent=2)
    elif args.format == "tsv":
        payload = render_tsv(cov, args.table)
    else:
        payload = render_markdown(cov, top=args.top)

    if args.out:
        Path(args.out).write_text(payload + "\n", encoding="utf-8")
        print(
            f"wrote {args.out} ({len(cov.endpoints)} endpoints, {cov.index.n_entries} entries)",
            file=sys.stderr,
        )
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
