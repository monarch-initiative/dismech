"""Export MONDO disease terms as prioritizer candidate rows."""

from __future__ import annotations

import argparse
import csv
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Any

from .mondo_priority import build_coverage_index

DEFAULT_MONDO_DB_PATH = Path.home() / ".data" / "oaklib" / "mondo.db"
DEFAULT_DISEASE_ROOT_ID = "MONDO:0000001"
DEFAULT_PRIORITY_SUBSETS = {
    "obo:mondo#rare",
    "obo:mondo#gard_rare",
    "obo:mondo#nord_rare",
    "obo:mondo#orphanet_rare",
    "obo:mondo#inferred_rare",
    "obo:mondo#clingen",
}
ORPHANET_PREFIXES = ("orphanet:", "ordo:")


def _normalize_text(text: str | None) -> str:
    if not text:
        return ""
    normalized = text.casefold().replace("_", " ")
    return " ".join("".join(ch if ch.isalnum() else " " for ch in normalized).split())


def _join_values(values: list[str]) -> str:
    return "|".join(sorted(dict.fromkeys(value for value in values if value)))


def _query_single_value_map(
    conn: sqlite3.Connection,
    predicate: str,
) -> dict[str, str]:
    values: dict[str, str] = {}
    query = """
    SELECT subject, value
    FROM statements
    WHERE predicate = ?
      AND subject LIKE 'MONDO:%'
      AND value IS NOT NULL
    ORDER BY subject, value
    """
    for subject, value in conn.execute(query, (predicate,)):
        values.setdefault(subject, value)
    return values


def _query_multi_value_map(
    conn: sqlite3.Connection,
    predicate: str,
) -> dict[str, list[str]]:
    values: dict[str, list[str]] = defaultdict(list)
    query = """
    SELECT subject, value
    FROM statements
    WHERE predicate = ?
      AND subject LIKE 'MONDO:%'
      AND value IS NOT NULL
    ORDER BY subject, value
    """
    for subject, value in conn.execute(query, (predicate,)):
        values[subject].append(value)
    return values


def _query_multi_object_map(
    conn: sqlite3.Connection,
    predicate: str,
) -> dict[str, list[str]]:
    values: dict[str, list[str]] = defaultdict(list)
    query = """
    SELECT subject, object
    FROM statements
    WHERE predicate = ?
      AND subject LIKE 'MONDO:%'
      AND object IS NOT NULL
    ORDER BY subject, object
    """
    for subject, object_id in conn.execute(query, (predicate,)):
        values[subject].append(object_id)
    return values


def _query_direct_parent_map(conn: sqlite3.Connection) -> dict[str, list[str]]:
    values: dict[str, list[str]] = defaultdict(list)
    query = """
    SELECT subject, object
    FROM statements
    WHERE predicate = 'rdfs:subClassOf'
      AND subject LIKE 'MONDO:%'
      AND object LIKE 'MONDO:%'
    ORDER BY subject, object
    """
    for subject, parent_id in conn.execute(query):
        values[subject].append(parent_id)
    return values


def _query_direct_child_counts(conn: sqlite3.Connection) -> dict[str, int]:
    counts: dict[str, int] = {}
    query = """
    SELECT object, COUNT(DISTINCT subject)
    FROM statements
    WHERE predicate = 'rdfs:subClassOf'
      AND subject LIKE 'MONDO:%'
      AND object LIKE 'MONDO:%'
    GROUP BY object
    """
    for object_id, count in conn.execute(query):
        counts[object_id] = int(count)
    return counts


def _query_descendant_ids(
    conn: sqlite3.Connection,
    disease_root_id: str,
) -> list[str]:
    query = """
    SELECT DISTINCT e.subject
    FROM entailed_edge e
    LEFT JOIN deprecated_node d ON e.subject = d.id
    WHERE e.predicate = 'rdfs:subClassOf'
      AND e.object = ?
      AND e.subject LIKE 'MONDO:%'
      AND e.subject != ?
      AND d.id IS NULL
    ORDER BY e.subject
    """
    return [row[0] for row in conn.execute(query, (disease_root_id, disease_root_id))]


def _query_top_level_category_ids(
    conn: sqlite3.Connection,
    disease_root_id: str,
) -> set[str]:
    query = """
    SELECT DISTINCT s.subject
    FROM statements s
    LEFT JOIN deprecated_node d ON s.subject = d.id
    WHERE s.predicate = 'rdfs:subClassOf'
      AND s.object = ?
      AND s.subject LIKE 'MONDO:%'
      AND d.id IS NULL
    """
    return {row[0] for row in conn.execute(query, (disease_root_id,))}


def _query_top_level_category_map(
    conn: sqlite3.Connection,
    top_level_category_ids: set[str],
) -> dict[str, list[str]]:
    if not top_level_category_ids:
        return {}

    placeholders = ",".join("?" for _ in top_level_category_ids)
    query = f"""
    SELECT subject, object
    FROM entailed_edge
    WHERE predicate = 'rdfs:subClassOf'
      AND subject LIKE 'MONDO:%'
      AND object IN ({placeholders})
      AND subject != object
    ORDER BY subject, object
    """
    values: dict[str, list[str]] = defaultdict(list)
    for subject, object_id in conn.execute(
        query, tuple(sorted(top_level_category_ids))
    ):
        values[subject].append(object_id)
    return values


