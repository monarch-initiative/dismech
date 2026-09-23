#!/usr/bin/env python3
"""Check ``Genetic.validity`` against the ClinGen assertions an entry cites (#10179).

``Genetic.validity`` records how well established a gene-disease association is,
on the ClinGen Gene-Disease Validity ladder (#11062). Most of the time the value
is not a judgement at all: the entry already cites a ClinGen ``CGGV:`` assertion,
and ``references_cache/CGGV_*.md`` holds that assertion's classification as one
table row. This script reads that row and compares it with the entry.

It walks ``kb/disorders`` and, for every ``genetic[]`` record, collects the
``CGGV:`` identifiers the entry cites anywhere (evidence ``reference``,
``external_assertions[].external_id``, ...) whose cached row names the same gene.
Matching is on the HGNC identifier when the record binds one, else on the gene
symbol.

**A tier belongs to a gene-disease pair, not to a gene.** An assertion only
speaks for the entry when its MONDO disease is the entry's own: the
``disease_term``, a ``has_subtypes[].subtype_term``, or a
``mappings.mondo_mappings`` term with ``mapping_predicate: skos:exactMatch``.
About a quarter of the ClinGen citations in the KB are for some other disease,
usually a broader ClinGen lumping (``ALPK3-Related_Hypertrophic_Cardiomyopathy``
cites ClinGen's generic hypertrophic cardiomyopathy) or the gene's second
disease. Those never feed ``backfill`` or ``conflict``.

Finding classes
---------------
``conflict``  (gates, exit 1)
    ``validity`` is set, the entry cites ClinGen for this gene, and no cited
    assertion carries that classification. Either the value or the citation is
    wrong. It starts at zero, so gating it costs nothing and stops a hand-typed
    tier from contradicting the source it sits next to.

``backfill``  (report)
    ``validity`` is absent and every cited assertion for the gene agrees, so the
    value can be copied from the source with no judgement involved. Only
    assertions for the entry's own disease count.

``ambiguous``  (report)
    ``validity`` is absent and the same-disease assertions for the gene
    disagree -- usually two modes of inheritance classified separately (JPH2 in
    dilated cardiomyopathy), or an entry whose subtypes are separate ClinGen
    diseases (ATP7A: Menkes disease and X-linked distal SMA). ``validity`` is
    single-valued, so which tier the record means is a curator's call and no
    value is suggested. Each row names the MOI to help.

``other_disease``  (report)
    ``validity`` is absent and the entry cites ClinGen for this gene only
    against a different MONDO disease. Whether ClinGen's entity is the entry's
    (a lumped parent, a synonym MONDO has not merged) is a curator's call.

``overstated``  (report)
    ``relationship_type: CAUSATIVE``, whose schema description says ClinGen
    Definitive or Strong, while every cited assertion for the gene is below
    Strong. Judged on same-disease assertions only. ``validity`` is where the
    tier belongs; this lists the records where the two slots currently tell a
    reader different things.

``uncached``  (report)
    A cited ``CGGV:`` identifier with no cache file, so nothing above can be
    judged for it. ``just clingen-rebuild --id <CGGV:...>`` generates one.

What it deliberately does not do
--------------------------------
It never writes to ``kb/``. ``backfill`` rows are mechanical, but a bulk edit
touching hundreds of entries would collide with every open curation PR, so the
list is a worklist rather than an ``--apply``.

It says nothing about a ``validity`` value on a gene the entry does not cite
ClinGen for. Such a value may come from GenCC, PanelApp or another submitter, or
from nowhere, and the record does not say which (see #10179).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dismech import kb_cache
from dismech.kb_cache import load_document

DEFAULT_KB_DIRS = ("kb/disorders",)
CACHE_DIR = ROOT / "references_cache"

# ClinGen's own spelling in the cached validity row -> GeneDiseaseValidityEnum.
CLINGEN_TO_ENUM = {
    "Definitive": "DEFINITIVE",
    "Strong": "STRONG",
    "Moderate": "MODERATE",
    "Limited": "LIMITED",
    "Disputed": "DISPUTED",
    "Refuted": "REFUTED",
    "No Known Disease Relationship": "NO_KNOWN_DISEASE_RELATIONSHIP",
}
# What `relationship_type: CAUSATIVE` claims, per its schema description.
CAUSATIVE_TIERS = frozenset({"DEFINITIVE", "STRONG"})

CGGV_RE = re.compile(r"CGGV:assertion_[A-Za-z0-9._:-]+")

CONFLICT = "conflict"
BACKFILL = "backfill"
AMBIGUOUS = "ambiguous"
OTHER_DISEASE = "other_disease"
OVERSTATED = "overstated"
UNCACHED = "uncached"
KINDS = (CONFLICT, BACKFILL, AMBIGUOUS, OTHER_DISEASE, OVERSTATED, UNCACHED)


@dataclass(frozen=True)
class Assertion:
    curie: str
    gene: str
    hgnc: str
    disease: str
    mondo: str
    moi: str
    classification: str  # GeneDiseaseValidityEnum value


@dataclass(frozen=True)
class Finding:
    path: str
    kind: str
    gene: str
    recorded: str
    clingen: str
    detail: str


def cache_path(curie: str, cache_dir: Path | None = None) -> Path:
    return (cache_dir or CACHE_DIR) / (curie.replace(":", "_", 1) + ".md")


def parse_assertion(curie: str, text: str) -> Assertion | None:
    """Read the single ``## Gene-disease validity`` table row of a CGGV cache file."""
    in_table = False
    for line in text.splitlines():
        if line.startswith("## "):
            in_table = line.strip() == "## Gene-disease validity"
            continue
        if not in_table or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] == "Gene" or set(cells[0]) <= {"-"}:
            continue
        if len(cells) < 6 or cells[5] not in CLINGEN_TO_ENUM:
            return None
        return Assertion(
            curie=curie,
            gene=cells[0],
            hgnc=cells[1].lower(),
            disease=cells[2],
            mondo=cells[3],
            moi=cells[4],
            classification=CLINGEN_TO_ENUM[cells[5]],
        )
    return None


