import csv
import sqlite3
from pathlib import Path

import yaml

from dismech.compare.mondo_export import export_mondo_priority_candidates


def _create_schema(db_path: Path) -> None:
    conn = sqlite3.connect(db_path)
    conn.executescript(
        """
        CREATE TABLE statements (
            subject TEXT,
            predicate TEXT,
            object TEXT,
            value TEXT
        );
        CREATE TABLE entailed_edge (
            subject TEXT,
            predicate TEXT,
            object TEXT
        );
        CREATE TABLE deprecated_node (
            id TEXT
        );
        """
    )
    conn.commit()
    conn.close()


def _insert_rows(db_path: Path, table: str, rows: list[tuple]) -> None:
    conn = sqlite3.connect(db_path)
    placeholders = ",".join("?" for _ in rows[0]) if rows else ""
    if rows:
        conn.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)
        conn.commit()
    conn.close()


def _write_yaml(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")


def _read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_export_mondo_priority_candidates_excludes_curated_and_builds_categories(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "mondo.db"
    output_path = tmp_path / "all_mondo_candidates.tsv"
    kb_dir = tmp_path / "kb" / "disorders"

    _create_schema(db_path)

    _insert_rows(
        db_path,
        "statements",
        [
            ("MONDO:0000001", "rdfs:label", None, "disease"),
            ("MONDO:1000000", "rdfs:label", None, "nervous system disease"),
            ("MONDO:1000000", "rdfs:subClassOf", "MONDO:0000001", None),
            ("MONDO:1000001", "rdfs:label", None, "cardiac disease"),
            ("MONDO:1000001", "rdfs:subClassOf", "MONDO:0000001", None),
            ("MONDO:2000000", "rdfs:label", None, "Example neuro disease"),
            (
                "MONDO:2000000",
                "IAO:0000115",
                None,
                "Example neurological disease definition.",
            ),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:1000000", None),
            ("MONDO:2000000", "oio:hasExactSynonym", None, "END"),
            ("MONDO:2000000", "oio:hasDbXref", None, "Orphanet:123"),
            ("MONDO:2000000", "oio:hasDbXref", None, "ORDO:456"),
            ("MONDO:2000000", "oio:inSubset", "obo:mondo#rare", None),
            ("MONDO:2000000", "oio:inSubset", "obo:mondo#clingen", None),
            ("MONDO:2100000", "rdfs:label", None, "Example neuro disease child"),
            ("MONDO:2100000", "rdfs:subClassOf", "MONDO:2000000", None),
            ("MONDO:2000001", "rdfs:label", None, "Existing disease"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:1000001", None),
            ("MONDO:2000002", "rdfs:label", None, "Deprecated disease"),
            ("MONDO:2000002", "rdfs:subClassOf", "MONDO:1000001", None),
        ],
    )
    _insert_rows(
        db_path,
        "entailed_edge",
        [
            ("MONDO:1000000", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:1000001", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:1000000"),
            ("MONDO:2100000", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2100000", "rdfs:subClassOf", "MONDO:1000000"),
            ("MONDO:2100000", "rdfs:subClassOf", "MONDO:2000000"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:1000001"),
            ("MONDO:2000002", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000002", "rdfs:subClassOf", "MONDO:1000001"),
        ],
    )
    _insert_rows(db_path, "deprecated_node", [("MONDO:2000002",)])

    _write_yaml(
        kb_dir / "Existing_Disease.yaml",
        {
            "name": "Existing disease",
            "disease_term": {
                "term": {"id": "MONDO:2000001", "label": "Existing disease"}
            },
        },
    )

    result = export_mondo_priority_candidates(
        mondo_db_path=db_path,
        output_path=output_path,
        kb_dir=kb_dir,
    )

    rows = _read_tsv(output_path)
    by_id = {row["mondo_id"]: row for row in rows}

    assert result["total_descendants"] == 5
    assert result["excluded_curated"] == 1
    assert result["exported_rows"] == 4

    assert "MONDO:2000001" not in by_id
    assert "MONDO:2000002" not in by_id

    neuro_row = by_id["MONDO:2000000"]
    assert neuro_row["definition"] == "Example neurological disease definition."
    assert neuro_row["synonyms"] == "END"
    assert neuro_row["parents"] == "nervous system disease"
    assert neuro_row["mondo_categories"] == "nervous system disease"
    assert neuro_row["child_count"] == "1"
    assert neuro_row["subset_match_count"] == "2"
    assert neuro_row["orphanet_match_count"] == "2"


def test_export_mondo_priority_candidates_limit_applies_after_curated_filter(
    tmp_path: Path,
) -> None:
    db_path = tmp_path / "mondo.db"
    output_path = tmp_path / "limited.tsv"

    _create_schema(db_path)
    _insert_rows(
        db_path,
        "statements",
        [
            ("MONDO:0000001", "rdfs:label", None, "disease"),
            ("MONDO:1000000", "rdfs:label", None, "system disease"),
            ("MONDO:1000000", "rdfs:subClassOf", "MONDO:0000001", None),
            ("MONDO:2000000", "rdfs:label", None, "Disease A"),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:1000000", None),
            ("MONDO:2000001", "rdfs:label", None, "Disease B"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:1000000", None),
        ],
    )
    _insert_rows(
        db_path,
        "entailed_edge",
        [
            ("MONDO:1000000", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000000", "rdfs:subClassOf", "MONDO:1000000"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:0000001"),
            ("MONDO:2000001", "rdfs:subClassOf", "MONDO:1000000"),
        ],
    )

    result = export_mondo_priority_candidates(
        mondo_db_path=db_path,
        output_path=output_path,
        limit=2,
    )

    rows = _read_tsv(output_path)
    assert result["exported_rows"] == 2
    assert len(rows) == 2
