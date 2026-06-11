"""
Disease + subtype inventory exporter.

Emits one CSV row for every disease entry **and** every subtype defined under
``has_subtypes``, recording whether each maps to a MONDO disease class (and via
what route). This gives a flat, auditable census of knowledge-base coverage and
MONDO alignment — including the gaps where no MONDO mapping exists.

MONDO resolution order for a disease or subtype:

1. The primary term (``disease_term`` / ``subtype_term``) when its id is a
   ``MONDO:`` CURIE.
2. An ``skos:exactMatch`` entry in ``mappings.mondo_mappings``.
3. Any other ``mappings.mondo_mappings`` entry.

When none of these yield a MONDO id, ``mondo_id`` is left blank and
``has_mondo`` is ``false``.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

import yaml

INVENTORY_COLUMNS = [
    "name",
    "entry_type",
    "parent_disease",
    "source_file",
    "primary_term_id",
    "primary_term_label",
    "mondo_id",
    "mondo_label",
    "mondo_source",
    "has_mondo",
]


def _term_of(descriptor: Any) -> dict[str, Any]:
    """Return the nested ``term`` dict from a descriptor, or an empty dict."""
    if isinstance(descriptor, dict) and isinstance(descriptor.get("term"), dict):
        return descriptor["term"]
    return {}


def _resolve_mondo(
    term_id: str | None,
    term_label: str | None,
    mappings: dict[str, Any] | None,
) -> tuple[str, str, str]:
    """Resolve a MONDO id/label/source for a disease or subtype.

    Returns ``(mondo_id, mondo_label, mondo_source)``; all empty strings when no
    MONDO mapping is available.
    """
    if term_id and term_id.startswith("MONDO:"):
        return term_id, term_label or "", "primary_term"

    mondo_mappings = (mappings or {}).get("mondo_mappings") or []
    fallback: tuple[str, str] | None = None
    for mapping in mondo_mappings:
        if not isinstance(mapping, dict):
            continue
        term = _term_of(mapping)
        mondo_id = term.get("id")
        if not mondo_id:
            continue
        if mapping.get("mapping_predicate") == "skos:exactMatch":
            return mondo_id, term.get("label") or "", "mondo_mappings"
        if fallback is None:
            fallback = (mondo_id, term.get("label") or "")

    if fallback is not None:
        return fallback[0], fallback[1], "mondo_mappings"
    return "", "", ""


def _row(
    name: str,
    entry_type: str,
    parent_disease: str,
    source_file: str,
    term: dict[str, Any],
    mappings: dict[str, Any] | None,
) -> dict[str, str]:
    term_id = term.get("id") or ""
    term_label = term.get("label") or ""
    mondo_id, mondo_label, mondo_source = _resolve_mondo(term_id, term_label, mappings)
    return {
        "name": name,
        "entry_type": entry_type,
        "parent_disease": parent_disease,
        "source_file": source_file,
        "primary_term_id": term_id,
        "primary_term_label": term_label,
        "mondo_id": mondo_id,
        "mondo_label": mondo_label,
        "mondo_source": mondo_source,
        "has_mondo": "true" if mondo_id else "false",
    }


def extract_rows(disorder: dict[str, Any], source_file: str) -> list[dict[str, str]]:
    """Return inventory rows for one disorder: the disease plus each subtype."""
    if not isinstance(disorder, dict):
        return []

    disease_name = disorder.get("name", "Unknown")
    rows = [
        _row(
            name=disease_name,
            entry_type="disease",
            parent_disease="",
            source_file=source_file,
            term=_term_of(disorder.get("disease_term")),
            mappings=disorder.get("mappings"),
        )
    ]

    for subtype in disorder.get("has_subtypes") or []:
        if not isinstance(subtype, dict) or not subtype.get("name"):
            continue
        rows.append(
            _row(
                name=subtype["name"],
                entry_type="subtype",
                parent_disease=disease_name,
                source_file=source_file,
                term=_term_of(subtype.get("subtype_term")),
                mappings=subtype.get("mappings"),
            )
        )
    return rows


def build_inventory(disorder_files: list[Path]) -> list[dict[str, str]]:
    """Build the full inventory across all disorder files."""
    rows: list[dict[str, str]] = []
    for file_path in disorder_files:
        with open(file_path) as handle:
            disorder = yaml.safe_load(handle)
        rows.extend(extract_rows(disorder, file_path.name))
    return rows


def write_csv(rows: list[dict[str, str]], output) -> None:
    """Write inventory rows as CSV to an open text stream."""
    writer = csv.DictWriter(output, fieldnames=INVENTORY_COLUMNS)
    writer.writeheader()
    writer.writerows(rows)


def _discover_disorder_files(input_dir: Path) -> list[Path]:
    return [
        path
        for path in sorted(input_dir.glob("*.yaml"))
        if not path.name.endswith(".history.yaml")
    ]


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Export a disease + subtype inventory with MONDO mappings as CSV"
    )
    parser.add_argument(
        "--input-dir",
        "-i",
        default="kb/disorders",
        help="Input directory with disorder YAML files",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="-",
        help="Output CSV path (use '-' for stdout)",
    )
    args = parser.parse_args()

    disorder_files = _discover_disorder_files(Path(args.input_dir))
    rows = build_inventory(disorder_files)

    if args.output == "-":
        write_csv(rows, sys.stdout)
    else:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", newline="") as handle:
            write_csv(rows, handle)
        diseases = sum(1 for row in rows if row["entry_type"] == "disease")
        subtypes = sum(1 for row in rows if row["entry_type"] == "subtype")
        with_mondo = sum(1 for row in rows if row["has_mondo"] == "true")
        print(
            f"Wrote {len(rows)} rows ({diseases} diseases + {subtypes} subtypes; "
            f"{with_mondo} with MONDO) to {output_path}"
        )


if __name__ == "__main__":
    main()
