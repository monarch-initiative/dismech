"""Tests for Subtype.derivation and subtype-scoped treatment effect modifiers.

A data-driven cluster (Ahlqvist's type 2 diabetes subgroups) can be a
``has_subtypes`` row only if the row says it is a statistical region rather
than a natural kind. ``SubtypeDerivation`` carries that: the boundary type, the
method, the features, the derivation cohort, and entity references to the data
(``cluster_data``). ``TreatmentEffectModifier.stratum_subtype`` /
``comparator_subtype`` then let a treatment's subgroup effect name the subtype
as a foreign key.
"""

from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from dismech.entity_refs import entity_ref_errors
from tests.test_data import check_subtype_derivations, check_subtype_foreign_keys

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _errors(validator, data):
    report = validator.validate(data, target_class="Disease")
    return [r for r in report.results if r.severity.name == "ERROR"]


EVIDENCE = [
    {
        "reference": "PMID:29503172",
        "supports": "SUPPORT",
        "evidence_source": "HUMAN_CLINICAL",
        "snippet": "We identified five replicable clusters of patients with diabetes",
        "explanation": "Derivation study.",
    }
]

CLUSTER_DERIVATION = {
    "boundary_type": "STATISTICAL_PARTITION",
    "partition_method": "k-means and hierarchical clustering",
    "partition_features": ["age at diagnosis", "BMI", "HbA1c", "HOMA2-B", "HOMA2-IR"],
    "derivation_population": "ANDIS, 8,980 newly diagnosed adults",
    "cluster_data": ["datasets#EGA:EGAS00000000001"],
    "evidence": EVIDENCE,
}


def _disease(derivation=None, modifier=None, datasets=True):
    subtype = {"name": "SIRD", "description": "Severe insulin-resistant diabetes."}
    if derivation is not None:
        subtype["derivation"] = derivation
    disease = {
        "name": "Example",
        "has_subtypes": [subtype, {"name": "MARD"}],
    }
    if datasets:
        disease["datasets"] = [
            {"accession": "EGA:EGAS00000000001", "title": "Example cohort"}
        ]
    if modifier is not None:
        disease["treatments"] = [{"name": "Thiazolidinedione", "effect_modifiers": [modifier]}]
    return disease


SUBTYPE_MODIFIER = {
    "effect_modifier_type": "DISEASE_SUBTYPE",
    "stratum": "cluster 3 (SIRD)",
    "stratum_subtype": "SIRD",
    "comparator_stratum": "cluster 5 (MARD)",
    "comparator_subtype": "MARD",
    "modified_outcome": "3-year HbA1c AUC",
    "effect_in_stratum": "LARGER_EFFECT",
    "modification_analysis": "POST_HOC_SUBGROUP",
}


def _write(tmp_path, data):
    path = tmp_path / "Example.yaml"
    path.write_text(yaml.safe_dump(data, sort_keys=False))
    return str(path)


def test_schema_declares_the_classes_and_slots(schema_view):
    assert "derivation" in {s.name for s in schema_view.class_induced_slots("Subtype")}
    der = schema_view.induced_slot("boundary_type", "SubtypeDerivation")
    assert der.required
    assert set(schema_view.get_enum("SubtypeBoundaryEnum").permissible_values) == {
        "CATEGORICAL",
        "CRITERIA_BASED",
        "THRESHOLD",
        "STATISTICAL_PARTITION",
    }
    tem = {s.name for s in schema_view.class_induced_slots("TreatmentEffectModifier")}
    assert {"stratum_subtype", "comparator_subtype"} <= tem
    assert "DISEASE_SUBTYPE" in schema_view.get_enum("EffectModifierTypeEnum").permissible_values


def test_full_cluster_subtype_validates(validator, tmp_path):
    data = _disease(CLUSTER_DERIVATION, SUBTYPE_MODIFIER)
    assert not _errors(validator, data)
    path = _write(tmp_path, data)
    check_subtype_foreign_keys(path)
    check_subtype_derivations(path)
    assert entity_ref_errors(data) == []


def test_boundary_type_is_required(validator):
    derivation = {k: v for k, v in CLUSTER_DERIVATION.items() if k != "boundary_type"}
    assert _errors(validator, _disease(derivation))


@pytest.mark.parametrize("missing", ["partition_method", "partition_features", "evidence"])
def test_statistical_partition_needs_method_features_and_evidence(tmp_path, missing):
    derivation = {k: v for k, v in CLUSTER_DERIVATION.items() if k != missing}
    with pytest.raises(AssertionError, match=missing):
        check_subtype_derivations(_write(tmp_path, _disease(derivation)))


def test_categorical_cannot_carry_partition_features(tmp_path):
    derivation = {"boundary_type": "CATEGORICAL", "partition_features": ["BMI"]}
    with pytest.raises(AssertionError, match="CATEGORICAL contradicts"):
        check_subtype_derivations(_write(tmp_path, _disease(derivation)))


def test_disease_subtype_modifier_needs_stratum_subtype(tmp_path):
    modifier = {k: v for k, v in SUBTYPE_MODIFIER.items() if k != "stratum_subtype"}
    with pytest.raises(AssertionError, match="needs stratum_subtype"):
        check_subtype_derivations(_write(tmp_path, _disease(modifier=modifier)))


@pytest.mark.parametrize("slot", ["stratum_subtype", "comparator_subtype"])
def test_effect_modifier_subtype_is_a_foreign_key(tmp_path, slot):
    modifier = {**SUBTYPE_MODIFIER, slot: "MOD"}
    with pytest.raises(AssertionError, match=slot):
        check_subtype_foreign_keys(_write(tmp_path, _disease(modifier=modifier)))


def test_effect_modifier_subtype_with_no_subtypes_declared(tmp_path):
    data = _disease(modifier=SUBTYPE_MODIFIER)
    data.pop("has_subtypes")
    with pytest.raises(AssertionError, match="stratum_subtype"):
        check_subtype_foreign_keys(_write(tmp_path, data))


@pytest.mark.parametrize(
    "ref, message",
    [
        ("datasets#EGA:EGAS99999999999", "does not resolve"),
        ("EGA:EGAS00000000001", "bare name"),
        ("phenotypes#Hyperglycemia", "may only point at"),
        ("dataset_typo#EGA:EGAS00000000001", "unknown section"),
    ],
)
def test_cluster_data_is_a_gated_entity_reference(ref, message):
    derivation = {**CLUSTER_DERIVATION, "cluster_data": [ref]}
    data = _disease(derivation)
    data["phenotypes"] = [{"name": "Hyperglycemia"}]
    errors = entity_ref_errors(data)
    assert any(message in e for e in errors), errors
