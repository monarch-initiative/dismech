"""Tests for the ClinGen structured-database source."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.clingen import (
    ClinGenSource,
    _ClinGenReportDetails,
    _parse_report_details,
)

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
    src = ClinGenSource(tmp_path, include_report_text=False)
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
    assert "- Report URL: https://search.clinicalgenome.org/kb/gene-validity/" in text
    assert "## Source" in text
    assert "ClinGen Gene-Disease Validity Curations CSV snapshot **2026-01-24**" in text


def test_serialize_can_include_clingen_evidence_summary(tmp_path: Path):
    (tmp_path / "gene_validity.csv").write_text(CSV_TEXT, encoding="utf-8")
    src = ClinGenSource(tmp_path)
    src._report_cache[HEXB_ASSERTION] = _ClinGenReportDetails(
        curation_id="CCID:005054",
        evidence_summary=(
            "HEXB was first reported in relation to Sandhoff disease.",
            "In summary, HEXB is definitively associated with Sandhoff disease.",
        ),
    )

    text = src.serialize(HEXB_ASSERTION).render()
    assert "## Evidence summary" in text
    assert "HEXB was first reported in relation to Sandhoff disease." in text
    assert "In summary, HEXB is definitively associated with Sandhoff disease." in text
    assert "- Curation ID: CCID:005054" in text


def test_parse_report_details_extracts_evidence_summary():
    html = """
    <html><body>
      <span>CCID:005054</span>
      <table>
        <tr>
          <td>Evidence Summary:</td>
          <td>
            <p>First evidence summary paragraph.</p>
            <p>Second evidence summary paragraph.</p>
          </td>
        </tr>
      </table>
    </body></html>
    """
    details = _parse_report_details(html)
    assert details.curation_id == "CCID:005054"
    assert details.evidence_summary == (
        "First evidence summary paragraph.",
        "Second evidence summary paragraph.",
    )


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


# ---------------------------------------------------------------------------
# Provenance of the file actually read (dismech#13575)
# ---------------------------------------------------------------------------

ALT_CSV_TEXT = CSV_TEXT.replace("FILE CREATED: 2026-01-24", "FILE CREATED: 2026-10-08")


def _sha256(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture()
def manifest_loaded(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Load a manifest whose pin does NOT match the fixture CSV, then restore.

    ``load_manifest`` mutates class attributes, so without the restore every
    later test in the process would see this manifest.
    """
    for attr in ("bulk_files", "_manifest_snapshot_date", "_manifest_schema_tag"):
        monkeypatch.setattr(
            ClinGenSource, attr, getattr(ClinGenSource, attr, None), raising=False
        )
    manifest = tmp_path / "MANIFEST.yaml"
    manifest.write_text(
        "snapshot_date: '2026-08-13'\n"
        "schema_tag: gene_validity.csv\n"
        "bulk_files:\n"
        "  - name: gene_validity.csv\n"
        "    url: https://search.clinicalgenome.org/kb/gene-validity/download\n"
        "    sha256: " + "deadbeef" * 8 + "\n"  # a string, not YAML int 0
        "    size_bytes: 1\n",
        encoding="utf-8",
    )
    ClinGenSource.load_manifest(manifest)
    return manifest


def test_snapshot_date_comes_from_the_csv_read_not_the_manifest(
    clingen_source: ClinGenSource, manifest_loaded: Path
):
    # The manifest says August; the CSV that was parsed says January. A cache
    # file must describe the data it was built from (dismech#13575).
    assert clingen_source.snapshot_date == "2026-01-24"
    text = clingen_source.serialize(HEXB_ASSERTION).render()
    assert "CSV snapshot **2026-01-24**" in text
    assert "2026-08-13" not in text


def test_cache_frontmatter_records_source_snapshot_and_sha256(
    clingen_source: ClinGenSource, tmp_path: Path
):
    path = clingen_source.write_cache_file(HEXB_ASSERTION, tmp_path / "out")
    text = path.read_text(encoding="utf-8")
    assert 'source_snapshot: "2026-01-24"' in text
    assert f'source_sha256: "{_sha256(tmp_path / "gene_validity.csv")}"' in text
    # ...and the deterministic frontmatter contract still accepts the file.
    assert check_cache_file(path) is None


