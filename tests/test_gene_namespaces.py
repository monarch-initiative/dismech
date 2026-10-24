"""Tests for non-human gene identifiers on model systems and datasets.

The schema tests fix where the namespaces are admitted: the `genes` of
`AnimalModel`, `ExperimentalModel` and `Dataset` take a
`GeneOrProductDescriptor`, and every other gene slot keeps `GeneDescriptor`.

The check tests fix what `scripts/check_gene_namespaces.py` treats as a
defect, including the order of preference: HGNC for human, the Alliance MOD
for a model organism, NCBIGene or UniProtKB otherwise. See that script's
docstring for why each gating class is one.
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

MOUSE = {"preferred_term": "mouse", "term": {"id": "NCBITaxon:10090", "label": "Mus musculus"}}
PIG = {"preferred_term": "pig", "term": {"id": "NCBITaxon:9823", "label": "Sus scrofa"}}
LABELS = {
    "MGI:1278313": "Coch",
    "ZFIN:ZDB-GENE-030131-3222": "tmem165",
    "NCBIGene:100624179": "COCH",
}


def _gene(curie: str, label: str) -> dict:
    return {"preferred_term": label, "term": {"id": curie, "label": label}}


MOUSE_COCH = _gene("MGI:1278313", "Coch")
ZEBRAFISH_TMEM165 = _gene("ZFIN:ZDB-GENE-030131-3222", "tmem165")
PIG_COCH = _gene("NCBIGene:100624179", "COCH")
PIG_TRYPSIN = _gene("UniProtKB:P00761", "Trypsin")
HUMAN_TMEM165 = _gene("hgnc:30760", "TMEM165")


def _doc(**sections) -> dict:
    return {"name": "X", **sections}


def _kinds(data: dict, labels: dict[str, str] | None = None) -> set[str]:
    return {f.kind for f in check_document(Path("x.yaml"), data, LABELS if labels is None else labels)}


@pytest.fixture(scope="module")
def view() -> SchemaView:
    return SchemaView(str(SCHEMA))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(SCHEMA, validation_plugins=[JsonschemaValidationPlugin(closed=True)])


def _errors(validator: Validator, record: dict, target: str) -> list:
    return [r for r in validator.validate(record, target_class=target).results if r.severity.name == "ERROR"]


# --------------------------------------------------------------------- schema


@pytest.mark.parametrize("cls", ["AnimalModel", "ExperimentalModel", "Dataset"])
def test_model_and_dataset_genes_admit_non_human_namespaces(view: SchemaView, cls: str) -> None:
    slot = view.induced_slot("genes", cls)
    assert slot.range == "GeneOrProductDescriptor"
    assert slot.multivalued


@pytest.mark.parametrize("cls", ["Genetic", "Pathophysiology", "Subtype"])
def test_human_gene_slots_stay_hgnc(view: SchemaView, cls: str) -> None:
    slots = view.class_slots(cls)
    for name in ("genes", "gene_term"):
        if name in slots:
            assert view.induced_slot(name, cls).range == "GeneDescriptor"


def test_every_admitted_prefix_is_declared(view: SchemaView) -> None:
    prefixes = view.schema.prefixes
    for prefix in cgn.NON_HUMAN_PREFIXES:
        assert prefix in prefixes, prefix


def test_records_with_non_human_genes_validate(validator: Validator) -> None:
    animal = {"species": "Mouse", "genes": [MOUSE_COCH]}
    cells = {"name": "ATDC5 knockout", "genes": [_gene("MGI:894407", "Tmem165")]}
    dataset = {"accession": "geo:GSE1", "genes": [MOUSE_COCH]}
    assert not _errors(validator, animal, "AnimalModel")
    assert not _errors(validator, cells, "ExperimentalModel")
    assert not _errors(validator, dataset, "Dataset")
    assert not _errors(validator, {"name": "HEK293 knockout", "genes": [HUMAN_TMEM165]}, "ExperimentalModel")


def test_closed_validator_reports_errors(validator: Validator) -> None:
    # Guard against a validator that validates nothing.
    assert _errors(validator, {"name": "x", "genes": [{"bogus": 1}]}, "ExperimentalModel")


# ---------------------------------------------------------------------- check


def test_preferred_namespaces_are_clean() -> None:
    data = _doc(
        animal_models=[{"name": "knock-in", "genes": [MOUSE_COCH]},
                       {"name": "morphant", "genes": [ZEBRAFISH_TMEM165]}],
        experimental_models=[{"name": "cells", "genes": [HUMAN_TMEM165]},
                             {"name": "pig cells", "organism": PIG, "genes": [PIG_COCH, PIG_TRYPSIN]}],
        datasets=[{"accession": "geo:GSE1", "organism": MOUSE, "genes": [MOUSE_COCH]}],
    )
    assert _kinds(data) == set()


@pytest.mark.parametrize("gene", [MOUSE_COCH, PIG_COCH, PIG_TRYPSIN])
def test_non_human_gene_outside_a_model_is_a_defect(gene: dict) -> None:
    data = _doc(genetic=[{"name": "COCH", "gene_term": gene}])
    assert "NON_HUMAN_OUTSIDE_MODEL" in _kinds(data)
    data = _doc(pathophysiology=[{"name": "node", "genes": [gene]}])
    assert "NON_HUMAN_OUTSIDE_MODEL" in _kinds(data)


@pytest.mark.parametrize("curie", [
    "MGI:MGI:1278313",          # GO's GPAD/GPI local-ID form
    "XENBASE:XB-GENE-479154",   # wrong casing
    "FlyBase:FBgn0000490",      # Bioregistry's spelling, not Biolink's FB
    "ZFIN:tmem165",             # a symbol, not an identifier
])
def test_malformed_mod_identifiers_are_defects(curie: str) -> None:
    assert _kinds(_doc(animal_models=[{"genes": [_gene(curie, "x")]}])) == {"MALFORMED_ID"}


@pytest.mark.parametrize("gene", [_gene("NCBIGene:12810", "Coch"), _gene("UniProtKB:Q62507", "Cochlin")])
def test_fallback_prefix_on_a_mod_organism_is_a_defect(gene: dict) -> None:
    data = _doc(datasets=[{"accession": "geo:GSE1", "organism": MOUSE, "genes": [gene]}])
    assert "MOD_PREFERRED" in _kinds(data, {"NCBIGene:12810": "Coch"})


def test_hgnc_on_a_mod_organism_is_reported_not_gated() -> None:
    data = _doc(datasets=[{"accession": "geo:GSE1", "organism": MOUSE, "genes": [_gene("hgnc:2180", "COCH")]}])
    assert _kinds(data) == {"HGNC_IN_MOD_ORGANISM"}
    assert "HGNC_IN_MOD_ORGANISM" not in cgn.GATING


def test_unchecked_prefix_on_a_model_is_reported_not_gated() -> None:
    data = _doc(animal_models=[{"genes": [_gene("ENSEMBL:ENSMUSG00000020953", "Coch")]}])
    assert _kinds(data) == {"UNCHECKED_PREFIX"}
    assert "UNCHECKED_PREFIX" not in cgn.GATING


@pytest.mark.parametrize("gene", [MOUSE_COCH, PIG_COCH])
def test_uncached_identifier_is_a_defect(gene: dict) -> None:
    # The term validator passes any label on an unrouted prefix, so an
    # identifier nothing has resolved must not pass here either.
    assert "UNRESOLVED" in _kinds(_doc(animal_models=[{"genes": [gene]}]), {})


def test_label_must_be_the_official_symbol() -> None:
    # MGI:107573 is Ott. It sat on main labelled Blm, which every reviewer
    # reads as correct; only the symbol comparison catches it.
    data = _doc(animal_models=[{"genes": [_gene("MGI:107573", "Blm")]}])
    assert _kinds(data, {"MGI:107573": "Ott"}) == {"LABEL_MISMATCH"}


class _Response:
    def __init__(self, payload: dict, status: int = 200) -> None:
        self.payload = payload
        self.status_code = status

    def raise_for_status(self) -> None:
        pass

    def json(self) -> dict:
        return self.payload


def test_fetch_ncbigene_reports_retired_human_and_mod_records(monkeypatch: pytest.MonkeyPatch) -> None:
    payload = {"result": {"uids": ["1", "2", "3", "4", "5"],
                          "1": {"name": "COCH", "status": "0", "currentid": "", "organism": {"taxid": 9823}},
                          "2": {"name": "Old", "status": "1", "currentid": "99"},
                          "3": {"error": "cannot get document summary"},
                          "4": {"name": "COCH", "status": "0", "currentid": "", "organism": {"taxid": 9606}},
                          "5": {"name": "Coch", "status": "0", "currentid": "", "organism": {"taxid": 10090}}}}
    import requests
    monkeypatch.setattr(requests, "get", lambda *a, **k: _Response(payload))
    out = cgn.fetch_ncbigene([f"NCBIGene:{i}" for i in range(1, 6)])
    assert out["NCBIGene:1"] == ("COCH", None)
    assert out["NCBIGene:2"][1][0] == "RETIRED" and "NCBIGene:99" in out["NCBIGene:2"][1][1]
    assert out["NCBIGene:3"] == (None, ("UNRESOLVED", "NCBI has no record for this ID"))
    assert out["NCBIGene:4"][1][0] == "HUMAN_GENE"
    assert out["NCBIGene:5"][1][0] == "MOD_PREFERRED" and "MGI:" in out["NCBIGene:5"][1][1]


def test_fetch_mod_reads_the_alliance_record(monkeypatch: pytest.MonkeyPatch) -> None:
    import requests
    records = {
        "MGI:1278313": _Response({"gene": {"geneSymbol": {"displayText": "Coch"},
                                           "taxon": {"curie": "NCBITaxon:10090"}}}),
        "MGI:99999999": _Response({}, status=400),
        "MGI:2": _Response({"gene": {"geneSymbol": {"displayText": "Coch"},
                                     "taxon": {"curie": "NCBITaxon:7955"}}}),
    }
    monkeypatch.setattr(requests, "get", lambda url, **k: records[url.rsplit("/", 1)[1]])
    assert cgn.fetch_mod("MGI:1278313") == ("Coch", None)
    assert cgn.fetch_mod("MGI:99999999")[1][0] == "UNRESOLVED"
    assert cgn.fetch_mod("MGI:2")[1][0] == "UNRESOLVED"  # filed under the wrong species


def test_cache_write_keeps_unchanged_rows_and_their_timestamps(tmp_path: Path) -> None:
    cache = tmp_path / "mgi" / "terms.csv"
    cgn.write_cache("MGI", {"MGI:2": "B"}, cache)
    first = cache.read_text()
    cgn.write_cache("MGI", {"MGI:1": "A", "MGI:2": "B"}, cache)
    rows = cache.read_text().splitlines()
    assert rows[0] == "curie,label,retrieved_at"
    assert [r.split(",")[0] for r in rows[1:]] == ["MGI:1", "MGI:2"]
    assert first.splitlines()[1] in rows  # MGI:2 kept its original timestamp
    assert not check_cache_file(cache)


def test_committed_caches_are_well_formed() -> None:
    for prefix in cgn.CACHED_PREFIXES:
        path = cgn.cache_path(prefix)
        if path.exists():
            assert not check_cache_file(path), path
    assert cgn.load_cache("MGI")["MGI:1278313"] == "Coch"


def test_worked_examples_pass_the_gate() -> None:
    files = [
        ROOT / "kb/disorders/TMEM165-Congenital_Disorder_of_Glycosylation.yaml",
        ROOT / "kb/disorders/Autosomal_Dominant_Nonsyndromic_Hearing_Loss_9.yaml",
        ROOT / "kb/disorders/Severe_Combined_Immunodeficiency_Due_To_CORO1A_Deficiency.yaml",
    ]
    assert not [f for f in scan_repo(files) if f.kind in cgn.GATING]
