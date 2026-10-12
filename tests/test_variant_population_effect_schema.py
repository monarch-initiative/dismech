"""Tests for Variant.population_effects (population-specific variant effects, #13677).

A variant's classification, penetrance, severity, phenotype spectrum, or frequency
can differ between human populations. ``population_effects`` records each such
finding as a ``VariantPopulationEffect``: the population in the source's words,
an optional HANCESTRO binding, how the source defined the group, and which aspect
of the effect differs (design decisions section 16).
"""

from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

ROOT_DIR = Path(__file__).parent.parent
SCHEMA_PATH = ROOT_DIR / "src" / "dismech" / "schema" / "dismech.yaml"
OAK_CONFIG_PATH = ROOT_DIR / "conf" / "oak_config.yaml"


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        SCHEMA_PATH,
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


VALID_EFFECT = {
    "population": "Japanese FMF patients",
    "ancestry_terms": [
        {
            "preferred_term": "Japanese",
            "term": {"id": "HANCESTRO:0019", "label": "Japanese"},
        }
    ],
    "ancestry_basis": "NOT_STATED",
    "comparator_stratum": "Mediterranean patients with FMF",
    "effect_differences": ["ALLELE_FREQUENCY"],
    "cohort_size": 80,
}


def _disease_with_effect(effect: dict) -> dict:
    return {
        "name": "Example",
        "genetic": [
            {
                "name": "MEFV",
                "variants": [{"name": "M694V", "population_effects": [effect]}],
            }
        ],
    }


def _errors(validator, data):
    report = validator.validate(data, target_class="Disease")
    return [r for r in report.results if r.severity.name == "ERROR"]


def test_variant_carries_population_effects(schema_view):
    slots = {s.name for s in schema_view.class_induced_slots("Variant")}
    assert "population_effects" in slots
    assert schema_view.get_slot("population_effects").range == "VariantPopulationEffect"


def test_valid_population_effect_validates(validator):
    errors = _errors(validator, _disease_with_effect(VALID_EFFECT))
    assert not errors, [str(e) for e in errors]


def test_population_wording_is_required(validator):
    effect = {k: v for k, v in VALID_EFFECT.items() if k != "population"}
    assert _errors(validator, _disease_with_effect(effect))


def test_population_wording_alone_is_enough(validator):
    """The HANCESTRO binding is optional; free text records what the study said."""
    errors = _errors(validator, _disease_with_effect({"population": "Sephardic Jewish patients"}))
    assert not errors, [str(e) for e in errors]


@pytest.mark.parametrize(
    "slot,bad_value",
    [("ancestry_basis", "ETHNIC"), ("effect_differences", ["MILDER"])],
)
def test_categorical_slots_are_enum_bound(validator, slot, bad_value):
    assert _errors(validator, _disease_with_effect({**VALID_EFFECT, slot: bad_value}))


@pytest.mark.parametrize("bad_frequency", [-0.1, 1.5])
def test_allele_frequency_is_a_proportion(validator, bad_frequency):
    assert _errors(validator, _disease_with_effect({**VALID_EFFECT, "allele_frequency": bad_frequency}))


def test_tested_null_is_recordable(schema_view):
    values = schema_view.get_enum("PopulationEffectDifferenceEnum").permissible_values
    assert "NO_DIFFERENCE" in values


def test_ancestry_basis_separates_self_report_from_genetic_inference(schema_view):
    values = set(schema_view.get_enum("AncestryBasisEnum").permissible_values)
    assert {"SELF_REPORTED", "GENETICALLY_INFERRED", "GEOGRAPHIC", "NOT_STATED"} <= values


def test_ancestry_descriptor_binds_to_hancestro_root(schema_view):
    enum = schema_view.get_enum("AncestryTerm")
    assert enum.reachable_from.source_nodes == ["HANCESTRO:0004"]
    binding = schema_view.induced_slot("term", "AncestryDescriptor").bindings[0]
    assert binding.range == "AncestryTerm"


def test_hancestro_prefix_is_declared_and_validated(schema_view):
    """An unlisted prefix is silently skipped by term validation (design decisions section 4)."""
    assert "HANCESTRO" in schema_view.schema.prefixes
    adapters = yaml.safe_load(OAK_CONFIG_PATH.read_text())["ontology_adapters"]
    assert adapters.get("HANCESTRO"), "HANCESTRO must map to an OAK adapter"
