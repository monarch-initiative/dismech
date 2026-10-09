"""Tests for non-human gene identifiers on model systems.

The schema tests fix where the namespaces are admitted: `AnimalModel.genes`
and `ExperimentalModel.genes` take a `GeneOrProductDescriptor`, and every other
gene slot keeps `GeneDescriptor`.

The check tests fix what `scripts/check_gene_namespaces.py` treats as a
defect. See that script's docstring for why each gating class is one.
"""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime import SchemaView

from dismech.term_cache_integrity import check_cache_file
from scripts import check_gene_namespaces as cgn
from scripts.check_gene_namespaces import check_document, scan_repo

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "src" / "dismech" / "schema" / "dismech.yaml"

MOUSE_COCH = {"preferred_term": "Coch", "term": {"id": "NCBIGene:12810", "label": "Coch"}}
MOUSE_COCHLIN = {"preferred_term": "mouse cochlin", "term": {"id": "UniProtKB:Q62507", "label": "Cochlin"}}
HUMAN_TMEM165 = {"preferred_term": "TMEM165", "term": {"id": "hgnc:30760", "label": "TMEM165"}}
CACHE = {"NCBIGene:12810": "Coch"}


def _gene(curie: str, label: str) -> dict:
    return {"preferred_term": label, "term": {"id": curie, "label": label}}


def _doc(**sections) -> dict:
    return {"name": "X", **sections}


def _kinds(data: dict, ncbigene: dict[str, str] | None = None) -> set[str]:
    return {f.kind for f in check_document(Path("x.yaml"), data, CACHE if ncbigene is None else ncbigene)}


@pytest.fixture(scope="module")
def view() -> SchemaView:
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def _errors(validator: Validator, record: dict, target: str) -> list:
    return [r for r in validator.validate(record, target_class=target).results if r.severity.name == "ERROR"]


# --------------------------------------------------------------------- schema


@pytest.mark.parametrize("cls", ["AnimalModel", "ExperimentalModel"])
def test_model_genes_admit_non_human_namespaces(view: SchemaView, cls: str) -> None:
    slot = view.induced_slot("genes", cls)
    assert slot.range == "GeneOrProductDescriptor"
    assert slot.multivalued


@pytest.mark.parametrize("cls", ["Genetic", "Pathophysiology", "Subtype"])
def test_human_gene_slots_stay_hgnc(view: SchemaView, cls: str) -> None:
    slots = view.class_slots(cls)
    for name in ("genes", "gene_term"):
        if name in slots:
            assert view.induced_slot(name, cls).range == "GeneDescriptor"


def test_both_prefixes_are_declared(view: SchemaView) -> None:
    prefixes = view.schema.prefixes
    assert "NCBIGene" in prefixes and "UniProtKB" in prefixes


def test_model_records_with_non_human_genes_validate(validator: Validator) -> None:
    animal = {"species": "Mouse", "genes": [MOUSE_COCH, MOUSE_COCHLIN]}
    cells = {"name": "ATDC5 knockout", "genes": [_gene("NCBIGene:21982", "Tmem165")]}
    assert not _errors(validator, animal, "AnimalModel")
    assert not _errors(validator, cells, "ExperimentalModel")
    assert not _errors(validator, {"name": "HEK293 knockout", "genes": [HUMAN_TMEM165]}, "ExperimentalModel")


def test_closed_validator_reports_errors(validator: Validator) -> None:
    # Guard against a validator that validates nothing.
    assert _errors(validator, {"name": "x", "genes": [{"bogus": 1}]}, "ExperimentalModel")


# ---------------------------------------------------------------------- check


def test_non_human_genes_on_models_are_clean() -> None:
    data = _doc(
        animal_models=[{"name": "knock-in", "genes": [MOUSE_COCH, MOUSE_COCHLIN]}],
        experimental_models=[{"name": "cells", "genes": [HUMAN_TMEM165]}],
    )
    assert _kinds(data) == set()


