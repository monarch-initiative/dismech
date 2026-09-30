"""Qualitative locations remain optional and distinct from regulatory targets."""

from importlib import import_module
from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

SCHEMA = Path(__file__).parents[1] / "src/dismech/schema/dismech.yaml"
EPHA4 = {"preferred_term": "EPHA4", "term": {"id": "hgnc:3388", "label": "EPHA4"}}
PAX3 = {"preferred_term": "PAX3", "term": {"id": "hgnc:8617", "label": "PAX3"}}
LMBR1 = {"preferred_term": "LMBR1", "term": {"id": "hgnc:13243", "label": "LMBR1"}}


@pytest.fixture(scope="module")
def validator():
    return Validator(
        SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


def _errors(validator, record, target_class="GenomicRegion"):
    return [
        result
        for result in validator.validate(record, target_class=target_class).results
        if result.severity.name == "ERROR"
    ]


@pytest.mark.parametrize("placement", ["GeneticContext", "Variant", "Genetic"])
def test_qualitative_region_and_legacy_text_coexist(validator, placement):
    region = {
        "name": "EPHA4-PAX3 regulatory boundary",
        "regulatory_element_type": "TAD_BOUNDARY",
        "between_genes": [EPHA4, PAX3],
    }
    record = {"affected_regions": [region]}
    if placement == "GeneticContext":
        record["allele_type"] = "Variable deletions extending through EPHA4"
    else:
        record["name"] = "Variable deletions extending through EPHA4"
    assert not _errors(validator, record, placement)
    # Adding regions never makes an old text-only record invalid.
    del record["affected_regions"]
    assert not _errors(validator, record, placement)


@pytest.mark.parametrize(
    "genes", [[EPHA4], [EPHA4, PAX3, {"preferred_term": "SHH"}], []]
)
def test_between_requires_two_anchors_when_supplied(validator, genes):
    assert _errors(validator, {"name": "Boundary", "between_genes": genes})


@pytest.mark.parametrize(
    "location",
    ["21", "X", "7q", "Xp", "17p13.3", "16p12.2-p11.2", "2q35-q36.3", "Xq28"],
)
def test_qualitative_cytogenetic_locations_validate(validator, location):
    assert not _errors(validator, {"name": "Interval", "chromosomal_region": location})


@pytest.mark.parametrize(
    "location", ["chr7q", "23q11", "17:100-200", "hg38", "16p12.2-11.2", "2-q35", "2-p"]
)
def test_non_cytogenetic_locations_rejected(validator, location):
    assert _errors(validator, {"name": "Interval", "chromosomal_region": location})


@pytest.mark.parametrize(
    "relation,value",
    [
        ("between_genes", ["EPHA4", "PAX3"]),
        ("within_gene", "LMBR1"),
        ("within_gene", [{"preferred_term": "LMBR1"}]),
        ("overlaps_genes", ["EPHA4"]),
        ("adjacent_to_genes", ["PAX3"]),
    ],
)
def test_gene_landmarks_require_typed_descriptors(validator, relation, value):
    assert _errors(validator, {"name": "Feature", relation: value})


def test_region_needs_a_name_but_not_an_identifier_or_coordinates(validator):
    assert not _errors(validator, {"name": "ZRS enhancer"})
    assert _errors(validator, {"description": "An unnamed enhancer"})


@pytest.mark.parametrize("model_module", ["dismech", "dismech_pydantic"])
@pytest.mark.parametrize("placement", ["GeneticContext", "Variant", "Genetic"])
def test_generated_models_load_regions_and_gene_landmarks(model_module, placement):
    model = import_module(f"dismech.datamodel.{model_module}")
    regions = [
        {
            "name": "Boundary",
            "regulatory_element_type": "TAD_BOUNDARY",
            "between_genes": [EPHA4, PAX3],
        },
        {
            "name": "ZRS",
            "within_gene": LMBR1,
            "overlaps_genes": [LMBR1],
        },
        {
            "name": "Example boundary-touching interval",
            "adjacent_to_genes": [PAX3],
        },
    ]
    record = {"affected_regions": regions}
    if placement != "GeneticContext":
        record["name"] = "Regional alteration"
    loaded = getattr(model, placement)(**record)
    assert all(
        isinstance(region, model.GenomicRegion) for region in loaded.affected_regions
    )
    assert loaded.affected_regions[0].between_genes[1].term.id == "hgnc:8617"
    assert loaded.affected_regions[1].within_gene.preferred_term == "LMBR1"
    assert loaded.affected_regions[1].overlaps_genes[0].preferred_term == "LMBR1"
    assert loaded.affected_regions[2].adjacent_to_genes[0].preferred_term == "PAX3"