def export_mondo_priority_candidates(
    mondo_db_path: Path,
    output_path: Path,
    disease_root_id: str = DEFAULT_DISEASE_ROOT_ID,
    kb_dir: Path | None = None,
    priority_subset_ids: set[str] | None = None,
    limit: int | None = None,
) -> dict[str, Any]:
    """Export MONDO descendants of the disease root into prioritizer rows."""
    priority_subset_ids = priority_subset_ids or DEFAULT_PRIORITY_SUBSETS

    with sqlite3.connect(mondo_db_path) as conn:
        descendant_ids = _query_descendant_ids(conn, disease_root_id)
        labels = _query_single_value_map(conn, "rdfs:label")
        definitions = _query_single_value_map(conn, "IAO:0000115")
        synonyms = _query_multi_value_map(conn, "oio:hasExactSynonym")
        xrefs = _query_multi_value_map(conn, "oio:hasDbXref")
        subsets = _query_multi_object_map(conn, "oio:inSubset")
        direct_parent_ids = _query_direct_parent_map(conn)
        direct_child_counts = _query_direct_child_counts(conn)
        top_level_category_ids = _query_top_level_category_ids(conn, disease_root_id)
        top_level_category_map = _query_top_level_category_map(
            conn, top_level_category_ids
        )

    coverage = build_coverage_index(kb_dir) if kb_dir is not None else None

    rows: list[dict[str, Any]] = []
    total_descendants = 0
    excluded_curated = 0

    for mondo_id in descendant_ids:
        label = labels.get(mondo_id, "").strip()
        if not label:
            continue

        total_descendants += 1
        normalized_label = _normalize_text(label)
        if coverage and (
            mondo_id in coverage.curated_ids
            or normalized_label in coverage.curated_labels
        ):
            excluded_curated += 1
            continue

        parent_labels = [
            labels[parent_id]
            for parent_id in direct_parent_ids.get(mondo_id, [])
            if parent_id in labels
        ]
        category_labels = [
            labels[category_id]
            for category_id in top_level_category_map.get(mondo_id, [])
            if category_id in labels
        ]
        if not category_labels:
            category_labels = parent_labels

        term_xrefs = xrefs.get(mondo_id, [])
        subset_memberships = subsets.get(mondo_id, [])
        orphanet_match_count = sum(
            1 for value in term_xrefs if value.casefold().startswith(ORPHANET_PREFIXES)
        )
        subset_match_count = sum(
            1 for value in subset_memberships if value in priority_subset_ids
        )

        rows.append(
            {
                "mondo_id": mondo_id,
                "label": label,
                "definition": " ".join(definitions.get(mondo_id, "").split()),
                "synonyms": _join_values(synonyms.get(mondo_id, [])),
                "parents": _join_values(parent_labels),
                "mondo_categories": _join_values(category_labels),
                "xrefs": _join_values(term_xrefs),
                "child_count": direct_child_counts.get(mondo_id, 0),
                "clingen_definitive_count": 0,
                "clingen_strong_count": 0,
                "subset_match_count": subset_match_count,
                "orphanet_match_count": orphanet_match_count,
                "is_obsolete": "false",
            }
        )

        if limit is not None and len(rows) >= limit:
            break

    fieldnames = [
        "mondo_id",
        "label",
        "definition",
        "synonyms",
        "parents",
        "mondo_categories",
        "xrefs",
        "child_count",
        "clingen_definitive_count",
        "clingen_strong_count",
        "subset_match_count",
        "orphanet_match_count",
        "is_obsolete",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    return {
        "output_path": output_path,
        "disease_root_id": disease_root_id,
        "total_descendants": total_descendants,
        "excluded_curated": excluded_curated,
        "exported_rows": len(rows),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export MONDO disease terms as prioritizer candidate rows."
    )
    parser.add_argument(
        "--mondo-db",
        default=str(DEFAULT_MONDO_DB_PATH),
        type=Path,
        help="Path to local MONDO sqlite database.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Output TSV path.",
    )
    parser.add_argument(
        "--disease-root-id",
        default=DEFAULT_DISEASE_ROOT_ID,
        help="Disease root MONDO identifier to expand from.",
    )
    parser.add_argument(
        "--kb-dir",
        type=Path,
        default=None,
        help="Optional kb/disorders path; when supplied, already curated roots are excluded.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional row limit for smoke testing.",
    )
    args = parser.parse_args()

    result = export_mondo_priority_candidates(
        mondo_db_path=args.mondo_db,
        output_path=args.output,
        disease_root_id=args.disease_root_id,
        kb_dir=args.kb_dir,
        limit=args.limit,
    )
    print(
        "Exported "
        f"{result['exported_rows']} MONDO prioritizer candidates to {result['output_path']}"
    )
    if args.kb_dir is not None:
        print(
            f"Excluded {result['excluded_curated']} already curated roots from "
            f"{result['total_descendants']} disease descendants."
        )
    else:
        print(
            f"Scanned {result['total_descendants']} disease descendants under "
            f"{result['disease_root_id']}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
