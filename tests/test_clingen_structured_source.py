"""Tests for the ClinGen structured-database source."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.clingen import ClinGenSource


CSV_TEXT = """"CLINGEN GENE DISEASE VALIDITY CURATIONS","","","","","","","","",""
"FILE CREATED: 2026-01-24","","","","","","","","",""
"WEBPAGE: https://search.clinicalgenome.org/kb/gene-validity","","","","","","","","",""
"+++++++++++","++++++++++++++","+++++++++++++","++++++++++++++++++","+++++++++","+++++++++","++++++++++++++","+++++++++++++","+++++++++++++++++++","+++++++++++++++++++"
"GENE SYMBOL","GENE ID (HGNC)","DISEASE LABEL","DISEASE ID (MONDO)","MOI","SOP","CLASSIFICATION","ONLINE REPORT","CLASSIFICATION DATE","GCEP"
"+++++++++++","++++++++++++++","+++++++++++++","++++++++++++++++++","+++++++++","+++++++++","++++++++++++++","+++++++++++++","+++++++++++++++++++","+++++++++++++++++++"
"HEXB","HGNC:4879","Sandhoff disease","MONDO:0010006","AR","SOP9","Definitive","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z","2022-09-15T16:00:00.000Z","Lysosomal Diseases Gene Curation Expert Panel"
"GLB1","HGNC:4298","mucopolysaccharidosis type 4B","MONDO:0009660","AR","SOP10","Definitive","https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_9e170fda-e08a-4fd3-a3e5-f08c5c0d55b8-2023-04-28T160000.000Z","2023-04-28T16:00:00.000Z","Lysosomal Diseases Gene Curation Expert Panel"
"""


HEXB_ASSERTION = (
    "CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z"
)


@pytest.fixture()
def clingen_source(tmp_path: Path) -> ClinGenSource:
    (tmp_path / "gene_validity.csv").write_text(CSV_TEXT, encoding="utf-8")
    src = ClinGenSource(tmp_path)
    src.index()
    return src


def test_index_reads_gene_validity_rows(clingen_source: ClinGenSource):
    idx = clingen_source.index()
    assert len(idx) == 2
    assert idx[HEXB_ASSERTION].gene_symbol == "HEXB"
    assert idx[HEXB_ASSERTION].disease_mondo_id == "MONDO:0010006"
    assert clingen_source.snapshot_date == "2026-01-24"


def test_serialize_clingen_assertion_has_expected_blocks(
    clingen_source: ClinGenSource,
):
    text = clingen_source.serialize(HEXB_ASSERTION).render()
    assert f'reference_id: "{HEXB_ASSERTION}"' in text
    assert 'title: "HEXB / Sandhoff disease (Definitive)"' in text
    assert 'database: "ClinGen"' in text
    assert 'content_type: "structured_record"' in text
    assert "journal:" not in text

    assert f"# {HEXB_ASSERTION}  HEXB / Sandhoff disease" in text
    assert "## Gene-disease validity" in text
    assert "| Gene | HGNC | Disease | MONDO | MOI | Classification |" in text
    assert (
        "| HEXB | HGNC:4879 | Sandhoff disease | MONDO:0010006 | AR | "
        "Definitive | SOP9 | Lysosomal Diseases Gene Curation Expert Panel | "
        "2022-09-15T16:00:00.000Z |"
    ) in text
    assert "## Online report" in text
    assert "## Source" in text
    assert "ClinGen Gene-Disease Validity Curations CSV snapshot **2026-01-24**" in text


def test_serialize_is_byte_deterministic(clingen_source: ClinGenSource):
    a = clingen_source.serialize(HEXB_ASSERTION).render()
    b = clingen_source.serialize(HEXB_ASSERTION).render()
    assert a == b


def test_cache_file_passes_frontmatter_contract(
    clingen_source: ClinGenSource, tmp_path: Path
):
    path = clingen_source.write_cache_file(HEXB_ASSERTION, tmp_path)
    assert check_cache_file(path) is None


def test_filename_matches_reference_id(clingen_source: ClinGenSource):
    entry = clingen_source.serialize(HEXB_ASSERTION)
    assert (
        entry.filename() == "CGGV_assertion_7f53d03d-f936-4628-ab75-351ae4da012a-"
        "2022-09-15T160000.000Z.md"
    )


@pytest.mark.parametrize(
    "identifier",
    [
        HEXB_ASSERTION,
        "assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z",
        f"CLINGEN:{HEXB_ASSERTION}",
        (
            "https://search.clinicalgenome.org/kb/gene-validity/"
            "CGGV:assertion_7f53d03d-f936-4628-ab75-351ae4da012a-"
            "2022-09-15T160000.000Z"
        ),
    ],
)
def test_serialize_accepts_native_bare_and_url_identifiers(
    clingen_source: ClinGenSource, identifier: str
):
    entry = clingen_source.serialize(identifier)
    assert entry.reference_id == HEXB_ASSERTION
    assert entry.title == "HEXB / Sandhoff disease (Definitive)"
