#!/usr/bin/env python3
"""Worklist of ClinVar "protective" variants checked against the dismech KB.

ClinVar is the one public resource that classifies germline variants as
*protective* in a structured, downloadable field. This script reads the
ClinVar ``variant_summary.txt.gz`` export, keeps every record whose aggregate
``ClinicalSignificance`` contains ``protective``, and reports for each one
whether a dismech entry already records the gene, and in which role. A
``genetic[]`` record with no bound ``gene_term`` is matched on the leading
gene symbol of its ``name``.

It is report-only. A ClinVar "protective" call is a lead: almost every such
record is a single submitter with ``no assertion criteria provided``, and the
protected-against condition is often a susceptibility or infection phenotype
that has no dismech entry at all. Nothing here edits ``kb/``.

KB status per record:

``RECORDED_PROTECTIVE``
    some entry has the gene in ``genetic[]`` with ``relationship_type: PROTECTIVE``.
``PROTECTIVE_IN_PROSE_ONLY``
    an entry carries the gene and its free-text ``association`` says it is
    protective, but no record types it ``relationship_type: PROTECTIVE``.
``GENE_OTHER_ROLE``
    the gene is in some entry's ``genetic[]``, never described as protective.
``DISEASE_ONLY``
    a MONDO id ClinVar gives for the condition is an entry's ``disease_term``,
    but that entry does not carry the gene.
``ABSENT``
    neither the gene nor the condition is in the KB.

Usage::

    uv run python scripts/clinvar_protective_worklist.py \\
        --variant-summary /path/to/variant_summary.txt.gz \\
        --out docs/reports/data/clinvar-protective-worklist.tsv

Without ``--variant-summary`` the ~460 MB export is streamed from the NCBI FTP
site and filtered in memory; it is never written to disk.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import io
import re
import sys
import urllib.request
from collections import defaultdict
from collections.abc import Iterable, Iterator
from pathlib import Path

from dismech import kb_cache
from dismech.kb_cache import load_document
from dismech.repo_root import repo_root

CLINVAR_URL = (
    "https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz"
)
KB_DIRS = ("kb/disorders", "kb/modules", "kb/comorbidities")
MONDO_RE = re.compile(r"MONDO:\d{7}")


def _open_summary(path: str | None) -> Iterator[str]:
    if path:
        handle = gzip.open(path, "rt", encoding="utf-8", errors="replace")
    else:
        response = urllib.request.urlopen(CLINVAR_URL)
        handle = io.TextIOWrapper(
            gzip.GzipFile(fileobj=response), encoding="utf-8", errors="replace"
        )
    with handle:
        yield from handle


def read_protective_records(lines: Iterable[str]) -> list[dict[str, str]]:
    """Return one dict per protective ClinVar variant (GRCh38 or unplaced)."""
    reader = csv.reader(lines, delimiter="\t")
    header = next(reader)
    header[0] = header[0].lstrip("#")
    idx = {name: i for i, name in enumerate(header)}
    seen: set[str] = set()
    records = []
    for row in reader:
        if len(row) < len(header):
            continue
        if row[idx["Assembly"]] == "GRCh37":
            continue  # each located variant appears once per assembly
        clinsig = row[idx["ClinicalSignificance"]]
        if "protective" not in clinsig.lower():
            continue
        variation_id = row[idx["VariationID"]]
        if variation_id in seen:
            continue
        seen.add(variation_id)
        records.append(
            {
                "variation_id": variation_id,
                "name": row[idx["Name"]],
                "gene_symbol": row[idx["GeneSymbol"]],
                "hgnc_id": row[idx["HGNC_ID"]],
                "clinical_significance": clinsig,
                "review_status": row[idx["ReviewStatus"]],
                "phenotypes": row[idx["PhenotypeList"]],
                "mondo_ids": ";".join(
                    sorted(set(MONDO_RE.findall(row[idx["PhenotypeIDS"]])))
                ),
                "rsid": row[idx["RS# (dbSNP)"]],
            }
        )
    return records


SYMBOL_RE = re.compile(r"^[A-Z][A-Z0-9-]{1,14}")


def index_kb(root: Path) -> tuple[dict, dict]:
    """Index KB genes and disease terms.

    Returns ``(genes, diseases)``. ``genes`` maps a key -- a lowercase hgnc
    CURIE, or ``sym:<SYMBOL>`` for a record with no bound gene term -- to a
    list of ``(entry, relationship_type, association)``. ``diseases`` maps a
    ``disease_term`` CURIE to entry stems.
    """
    genes: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    diseases: dict[str, list[str]] = defaultdict(list)
    for kb_dir in KB_DIRS:
        for path in sorted((root / kb_dir).glob("*.yaml")):
            doc = load_document(path)
            if not isinstance(doc, dict):
                continue
            stem = path.stem
            term = (doc.get("disease_term") or {}).get("term") or {}
            if term.get("id"):
                diseases[term["id"]].append(stem)
            for gene in doc.get("genetic") or []:
                if not isinstance(gene, dict):
                    continue
                gene_term = gene.get("gene_term") or {}
                gid = (gene_term.get("term") or {}).get("id")
                value = (
                    stem,
                    str(gene.get("relationship_type") or "-"),
                    " ".join(str(gene.get("association") or "").split()),
                )
                if gid:
                    genes[gid.lower()].append(value)
                    continue
                # Unbound record: fall back to the leading symbol of its name.
                label = str(gene.get("name") or gene_term.get("preferred_term") or "")
                match = SYMBOL_RE.match(label)
                if match:
                    genes[f"sym:{match.group(0)}"].append(value)
    return genes, diseases


def _says_protective(relationship: str, association: str) -> bool:
    return relationship == "PROTECTIVE" or "protect" in association.lower()


def classify(record: dict[str, str], genes: dict, diseases: dict) -> dict[str, str]:
    keys = [h.strip().lower() for h in record["hgnc_id"].split(";") if h.strip()]
    keys += [f"sym:{s.strip()}" for s in record["gene_symbol"].split(";") if s.strip()]
    hits = list(dict.fromkeys(hit for k in keys for hit in genes.get(k, [])))
    entries_with_gene = {stem for stem, _, _ in hits}
    disease_entries = sorted(
        {
            stem
            for mondo in record["mondo_ids"].split(";")
            if mondo
            for stem in diseases.get(mondo, [])
        }
        - entries_with_gene
    )
    if any(rel == "PROTECTIVE" for _, rel, _ in hits):
        status = "RECORDED_PROTECTIVE"
    elif any(_says_protective(rel, assoc) for _, rel, assoc in hits):
        status = "PROTECTIVE_IN_PROSE_ONLY"
    elif hits:
        status = "GENE_OTHER_ROLE"
    elif disease_entries:
        status = "DISEASE_ONLY"
    else:
        status = "ABSENT"
    roles = sorted(
        {
            f"{stem}:{rel}" + (f" ({assoc[:60]})" if assoc else "")
            for stem, rel, assoc in hits
        }
    )
    return {
        **record,
        "kb_status": status,
        "kb_gene_roles": "; ".join(roles),
        "kb_condition_entries": "; ".join(disease_entries),
    }


COLUMNS = [
    "kb_status",
    "gene_symbol",
    "hgnc_id",
    "variation_id",
    "rsid",
    "name",
    "clinical_significance",
    "review_status",
    "phenotypes",
    "mondo_ids",
    "kb_gene_roles",
    "kb_condition_entries",
]
STATUS_ORDER = [
    "ABSENT",
    "DISEASE_ONLY",
    "GENE_OTHER_ROLE",
    "PROTECTIVE_IN_PROSE_ONLY",
    "RECORDED_PROTECTIVE",
]


def prose_census(genes: dict) -> list[dict[str, str]]:
    """KB ``genetic[]`` records that say "protect" in prose but are not typed so."""
    rows = []
    for key, hits in genes.items():
        for stem, rel, assoc in hits:
            if rel != "PROTECTIVE" and "protect" in assoc.lower():
                rows.append(
                    {
                        "entry": stem,
                        "gene_key": key,
                        "relationship_type": rel,
                        "association": assoc,
                    }
                )
    return sorted(rows, key=lambda r: (r["entry"], r["gene_key"]))


def main(argv: list[str] | None = None) -> int:
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--variant-summary", help="local variant_summary.txt.gz")
    parser.add_argument("--out", help="write the TSV here (default: stdout)")
    parser.add_argument(
        "--prose-census",
        help=(
            "also write a TSV of KB genetic[] records whose association text says"
            " protective but whose relationship_type is not PROTECTIVE"
        ),
    )
    args = parser.parse_args(argv)

    records = read_protective_records(_open_summary(args.variant_summary))
    genes, diseases = index_kb(repo_root())
    rows = [classify(r, genes, diseases) for r in records]
    rows.sort(
        key=lambda r: (
            STATUS_ORDER.index(r["kb_status"]),
            r["gene_symbol"],
            r["variation_id"],
        )
    )

    out = open(args.out, "w", newline="") if args.out else sys.stdout
    try:
        writer = csv.DictWriter(out, COLUMNS, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if args.out:
            out.close()

    if args.prose_census:
        census = prose_census(genes)
        with open(args.prose_census, "w", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                ["entry", "gene_key", "relationship_type", "association"],
                delimiter="\t",
            )
            writer.writeheader()
            writer.writerows(census)
        print(
            f"{len(census)} KB genetic[] records call a gene protective in prose only",
            file=sys.stderr,
        )

    counts = defaultdict(int)
    for r in rows:
        counts[r["kb_status"]] += 1
    summary = ", ".join(f"{s}={counts[s]}" for s in STATUS_ORDER)
    print(f"{len(rows)} protective ClinVar variants: {summary}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
