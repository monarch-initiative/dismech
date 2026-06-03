"""Tests for the structured genetics slots/enums added for issue #126.

These tests pin down the data-model improvements that constrain the
previously free-text `association` slot in the `Genetic` class to a
controlled vocabulary, add a `variant_origin` slot bound to GENO allele
origin terms, and add composable genetic-context slots for two-hit mechanisms.
"""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    # Use closed=True so unknown enum values are flagged as errors. This is
    # required to demonstrate that the new enum constraints actually bite.
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def test_gene_disease_relationship_enum_defined(schema_view):
    """The new GeneDiseaseRelationshipEnum exists with the expected values."""
    enum = schema_view.get_enum("GeneDiseaseRelationshipEnum")
    assert enum is not None
    expected = {
        "CAUSATIVE",
        "RISK_FACTOR",
        "PROTECTIVE",
        "MODIFIER",
        "SUSCEPTIBILITY",
        "SOMATIC_DRIVER",
        "COOPERATING",
        "BIOMARKER",
        "DISPUTED",
        "UNKNOWN",
    }
    actual = set(enum.permissible_values.keys())
    missing = expected - actual
    assert not missing, f"Missing enum values: {missing}"


def test_variant_origin_enum_bound_to_geno(schema_view):
    """VariantOriginEnum exists and binds GERMLINE/SOMATIC to GENO terms."""
    enum = schema_view.get_enum("VariantOriginEnum")
    assert enum is not None
    pvs = enum.permissible_values
    assert "GERMLINE" in pvs and "SOMATIC" in pvs
    # GENO bindings verified via OAK against sqlite:obo:geno
    assert pvs["GERMLINE"].meaning == "GENO:0000888"
    assert pvs["SOMATIC"].meaning == "GENO:0000882"
    assert pvs["DE_NOVO"].meaning == "GENO:0000880"
    assert pvs["UNKNOWN"].meaning == "GENO:0000881"


def test_genetic_class_has_new_slots(schema_view):
    """The Genetic class includes the new structured slots."""
    cls = schema_view.get_class("Genetic")
    assert cls is not None
    induced = schema_view.class_induced_slots("Genetic")
    slot_names = {s.name for s in induced}
    assert "relationship_type" in slot_names
    assert "variant_origin" in slot_names
    # Free-text association slot is preserved for backward compatibility
    assert "association" in slot_names


def test_genetic_context_class_has_composable_two_hit_slots(schema_view):
    """GeneticContext exposes reusable origin, hit-role, event, and impact slots."""
    cls = schema_view.get_class("GeneticContext")
    assert cls is not None
    induced = schema_view.class_induced_slots("GeneticContext")
    slot_names = {s.name for s in induced}
    assert "variant_origin" in slot_names
    assert "allelic_hit_role" in slot_names
    assert "allelic_events" in slot_names
    assert "functional_impact_category" in slot_names
    assert "allele_type" in slot_names
    assert "functional_impact" in slot_names

    assert schema_view.induced_slot("variant_origin", "GeneticContext").range == (
        "VariantOriginEnum"
    )
    assert schema_view.induced_slot("allelic_hit_role", "GeneticContext").range == (
        "AllelicHitRoleEnum"
    )
    assert schema_view.induced_slot("allelic_events", "GeneticContext").range == (
        "AllelicEventEnum"
    )
    assert (
        schema_view.induced_slot("functional_impact_category", "GeneticContext").range
        == "FunctionalImpactEnum"
    )


def test_genetic_record_validates_with_structured_fields(validator):
    """A minimal Disease using the new structured fields validates."""
    disease = {
        "name": "Test Disease For Issue 126",
        "genetic": [
            {
                "name": "BRCA1",
                "association": "Germline pathogenic loss-of-function variants",
                "relationship_type": "CAUSATIVE",
                "variant_origin": "GERMLINE",
            },
            {
                "name": "TP53",
                "relationship_type": "SOMATIC_DRIVER",
                "variant_origin": "SOMATIC",
            },
            {
                "name": "HLA-B51",
                "relationship_type": "RISK_FACTOR",
            },
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_pathophysiology_genetic_context_validates_with_composable_two_hit_fields(
    validator,
):
    """A two-hit Pathophysiology context composes independent enum dimensions."""
    disease = {
        "name": "Test Two Hit Disease",
        "pathophysiology": [
            {
                "name": "Somatic second-hit gene inactivation",
                "genetic_context": {
                    "gene": {
                        "preferred_term": "AIP",
                        "term": {"id": "hgnc:358", "label": "AIP"},
                    },
                    "variant_origin": "SOMATIC",
                    "allelic_hit_role": "SECOND_HIT",
                    "allelic_events": ["DELETION", "LOSS_OF_HETEROZYGOSITY"],
                    "functional_impact_category": "LOSS_OF_FUNCTION",
                },
            }
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, f"Unexpected validation errors: {[str(e) for e in errors]}"


def test_invalid_relationship_type_rejected(validator):
    """An out-of-vocabulary relationship_type fails validation."""
    disease = {
        "name": "Test Disease Invalid",
        "genetic": [
            {
                "name": "FOO",
                "relationship_type": "TOTALLY_MADE_UP_VALUE",
            }
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for invalid relationship_type"


def test_invalid_allelic_event_rejected(validator):
    """Ad hoc cross-product second-hit event labels fail validation."""
    disease = {
        "name": "Test Disease Invalid Genetic Context",
        "pathophysiology": [
            {
                "name": "Somatic second-hit gene inactivation",
                "genetic_context": {
                    "variant_origin": "SOMATIC",
                    "allelic_hit_role": "SECOND_HIT",
                    "allelic_events": ["SECOND_HIT_DELETION_LOH"],
                    "functional_impact_category": "LOSS_OF_FUNCTION",
                },
            }
        ],
    }
    report = validator.validate(disease, target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert errors, "Expected validation error for ad hoc allelic event"
