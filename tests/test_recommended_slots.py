"""Tests for schema slots that drive recommended-field compliance scoring."""

from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.mark.parametrize(
    ("class_name", "slot_name"),
    [
        ("Disease", "disease_term"),
        ("Phenotype", "phenotype_term"),
        ("Treatment", "treatment_term"),
        ("Treatment", "therapeutic_modality"),
        ("Diagnosis", "diagnosis_term"),
        ("Inheritance", "inheritance_term"),
        ("CausalEdge", "causal_link_type"),
    ],
)
def test_core_semantic_slots_are_recommended(
    schema_view: SchemaView, class_name: str, slot_name: str
) -> None:
    """Core semantic slots should contribute to compliance when their object exists."""
    assert schema_view.get_slot(slot_name).recommended is True
    assert schema_view.induced_slot(slot_name, class_name).recommended is True


@pytest.mark.parametrize(
    "slot_name",
    [
        "reference_title",
        "evidence_source",
    ],
)
def test_evidence_item_quality_slots_are_recommended(
    schema_view: SchemaView, slot_name: str
) -> None:
    """Every evidence item should expose its core provenance and interpretation."""
    assert schema_view.induced_slot(slot_name, "EvidenceItem").recommended is True
