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

Two ways a node is recognized as the origin
-------------------------------------------
Both read a **structured claim the entry makes**. Neither reads a naming
convention, and there is no fallback chain: an entry that does not say where it
starts is reported as not saying it, rather than guessed at.

``SOMATIC_LESION``
    A node carrying ``genetic_context.variant_origin: SOMATIC`` (or
    ``GERMLINE_AND_SOMATIC``) -- the transforming lesion. Not restricted to root
    nodes: a transformation or second-hit lesion is still a somatic event.
    ``allelic_hit_role: FIRST_HIT`` narrows it further.

``ENVIRONMENTAL_TRIGGER``
    A node that an ``environmental[].influences_mechanisms`` link marks with
    ``environmental_effect: TRIGGERS`` -- non-mutational initiation, where there
    is no host lesion to mark at all: HPV in anal carcinoma, H. pylori in gastric
    adenocarcinoma, asbestos in mesothelioma, UV in cutaneous SCC. It applies
    only when no somatic lesion is recorded, because a recorded lesion *is* the
    transforming event and the exposure is then upstream context.

An earlier version had a third rule that read an initiating-sounding ``role``
string on a root node, plus a fallback chain so a stronger rule could not
discard a weaker rule's answer. Both existed to paper over entries that had not
recorded their origin, and both mis-fired: the role rule derived macrophage and
pancreatic stellate cell as the "cell of origin" of pancreatic ductal
adenocarcinoma from a chronic-inflammation node. The records were marked instead
(``scripts/backfill_cancer_origin.py``) and the rules deleted.

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

from dismech.yaml_io import safe_load_path

KB_DIRS = ("kb/disorders", "kb/groupings")

# --- what counts as a neoplasm entry -----------------------------------------

# Matched against name + categories + disease_term label. Deliberately broad:
# a false positive costs one advisory line, a false negative hides the entry
# from the census entirely.
NEOPLASM_RE = re.compile(
    r"cancer|neoplas|tumou?r|leuk[ae]m|lymphom|sarcom|carcinom|myelom|glioma"
    r"|blastoma|melanoma|malignan|mesotheliom|adenoma|myeloprolif|myelodysplas"
    r"|mycosis fungoides|sezary|polycythemia vera|thrombocythemia",
    re.IGNORECASE,
)

# Two ways the sweep above picks up something that is not a neoplasm: a
# paraneoplastic syndrome is a disease *of* a tumor's host, not a tumor; and
# MONDO labels a handful of non-oncologic entities "malignant" in the older
# clinical sense ("malignant migrating partial seizures of infancy", which is an
# epilepsy). Both were derived a cell of origin they cannot have.
NOT_NEOPLASM_RE = re.compile(
    r"paraneoplastic|migrating partial seizures|malignant hyperthermia"
    r"|malignant atrophic papulosis",
    re.IGNORECASE,
)

# Germline predisposition syndromes are Mendelian diseases (design decisions
# Sec 3a says so in as many words) and are assessed under the plain lump/split
# rules, not this one. They are counted and skipped.
PREDISPOSITION_RE = re.compile(
    r"predispos|hereditary cancer|cancer syndrome|tumor syndrome|tumour syndrome",
    re.IGNORECASE,
)
# ...unless the entry also carries a somatic-neoplasm category, which means it
# curates the cancer itself rather than the syndrome.
SOMATIC_CATEGORY_RE = re.compile(
    r"solid tumor|hematologic|sarcoma|carcinoma|leukemia|lymphoma|molecularly",
    re.IGNORECASE,
)

# --- origin detection ---------------------------------------------------------

SOMATIC_ORIGINS = {"SOMATIC", "GERMLINE_AND_SOMATIC"}

RULE_SOMATIC = "SOMATIC_LESION"
RULE_TRIGGER = "ENVIRONMENTAL_TRIGGER"

FINDING_NO_ORIGIN = "NO_ORIGIN"
FINDING_NO_CELL = "ORIGIN_WITHOUT_CELL"
FINDING_MULTI = "MULTI_ORIGIN_CELL"

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
    """Pull ``(id, display name)`` pairs out of a list of ontology descriptors.

    The display name prefers ``preferred_term`` over the ontology ``label``,
    because a curator uses that slot to say something the label does not.
    Epithelioid sarcoma is the case: its origin is bound to ``CL:0000134`` under
    ``preferred_term: mesenchymal cell of uncertain differentiation``, which is
    a deliberate hedge. Reporting the label instead made the census say
    "mesenchymal stem cell" -- a claim the entry is careful not to make.

    Only the display name changes. The CURIE is what identifies a cell, so
    de-duplication, multi-origin detection and the generic-term checks are
    unaffected.
    """
    out: list[tuple[str, str]] = []
    if not isinstance(descriptors, list):
        return out
    for descriptor in descriptors:
        if not isinstance(descriptor, dict):
            continue
        term = descriptor.get("term")
        if isinstance(term, dict) and term.get("id"):
            preferred = descriptor.get("preferred_term")
            display = (
                str(preferred)
                if isinstance(preferred, str) and preferred.strip()
                else str(term.get("label", ""))
            )
            out.append((str(term["id"]), display))
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


