"""Tests for the ToxCast assay-endpoint annotation client.

All tests run offline against a trimmed fixture of live CTX API responses. Seven
endpoints are kept, chosen to exercise each field group and each documented gap
rather than to be representative. No test needs ``CTX_API_KEY``.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from dismech.toxcast_assays import (
    AnnotationsMissing,
    MissingAPIKey,
    ToxCastAssayAnnotations,
    parse_annotation,
    parse_gene,
)

DATA_DIR = Path(__file__).parent / "data" / "toxcast"


def _raw(aeid: int) -> dict:
    doc = json.loads((DATA_DIR / "assay_annotations.json").read_text(encoding="utf-8"))
    return next(e for e in doc["endpoints"] if e["aeid"] == aeid)


@pytest.fixture
def annotations(tmp_path: Path) -> ToxCastAssayAnnotations:
    data_dir = tmp_path / "toxcast"
    data_dir.mkdir()
    (data_dir / "assay_annotations.json").write_text(
        (DATA_DIR / "assay_annotations.json").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    return ToxCastAssayAnnotations(data_dir)


# ----- the seven field groups #12858 names -----


def test_carries_every_field_group_that_defines_biological_attributes():
    """Endpoint 1816 populates all seven, so it is the completeness check."""
    e = parse_annotation(_raw(1816))
    assert e.name == "TOX21_AR_LUC_MDAKB2_Antagonist_0.5nM_R1881"
    assert e.gene_symbols == ("AR",)
    assert (e.target_type, e.target_type_sub) == ("protein", "receptor")
    assert (e.target_family, e.target_family_sub) == ("nuclear receptor", "steroidal")
    assert e.biological_process == "regulation of transcription factor activity"
    assert (e.organism, e.tissue, e.cell) == ("human", "breast", "MDA-kb2")
    assert e.function_type == "antagonist"
    assert e.signal_direction == "loss"


def test_gene_carries_identifiers_not_just_a_symbol():
    """A bare symbol is species-specific and not a stable key."""
    gene = parse_annotation(_raw(1816)).genes[0]
    assert gene.symbol == "AR"
    assert gene.full_name == "androgen receptor"
    assert gene.entrez_gene_id == 367
    assert gene.uniprot_accession == "P10275"


def test_two_intended_genes_are_both_kept():
    """A hit on a two-gene endpoint isolates neither target."""
    e = parse_annotation(_raw(744))
    assert e.gene_symbols == ("ESR1", "ESR2")
    assert e.gene_label == "ESR1;ESR2"


def test_gene_symbol_is_species_specific():
    """Endpoint 725 names mouse Esr1, not human ESR1."""
    e = parse_annotation(_raw(725))
    assert e.gene_symbols == ("Esr1",)
    assert not e.is_human


def test_absent_gene_target_is_empty_not_invented():
    """Roughly a third of endpoints declare no intended gene target."""
    e = parse_annotation(_raw(783))
    assert e.genes == ()
    assert e.gene_label == "-"


def test_viability_counter_screen_is_flagged():
    """A hit here is cytotoxicity, not activity at the intended target."""
    assert parse_annotation(_raw(787)).is_viability is True


def test_format_type_distinguishes_biochemical_from_cell_based():
    """`experimental_model_type` has no value for a non-cell-based assay, which
    is an open question on #12858, so the distinction has to survive parsing."""
    assert parse_annotation(_raw(3089)).format_type == "biochemical"
    assert parse_annotation(_raw(1816)).format_type == "cell-based"


def test_target_type_sub_distinguishes_a_transporter_from_a_receptor():
    """Endpoint 3089 targets transthyretin, a transport protein."""
    e = parse_annotation(_raw(3089))
    assert e.target_type_sub == "transporter"
    assert e.function_type == "binding"


def test_citation_pmids_are_captured_so_a_mapping_can_cite_the_method():
    assert 16481145 in parse_annotation(_raw(2)).citation_pmids


def test_parse_gene_returns_none_without_a_symbol():
    assert parse_gene({"entrezGeneId": 1}) is None


# ----- the snapshot -----


def test_load_indexes_every_endpoint(annotations: ToxCastAssayAnnotations):
    snapshot = annotations.load()
    assert len(snapshot) == 7
    assert snapshot.retrieved == "2026-09-24"
    assert snapshot.get(1816).name.startswith("TOX21_AR_LUC")


def test_with_genes_excludes_the_gene_less_endpoints(
    annotations: ToxCastAssayAnnotations,
):
    with_genes = {e.aeid for e in annotations.load().with_genes()}
    assert 783 not in with_genes and 787 not in with_genes
    assert {2, 725, 744, 1816, 3089} <= with_genes


def test_by_gene_symbol_merges_orthologs_onto_one_key(
    annotations: ToxCastAssayAnnotations,
):
    """Upper-casing collects human ESR1 and mouse Esr1 together, which is what
    a coverage count wants — but each endpoint still says its own species."""
    by_gene = annotations.load().by_gene_symbol()
    esr1 = by_gene["ESR1"]
    assert {e.aeid for e in esr1} == {2, 725, 744}
    assert sum(1 for e in esr1 if e.is_human) == 2


def test_a_two_gene_endpoint_appears_under_both_symbols(
    annotations: ToxCastAssayAnnotations,
):
    by_gene = annotations.load().by_gene_symbol()
    assert 744 in {e.aeid for e in by_gene["ESR1"]}
    assert 744 in {e.aeid for e in by_gene["ESR2"]}


# ----- errors and offline contract -----


def test_missing_annotations_names_the_remedy(tmp_path: Path):
    with pytest.raises(AnnotationsMissing) as exc:
        ToxCastAssayAnnotations(tmp_path / "nope").load()
    assert "just toxcast-refresh" in str(exc.value)


def test_missing_api_key_names_the_remedy(tmp_path: Path, monkeypatch):
    monkeypatch.delenv("CTX_API_KEY", raising=False)
    with pytest.raises(MissingAPIKey) as exc:
        ToxCastAssayAnnotations(tmp_path)._get("bioactivity/assay/")
    assert "ccte_api@epa.gov" in str(exc.value)


def test_refresh_writes_a_manifest_recording_provenance(tmp_path: Path, monkeypatch):
    """The annotations are gitignored, so the manifest is what records the fetch."""
    src = ToxCastAssayAnnotations(tmp_path / "toxcast")
    raw = json.loads((DATA_DIR / "assay_annotations.json").read_text())["endpoints"]
    monkeypatch.setattr(src, "_get", lambda path: raw)
    assert src.refresh() == 7
    manifest = src.manifest_path.read_text()
    assert "n_endpoints: 7" in manifest
    assert "retrieved:" in manifest
    assert "invitrodbVersion" in manifest  # says where the release can be read


def test_refresh_is_a_noop_when_already_cached(annotations: ToxCastAssayAnnotations):
    """Guards against refetching several megabytes on every invocation."""

    def _fail(path):  # pragma: no cover - must not be reached
        raise AssertionError("refresh should not fetch when already cached")

    annotations._get = _fail  # type: ignore[method-assign]
    assert annotations.refresh() == 7