@pytest.mark.parametrize("gene", [MOUSE_COCH, MOUSE_COCHLIN])
def test_non_human_gene_outside_a_model_is_a_defect(gene: dict) -> None:
    data = _doc(genetic=[{"name": "COCH", "gene_term": gene}])
    assert "NON_HUMAN_OUTSIDE_MODEL" in _kinds(data)
    data = _doc(pathophysiology=[{"name": "node", "genes": [gene]}])
    assert "NON_HUMAN_OUTSIDE_MODEL" in _kinds(data)


def test_unchecked_prefix_on_a_model_is_reported_not_gated() -> None:
    data = _doc(animal_models=[{"genes": [_gene("MGI:88435", "Coch")]}])
    assert _kinds(data) == {"UNCHECKED_PREFIX"}
    assert "UNCHECKED_PREFIX" not in cgn.GATING


def test_uncached_ncbigene_is_a_defect() -> None:
    # The term validator passes any label on an unrouted prefix, so an
    # identifier nothing has resolved must not pass here either.
    assert "NCBIGENE_UNRESOLVED" in _kinds(_doc(animal_models=[{"genes": [MOUSE_COCH]}]), {})


def test_ncbigene_label_must_be_the_official_symbol() -> None:
    data = _doc(animal_models=[{"genes": [_gene("NCBIGene:12810", "Cochlin")]}])
    assert "NCBIGENE_LABEL_MISMATCH" in _kinds(data)


def test_fetch_reports_retired_and_human_records(monkeypatch: pytest.MonkeyPatch) -> None:
    class Response:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict:
            return {"result": {"uids": ["1", "2", "3", "4"],
                               "1": {"name": "Live", "status": "0", "currentid": "",
                                     "organism": {"taxid": 10090}},
                               "2": {"name": "Old", "status": "1", "currentid": "99"},
                               "3": {"error": "cannot get document summary"},
                               "4": {"name": "COCH", "status": "0", "currentid": "",
                                     "organism": {"taxid": 9606}}}}

    import requests
    monkeypatch.setattr(requests, "get", lambda *a, **k: Response())
    out = cgn.fetch_ncbigene(["NCBIGene:1", "NCBIGene:2", "NCBIGene:3", "NCBIGene:4"])
    assert out["NCBIGene:1"] == ("Live", None)
    assert "replaced by NCBIGene:99" in out["NCBIGene:2"][1]
    assert out["NCBIGene:3"][0] is None and out["NCBIGene:3"][1]
    assert out["NCBIGene:4"][1].startswith("human gene")


def test_cache_write_keeps_unchanged_rows_and_their_timestamps(tmp_path: Path) -> None:
    cache = tmp_path / "ncbigene" / "terms.csv"
    cgn.write_ncbigene_cache({"NCBIGene:2": "B"}, cache)
    first = cache.read_text()
    cgn.write_ncbigene_cache({"NCBIGene:1": "A", "NCBIGene:2": "B"}, cache)
    rows = cache.read_text().splitlines()
    assert rows[0] == "curie,label,retrieved_at"
    assert [r.split(",")[0] for r in rows[1:]] == ["NCBIGene:1", "NCBIGene:2"]
    assert first.splitlines()[1] in rows  # NCBIGene:2 kept its original timestamp
    assert not check_cache_file(cache)


def test_committed_caches_are_well_formed() -> None:
    ncbigene = ROOT / "cache" / "ncbigene" / "terms.csv"
    assert not check_cache_file(ncbigene)
    assert cgn.load_ncbigene_cache(ncbigene)["NCBIGene:12810"] == "Coch"
    assert not check_cache_file(ROOT / "cache" / "uniprotkb" / "terms.csv")


def test_worked_examples_pass_the_gate() -> None:
    files = [
        ROOT / "kb/disorders/TMEM165-Congenital_Disorder_of_Glycosylation.yaml",
        ROOT / "kb/disorders/Autosomal_Dominant_Nonsyndromic_Hearing_Loss_9.yaml",
        ROOT / "kb/disorders/Severe_Combined_Immunodeficiency_Due_To_CORO1A_Deficiency.yaml",
    ]
    findings = scan_repo(files)
    assert not findings
