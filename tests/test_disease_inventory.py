"""Tests for the disease + subtype inventory exporter."""

import csv
import io
from pathlib import Path

from dismech.export.disease_inventory import (
    INVENTORY_COLUMNS,
    build_inventory,
    extract_rows,
    write_csv,
)


def test_extract_rows_disease_and_subtypes():
    disorder = {
        "name": "Example Disease",
        "disease_term": {"term": {"id": "MONDO:0001", "label": "example disease"}},
        "has_subtypes": [
            # Subtype with a MONDO primary term.
            {
                "name": "Type 1",
                "subtype_term": {"term": {"id": "MONDO:0002", "label": "type 1"}},
            },
            # Subtype with no primary term but a MONDO cross-reference mapping.
            {
                "name": "Type 2",
                "mappings": {
                    "mondo_mappings": [
                        {
                            "term": {"id": "MONDO:0003", "label": "type 2"},
                            "mapping_predicate": "skos:exactMatch",
                        }
                    ]
                },
            },
            # Subtype with no MONDO mapping at all.
            {"name": "Type 3"},
            # Unnamed subtype is skipped.
            {"description": "no name"},
        ],
    }

    rows = extract_rows(disorder, "Example_Disease.yaml")

    assert len(rows) == 4  # 1 disease + 3 named subtypes
    assert set(rows[0]) == set(INVENTORY_COLUMNS)

    disease_row = rows[0]
    assert disease_row["entry_type"] == "disease"
    assert disease_row["parent_disease"] == ""
    assert disease_row["mondo_id"] == "MONDO:0001"
    assert disease_row["mondo_source"] == "primary_term"
    assert disease_row["has_mondo"] == "true"

    type1, type2, type3 = rows[1], rows[2], rows[3]
    assert type1["entry_type"] == "subtype"
    assert type1["parent_disease"] == "Example Disease"
    assert type1["mondo_id"] == "MONDO:0002"
    assert type1["mondo_source"] == "primary_term"

    assert type2["mondo_id"] == "MONDO:0003"
    assert type2["mondo_source"] == "mondo_mappings"
    assert type2["has_mondo"] == "true"

    assert type3["mondo_id"] == ""
    assert type3["mondo_source"] == ""
    assert type3["has_mondo"] == "false"


def test_non_mondo_primary_term_falls_back_to_blank():
    disorder = {
        "name": "Oncology Subtype Parent",
        "disease_term": {"term": {"id": "NCIT:C1234", "label": "some neoplasm"}},
    }
    rows = extract_rows(disorder, "Onc.yaml")
    assert rows[0]["primary_term_id"] == "NCIT:C1234"
    assert rows[0]["mondo_id"] == ""
    assert rows[0]["has_mondo"] == "false"


def test_write_csv_roundtrip(tmp_path: Path):
    disorder = {
        "name": "D",
        "disease_term": {"term": {"id": "MONDO:0001", "label": "d"}},
        "has_subtypes": [{"name": "S"}],
    }
    yaml_path = tmp_path / "D.yaml"
    import yaml

    yaml_path.write_text(yaml.safe_dump(disorder))

    rows = build_inventory([yaml_path])
    buffer = io.StringIO()
    write_csv(rows, buffer)

    parsed = list(csv.DictReader(io.StringIO(buffer.getvalue())))
    assert [r["entry_type"] for r in parsed] == ["disease", "subtype"]
    assert parsed[0]["source_file"] == "D.yaml"