def find_origins(data: dict) -> list[OriginNode]:
    """Return the nodes this entry marks as where the disease starts.

    Strict precedence, not a union: a recorded somatic lesion suppresses the
    exposure rule entirely. The cell of origin is the cell the transforming
    event occurred in, so once the entry names that event the exposure is
    upstream context -- in pancreatic ductal adenocarcinoma, chronic
    pancreatitis really does TRIGGER the inflammation node, but that node binds
    macrophage and pancreatic stellate cell while the disease arises in the
    ductal cell named on the KRAS lesion.
    """
    pathophysiology = data.get("pathophysiology") or []
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

    origins: dict[str, OriginNode] = {}

    # Rule 1 -- the transforming lesion.
    for node in nodes:
        genetic_context = node.get("genetic_context")
        if (
            isinstance(genetic_context, dict)
            and genetic_context.get("variant_origin") in SOMATIC_ORIGINS
        ):
            origins[str(node.get("name", ""))] = build(node, RULE_SOMATIC)

    # Rule 2 -- non-mutational initiation, read from the environmental link that
    # says so. `environmental_effect: TRIGGERS` is the same value the KGX
    # exporter and compliance scoring treat as causal, so this is not a
    # cell-of-origin-specific convention.
    triggered: set[str] = set()
    for exposure in data.get("environmental") or []:
        if not isinstance(exposure, dict):
            continue
        for link in exposure.get("influences_mechanisms") or []:
            if isinstance(link, dict) and link.get("environmental_effect") == "TRIGGERS":
                target = link.get("target")
                if isinstance(target, str):
                    triggered.add(target)
    # An exposure link speaks only when no lesion is recorded, and that is a
    # statement about meaning rather than confidence: the cell of origin is the
    # cell the transforming event occurred in, so if the entry records that
    # event, the exposure is upstream context and not the origin. Pancreatic
    # ductal adenocarcinoma is the case that makes the difference visible --
    # chronic pancreatitis genuinely TRIGGERS its inflammation node, but that
    # node binds macrophage and pancreatic stellate cell, while the disease
    # arises in the ductal cell named on the KRAS lesion.
    if not origins:
        for node in nodes:
            name = str(node.get("name", ""))
            if name in triggered:
                origins[name] = build(node, RULE_TRIGGER)

    return list(origins.values())


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
    is_neoplasm = (
        bool(NEOPLASM_RE.search(haystack)) or has_icdo
    ) and not NOT_NEOPLASM_RE.search(haystack)
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
    report.origins = find_origins(data)
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
    for rule in (RULE_SOMATIC, RULE_TRIGGER):
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
            print(f"  {report.path}  (subtypes={report.subtype_count})")
            for origin in report.origins:
                if not origin.cell_terms:
                    continue
                cells = "; ".join(f"{c} {lab}".strip() for c, lab in origin.cell_terms)
                print(f"     [{origin.rule}] {origin.name!r}: {cells}")
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
    """One tab-separated line per assessed entry: path, rules, findings, cells."""
    for report in reports:
        if not report.is_neoplasm or report.is_predisposition:
            continue
        cells = _fmt_cells(report) or "-"
        rules = ",".join(report.rules) or "-"
        findings = ",".join(report.findings) or "OK"
        print(f"{report.path}\t{rules}\t{findings}\t{cells}")


TSV_COLUMNS = (
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
)


def render_tsv(reports: list[EntryReport]) -> None:
    print("\t".join(TSV_COLUMNS))
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
        choices=(FINDING_NO_ORIGIN, FINDING_NO_CELL, FINDING_MULTI),
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
        print()
        render_list(reports)
    else:
        render_summary(reports, verbose=False)

    gating = set(args.fail_on)
    if args.strict:
        gating |= {FINDING_NO_ORIGIN, FINDING_NO_CELL, FINDING_MULTI}
    if gating:
        hits = [r for r in reports if gating.intersection(r.findings)]
        if hits:
            print(f"\n{len(hits)} entry(ies) match the gating finding classes.")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
