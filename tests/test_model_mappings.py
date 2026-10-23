"""Tests for `AnimalModel.model_mappings` and its cache-backed gate (#15395).

The **schema** tests fix the slot's shape: a multivalued TermMapping whose term
is constrained to an MGI genotype, ZFIN fish or RGD strain ID, with a required
justification.

The **check** tests fix what `scripts/check_model_mappings.py` treats as a
defect. The one that motivates the script is NOT_A_GENOTYPE: MGI and RGD share
one ID space for genes and genotypes, so the schema pattern accepts the Arx
gene `MGI:1097716` in a mapping, and only the cached record type catches it.
"""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

from scripts.check_model_mappings import (
    check_document,
    load_cache,
    normalize_label,
    scan_repo,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"

CACHE = {
    "MGI:3844352": {
        "curie": "MGI:3844352",
        "label": "Arx<tm1Gldn>/Y Tg(mI56i-cre,-EGFP)1Kc/0",
        "category": "biolink:Genotype",
        "taxon": "NCBITaxon:10090",
    },
    "MGI:1097716": {
        "curie": "MGI:1097716",
        "label": "Arx",
        "category": "biolink:Gene",
        "taxon": "NCBITaxon:10090",
    },
    "MGI:9999999": {"curie": "MGI:9999999", "label": "", "category": "", "taxon": ""},
}


def _mapping(curie="MGI:3844352", label=None, predicate="skos:narrowMatch"):
    if label is None:
        label = CACHE.get(curie, {}).get("label", "x")
    return {
        "term": {"id": curie, "label": label},
        "mapping_predicate": predicate,
        "mapping_justification": "Same line and paper.",
    }


def _kinds(*models) -> set[str]:
    doc = {"animal_models": [{"model_mappings": list(m)} for m in models]}
    return {f.kind for f in check_document(Path("x.yaml"), doc, CACHE)}


# --------------------------------------------------------------------- schema


@pytest.fixture(scope="module")
def view() -> SchemaView:
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def test_animal_model_carries_model_mappings(view: SchemaView) -> None:
    slot = view.induced_slot("model_mappings", "AnimalModel")
    assert slot.multivalued
    assert slot.range == "AnimalModelMapping"
    assert "TermMapping" in view.class_ancestors("AnimalModelMapping")
    assert view.induced_slot("mapping_justification", "AnimalModelMapping").required


def _disease(curie: str) -> dict:
    return {
        "name": "Test Disease",
        "animal_models": [
            {"species": "Mus musculus", "model_mappings": [_mapping(curie, label="x")]}
        ],
    }


@pytest.mark.parametrize(
    "curie", ["MGI:3844352", "ZFIN:ZDB-FISH-190605-7", "RGD:2293012"]
)
def test_mod_record_ids_validate(validator: Validator, curie: str) -> None:
    report = validator.validate(_disease(curie), target_class="Disease")
    errors = [r for r in report.results if r.severity.name == "ERROR"]
    assert not errors, [str(e) for e in errors]


@pytest.mark.parametrize(
    "curie", ["hgnc:18060", "ZFIN:ZDB-GENE-980526-166", "MGI:", "NCBIGene:170302"]
)
def test_other_ids_are_rejected(validator: Validator, curie: str) -> None:
    report = validator.validate(_disease(curie), target_class="Disease")
    assert any(r.severity.name == "ERROR" for r in report.results)


# ----------------------------------------------------------------- labels


@pytest.mark.parametrize(
    "source, expected",
    [
        (
            "Npr2<sup>pwe</sup>/Npr2<sup>pwe</sup>  [background:] involves: C3H/HeJ * C57BL/6",
            "Npr2<pwe>/Npr2<pwe>",
        ),
        (
            "Adnp<sup>em1Goz</sup>/Adnp<sup>+</sup>  [background:] C57BL/6N-Adnp<sup>em1Goz</sup>",
            "Adnp<em1Goz>/Adnp<+>",
        ),
        (
            "ACI.BBDP-(<i>RT1<sup>u</sup></i>)(<i>Gimap5</i>)/Sunn",
            "ACI.BBDP-(RT1<u>)(Gimap5)/Sunn",
        ),
        ("AB + CRISPR1-g6pd", "AB + CRISPR1-g6pd"),
    ],
)
def test_normalize_label(source: str, expected: str) -> None:
    assert normalize_label(source) == expected


# ------------------------------------------------------------------ check


def test_clean_mapping_passes() -> None:
    assert _kinds([_mapping()]) == set()


def test_gene_id_is_not_a_genotype() -> None:
    assert "NOT_A_GENOTYPE" in _kinds([_mapping("MGI:1097716")])


def test_label_mismatch() -> None:
    assert "LABEL_MISMATCH" in _kinds([_mapping(label="Arx<tm1Gldn>/Y")])


def test_uncached_and_unknown() -> None:
    assert _kinds([_mapping("MGI:1234567", label="x")]) == {"UNCACHED"}
    assert _kinds([_mapping("MGI:9999999", label="x")]) == {"UNKNOWN_RECORD"}


def test_close_match_is_not_a_model_predicate() -> None:
    assert "BAD_PREDICATE" in _kinds([_mapping(predicate="skos:closeMatch")])


def test_duplicate_within_one_model() -> None:
    assert "DUPLICATE" in _kinds([_mapping(), _mapping()])


def test_two_models_cannot_both_be_the_same_genotype() -> None:
    exact = _mapping(predicate="skos:exactMatch")
    assert "SHARED_EXACT" in _kinds([exact], [exact])
    # Two lines may each contain the same genotype, though.
    assert _kinds([_mapping()], [_mapping()]) == set()


def test_committed_kb_passes() -> None:
    findings = scan_repo(cache=load_cache())
    assert not findings, [f"{f.path.name}: {f.kind}: {f.detail}" for f in findings]
