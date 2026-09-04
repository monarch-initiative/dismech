#!/usr/bin/env python3
"""Audit ``has_subtypes`` usage and subtype-gene pathograph wiring.

Two questions, both raised together (a lumped entry can be the right call and
still throw information away):

1. **How actively is ``has_subtypes`` used?** A subtype earns its keep when
   other sections stratify by it via the ``subtype:`` foreign key (Phenotype,
   Biochemical, Genetic, Prevalence, ProgressionInfo, HistopathologyFinding,
   ImagingFinding, PhenotypeContext — the classes carrying the slot). A subtype
   list nothing ever references is a nosology index card: legitimate, but it
   records no subtype-specific phenotypic effect, which for a
   gene-per-subtype disease is exactly the information lumping risks losing.

2. **Is each gene-specific subtype's gene wired into the pathograph?** The
   pathograph links a gene to mechanisms in exactly two machine-readable ways
   (see ``dismech.graph``): a pathophysiology node carrying the gene as a
   structured descriptor (``gene:`` / ``genes:``), or a ``genetic:`` node whose
   gene keys auto-link it to such a pathophysiology node. A subtype that names
   a gene in ``has_subtypes[].genes`` while neither path exists is
   deterministically detectable — and means the gene-specific mechanism is
   either uncurated or curated only as prose.

Per subtype-gene verdicts (most- to least-wired):

* ``WIRED_DIRECT``      — a pathophysiology node carries the gene as a
  structured descriptor. The gene's mechanism is first-class in the graph.
* ``WIRED_VIA_GENETIC`` — a matching ``genetic:`` node emits at least one
  auto-inferred edge into a pathophysiology node.
* ``GENETIC_NONCAUSAL`` — a matching ``genetic:`` node exists but its
  ``relationship_type``/``association`` marks it non-contributing (MODIFIER,
  BIOMARKER, PROTECTIVE, DISPUTED, UNKNOWN), so ``dismech.graph`` deliberately
  draws no mechanism edge. Usually correct as-is; listed for completeness.
* ``GENETIC_UNWIRED``   — a contributing ``genetic:`` node exists but no
  pathophysiology node carries the gene, so the genetic node floats
  disconnected from the mechanism chain.
* ``ABSENT``            — the gene appears nowhere in the entry's ``genetic:``
  section or pathophysiology descriptors. The strongest finding: the entry
  says "this subtype is caused by gene G" and the pathograph has never heard
  of G.
* ``NO_KEYS``           — the subtype's gene descriptor has no usable
  preferred_term/label/id (malformed; should not normally occur).

The ``name_mention`` column is an advisory sub-signal on ``GENETIC_UNWIRED``
and ``ABSENT`` rows: the gene symbol appears as a word inside some
pathophysiology node's *name* (e.g. the Androgen_Insensitivity_Syndrome chain
starts at a node literally named "AR Germline Pathogenic Variant" that carries
no gene descriptor). There the mechanism chain likely exists and the fix is
adding the structured descriptor to the node; without a mention, the fix is
usually real curation. Name matching is not part of the graph contract —
``dismech.graph`` matches structured descriptors only — which is why prose-only
wiring shows up here as a gap.

Advisory by default, like ``model-scale-audit``: the backlog predates the
audit, so there is no gate and no baseline. ``--strict`` exits non-zero on any
``ABSENT`` or ``GENETIC_UNWIRED`` row for use in focused sweeps.

Usage::

    uv run python scripts/subtype_usage_audit.py                      # summary census
    uv run python scripts/subtype_usage_audit.py --format tsv         # per-gene rows
    uv run python scripts/subtype_usage_audit.py --format list --status ABSENT
    uv run python scripts/subtype_usage_audit.py kb/disorders/Alport_Syndrome.yaml
    uv run python scripts/subtype_usage_audit.py --strict
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO_ROOT / "src"))

# Imported after the sys.path insertion above, so they resolve from src/.
# The private graph helpers are the single source of truth for gene-key
# matching; reimplementing them here would let the audit drift from what the
# pathograph actually does.
from dismech.graph import (  # noqa: E402
    _descriptor_lookup_keys,
    _gene_lookup_keys,
    _genetic_item_infers_mechanism_edges,
    build_causal_graph,
)
from dismech.yaml_io import safe_load  # noqa: E402

#: Classes carrying the ``subtype`` foreign-key slot map to these list-valued
#: Disease sections (PhenotypeContext is nested and handled separately).
_SUBTYPE_FK_SECTIONS = (
    "phenotypes",
    "biochemical",
    "genetic",
    "prevalence",
    "progression",
    "histopathology",
    "imaging",
)

_WIRING_ORDER = (
    "WIRED_DIRECT",
    "WIRED_VIA_GENETIC",
    "GENETIC_NONCAUSAL",
    "GENETIC_UNWIRED",
    "ABSENT",
    "NO_KEYS",
)

_STRICT_STATUSES = frozenset({"ABSENT", "GENETIC_UNWIRED"})


@dataclass
class GeneRow:
    """One subtype-gene wiring verdict."""

    entry: str
    subtype: str
    gene: str
    status: str
    name_mention: bool
    genetic_nodes: list[str] = field(default_factory=list)


@dataclass
class EntryCensus:
    """Per-entry ``has_subtypes`` usage numbers."""

    entry: str
    n_subtypes: int
    n_referenced: int
    fk_refs: int
    n_gene_subtypes: int


def _iter_subtypes(subtypes: list) -> list[dict]:
    """Flatten a ``has_subtypes`` list including nested ``children``."""
    out: list[dict] = []
    stack = list(subtypes or [])
    while stack:
        item = stack.pop(0)
        if not isinstance(item, dict):
            continue
        out.append(item)
        stack = list(item.get("children") or []) + stack
    return out


def _collect_fk_targets(disorder: dict) -> Counter:
    """Count ``subtype:`` foreign-key references by target name."""
    used: Counter = Counter()
    for section in _SUBTYPE_FK_SECTIONS:
        for item in disorder.get(section) or []:
            if isinstance(item, dict) and item.get("subtype"):
                used[str(item["subtype"])] += 1
    for phenotype in disorder.get("phenotypes") or []:
        if not isinstance(phenotype, dict):
            continue
        context = phenotype.get("context")
        if isinstance(context, dict) and context.get("subtype"):
            used[str(context["subtype"])] += 1
    return used


def _gene_display(descriptor: dict) -> str:
    term = descriptor.get("term")
    label = term.get("label") if isinstance(term, dict) else None
    return str(descriptor.get("preferred_term") or label or "?")


def _symbol_words(descriptor: dict) -> set[str]:
    """Gene symbols usable for whole-word matching against node names."""
    words = set()
    term = descriptor.get("term")
    for value in (
        descriptor.get("preferred_term"),
        term.get("label") if isinstance(term, dict) else None,
    ):
        if isinstance(value, str) and value.strip() and len(value) <= 20:
            words.add(value.strip().lower())
    return words


def audit_entry(path: Path) -> tuple[EntryCensus | None, list[GeneRow]]:
    """Audit one disorder file; returns (census, gene wiring rows)."""
    disorder = safe_load(path.read_text())
    if not isinstance(disorder, dict):
        return None, []
    subtypes = _iter_subtypes(disorder.get("has_subtypes") or [])
    if not subtypes:
        return None, []

    fk_targets = _collect_fk_targets(disorder)
    census = EntryCensus(
        entry=path.stem,
        n_subtypes=len(subtypes),
        n_referenced=sum(1 for s in subtypes if s.get("name") in fk_targets),
        fk_refs=sum(fk_targets.values()),
        n_gene_subtypes=sum(1 for s in subtypes if s.get("genes")),
    )

    gene_rows: list[GeneRow] = []
    subtype_genes = [
        (str(s.get("name") or "?"), g)
        for s in subtypes
        for g in (s.get("genes") or [])
        if isinstance(g, dict)
    ]
    if not subtype_genes:
        return census, gene_rows

    graph = build_causal_graph(disorder)
    patho_names = {
        name
        for name, info in graph.nodes.items()
        if info.node_type == "pathophysiology"
    }
    patho_gene_keys: set[str] = set()
    for item in disorder.get("pathophysiology") or []:
        if isinstance(item, dict):
            patho_gene_keys |= _gene_lookup_keys(item)
    patho_name_words = {
        word
        for name in patho_names
        for word in re.split(r"[^a-z0-9-]+", name.lower())
        if word
    }

    genetic_by_key: dict[str, set[str]] = {}
    contributing: set[str] = set()
    for item in disorder.get("genetic") or []:
        if not isinstance(item, dict) or not item.get("name"):
            continue
        name = str(item["name"])
        if _genetic_item_infers_mechanism_edges(item):
            contributing.add(name)
        for key in _gene_lookup_keys(item, allow_name_fallback=True):
            genetic_by_key.setdefault(key, set()).add(name)
    genetic_with_mech_edge = {
        edge.source
        for edge in graph.edges
        if edge.source_type == "genetic" and edge.target in patho_names
    }

    for subtype_name, descriptor in subtype_genes:
        keys = _descriptor_lookup_keys(descriptor)
        display = _gene_display(descriptor)
        mention = bool(_symbol_words(descriptor) & patho_name_words)
        if not keys:
            status, nodes = "NO_KEYS", []
        elif keys & patho_gene_keys:
            status, nodes = "WIRED_DIRECT", []
        else:
            matched: set[str] = set()
            for key in keys:
                matched |= genetic_by_key.get(key, set())
            if not matched:
                status, nodes = "ABSENT", []
            elif matched & genetic_with_mech_edge:
                status, nodes = "WIRED_VIA_GENETIC", sorted(matched)
            elif matched & contributing:
                status, nodes = "GENETIC_UNWIRED", sorted(matched)
            else:
                status, nodes = "GENETIC_NONCAUSAL", sorted(matched)
        gene_rows.append(
            GeneRow(
                entry=path.stem,
                subtype=subtype_name,
                gene=display,
                status=status,
                name_mention=mention,
                genetic_nodes=nodes,
            )
        )
    return census, gene_rows


def _print_summary(censuses: list[EntryCensus], rows: list[GeneRow]) -> None:
    n_entries = len(censuses)
    n_subtypes = sum(c.n_subtypes for c in censuses)
    n_referenced = sum(c.n_referenced for c in censuses)
    inert_entries = [c for c in censuses if c.fk_refs == 0]
    gene_entries = [c for c in censuses if c.n_gene_subtypes]
    print("has_subtypes usage census")
    print(f"  entries with has_subtypes:        {n_entries}")
    print(f"  subtypes (incl. children):        {n_subtypes}")
    print(
        f"  subtypes referenced by subtype FK: {n_referenced} "
        f"({n_referenced / n_subtypes:.0%})"
        if n_subtypes
        else "  subtypes referenced by subtype FK: 0"
    )
    print(
        f"  entries with zero subtype FK refs: {len(inert_entries)} "
        f"(subtype list present, nothing stratified by it)"
    )
    print(f"  entries with gene-specific subtypes: {len(gene_entries)}")
    print()
    print("subtype-gene pathograph wiring")
    status_counts = Counter(row.status for row in rows)
    for status in _WIRING_ORDER:
        if status_counts.get(status):
            print(f"  {status:<18} {status_counts[status]}")
    flagged = [row for row in rows if row.status in _STRICT_STATUSES]
    with_mention = sum(1 for row in flagged if row.name_mention)
    if flagged:
        print(
            f"  -> {len(flagged)} genes not wired into the pathograph, "
            f"across {len({row.entry for row in flagged})} entries "
            f"({with_mention} with the symbol in a pathophysiology node name, "
            f"where adding the descriptor is likely the whole fix)"
        )


def _print_list(rows: list[GeneRow]) -> None:
    by_entry: dict[str, list[GeneRow]] = {}
    for row in rows:
        by_entry.setdefault(row.entry, []).append(row)
    for entry in sorted(by_entry):
        print(entry)
        for row in by_entry[entry]:
            mention = " [symbol in a pathophysiology node name]" if row.name_mention else ""
            via = f" via genetic: {', '.join(row.genetic_nodes)}" if row.genetic_nodes else ""
            print(f"  {row.status:<18} {row.subtype} -> {row.gene}{via}{mention}")


def _write_tsv(rows: list[GeneRow], out) -> None:
    writer = csv.writer(out, delimiter="\t", lineterminator="\n")
    writer.writerow(
        ["entry", "subtype", "gene", "status", "name_mention", "genetic_nodes"]
    )
    for row in rows:
        writer.writerow(
            [
                row.entry,
                row.subtype,
                row.gene,
                row.status,
                "yes" if row.name_mention else "no",
                "; ".join(row.genetic_nodes),
            ]
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="Disorder YAML files to audit (default: all of kb/disorders/)",
    )
    parser.add_argument(
        "--format",
        choices=("summary", "tsv", "list"),
        default="summary",
        dest="fmt",
    )
    parser.add_argument(
        "--status",
        action="append",
        choices=_WIRING_ORDER,
        help="Restrict tsv/list output to these statuses (repeatable). "
        "Default for list: ABSENT and GENETIC_UNWIRED; tsv: all.",
    )
    parser.add_argument("--out", type=Path, help="Write tsv output to this path")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any ABSENT or GENETIC_UNWIRED gene is found",
    )
    args = parser.parse_args()

    files = args.files or sorted((_REPO_ROOT / "kb" / "disorders").glob("*.yaml"))
    censuses: list[EntryCensus] = []
    rows: list[GeneRow] = []
    for path in files:
        census, gene_rows = audit_entry(path)
        if census:
            censuses.append(census)
        rows.extend(gene_rows)

    if args.fmt == "summary":
        _print_summary(censuses, rows)
    else:
        statuses = set(args.status or [])
        if args.fmt == "list" and not statuses:
            statuses = set(_STRICT_STATUSES)
        shown = [row for row in rows if not statuses or row.status in statuses]
        if args.fmt == "tsv":
            if args.out:
                with args.out.open("w") as handle:
                    _write_tsv(shown, handle)
                print(f"wrote {len(shown)} rows to {args.out}", file=sys.stderr)
            else:
                _write_tsv(shown, sys.stdout)
        else:
            _print_list(shown)

    if args.strict and any(row.status in _STRICT_STATUSES for row in rows):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