def test_warns_when_the_pinned_sha256_differs_from_the_csv_read(
    tmp_path: Path, manifest_loaded: Path, caplog: pytest.LogCaptureFixture
):
    (tmp_path / "gene_validity.csv").write_text(CSV_TEXT, encoding="utf-8")
    src = ClinGenSource(tmp_path, include_report_text=False)
    with caplog.at_level("WARNING", logger="dismech.structured_sources.clingen"):
        src.index()
    messages = [r.getMessage() for r in caplog.records if r.levelname == "WARNING"]
    assert any("does not match" in m and "MANIFEST" in m for m in messages), messages


def test_no_pin_warning_when_the_csv_matches_the_manifest(
    tmp_path: Path, manifest_loaded: Path, caplog: pytest.LogCaptureFixture
):
    csv = tmp_path / "gene_validity.csv"
    csv.write_text(CSV_TEXT, encoding="utf-8")
    from dismech.structured_sources.base import BulkFile

    ClinGenSource.bulk_files = (
        BulkFile(name="gene_validity.csv", url="u", sha256=_sha256(csv)),
    )
    src = ClinGenSource(tmp_path, include_report_text=False)
    with caplog.at_level("WARNING", logger="dismech.structured_sources.clingen"):
        src.index()
    assert not [r for r in caplog.records if r.levelname == "WARNING"]


def test_warns_when_falling_back_to_the_committed_csv(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
):
    # No gene_validity.csv under data_dir: the source falls back to the
    # committed cache/clingen/gene_validity.csv, and must say so, because on a
    # fresh checkout that file is a January 2026 export (dismech#13575).
    src = ClinGenSource(tmp_path / "empty", include_report_text=False)
    with caplog.at_level("WARNING", logger="dismech.structured_sources.clingen"):
        path = src._csv_path()
    assert path.parts[-3:] == ("cache", "clingen", "gene_validity.csv")
    messages = [r.getMessage() for r in caplog.records if r.levelname == "WARNING"]
    assert any("cache/clingen/gene_validity.csv" in m for m in messages), messages


def test_explicit_csv_path_overrides_the_data_dir(tmp_path: Path):
    (tmp_path / "gene_validity.csv").write_text(CSV_TEXT, encoding="utf-8")
    other = tmp_path / "elsewhere" / "fresh.csv"
    other.parent.mkdir()
    other.write_text(ALT_CSV_TEXT, encoding="utf-8")
    src = ClinGenSource(tmp_path, include_report_text=False, csv_path=other)
    assert src.snapshot_date == "2026-10-08"
    assert src.serialize(HEXB_ASSERTION).extra_frontmatter["source_sha256"] == _sha256(
        other
    )


def test_rebuild_cli_accepts_an_explicit_csv(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    from typer.testing import CliRunner

    from dismech.structured_sources.cli import app

    for attr in ("bulk_files", "_manifest_snapshot_date", "_manifest_schema_tag"):
        monkeypatch.setattr(
            ClinGenSource, attr, getattr(ClinGenSource, attr, None), raising=False
        )
    csv = tmp_path / "fresh.csv"
    csv.write_text(ALT_CSV_TEXT, encoding="utf-8")
    out = tmp_path / "out"
    result = CliRunner().invoke(
        app,
        [
            "rebuild",
            "clingen",
            "--csv-only",
            "--csv",
            str(csv),
            "--cache-dir",
            str(out),
            "--id",
            HEXB_ASSERTION,
        ],
    )
    assert result.exit_code == 0, result.output
    text = (
        out
        / "CGGV_assertion_7f53d03d-f936-4628-ab75-351ae4da012a-2022-09-15T160000.000Z.md"
    ).read_text()
    assert "CSV snapshot **2026-10-08**" in text
    assert f'source_sha256: "{_sha256(csv)}"' in text
