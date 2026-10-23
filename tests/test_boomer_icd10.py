"""ICD coverage must retain vocabulary identity and literal-valued mappings."""

import importlib.util
import sqlite3
from pathlib import Path

SCRIPT = (
    Path(__file__).resolve().parents[1] / "analyses/boomer/scripts/icd10_coverage.py"
)
spec = importlib.util.spec_from_file_location("boomer_icd10_coverage", SCRIPT)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def test_mapping_index_preserves_vocabularies_directions_and_literal_targets():
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE statements (subject TEXT, predicate TEXT, object TEXT, value TEXT)"
        )
        connection.executemany(
            "INSERT INTO statements VALUES (?, ?, ?, ?)",
            [
                ("ORDO:324", "skos:broadMatch", None, "ICD-10:E75.2"),
                ("MONDO:1", "skos:exactMatch", "ICD10CM:E75.2", None),
                ("MONDO:1", "oio:hasDbXref", None, "ICD10:E75.2"),
                ("MONDO:1", "rdfs:label", None, "ICD10CM:NotAMapping"),
                ("MONDO:1", "skos:exactMatch", "icd11f:123", None),
            ],
        )
        result = audit.mapping_index(connection)
    assert result["ORDO:324"] == {("skos:broadMatch", "ICD-10:E75.2")}
    assert result["MONDO:1"] == {
        ("skos:exactMatch", "ICD10CM:E75.2"),
        ("oio:hasDbXref", "ICD10:E75.2"),
    }
