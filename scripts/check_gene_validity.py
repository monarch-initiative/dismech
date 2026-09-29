#!/usr/bin/env python3
"""Check ``Genetic.gene_disease_validity`` against the ClinGen assertions it cites (#10179).

``Genetic.gene_disease_validity`` records external classifications of how well
established a gene-disease relationship is: the tier, who assigned it
(``classified_by``), and the assertion's identifier (``external_id``). For a
ClinGen classification the tier is already written in the cited assertion:
``references_cache/CGGV_*.md`` holds it as one table row. This script reads that
row and compares it with the entry, and lists the ClinGen assertions an entry
cites but has not recorded.

It walks ``kb/disorders`` and, for every ``genetic[]`` record, collects the
``CGGV:`` identifiers the entry cites anywhere (evidence ``reference``,
``external_assertions[].external_id``, ...) whose cached row names the same
gene. Matching is on the HGNC identifier when the record binds one, else on the
gene symbol.

**An assertion belongs to the record that cites it.** An entry can carry
several ``genetic[]`` records for one gene -- a causative row and a
susceptibility row for the same locus -- and a ClinGen tier describes only one
of those claims. So an assertion is attributed to the record(s) whose own
subtree cites it. When it is cited elsewhere in the entry (an
``external_assertions`` block, a pathophysiology node) it is attributed to the
gene's record only if the gene has exactly one; otherwise it is ``unplaced``
and reported once, never copied onto every row.

**A tier belongs to a gene-disease pair, not to a gene.** An assertion only
speaks for the entry when its MONDO disease is the entry's own: the
``disease_term``, a ``has_subtypes[].subtype_term``, or a
``mappings.mondo_mappings`` term with ``mapping_predicate: skos:exactMatch``.
About a quarter of the ClinGen citations in the KB are for some other disease,
usually a broader ClinGen lumping (``ALPK3-Related_Hypertrophic_Cardiomyopathy``
cites ClinGen's generic hypertrophic cardiomyopathy) or the gene's second
disease. Those never feed ``backfill``.

Finding classes
---------------
``conflict``  (gates, exit 1)
    A recorded ``classified_by: CLINGEN`` assertion whose ``external_id`` is a
    cached ``CGGV:`` record that disagrees with it -- a different tier, or a
    different gene. Either the value or the identifier is wrong. It starts at
    zero, so gating it costs nothing and stops a hand-typed tier from
    contradicting the source it names.

``unsourced``  (report)
    A recorded ``classified_by: CLINGEN`` assertion with no ``CGGV:``
    ``external_id``, so nothing can check it.

``backfill``  (report)
    The entry cites a same-disease ClinGen assertion for the gene that
    ``gene_disease_validity`` does not record. The row is the assertion to
    copy: tier, MOI and identifier, with no judgement involved. A gene with
    two same-disease assertions (two modes of inheritance, or subtypes that
    are separate ClinGen diseases) gets two rows, one per assertion.

``other_disease``  (report)
    The entry cites ClinGen for this gene only against a different MONDO
    disease, and records nothing. Whether ClinGen's entity is the entry's (a
    lumped parent, a synonym MONDO has not merged) is a curator's call.

``unplaced``  (report)
    A same-disease ClinGen assertion cited outside ``genetic[]`` for a gene
    with several records, none of which cites it. Which claim the tier
    describes is a curator's call.

``overstated``  (report)
    ``relationship_type: CAUSATIVE``, whose schema description says ClinGen
    Definitive or Strong, while every cited same-disease ClinGen assertion for
    the gene is below Strong. The two slots currently tell a reader different
    things.

``uncached``  (report)
    A cited ``CGGV:`` identifier with no cache file, so nothing above can be
    judged for it. ``just clingen-rebuild --id <CGGV:...>`` generates one.

What it deliberately does not do
--------------------------------
It never writes to ``kb/``. ``backfill`` rows are mechanical, but a bulk edit
touching hundreds of entries would collide with every open curation PR, so the
list is a worklist rather than an ``--apply``.

It checks only ClinGen assertions, the one source dismech caches per record.
A recorded Gene2Phenotype, Orphanet or PanelApp classification is not checked.
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

# ClinGen's own spelling in the cached validity row ->
# GeneDiseaseValidityClassificationEnum.
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
UNSOURCED = "unsourced"
BACKFILL = "backfill"
OTHER_DISEASE = "other_disease"
UNPLACED = "unplaced"
OVERSTATED = "overstated"
UNCACHED = "uncached"
KINDS = (CONFLICT, UNSOURCED, BACKFILL, OTHER_DISEASE, UNPLACED, OVERSTATED, UNCACHED)


@dataclass(frozen=True)
class Assertion:
    curie: str
    gene: str
    hgnc: str
    disease: str
    mondo: str
    moi: str
    classification: str  # GeneDiseaseValidityClassificationEnum value


@dataclass(frozen=True)
class Finding:
    path: str
    kind: str
    record: str  # genetic[].name the finding is about; "" when none
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


def _describe(a: Assertion) -> str:
    return f"{a.disease} {a.mondo} {a.moi} ({a.classification}) {a.curie}"


def recorded_assertions(record: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        item
        for item in record.get("gene_disease_validity") or []
        if isinstance(item, dict)
    ]


def assess(
    data: dict[str, Any], display: str, cache_dir: Path | None = None
) -> list[Finding]:
    findings: list[Finding] = []
    assertions: list[Assertion] = []
    for curie in sorted(cited_cggv(data)):
        assertion = load_assertion(curie, cache_dir)
        if assertion is None:
            # Missing file, or a file whose validity row does not parse.
            findings.append(Finding(display, UNCACHED, "", "", "", "", curie))
        else:
            assertions.append(assertion)
    by_curie = {a.curie: a for a in assertions}

    own = entry_diseases(data)
    records = [r for r in data.get("genetic") or [] if isinstance(r, dict)]

    # Attribute each assertion to the record(s) it describes (module docstring).
    owned: dict[int, list[Assertion]] = {id(r): [] for r in records}
    for a in assertions:
        candidates = [r for r in records if a in assertions_for(r, [a])]
        citing = [r for r in candidates if a.curie in cited_cggv(r)]
        owners = citing or (candidates if len(candidates) == 1 else [])
        for r in owners:
            owned[id(r)].append(a)
        if candidates and not owners and a.mondo in own:
            findings.append(
                Finding(
                    display,
                    UNPLACED,
                    "",
                    a.gene,
                    "",
                    a.classification,
                    f"{_describe(a)}; records: "
                    + ", ".join(str(r.get("name") or "?") for r in candidates),
                )
            )

    for record in records:
        name = str(record.get("name") or "?")
        gene = gene_keys(record)[1] or name
        hgnc = gene_keys(record)[0]
        recorded = recorded_assertions(record)

        recorded_ids: set[str] = set()
        for item in recorded:
            tier = str(item.get("validity_classification") or "")
            external_id = str(item.get("external_id") or "")
            recorded_ids.add(external_id)
            if item.get("classified_by") != "CLINGEN":
                continue
            if not external_id.startswith("CGGV:"):
                findings.append(
                    Finding(
                        display, UNSOURCED, name, gene, tier, "", external_id or "-"
                    )
                )
                continue
            source = by_curie.get(external_id)
            if source is None:
                continue  # reported as uncached above
            wrong_gene = (hgnc and source.hgnc != hgnc) or (
                not hgnc and source.gene.upper() != gene.upper()
            )
            if source.classification != tier or wrong_gene:
                findings.append(
                    Finding(
                        display,
                        CONFLICT,
                        name,
                        gene,
                        tier,
                        source.classification,
                        f"{external_id} is {source.gene} / {_describe(source)}",
                    )
                )

        matched = owned[id(record)]
        if not matched:
            continue
        same = [a for a in matched if a.mondo in own]
        if not same:
            if not recorded:
                findings.append(
                    Finding(
                        display,
                        OTHER_DISEASE,
                        name,
                        gene,
                        "",
                        ",".join(sorted({a.classification for a in matched})),
                        "; ".join(_describe(a) for a in matched),
                    )
                )
            continue

        for a in same:
            if a.curie not in recorded_ids:
                findings.append(
                    Finding(
                        display,
                        BACKFILL,
                        name,
                        gene,
                        "",
                        a.classification,
                        _describe(a),
                    )
                )

        # Deliberately ignores mode of inheritance: CAUSATIVE is overstated
        # only when no same-disease assertion for this record reaches Strong.
        # JPH2 in dilated cardiomyopathy (Strong AR, Limited AD) is therefore
        # not flagged; which MOI the record claims is not machine-readable.
        tiers = {a.classification for a in same}
        if record.get("relationship_type") == "CAUSATIVE" and not (
            tiers & CAUSATIVE_TIERS
        ):
            findings.append(
                Finding(
                    display,
                    OVERSTATED,
                    name,
                    gene,
                    "CAUSATIVE",
                    ",".join(sorted(tiers)),
                    "; ".join(_describe(a) for a in same),
                )
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
    yield "path\tkind\trecord\tgene\trecorded\tclingen\tdetail"
    for f in findings:
        yield (
            f"{f.path}\t{f.kind}\t{f.record}\t{f.gene}\t{f.recorded}"
            f"\t{f.clingen}\t{f.detail}"
        )


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
        print("Genetic.gene_disease_validity vs cited ClinGen assertions")
        for kind in KINDS:
            print(f"  {kind:<11} {counts[kind]}")
        for f in shown:
            if f.kind == UNCACHED:
                print(f"  [{f.kind}] {f.path}: {f.detail}")
            else:
                recorded = f" recorded={f.recorded}" if f.recorded else ""
                print(
                    f"  [{f.kind}] {f.path}: {f.record or '-'} ({f.gene}){recorded} "
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
