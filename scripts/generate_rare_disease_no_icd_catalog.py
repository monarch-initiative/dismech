#!/usr/bin/env python3
"""Generate rare-disease ICD coverage catalogs with review status columns.

This script builds project CSVs for:
- all active MONDO rare diseases and their ICD coverage
- rare diseases missing ICD-11 Foundation mappings
- rare diseases missing all ICD mappings
- rare diseases missing ICD-11 Foundation but having another ICD mapping

It also adds independent ICD-11F candidate matches by directly matching
MONDO labels/exact synonyms to ICD-11F labels (not using MONDO xrefs).
"""

from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from collections import defaultdict
from pathlib import Path


ICD11_PREFIXES = ("icd11.foundation:", "icd11f:")
ICD10CM_PREFIX = "icd10cm:"
ANY_ICD_PREFIXES = ICD11_PREFIXES + ("icd10cm:", "icd10who:", "icd9:")

STATUS_COLUMNS = [
    "search_status",
    "search_method",
    "search_date",
    "searched_by",
    "selected_icd11f_id",
    "selected_icd11f_label",
    "search_confidence",
    "search_notes",
]

DEFAULT_STATUS = {
    "search_status": "NOT_REVIEWED",
    "search_method": "",
    "search_date": "",
    "searched_by": "",
    "selected_icd11f_id": "",
    "selected_icd11f_label": "",
    "search_confidence": "",
    "search_notes": "",
}

BASE_FIELDS = [
    "mondo_id",
    "label",
    "definition",
    "ordo_mappings",
    "orphanet_mappings",
    "omim_mappings",
    "omimps_mappings",
    "has_icd11f",
    "icd11f_xrefs",
    "has_icd10cm",
    "icd10cm_xrefs",
    "has_any_icd",
    "any_icd_xrefs",
    "independent_candidate_icd11f_count",
    "independent_candidate_icd11f_ids",
    "independent_candidate_icd11f_labels",
    "independent_candidate_match_on",
]


