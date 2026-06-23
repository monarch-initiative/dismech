"""
Mondo EMC (Externally Managed Content) TSV exporter.

Generates a stable TSV of dismech content that Mondo can ingest via its EMC
pipeline. One row per disorder that has a MONDO identifier.

MONDO ID resolution order
-------------------------
1. ``disease_term.term.id`` — the canonical disease identity field used in
   every dismech entry.  ~99 % of disorders carry a ``MONDO:`` CURIE here.
2. ``mappings.mondo_mappings`` (``skos:exactMatch``) — fallback for the small
   number of entries whose ``disease_term`` either is empty or maps to a
   non-MONDO ontology term.  The ``mappings`` block is primarily user-facing
   metadata and cross-reference provenance; it is not the canonical source.

Columns
-------
mondo_id               MONDO CURIE
mondo_label            Mondo term label (from whichever source resolved the ID)
dismech_url            Canonical URL to the dismech disorder page
dismech_definition     Top-level ``description`` field, normalised to a single line
dismech_exact_synonyms Pipe-separated values from the top-level ``synonyms`` list
dismech_pmids          Pipe-separated PMID CURIEs collected from all ``evidence``
                       items in the disorder file (definitions, pathophysiology,
                       phenotypes, etc.) that reference a ``PMID:`` identifier.
                       Empty when no PMIDs are cited anywhere in the file.

Empty cells are written as empty strings; Mondo decides per-row what to ingest.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

from dismech.export.utils import discover_disorder_files

DISMECH_BASE_URL = "https://dismech.monarchinitiative.org/pages/disorders"

TSV_COLUMNS = [
    "mondo_id",
    "mondo_label",
    "dismech_url",
    "dismech_definition",
    "dismech_exact_synonyms",
    "dismech_pmids",
]

_PMID_RE = re.compile(r"^PMID:\d+$")


def _collect_pmids(data: Any, seen: set[str] | None = None) -> list[str]:
    """Recursively collect unique PMID CURIEs from all ``reference`` fields."""
    if seen is None:
        seen = set()
    if isinstance(data, dict):
        ref = data.get("reference")
        if isinstance(ref, str) and _PMID_RE.match(ref) and ref not in seen:
            seen.add(ref)
        for value in data.values():
            _collect_pmids(value, seen)
    elif isinstance(data, list):
        for item in data:
            _collect_pmids(item, seen)
    return sorted(seen)


def _resolve_mondo_from_disease_term(data: dict[str, Any]) -> tuple[str, str]:
    """Return ``(mondo_id, mondo_label)`` from the ``disease_term`` field.

    Returns ``("", "")`` when ``disease_term.term.id`` is absent or not a
    ``MONDO:`` CURIE.
    """
    disease_term = data.get("disease_term") or {}
    term = disease_term.get("term") or {}
    term_id = (term.get("id") or "").strip()
    if term_id.startswith("MONDO:"):
        return term_id, (term.get("label") or "").strip()
    return "", ""


def _resolve_mondo_from_mappings(data: dict[str, Any]) -> tuple[str, str]:
    """Return ``(mondo_id, mondo_label)`` from the first skos:exactMatch in
    ``mappings.mondo_mappings``.

    Returns ``("", "")`` when no exactMatch exists.
    """
    mappings = data.get("mappings") or {}
    for mapping in (mappings.get("mondo_mappings")) or []:
        if not isinstance(mapping, dict):
            continue
        if mapping.get("mapping_predicate") != "skos:exactMatch":
            continue
        term = mapping.get("term") or {}
        mondo_id = (term.get("id") or "").strip()
        if not mondo_id:
            continue
        return mondo_id, (term.get("label") or "").strip()
    return "", ""


def _resolve_mondo(data: dict[str, Any]) -> tuple[str, str]:
    """Resolve MONDO ID/label for a disorder, trying ``disease_term`` first."""
    mondo_id, mondo_label = _resolve_mondo_from_disease_term(data)
    if mondo_id:
        return mondo_id, mondo_label
    return _resolve_mondo_from_mappings(data)


def _normalize_description(raw: str | None) -> str:
    """Collapse all whitespace (including newlines) in a description to single spaces."""
    if not raw:
        return ""
    return " ".join(str(raw).split())


def emc_row_for_disorder(yaml_path: Path) -> dict[str, str] | None:
    """Return a TSV row dict for one disorder, or ``None`` if not eligible.

    A disorder is eligible when a MONDO identifier can be resolved — either
    from ``disease_term.term.id`` or from ``mappings.mondo_mappings``.
    """
    data: dict[str, Any] = yaml.safe_load(yaml_path.read_text()) or {}
    mondo_id, mondo_label = _resolve_mondo(data)
    if not mondo_id:
        return None

    definition = _normalize_description(data.get("description"))
    synonyms = data.get("synonyms") or []
    synonyms_str = "|".join(str(s) for s in synonyms if s)
    pmids = _collect_pmids(data)
    pmids_str = "|".join(pmids)

    dismech_url = f"{DISMECH_BASE_URL}/{yaml_path.stem}.html"

    return {
        "mondo_id": mondo_id,
        "mondo_label": mondo_label,
        "dismech_url": dismech_url,
        "dismech_definition": definition,
        "dismech_exact_synonyms": synonyms_str,
        "dismech_pmids": pmids_str,
    }


def build_emc_export(disorder_files: list[Path]) -> list[dict[str, str]]:
    """Build the full EMC export across all disorder files."""
    rows: list[dict[str, str]] = []
    for file_path in disorder_files:
        row = emc_row_for_disorder(file_path)
        if row is not None:
            rows.append(row)
    rows.sort(key=lambda r: r["mondo_id"])
    return rows


def write_tsv(rows: list[dict[str, str]], output: Any) -> None:
    """Write EMC rows as tab-separated values to an open text stream."""
    writer = csv.DictWriter(
        output,
        fieldnames=TSV_COLUMNS,
        delimiter="\t",
        lineterminator="\n",
        extrasaction="ignore",
    )
    writer.writeheader()
    writer.writerows(rows)


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description=(
            "Generate a Mondo EMC TSV from the dismech knowledge base. "
            "One row per disorder with a MONDO identifier."
        )
    )
    parser.add_argument(
        "--kb-dir",
        "-i",
        default="kb/disorders",
        help="Input directory with disorder YAML files (default: kb/disorders)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="exports/mondo_emc.tsv",
        help="Output TSV path (use '-' for stdout; default: exports/mondo_emc.tsv)",
    )
    args = parser.parse_args()

    disorder_files = discover_disorder_files(Path(args.kb_dir))
    rows = build_emc_export(disorder_files)

    if args.output == "-":
        write_tsv(rows, sys.stdout)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", newline="", encoding="utf-8") as handle:
            write_tsv(rows, handle)
        print(
            f"Wrote {len(rows)} row(s) to {output_path}"
        )


if __name__ == "__main__":
    main()