def load_assertion(curie: str, cache_dir: Path | None = None) -> Assertion | None:
    path = cache_path(curie, cache_dir)
    if not path.is_file():
        return None
    return parse_assertion(curie, path.read_text(encoding="utf-8"))


def cited_cggv(node: Any) -> set[str]:
    """Every ``CGGV:`` identifier appearing in any string value of the entry."""
    found: set[str] = set()

    def walk(value: Any) -> None:
        if isinstance(value, str):
            found.update(CGGV_RE.findall(value))
        elif isinstance(value, dict):
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(node)
    return found


def gene_keys(record: dict[str, Any]) -> tuple[str, str]:
    """Return ``(hgnc_curie, symbol)`` for a genetic record, either may be empty."""
    gene_term = record.get("gene_term")
    term = gene_term.get("term") if isinstance(gene_term, dict) else None
    if not isinstance(term, dict):
        term = {}
    hgnc = str(term.get("id") or "").lower()
    symbol = str(term.get("label") or record.get("name") or "").strip()
    return (hgnc if hgnc.startswith("hgnc:") else ""), symbol


def entry_diseases(data: dict[str, Any]) -> set[str]:
    """MONDO identifiers that name the entry's own disease (see module docstring)."""

    def term_id(holder: Any) -> str:
        if not isinstance(holder, dict):
            return ""
        term = holder.get("term")
        return str(term.get("id") or "") if isinstance(term, dict) else ""

    ids = {term_id(data.get("disease_term"))}
    for subtype in data.get("has_subtypes") or []:
        if isinstance(subtype, dict):
            ids.add(term_id(subtype.get("subtype_term")))
    mappings = data.get("mappings")
    if isinstance(mappings, dict):
        for mapping in mappings.get("mondo_mappings") or []:
            if (
                isinstance(mapping, dict)
                and mapping.get("mapping_predicate") == "skos:exactMatch"
            ):
                ids.add(term_id(mapping))
    ids.discard("")
    return ids


def assertions_for(
    record: dict[str, Any], assertions: list[Assertion]
) -> list[Assertion]:
    hgnc, symbol = gene_keys(record)
    if hgnc:
        return [a for a in assertions if a.hgnc == hgnc]
    return [a for a in assertions if a.gene.upper() == symbol.upper()]