def normalize_text(text: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", " ", text.lower())
    return " ".join(normalized.split())


def join_values(values: list[str]) -> str:
    return "|".join(sorted(set(v for v in values if v)))


def fetch_rare_term_ids(conn: sqlite3.Connection) -> list[str]:
    query = """
    SELECT DISTINCT s.subject
    FROM statements s
    LEFT JOIN deprecated_node d ON s.subject = d.id
    WHERE s.predicate = 'oio:inSubset'
      AND s.object = 'obo:mondo#rare'
      AND d.id IS NULL
    ORDER BY s.subject
    """
    return [row[0] for row in conn.execute(query)]


def fetch_single_value_map(conn: sqlite3.Connection, predicate: str) -> dict[str, str]:
    out: dict[str, str] = {}
    query = """
    SELECT subject, value
    FROM statements
    WHERE predicate = ?
      AND value IS NOT NULL
    ORDER BY subject, value
    """
    for subject, value in conn.execute(query, (predicate,)):
        if subject not in out:
            out[subject] = value
    return out


def fetch_multi_value_map(
    conn: sqlite3.Connection, predicate: str
) -> dict[str, list[str]]:
    out: dict[str, list[str]] = defaultdict(list)
    query = """
    SELECT subject, value
    FROM statements
    WHERE predicate = ?
      AND value IS NOT NULL
    ORDER BY subject, value
    """
    for subject, value in conn.execute(query, (predicate,)):
        out[subject].append(value)
    return out


def build_icd11_label_index(
    conn: sqlite3.Connection,
) -> dict[str, list[tuple[str, str]]]:
    by_norm: dict[str, list[tuple[str, str]]] = defaultdict(list)
    query = """
    SELECT subject, value
    FROM statements
    WHERE predicate = 'rdfs:label'
      AND value IS NOT NULL
    """
    for subject, label in conn.execute(query):
        norm = normalize_text(label)
        if norm:
            by_norm[norm].append((subject, label))
    return by_norm


def has_prefix(value: str, prefixes: tuple[str, ...]) -> bool:
    low = value.lower()
    return any(low.startswith(p) for p in prefixes)


def values_with_prefix(values: list[str], prefixes: tuple[str, ...]) -> list[str]:
    return [v for v in values if has_prefix(v, prefixes)]


def match_icd11_candidates(
    label: str,
    exact_synonyms: list[str],
    icd11_index: dict[str, list[tuple[str, str]]],
) -> tuple[list[str], list[str], list[str]]:
    # Track whether a candidate came from exact label and/or exact synonym match.
    candidate_sources: dict[str, set[str]] = defaultdict(set)
    candidate_labels: dict[str, str] = {}

    terms = [("label", label)] + [("exact_synonym", s) for s in exact_synonyms]
    for source, text in terms:
        if not text:
            continue
        norm = normalize_text(text)
        if not norm:
            continue
        for icd_id, icd_label in icd11_index.get(norm, []):
            candidate_sources[icd_id].add(source)
            candidate_labels[icd_id] = icd_label

    candidate_ids = sorted(candidate_sources)
    candidate_id_values = candidate_ids
    candidate_label_values = [candidate_labels[cid] for cid in candidate_ids]
    candidate_source_values = [
        f"{cid}:{'+'.join(sorted(candidate_sources[cid]))}" for cid in candidate_ids
    ]
    return candidate_id_values, candidate_label_values, candidate_source_values


def load_existing_status(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            return {}
        if "mondo_id" not in reader.fieldnames:
            return {}
        missing_cols = [c for c in STATUS_COLUMNS if c not in reader.fieldnames]
        if missing_cols:
            return {}

        status_map: dict[str, dict[str, str]] = {}
        for row in reader:
            mondo_id = row.get("mondo_id")
            if not mondo_id:
                continue
            status_map[mondo_id] = {c: row.get(c, "") for c in STATUS_COLUMNS}
        return status_map


def apply_status(
    rows: list[dict[str, str]], existing_status: dict[str, dict[str, str]]
) -> None:
    for row in rows:
        saved = existing_status.get(row["mondo_id"], {})
        for col in STATUS_COLUMNS:
            row[col] = saved.get(col, DEFAULT_STATUS[col])


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_rows(
    rare_ids: list[str],
    labels: dict[str, str],
    definitions: dict[str, str],
    xrefs: dict[str, list[str]],
    exact_synonyms: dict[str, list[str]],
    icd11_index: dict[str, list[tuple[str, str]]],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for mondo_id in rare_ids:
        label = labels.get(mondo_id, "").strip()
        definition = " ".join(definitions.get(mondo_id, "").split())
        term_xrefs = xrefs.get(mondo_id, [])
        term_synonyms = exact_synonyms.get(mondo_id, [])

        icd11f_xrefs = values_with_prefix(term_xrefs, ICD11_PREFIXES)
        icd10cm_xrefs = values_with_prefix(term_xrefs, (ICD10CM_PREFIX,))
        any_icd_xrefs = values_with_prefix(term_xrefs, ANY_ICD_PREFIXES)
        ordo_xrefs = values_with_prefix(term_xrefs, ("ordo:",))
        orphanet_xrefs = values_with_prefix(term_xrefs, ("orphanet:",))
        omim_xrefs = values_with_prefix(term_xrefs, ("omim:",))
        omimps_xrefs = values_with_prefix(term_xrefs, ("omimps:",))

        cand_ids, cand_labels, cand_sources = match_icd11_candidates(
            label=label,
            exact_synonyms=term_synonyms,
            icd11_index=icd11_index,
        )

        row = {
            "mondo_id": mondo_id,
            "label": label,
            "definition": definition,
            "ordo_mappings": join_values(ordo_xrefs),
            "orphanet_mappings": join_values(orphanet_xrefs),
            "omim_mappings": join_values(omim_xrefs),
            "omimps_mappings": join_values(omimps_xrefs),
            "has_icd11f": "1" if icd11f_xrefs else "0",
            "icd11f_xrefs": join_values(icd11f_xrefs),
            "has_icd10cm": "1" if icd10cm_xrefs else "0",
            "icd10cm_xrefs": join_values(icd10cm_xrefs),
            "has_any_icd": "1" if any_icd_xrefs else "0",
            "any_icd_xrefs": join_values(any_icd_xrefs),
            "independent_candidate_icd11f_count": str(len(cand_ids)),
            "independent_candidate_icd11f_ids": join_values(cand_ids),
            "independent_candidate_icd11f_labels": join_values(cand_labels),
            "independent_candidate_match_on": join_values(cand_sources),
        }
        rows.append(row)

    rows.sort(key=lambda r: (r["label"].lower(), r["mondo_id"]))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate rare MONDO diseases ICD gap catalogs with review status flags."
    )
    parser.add_argument(
        "--mondo-db",
        default=str(Path.home() / ".data/oaklib/mondo.db"),
        help="Path to MONDO sqlite database (default: ~/.data/oaklib/mondo.db)",
    )
    parser.add_argument(
        "--icd11f-db",
        default=str(Path.home() / ".data/oaklib/icd11f.db"),
        help="Path to ICD-11F sqlite database (default: ~/.data/oaklib/icd11f.db)",
    )
    parser.add_argument(
        "--out-dir",
        default="projects/RARE_DISEASE_NO_ICD_CODE",
        help="Output directory for CSV files",
    )
    args = parser.parse_args()

    mondo_db = Path(args.mondo_db)
    icd11f_db = Path(args.icd11f_db)
    out_dir = Path(args.out_dir)

    if not mondo_db.exists():
        raise FileNotFoundError(f"MONDO DB not found: {mondo_db}")
    if not icd11f_db.exists():
        raise FileNotFoundError(f"ICD11F DB not found: {icd11f_db}")

    with (
        sqlite3.connect(mondo_db) as mondo_conn,
        sqlite3.connect(icd11f_db) as icd11_conn,
    ):
        rare_ids = fetch_rare_term_ids(mondo_conn)
        labels = fetch_single_value_map(mondo_conn, "rdfs:label")
        definitions = fetch_single_value_map(mondo_conn, "IAO:0000115")
        xrefs = fetch_multi_value_map(mondo_conn, "oio:hasDbXref")
        exact_synonyms = fetch_multi_value_map(mondo_conn, "oio:hasExactSynonym")
        icd11_index = build_icd11_label_index(icd11_conn)

        all_rows = build_rows(
            rare_ids=rare_ids,
            labels=labels,
            definitions=definitions,
            xrefs=xrefs,
            exact_synonyms=exact_synonyms,
            icd11_index=icd11_index,
        )

    missing_icd11f_rows = [r.copy() for r in all_rows if r["has_icd11f"] == "0"]
    missing_any_icd_rows = [r.copy() for r in all_rows if r["has_any_icd"] == "0"]
    missing_icd11f_with_other_icd_rows = [
        r.copy() for r in all_rows if r["has_icd11f"] == "0" and r["has_any_icd"] == "1"
    ]

    # Preserve manually curated review statuses if these files already exist.
    missing_icd11f_path = out_dir / "rare_without_icd11f.csv"
    missing_any_icd_path = out_dir / "rare_without_any_icd.csv"
    missing_icd11f_with_other_icd_path = (
        out_dir / "rare_without_icd11f_but_with_other_icd.csv"
    )

    apply_status(missing_icd11f_rows, load_existing_status(missing_icd11f_path))
    apply_status(missing_any_icd_rows, load_existing_status(missing_any_icd_path))
    apply_status(
        missing_icd11f_with_other_icd_rows,
        load_existing_status(missing_icd11f_with_other_icd_path),
    )

    write_csv(out_dir / "rare_terms_icd_status.csv", BASE_FIELDS, all_rows)
    write_csv(missing_icd11f_path, BASE_FIELDS + STATUS_COLUMNS, missing_icd11f_rows)
    write_csv(missing_any_icd_path, BASE_FIELDS + STATUS_COLUMNS, missing_any_icd_rows)
    write_csv(
        missing_icd11f_with_other_icd_path,
        BASE_FIELDS + STATUS_COLUMNS,
        missing_icd11f_with_other_icd_rows,
    )

    print(f"Wrote {out_dir / 'rare_terms_icd_status.csv'} ({len(all_rows)} rows)")
    print(f"Wrote {missing_icd11f_path} ({len(missing_icd11f_rows)} rows)")
    print(f"Wrote {missing_any_icd_path} ({len(missing_any_icd_rows)} rows)")
    print(
        "Wrote "
        f"{missing_icd11f_with_other_icd_path} "
        f"({len(missing_icd11f_with_other_icd_rows)} rows)"
    )


if __name__ == "__main__":
    main()
