#!/usr/bin/env python3
"""Find the cell of origin of a neoplasm entry, and report where it is missing.

Why there is no ``cell_of_origin:`` slot
----------------------------------------
The cell a cancer arises from is one of the strongest lump/split signals the
field has -- WHO's taxonomy is a histogenesis backbone with molecular
alterations promoted into it case by case (design decisions Sec 3a), and the
cancer SOP already names "different cell of origin" as its first split
criterion. But dismech does not need a new slot to say it, because the entry
already carries both halves of the statement:

* **which node is the origin** -- a pathophysiology node whose
  ``genetic_context.variant_origin`` is ``SOMATIC`` is, by definition, where the
  transforming lesion occurred;
* **which cell it happened in** -- that node's ``cell_types``.

So the cell of origin is *derived*: find the initiating node, read its cell
types. This script implements that derivation, reports the entries where it
fails, and turns the multi-origin case into the grouping signal it should be.

Three ways a node is recognized as the origin
---------------------------------------------
Applied in order; the first that matches wins, and the rule that fired is
reported so a curator can tell a deliberate marking from a lucky guess.

``SOMATIC_LESION``
    A node carrying ``genetic_context.variant_origin: SOMATIC`` (or
    ``GERMLINE_AND_SOMATIC``). This is the marker to prefer, and the only one
    that is unambiguous: it is a structured claim about a mutational event, not
    a naming convention. ``allelic_hit_role: FIRST_HIT`` narrows it further.

``INITIATING_ROLE``
    A **root** node (nothing in the entry lists it as a ``downstream`` target)
    whose free-text ``role`` is one of the initiating spellings. Weaker: ``role``
    is an unconstrained string and the KB holds ~90 distinct values on
    pathophysiology nodes, so this rule reads a convention rather than a claim.

``EXPOSURE_TRIGGER``
    A root node carrying ``triggers`` -- the non-mutational initiation case
    (HTLV-1 in adult T-cell leukemia, EBV, chemical carcinogens), where there is
    no somatic lesion in the host genome to mark, yet the entry still names the
    initiating event and the cell it acts on.

What is reported
----------------
``NO_ORIGIN``
    No rule fired. The entry may still bind cell types -- it just does not say
    which of them the disease *comes from*. This is the backlog, and it is most
    of the corpus today, which is why the script is advisory by default.

``ORIGIN_WITHOUT_CELL``
    An origin node was identified but binds no CL term. The marking is there and
    the derivation still yields nothing, so this is the cheapest class to fix.

``MULTI_ORIGIN_CELL``
    Origin nodes name more than one distinct CL term. **This is the finding the
    script exists for.** It is not automatically a defect -- it means one of
    three quite different things, and only a curator can say which:

    1. a grouping wearing a Disease entry's clothes (Kidney_Sarcoma's four
       mesenchymal lineages, Appendiceal_Neoplasm's epithelial + goblet +
       enteroendocrine) -- these are L1 pools per the granularity ladder;
    2. one disease with genuine cell-of-origin *subtypes* (DLBCL's centrocyte
       and centroblast, which WHO treats as GCB/ABC strata of one entity);
    3. an unresolved question in the literature (Ewing sarcoma's mesenchymal
       stem cell vs. neural crest cell), where naming both is the honest answer.

    So this never gates. It is a worklist for the lump/split call, and the
    remedy for (1) is a `Grouping`, for (2) `has_subtypes`, and for (3) a note.

``CONTEXT_NODE_MARKED``
    The node the derivation landed on describes the setting rather than the
    origin -- microenvironment remodeling, chronic inflammation, immune evasion.
    Binding macrophage, Treg and fibroblast there is correct curation; treating
    them as the cell of origin is not. This is the failure mode of the
    ``INITIATING_ROLE`` rule, and the remedy is to mark the transforming lesion
    with ``genetic_context`` so the stronger rule wins. Pancreatic ductal
    adenocarcinoma was the worked case: a "Chronic Pancreatic Inflammation" root
    node marked ``role: trigger`` yielded macrophage + pancreatic stellate cell,
    while the actual origin sat unmarked one node over on ``KRAS Oncogene
    Activation`` with ``pancreatic ductal cell``.

Usage
-----
::

    just check-cancer-origin                     # summary + the multi-origin worklist
    just check-cancer-origin --format list       # every entry, one line each
    just check-cancer-origin --format tsv        # machine-readable
    just check-cancer-origin --strict            # exit 1 on any finding
    just list-cancer-origin                      # full census including derived cells

See ``docs/cancer-cell-of-origin.md``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech.yaml_io import safe_load_path  # noqa: E402

KB_DIRS = ("kb/disorders", "kb/groupings")

# --- what counts as a neoplasm entry -----------------------------------------

# Matched against name + categories + disease_term label. Deliberately broad:
# a false positive costs one advisory line, a false negative hides the entry
# from the census entirely.
NEOPLASM_RE = re.compile(
    r"cancer|neoplas|tumou?r|leuk[ae]m|lymphom|sarcom|carcinom|myelom|glioma"
    r"|blastoma|melanoma|malignan|mesotheliom|adenoma|myeloprolif|myelodysplas"
    r"|mycosis fungoides|sezary|polycythemia vera|thrombocythemia",
    re.I,
)

# Germline predisposition syndromes are Mendelian diseases (design decisions
# Sec 3a says so in as many words) and are assessed under the plain lump/split
# rules, not this one. They are counted and skipped.
PREDISPOSITION_RE = re.compile(
    r"predispos|hereditary cancer|cancer syndrome|tumor syndrome|tumour syndrome",
    re.I,
)
# ...unless the entry also carries a somatic-neoplasm category, which means it
# curates the cancer itself rather than the syndrome.
SOMATIC_CATEGORY_RE = re.compile(
    r"solid tumor|hematologic|sarcoma|carcinoma|leukemia|lymphoma|molecularly",
    re.I,
)

# --- origin detection ---------------------------------------------------------

SOMATIC_ORIGINS = {"SOMATIC", "GERMLINE_AND_SOMATIC"}

# `role` is an unconstrained string; these are the spellings that assert the
# node is where the disease starts, normalized for case and separator. Values
# meaning "downstream" (consequence, effector, outcome...) are absent on
# purpose -- this set is not a vocabulary for `role`, it is the subset of it
# that this derivation reads.
INITIATING_ROLES = {
    "trigger",
    "driver",
    "root",
    "primary",
    "primary defect",
    "initiator",
    "initiating",
    "initiating mechanism",
    "initiating event",
    "commitment step",
    "upstream",
}

RULE_SOMATIC = "SOMATIC_LESION"
RULE_ROLE = "INITIATING_ROLE"
RULE_TRIGGER = "EXPOSURE_TRIGGER"

FINDING_NO_ORIGIN = "NO_ORIGIN"
FINDING_NO_CELL = "ORIGIN_WITHOUT_CELL"
FINDING_MULTI = "MULTI_ORIGIN_CELL"
FINDING_CONTEXT = "CONTEXT_NODE_MARKED"

# A node whose name says "microenvironment", "immune evasion" or "chronic
# inflammation" describes the setting the tumor grows in, not the cell it came
# from. Such nodes routinely bind macrophage / Treg / fibroblast, and they are
# root nodes, so the role rule can pick them up and hand back a stromal "cell of
# origin". Matched on the node NAME rather than on a list of stromal CL terms,
# because there is no cell type that is stromal everywhere: a T cell is
# microenvironment in a carcinoma and the cell of origin in a T-cell lymphoma.
CONTEXT_NODE_RE = re.compile(
    r"microenvironment|immune (evasion|escape|suppress|surveillance)"
    r"|immunosuppress|t-?cell exhaustion|inflammat|desmoplas"
    r"|tumou?r stroma|stromal (remodel|activation|reaction)"
    r"|angiogen|myeloid suppression|regulatory t-?cell",
    re.I,
)


def normalize_role(value: object) -> str:
    """Case- and separator-fold a free-text ``role`` for comparison only."""
    if not isinstance(value, str):
        return ""
    return re.sub(r"[\s_-]+", " ", value).strip().lower()


@dataclass
class OriginNode:
    """One pathophysiology node identified as where the disease starts."""

    name: str
    rule: str
    cell_terms: list[tuple[str, str]] = field(default_factory=list)
    is_root: bool = True
    first_hit: bool = False

    @property
    def cell_ids(self) -> set[str]:
        return {cid for cid, _ in self.cell_terms}


@dataclass
class EntryReport:
    """The derivation result for one KB entry."""

    path: str
    name: str
    is_neoplasm: bool
    is_predisposition: bool
    n_pathophysiology: int = 0
    origins: list[OriginNode] = field(default_factory=list)
    all_cell_ids: set[str] = field(default_factory=set)
    ncit_ids: list[str] = field(default_factory=list)
    subtype_count: int = 0
    findings: list[str] = field(default_factory=list)

    @property
    def origin_cells(self) -> list[tuple[str, str]]:
        seen: dict[str, str] = {}
        for origin in self.origins:
            for cid, label in origin.cell_terms:
                seen.setdefault(cid, label)
        return sorted(seen.items())

    @property
    def rules(self) -> list[str]:
        out: list[str] = []
        for origin in self.origins:
            if origin.rule not in out:
                out.append(origin.rule)
        return out


def _terms(descriptors: object) -> list[tuple[str, str]]:
    """Pull ``(id, label)`` pairs out of a list of ontology descriptors."""
    out: list[tuple[str, str]] = []
    if not isinstance(descriptors, list):
        return out
    for descriptor in descriptors:
        if not isinstance(descriptor, dict):
            continue
        term = descriptor.get("term")
        if isinstance(term, dict) and term.get("id"):
            out.append((str(term["id"]), str(term.get("label", ""))))
    return out


def _downstream_targets(nodes: Iterable[dict]) -> set[str]:
    """Names that some *other* node lists as a downstream target."""
    targets: set[str] = set()
    for node in nodes:
        source = node.get("name")
        for edge in node.get("downstream") or []:
            if not isinstance(edge, dict):
                continue
            target = edge.get("target")
            # A self-loop does not make a node non-root: the flat node namespace
            # collapses a pathophysiology node and a same-named phenotype into
            # one node, which is issue #9896, not an incoming causal edge.
            if isinstance(target, str) and target != source:
                targets.add(target)
    return targets


def find_origins(pathophysiology: list[dict]) -> list[OriginNode]:
    """Apply the three origin rules in precedence order."""
    nodes = [n for n in pathophysiology if isinstance(n, dict)]
    targeted = _downstream_targets(nodes)

    def build(node: dict, rule: str) -> OriginNode:
        genetic_context = node.get("genetic_context")
        first_hit = (
            isinstance(genetic_context, dict)
            and genetic_context.get("allelic_hit_role") == "FIRST_HIT"
        )
        return OriginNode(
            name=str(node.get("name", "")),
            rule=rule,
            cell_terms=_terms(node.get("cell_types")),
            is_root=node.get("name") not in targeted,
            first_hit=first_hit,
        )

    # Rule 1 -- a somatic lesion is a claim, not a convention, so it ranks
    # first and is NOT restricted to root nodes: a second-hit or transformation
    # lesion is still where a somatic event occurred.
    somatic = [
        build(node, RULE_SOMATIC)
        for node in nodes
        if isinstance(node.get("genetic_context"), dict)
        and node["genetic_context"].get("variant_origin") in SOMATIC_ORIGINS
    ]

    # Rule 2 -- an initiating role, on a root node only. Off a root node the
    # word "trigger" describes a step within the cascade, not the origin.
    by_role = [
        build(node, RULE_ROLE)
        for node in nodes
        if node.get("name") not in targeted
        and normalize_role(node.get("role")) in INITIATING_ROLES
    ]

    # Rule 3 -- non-mutational initiation (oncovirus, carcinogen exposure).
    by_trigger = [
        build(node, RULE_TRIGGER)
        for node in nodes
        if node.get("name") not in targeted and node.get("triggers")
    ]

    # Precedence with a fallback: take the strongest rule that actually yields a
    # cell. A lesion node routinely carries the gene and not the cell it occurred
    # in, and letting the strongest rule win *outright* would then throw away a
    # weaker rule's correct answer and report the entry as unmarked. If no rule
    # yields a cell, still return the strongest match so the entry is reported
    # as ORIGIN_WITHOUT_CELL rather than silently as NO_ORIGIN.
    ranked = [somatic, by_role, by_trigger]
    for candidates in ranked:
        if candidates and any(c.cell_terms for c in candidates):
            return candidates
    for candidates in ranked:
        if candidates:
            return candidates
    return []


def _display_path(path: Path) -> str:
    """Repo-relative when the file is in the repo, verbatim otherwise (tmpdirs)."""
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def assess(path: Path) -> EntryReport | None:
    """Derive the cell of origin for one entry, or return None if unreadable."""
    try:
        data = safe_load_path(path)
    except Exception as exc:  # pragma: no cover - malformed YAML is another gate's job
        print(f"warning: could not parse {path}: {exc}", file=sys.stderr)
        return None
    if not isinstance(data, dict):
        return None

    name = str(data.get("name", path.stem))
    categories = data.get("categories") or []
    category_text = " | ".join(str(c) for c in categories if c)
    disease_term = data.get("disease_term")
    label = ""
    if isinstance(disease_term, dict):
        term = disease_term.get("term")
        if isinstance(term, dict):
            label = str(term.get("label", ""))

    classifications = data.get("classifications")
    has_icdo = isinstance(classifications, dict) and bool(
        classifications.get("icdo_morphology")
    )
    haystack = f"{name} {category_text} {label}"
    is_neoplasm = bool(NEOPLASM_RE.search(haystack)) or has_icdo
    is_predisposition = bool(PREDISPOSITION_RE.search(haystack)) and not (
        SOMATIC_CATEGORY_RE.search(category_text)
    )

    report = EntryReport(
        path=_display_path(path),
        name=name,
        is_neoplasm=is_neoplasm,
        is_predisposition=is_predisposition,
    )
    if not is_neoplasm or is_predisposition:
        return report

    pathophysiology = data.get("pathophysiology") or []
    if not isinstance(pathophysiology, list):
        pathophysiology = []
    report.n_pathophysiology = len(pathophysiology)
    report.subtype_count = len(data.get("has_subtypes") or [])
    report.origins = find_origins(pathophysiology)
    for node in pathophysiology:
        if isinstance(node, dict):
            report.all_cell_ids.update(cid for cid, _ in _terms(node.get("cell_types")))

    mappings = data.get("mappings")
    if isinstance(mappings, dict):
        for mapping in mappings.get("ncit_mappings") or []:
            if isinstance(mapping, dict):
                term = mapping.get("term")
                if isinstance(term, dict) and term.get("id"):
                    report.ncit_ids.append(str(term["id"]))

    if any(CONTEXT_NODE_RE.search(o.name) for o in report.origins):
        report.findings.append(FINDING_CONTEXT)
    if not report.origins:
        report.findings.append(FINDING_NO_ORIGIN)
    elif not report.origin_cells:
        report.findings.append(FINDING_NO_CELL)
    if len(report.origin_cells) > 1:
        report.findings.append(FINDING_MULTI)
    return report


def iter_paths(args_files: list[str]) -> Iterator[Path]:
    if args_files:
        for raw in args_files:
            path = Path(raw)
            yield path if path.is_absolute() else (ROOT / path)
        return
    for directory in KB_DIRS:
        base = ROOT / directory
        if base.is_dir():
            yield from sorted(base.glob("*.yaml"))


# --- reporting ---------------------------------------------------------------


def _fmt_cells(report: EntryReport) -> str:
    return "; ".join(f"{cid} {label}".strip() for cid, label in report.origin_cells)


def render_summary(reports: list[EntryReport], *, verbose: bool) -> None:
    assessed = [r for r in reports if r.is_neoplasm and not r.is_predisposition]
    skipped = [r for r in reports if r.is_neoplasm and r.is_predisposition]
    marked = [r for r in assessed if r.origins]
    derived = [r for r in assessed if r.origin_cells]
    multi = [r for r in assessed if FINDING_MULTI in r.findings]
    no_cell = [r for r in assessed if FINDING_NO_CELL in r.findings]
    no_origin = [r for r in assessed if FINDING_NO_ORIGIN in r.findings]

    print(f"Neoplasm entries assessed: {len(assessed)}")
    print(f"  germline predisposition syndromes skipped: {len(skipped)}")
    print(f"  origin node identified:                    {len(marked)}")
    for rule in (RULE_SOMATIC, RULE_ROLE, RULE_TRIGGER):
        count = sum(1 for r in marked if rule in r.rules)
        print(f"      via {rule:<16} {count}")
    print(f"  cell of origin derived:                    {len(derived)}")
    print(f"  cell types bound somewhere but no origin:  "
          f"{sum(1 for r in no_origin if r.all_cell_ids)}")
    print()

    if multi:
        print(f"-- {len(multi)} entry(ies) deriving MORE THAN ONE cell of origin --")
        print(
            "   Read as a lump/split question, not a defect: a grouping wearing a\n"
            "   Disease entry's clothes, a disease with cell-of-origin subtypes, or\n"
            "   a genuinely unsettled origin. See docs/cancer-cell-of-origin.md.\n"
        )
        for report in sorted(multi, key=lambda r: -len(r.origin_cells)):
            flag = " [context node marked]" if FINDING_CONTEXT in report.findings else ""
            print(f"  {report.path}  (subtypes={report.subtype_count}){flag}")
            for origin in report.origins:
                if not origin.cell_terms:
                    continue
                cells = "; ".join(f"{c} {lab}".strip() for c, lab in origin.cell_terms)
                print(f"     [{origin.rule}] {origin.name!r}: {cells}")
        print()

    context_only = [
        r for r in assessed if FINDING_CONTEXT in r.findings and FINDING_MULTI not in r.findings
    ]
    if context_only:
        print(
            f"-- {len(context_only)} entry(ies) whose only marked origin is a "
            "context node --"
        )
        print(
            "   A microenvironment / inflammation / immune-evasion node is where the\n"
            "   tumor lives, not where it came from. Mark the transforming lesion\n"
            "   instead, with genetic_context.variant_origin: SOMATIC.\n"
        )
        for report in context_only:
            names = ", ".join(repr(o.name) for o in report.origins)
            print(f"  {report.path}: {names}")
        print()

    if no_cell:
        print(f"-- {len(no_cell)} entry(ies) marking an origin node that binds no cell --")
        print("   Cheapest class to fix: the marking is already there.\n")
        for report in no_cell:
            names = ", ".join(repr(o.name) for o in report.origins)
            print(f"  {report.path}: {names}")
        print()

    if no_origin and verbose:
        print(f"-- {len(no_origin)} entry(ies) with no origin node identified --\n")
        for report in no_origin:
            hint = (
                f"{len(report.all_cell_ids)} cell type(s) bound elsewhere"
                if report.all_cell_ids
                else "no cell types anywhere"
            )
            print(f"  {report.path}: {hint}")
        print()
    elif no_origin:
        print(
            f"{len(no_origin)} entry(ies) have no origin node identified "
            f"(--format list to see them).\n"
        )


def render_list(reports: list[EntryReport]) -> None:
    for report in reports:
        if not report.is_neoplasm or report.is_predisposition:
            continue
        cells = _fmt_cells(report) or "-"
        rules = ",".join(report.rules) or "-"
        findings = ",".join(report.findings) or "OK"
        print(f"{report.path}\t{rules}\t{findings}\t{cells}")


def render_tsv(reports: list[EntryReport]) -> None:
    print(
        "\t".join(
            [
                "path",
                "name",
                "assessed",
                "rules",
                "origin_nodes",
                "origin_cell_ids",
                "origin_cell_labels",
                "n_pathophysiology",
                "n_subtypes",
                "ncit_ids",
                "findings",
            ]
        )
    )
    for report in reports:
        if not report.is_neoplasm:
            continue
        assessed = "no" if report.is_predisposition else "yes"
        print(
            "\t".join(
                [
                    report.path,
                    report.name,
                    assessed,
                    ",".join(report.rules),
                    "; ".join(o.name for o in report.origins),
                    ",".join(cid for cid, _ in report.origin_cells),
                    "; ".join(label for _, label in report.origin_cells),
                    str(report.n_pathophysiology),
                    str(report.subtype_count),
                    ",".join(report.ncit_ids),
                    ",".join(report.findings),
                ]
            )
        )


def render_json(reports: list[EntryReport]) -> None:
    payload = [
        {
            "path": r.path,
            "name": r.name,
            "assessed": r.is_neoplasm and not r.is_predisposition,
            "predisposition": r.is_predisposition,
            "rules": r.rules,
            "origin_nodes": [
                {
                    "name": o.name,
                    "rule": o.rule,
                    "is_root": o.is_root,
                    "first_hit": o.first_hit,
                    "cell_types": [{"id": cid, "label": lab} for cid, lab in o.cell_terms],
                }
                for o in r.origins
            ],
            "origin_cells": [{"id": cid, "label": lab} for cid, lab in r.origin_cells],
            "ncit_ids": r.ncit_ids,
            "n_subtypes": r.subtype_count,
            "findings": r.findings,
        }
        for r in reports
        if r.is_neoplasm
    ]
    print(json.dumps(payload, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="*", help="KB YAML files (default: whole KB)")
    parser.add_argument(
        "--format",
        choices=("summary", "list", "tsv", "json"),
        default="summary",
        help="summary (default) prints the multi-origin worklist; list adds every entry",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 on any finding (not wired into CI: most of the corpus is unmarked)",
    )
    parser.add_argument(
        "--fail-on",
        action="append",
        default=[],
        choices=(FINDING_NO_ORIGIN, FINDING_NO_CELL, FINDING_MULTI, FINDING_CONTEXT),
        help="exit 1 on this finding class only; repeatable",
    )
    args = parser.parse_args(argv)

    reports = [r for r in (assess(p) for p in iter_paths(args.files)) if r is not None]

    if args.format == "tsv":
        render_tsv(reports)
    elif args.format == "json":
        render_json(reports)
    elif args.format == "list":
        render_summary(reports, verbose=True)
    else:
        render_summary(reports, verbose=False)

    gating = set(args.fail_on)
    if args.strict:
        gating |= {FINDING_NO_ORIGIN, FINDING_NO_CELL, FINDING_MULTI, FINDING_CONTEXT}
    if gating:
        hits = [r for r in reports if gating.intersection(r.findings)]
        if hits:
            print(f"\n{len(hits)} entry(ies) match the gating finding classes.")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