def assess(
    data: dict[str, Any], display: str, cache_dir: Path | None = None
) -> list[Finding]:
    findings: list[Finding] = []
    assertions: list[Assertion] = []
    for curie in sorted(cited_cggv(data)):
        assertion = load_assertion(curie, cache_dir)
        if assertion is None:
            # Missing file, or a file whose validity row does not parse.
            findings.append(Finding(display, UNCACHED, "", "", "", curie))
        else:
            assertions.append(assertion)

    own = entry_diseases(data)
    for record in data.get("genetic") or []:
        if not isinstance(record, dict):
            continue
        matched = assertions_for(record, assertions)
        if not matched:
            continue
        gene = gene_keys(record)[1] or str(record.get("name") or "?")
        recorded = str(record.get("validity") or "")
        same = [a for a in matched if a.mondo in own]
        if not same:
            if not recorded:
                other = sorted({a.classification for a in matched})
                detail = "; ".join(
                    f"{a.disease} {a.mondo} {a.moi} ({a.classification})"
                    for a in matched
                )
                findings.append(
                    Finding(display, OTHER_DISEASE, gene, "", ",".join(other), detail)
                )
            continue

        tiers = sorted({a.classification for a in same})
        clingen = ",".join(tiers)
        detail = "; ".join(
            f"{a.disease} {a.mondo} {a.moi} ({a.classification})" for a in same
        )

        if recorded:
            if recorded not in tiers:
                findings.append(
                    Finding(display, CONFLICT, gene, recorded, clingen, detail)
                )
        elif len(tiers) == 1:
            findings.append(Finding(display, BACKFILL, gene, "", clingen, detail))
        else:
            findings.append(Finding(display, AMBIGUOUS, gene, "", clingen, detail))

        if record.get("relationship_type") == "CAUSATIVE" and not (
            set(tiers) & CAUSATIVE_TIERS
        ):
            findings.append(
                Finding(display, OVERSTATED, gene, "CAUSATIVE", clingen, detail)
            )
    return findings


def _display(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def iter_entries(paths: list[str]) -> tuple[list[Path], list[str]]:
    """Same argument convention as ``check_causal_targets.py`` (#11939)."""
    if not paths:
        files: list[Path] = []
        for root in DEFAULT_KB_DIRS:
            files.extend(sorted((ROOT / root).glob("*.yaml")))
        return files, []
    files = []
    usage_errors: list[str] = []
    for raw in paths:
        path = Path(raw)
        if path.is_dir():
            found = sorted(path.rglob("*.yaml"))
            if not found:
                usage_errors.append(
                    f"{_display(path)}: directory contains no *.yaml files"
                )
            files.extend(found)
        else:
            files.append(path)
    return files, usage_errors


def collect(paths: list[str]) -> tuple[list[Finding], list[str]]:
    files, usage_errors = iter_entries(paths)
    findings: list[Finding] = []
    for path in files:
        if path.name.endswith(".history.yaml"):
            continue
        try:
            data = load_document(path)
        except OSError as exc:
            usage_errors.append(f"{_display(path)}: {exc.strerror or exc}")
            continue
        except Exception:
            # A parse failure is check-duplicate-keys' / linkml-validate's to report.
            continue
        if isinstance(data, dict):
            findings.extend(assess(data, _display(path)))
    return findings, usage_errors


def iter_rows(findings: list[Finding]) -> Iterator[str]:
    yield "path\tkind\tgene\trecorded\tclingen\tdetail"
    for f in findings:
        yield "\t".join((f.path, f.kind, f.gene, f.recorded, f.clingen, f.detail))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", nargs="*", help="default: kb/disorders")
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    parser.add_argument(
        "--kind",
        choices=KINDS,
        action="append",
        help="only report this finding class (repeatable)",
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="exit 0 even when a conflict is found (census mode)",
    )
    args = parser.parse_args(argv)

    # One walk over the corpus, so the parsed-KB cache would be pure cost.
    kb_cache.default_off()
    findings, usage_errors = collect(args.paths)
    if usage_errors:
        for message in usage_errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 2

    shown = [f for f in findings if not args.kind or f.kind in args.kind]
    if args.format == "tsv":
        for row in iter_rows(shown):
            print(row)
    else:
        counts = {kind: sum(f.kind == kind for f in findings) for kind in KINDS}
        print("Genetic.validity vs cited ClinGen assertions")
        for kind in KINDS:
            print(f"  {kind:<11} {counts[kind]}")
        for f in shown:
            if f.kind == UNCACHED:
                print(f"  [{f.kind}] {f.path}: {f.detail}")
            else:
                recorded = f" recorded={f.recorded}" if f.recorded else ""
                print(
                    f"  [{f.kind}] {f.path}: {f.gene}{recorded} "
                    f"clingen={f.clingen} -- {f.detail}"
                )

    conflicts = [f for f in findings if f.kind == CONFLICT]
    if conflicts and not args.report:
        print(
            f"FAIL: {len(conflicts)} validity value(s) contradict the ClinGen "
            "assertion the entry cites.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
