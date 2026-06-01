"""Tests for medical action category schema metadata."""

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def test_medical_action_categories_have_broad_ncit_meanings(schema_view):
    """Medical action categories are mapped to broad NCIT concepts."""
    enum = schema_view.get_enum("MedicalActionCategoryEnum")
    assert enum is not None

    expected = {
        "THERAPEUTIC": ("NCIT:C49236", "Therapeutic Procedure"),
        "DIAGNOSTIC": ("NCIT:C18020", "Diagnostic Procedure"),
        "SCREENING": ("NCIT:C15419", "Disease Screening"),
        "MONITORING": ("NCIT:C61256", "Monitoring"),
        "COUNSELING_INFORMATIONAL": ("NCIT:C61547", "Counseling"),
    }

    for value, (meaning, title) in expected.items():
        permissible_value = enum.permissible_values[value]
        assert permissible_value.meaning == meaning
        assert permissible_value.title == title
