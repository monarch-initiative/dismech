#!/usr/bin/env python3
"""Compare each ClinGen validity row's gene with its MONDO class's causal gene (#12941).

A ClinGen Gene-Disease Validity row names a gene and a MONDO disease. MONDO
records, for most Mendelian classes, the gene the disease is defined by: an
``RO:0004003`` ("has material basis in germline mutation in") restriction on the
class. Nothing compared the two, so a row pairing one gene with another gene's
disease is quotable as-is::

    "COQ6","HGNC:20233","primary coenzyme Q10 deficiency 8","MONDO:0014754",...

``MONDO:0014754`` is defined by ``HGNC:2244`` (COQ7). COQ6's own class is
``MONDO:0013836``. The row is a real gene, a real MONDO class and a real ClinGen
classification, so a ``CGGV:`` snippet quoting it would pass every gate -- the
upstream form of the self-consistent-but-wrong gene binding in CLAUDE.md.

Classification, one per row
---------------------------
``match``
    The row's HGNC id is among the class's ``RO:0004003`` genes.
``names_another_gene``
    The class asserts one or more human causal genes, the row's gene is not one
    of them, and ClinGen classifies the pair as a real relationship (Definitive,
    Strong, Moderate or Limited). The finding this exists for.
``contested_pairing``
    The same mismatch on a Disputed, Refuted or No Known Disease Relationship
    row. These are usually deliberate: ClinGen curated a gene proposed for
    another gene's disease and found against it (KRAS, BRAF and SOS1 against
    HRAS-defined Costello syndrome). Counted, and listed in ``--format tsv``.
``no_causal_gene``
    The class asserts no human (HGNC) causal gene. Usually a broader class ClinGen curates
    against (``hypertrophic cardiomyopathy``), which MONDO does not define by a
    single gene. Counted, not reported.
``obsolete``
    MONDO has retired the class; the replacement, if any, is printed.
``not_found``
    OLS answered and has no such class.
``uncached`` / ``lookup_failed``
    No answer: not in the local cache (run with ``--resolve``), or OLS could
    not be asked.

The MONDO facts come from OLS (:mod:`dismech.mondo_ols`, the same reader
``just preflight-dr`` uses) and are cached in the gitignored
``tmp/clingen_mondo_genes.json``, so after one ``--resolve`` run the report is
offline. The cache records the MONDO release OLS served; delete the file (or
pass ``--refresh``) to re-read it after a MONDO release.

Each row also says whether any ``kb/`` entry cites its ``CGGV:`` assertion,
because a mispaired row is a curation hazard mainly when somebody quotes it.

Report-only: exits 0 even with findings. ``--strict`` exits 1 on
``names_another_gene``. A mispaired row is ClinGen's to correct upstream, not
something a dismech entry can fix, so this is a report and has no baseline.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from dismech.mondo_ols import (  # noqa: E402
    OlsLookupError,
    OlsTermNotFound,
    fetch_mondo_release,
    fetch_mondo_term,
)
from dismech.repo_root import repo_root  # noqa: E402

CACHE_VERSION = 1
CSV_HEADERS = [
    "GENE SYMBOL",
    "GENE ID (HGNC)",
    "DISEASE LABEL",
    "DISEASE ID (MONDO)",
    "MOI",
    "SOP",
    "CLASSIFICATION",
    "ONLINE REPORT",
    "CLASSIFICATION DATE",
    "GCEP",
]
ASSERTION_RE = re.compile(r"CGGV:assertion_[A-Za-z0-9_.:-]+")

MATCH = "match"
NAMES_ANOTHER_GENE = "names_another_gene"
CONTESTED_PAIRING = "contested_pairing"
NO_CAUSAL_GENE = "no_causal_gene"
OBSOLETE = "obsolete"
NOT_FOUND = "not_found"
UNCACHED = "uncached"
LOOKUP_FAILED = "lookup_failed"
STATUS_ORDER = (
    NAMES_ANOTHER_GENE,
    OBSOLETE,
    NOT_FOUND,
    CONTESTED_PAIRING,
    MATCH,
    NO_CAUSAL_GENE,
    UNCACHED,
    LOOKUP_FAILED,
)
#: Statuses listed row by row; the rest are counted.
REPORTED = (NAMES_ANOTHER_GENE, OBSOLETE, NOT_FOUND)
#: ClinGen tiers asserting that the gene does NOT cause the disease.
CONTESTED_TIERS = frozenset({"disputed", "refuted", "no known disease relationship"})


@dataclass(frozen=True)
class ValidityRow:
    gene_symbol: str
    gene_id: str
    disease_label: str
    mondo_id: str
    moi: str
    classification: str
    assertion_id: str


@dataclass(frozen=True)
class Finding:
    row: ValidityRow
    status: str
    mondo_label: str = ""
    mondo_genes: tuple[str, ...] = ()
    mondo_gene_labels: tuple[str, ...] = ()
    replaced_by: tuple[str, ...] = ()
    cited_in: tuple[str, ...] = ()
    detail: str = ""


def default_csv() -> Path:
    """The export ``clingen-rebuild`` would read: ``data/`` first, then the committed copy."""
    root = repo_root()
    fresh = root / "data" / "clingen" / "gene_validity.csv"
    return fresh if fresh.exists() else root / "cache" / "clingen" / "gene_validity.csv"


def default_cache() -> Path:
    return repo_root() / "tmp" / "clingen_mondo_genes.json"


def _assertion_id(url: str) -> str:
    """The record id at the end of the report URL.

    Usually ``CGGV:assertion_...``; a few legacy rows carry another prefix
    (``CGGCIEX:assertion_3211``), which is kept as-is rather than dropped.
    """
    segment = url.replace("%3A", ":").rstrip("/").rsplit("/", 1)[-1]
    if segment.startswith("assertion_"):
        return f"CGGV:{segment}"
    return segment if "assertion_" in segment else ""


def read_rows(path: Path) -> tuple[list[ValidityRow], str]:
    """The data rows of a ClinGen validity export, and its ``FILE CREATED`` date."""
    reader = csv.reader(path.read_text(encoding="utf-8-sig").splitlines())
    created = ""
    for row in reader:
        if row and row[0].startswith("FILE CREATED:"):
            created = row[0].split(":", 1)[1].strip()
        if row[: len(CSV_HEADERS)] == CSV_HEADERS:
            break
    else:
        raise ValueError(f"{path} has no ClinGen validity header row")
    rows: list[ValidityRow] = []
    for row in reader:
        if len(row) < len(CSV_HEADERS) or all(set(c) <= {"+"} for c in row):
            continue
        data = dict(zip(CSV_HEADERS, (c.strip() for c in row)))
        if not data["GENE SYMBOL"] or not data["DISEASE ID (MONDO)"]:
            continue
        rows.append(
            ValidityRow(
                gene_symbol=data["GENE SYMBOL"],
                gene_id=data["GENE ID (HGNC)"].upper(),
                disease_label=data["DISEASE LABEL"],
                mondo_id=data["DISEASE ID (MONDO)"],
                moi=data["MOI"],
                classification=data["CLASSIFICATION"],
                assertion_id=_assertion_id(data["ONLINE REPORT"]),
            )
        )
    return rows, created


def load_cache(path: Path) -> dict:
    if not path.exists():
        return {"version": CACHE_VERSION, "release": "", "terms": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") != CACHE_VERSION:
        return {"version": CACHE_VERSION, "release": "", "terms": {}}
    return data


def save_cache(path: Path, cache: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    cache["terms"] = dict(sorted(cache["terms"].items()))
    path.write_text(
        json.dumps(cache, indent=1, sort_keys=True) + "\n", encoding="utf-8"
    )


def _fetch(mondo_id: str, timeout: float) -> tuple[str, dict]:
    try:
        facts = fetch_mondo_term(mondo_id, timeout=timeout)
    except OlsTermNotFound:
        return mondo_id, {"not_found": True}
    except OlsLookupError as exc:
        return mondo_id, {"error": str(exc)}
    return mondo_id, {
        "label": facts.label,
        "obsolete": facts.obsolete,
        "genes": list(facts.genes),
        "gene_labels": dict(facts.gene_labels),
        "replaced_by": list(facts.replaced_by),
    }


def resolve(
    mondo_ids: set[str], cache: dict, *, refresh: bool, workers: int, timeout: float
) -> int:
    """Fetch every uncached id (all of them under ``refresh``); return the count fetched."""
    todo = sorted(m for m in mondo_ids if refresh or m not in cache["terms"])
    if not todo:
        return 0
    stamp = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for mondo_id, facts in pool.map(lambda m: _fetch(m, timeout), todo):
            if "error" in facts:  # never cache a failed lookup as a fact
                cache["terms"].pop(mondo_id, None)
                cache.setdefault("errors", {})[mondo_id] = facts["error"]
                continue
            cache.get("errors", {}).pop(mondo_id, None)
            facts["retrieved_at"] = stamp
            cache["terms"][mondo_id] = facts
    cache["release"] = fetch_mondo_release(timeout=timeout) or cache.get("release", "")
    return len(todo)


def kb_citations(root: Path) -> dict[str, list[str]]:
    """``CGGV:`` assertion id -> the ``kb/`` files that mention it."""
    cited: dict[str, set[str]] = {}
    for path in sorted((root / "kb").rglob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        if "CGGV:" not in text:
            continue
        for match in set(ASSERTION_RE.findall(text)):
            cited.setdefault(match, set()).add(path.stem)
    return {k: sorted(v) for k, v in cited.items()}


def classify(row: ValidityRow, cache: dict, cited: dict[str, list[str]]) -> Finding:
    cited_in = tuple(cited.get(row.assertion_id, ()))
    facts = cache["terms"].get(row.mondo_id)
    if facts is None:
        error = cache.get("errors", {}).get(row.mondo_id)
        status = LOOKUP_FAILED if error else UNCACHED
        return Finding(row, status, cited_in=cited_in, detail=error or "")
    if facts.get("not_found"):
        return Finding(row, NOT_FOUND, cited_in=cited_in)
    # Only HGNC genes are comparable with the row; MONDO's non-human classes
    # carry NCBIGene fillers for the animal's own gene.
    genes = tuple(g for g in facts.get("genes", ()) if g.upper().startswith("HGNC:"))
    labels = tuple(facts.get("gene_labels", {}).get(g, "") for g in genes)
    common = dict(
        mondo_label=facts.get("label", ""),
        mondo_genes=genes,
        mondo_gene_labels=labels,
        replaced_by=tuple(facts.get("replaced_by", ())),
        cited_in=cited_in,
    )
    if facts.get("obsolete"):
        return Finding(row, OBSOLETE, **common)
    if not genes:
        return Finding(row, NO_CAUSAL_GENE, **common)
    if row.gene_id in {g.upper() for g in genes}:
        return Finding(row, MATCH, **common)
    if row.classification.lower() in CONTESTED_TIERS:
        return Finding(row, CONTESTED_PAIRING, **common)
    return Finding(row, NAMES_ANOTHER_GENE, **common)


def _genes_text(f: Finding) -> str:
    return ", ".join(
        f"{label} ({gene})" if label else gene
        for gene, label in zip(f.mondo_genes, f.mondo_gene_labels)
    )


def tsv_lines(findings: list[Finding]):
    yield (
        "status\tassertion\tgene\tgene_id\tmondo_id\tclingen_disease_label"
        "\tmondo_label\tmondo_causal_genes\treplaced_by\tclassification\tmoi\tcited_in"
    )
    for f in findings:
        r = f.row
        yield "\t".join(
            [
                f.status,
                r.assertion_id,
                r.gene_symbol,
                r.gene_id,
                r.mondo_id,
                r.disease_label,
                f.mondo_label,
                _genes_text(f),
                ",".join(f.replaced_by),
                r.classification,
                r.moi,
                ",".join(f.cited_in),
            ]
        )


def _row_line(f: Finding) -> str:
    r = f.row
    line = f"  {r.gene_symbol} ({r.gene_id}) -> {r.mondo_id} {r.disease_label!r}"
    if f.status == NAMES_ANOTHER_GENE:
        line += f"; MONDO's causal gene: {_genes_text(f)}"
    elif f.status == OBSOLETE:
        line += f"; replaced by {', '.join(f.replaced_by) or 'nothing'}"
    line += f" [{r.classification}, {r.moi}]"
    if f.cited_in:
        line += f"\n      cited by kb/: {', '.join(f.cited_in)}"
    if r.assertion_id:
        line += f"\n      {r.assertion_id}"
    return line


def summary_lines(
    findings: list[Finding], *, csv_path: Path, created: str, cache: dict
):
    counts = Counter(f.status for f in findings)
    yield f"ClinGen export: {csv_path} (FILE CREATED {created or 'unknown'})"
    yield f"MONDO facts: OLS, release {cache.get('release') or 'unknown'}"
    yield f"rows: {len(findings)} across {len({f.row.mondo_id for f in findings})} MONDO classes"
    for status in STATUS_ORDER:
        if counts[status]:
            yield f"  {status:<20} {counts[status]}"
    if counts[UNCACHED]:
        yield ""
        yield (
            f"{counts[UNCACHED]} row(s) have no cached MONDO facts and so no opinion; "
            "run `just list-clingen-mondo-gene-mismatches-online` to fetch them."
        )
    for status in REPORTED:
        rows = [f for f in findings if f.status == status]
        if not rows:
            continue
        cited = sum(1 for f in rows if f.cited_in)
        yield ""
        yield f"{status} ({len(rows)}; {cited} cited by a kb/ entry):"
        for f in sorted(rows, key=lambda f: (not f.cited_in, f.row.gene_symbol)):
            yield _row_line(f)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--csv", type=Path, help="ClinGen validity export to read")
    parser.add_argument("--cache", type=Path, help="MONDO facts cache (JSON)")
    parser.add_argument(
        "--resolve", action="store_true", help="fetch uncached MONDO classes from OLS"
    )
    parser.add_argument(
        "--refresh", action="store_true", help="re-fetch every MONDO class from OLS"
    )
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    parser.add_argument(
        "--findings-only",
        action="store_true",
        help="with --format tsv, only the reported statuses",
    )
    parser.add_argument(
        "--strict", action="store_true", help=f"exit 1 on any {NAMES_ANOTHER_GENE} row"
    )
    args = parser.parse_args(argv)

    csv_path = args.csv or default_csv()
    cache_path = args.cache or default_cache()
    rows, created = read_rows(csv_path)
    cache = load_cache(cache_path)
    if args.resolve or args.refresh:
        fetched = resolve(
            {r.mondo_id for r in rows},
            cache,
            refresh=args.refresh,
            workers=args.workers,
            timeout=args.timeout,
        )
        save_cache(cache_path, cache)
        print(
            f"fetched {fetched} MONDO class(es) from OLS -> {cache_path}",
            file=sys.stderr,
        )

    cited = kb_citations(repo_root())
    findings = [classify(r, cache, cited) for r in rows]

    if args.format == "tsv":
        shown = (
            [f for f in findings if f.status in REPORTED]
            if args.findings_only
            else findings
        )
        for line in tsv_lines(shown):
            print(line)
    else:
        for line in summary_lines(
            findings, csv_path=csv_path, created=created, cache=cache
        ):
            print(line)

    if args.strict and any(f.status == NAMES_ANOTHER_GENE for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
