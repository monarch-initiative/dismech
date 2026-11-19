"""Tests for the IMPC structured-database source.

The synthetic-fixture tests always run. The release-data tests run only when
the pinned reports are in ``data/impc/`` (``just impc-refresh``).
"""

from __future__ import annotations

import csv
import gzip
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.base import MissingBulkDataError
from dismech.structured_sources.impc import IMPCSource, normalize_identifier

REPO_ROOT = Path(__file__).parent.parent
IMPC_DIR = REPO_ROOT / "data" / "impc"
MANIFEST = IMPC_DIR / "MANIFEST.yaml"


def _write_gz_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with gzip.open(path, "wt", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


ASSERTION_HEADER = [
    "marker_accession_id",
    "marker_symbol",
    "phenotyping_center",
    "sex",
    "zygosity",
    "allele_symbol",
    "procedure_name",
    "parameter_name",
    "mp_term_id",
    "mp_term_name",
    "p_value",
    "effect_size",
    "resource_name",
]
COMPLETENESS_HEADER = [
    "Gene Symbol",
    "Gene Accession Id",
    "Allele Symbol",
    "Colony Id",
    "Phenotyping Center",
    "Zygosity",
    "Life Stage",
    "Procedure Count: Successful",
    "Top-level MP Name: Successful",
    "Top-level MP Name: Significant",
]
VIABILITY_HEADER = [
    "Gene Symbol",
    "Gene Accession Id",
    "Allele Symbol",
    "Colony Id",
    "Phenotyping Center",
    "Zygosity",
    "Total # Pups",
    "Percentage HOMs / HEMs",
    "Supporting Data",
    "Viability Phenotype HOMs/HEMIs",
]


@pytest.fixture
def fixture_source(tmp_path: Path) -> IMPCSource:
    allele = "Abc1<tm1b(KOMP)Wtsi>"
    _write_gz_csv(
        tmp_path / "genotype-phenotype-assertions-ALL.csv.gz",
        ASSERTION_HEADER,
        [
            ["MGI:12", "Abc1", "WTSI", "female", "homozygote", allele, "Hematology",
             "Platelet count", "MP:0003179", "thrombocytopenia", "1.2E-5", "0.8", "IMPC"],
            ["MGI:12", "Abc1", "WTSI", "male", "homozygote", allele, "Hematology",
             "Platelet count", "MP:0003179", "thrombocytopenia", "3.4E-4", "0.6", "IMPC"],
            # An exact duplicate row is emitted once.
            ["MGI:12", "Abc1", "WTSI", "male", "homozygote", allele, "Hematology",
             "Platelet count", "MP:0003179", "thrombocytopenia", "3.4E-4", "0.6", "IMPC"],
        ],
    )
    _write_gz_csv(
        tmp_path / "procedureCompletenessAndPhenotypeHits.csv.gz",
        COMPLETENESS_HEADER,
        [
            ["Abc1", "MGI:12", allele, "C1", "WTSI", "homozygote", "Early adult", "14",
             "vision/eye phenotype|hematopoietic system phenotype", "hematopoietic system phenotype"],
            ["Def2", "MGI:3", "Def2<em1(IMPC)J>", "C2", "JAX", "homozygote", "Early adult", "12",
             "vision/eye phenotype", "None"],
        ],
    )
    _write_gz_csv(
        tmp_path / "viability.csv.gz",
        VIABILITY_HEADER,
        [["Abc1", "MGI:12", allele, "C1", "WTSI", "homozygote", "90", "0.2444",
          "Homozygous - Viable", "viable"]],
    )
    IMPCSource._manifest_release = "99.0"
    IMPCSource._manifest_snapshot_date = "2026-01-01"
    return IMPCSource(tmp_path)


@pytest.mark.parametrize(
    "raw",
    ["IMPC:MGI:12", "MGI:12", "IMPC:12", "IMPC_MGI_12", "impc:mgi:12", "12"],
)
def test_normalize_identifier_accepts_each_spelling(raw: str):
    assert normalize_identifier(raw) == "MGI:12"


def test_normalize_identifier_rejects_garbage():
    with pytest.raises(ValueError):
        normalize_identifier("IMPC:Abc1")


def test_identifiers_sorted_numerically(fixture_source: IMPCSource):
    assert list(fixture_source.identifiers()) == ["IMPC:MGI:3", "IMPC:MGI:12"]


def test_record_has_quotable_rows(fixture_source: IMPCSource):
    entry = fixture_source.serialize("IMPC:MGI:12")
    text = entry.render()
    assert entry.reference_id == "IMPC:MGI:12"
    assert entry.filename() == "IMPC_MGI_12.md"
    assert 'database: "IMPC"' in text
    assert "| MP:0003179 | thrombocytopenia | Hematology | Platelet count | homozygote | female |" in text
    assert text.count("| MP:0003179 | thrombocytopenia | Hematology | Platelet count | homozygote | male |") == 1
    assert "| Abc1<tm1b(KOMP)Wtsi> | C1 | homozygote | viable | 90 | 0.24 | WTSI |" in text
    # Systems are sorted, so the tested list is stable across releases.
    assert "| hematopoietic system phenotype; vision/eye phenotype | hematopoietic system phenotype |" in text
    assert "- Data release: 99.0 (2026-01-01)" in text


def test_tested_without_call_is_explicit(fixture_source: IMPCSource):
    text = fixture_source.serialize("MGI:3").render()
    assert "| Def2<em1(IMPC)J> | C2 | homozygote | Early adult | JAX | 12 | vision/eye phenotype | none |" in text
    assert "No significant phenotype call in this release." in text
    assert "No viability record in this release." in text


def test_written_file_passes_cache_contract(fixture_source: IMPCSource, tmp_path: Path):
    path = fixture_source.write_cache_file("IMPC:MGI:12", tmp_path / "cache")
    assert check_cache_file(path) is None


def test_unknown_gene_raises(fixture_source: IMPCSource):
    with pytest.raises(KeyError):
        fixture_source.serialize("IMPC:MGI:999")


def test_missing_reports_name_the_remedy(tmp_path: Path):
    with pytest.raises(MissingBulkDataError, match="just impc-refresh"):
        IMPCSource(tmp_path).index()


@pytest.mark.skipif(
    not (IMPC_DIR / "viability.csv.gz").exists(),
    reason="IMPC release reports absent; run `just impc-refresh`",
)
def test_committed_cache_matches_pinned_release(tmp_path: Path):
    """Every committed IMPC record rebuilds byte-for-byte from the pinned release."""
    IMPCSource.load_manifest(MANIFEST)
    src = IMPCSource(IMPC_DIR)
    committed = sorted((REPO_ROOT / "references_cache").glob("IMPC_MGI_*.md"))
    for path in committed:
        ref = path.stem.replace("IMPC_MGI_", "IMPC:MGI:")
        rebuilt = src.write_cache_file(ref, tmp_path)
        assert rebuilt.read_text() == path.read_text(), path.name
