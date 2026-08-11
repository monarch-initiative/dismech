"""Unit tests for the Mondo EMC TSV exporter."""

import csv
import io
from pathlib import Path

import yaml

from dismech.export.mondo_emc_export import (
    DISMECH_BASE_URL,
    TSV_COLUMNS,
    _collect_pmids,
    _normalize_description,
    _resolve_mondo,
    build_emc_export,
    emc_row_for_disorder,
    write_tsv,
)


def _write_yaml(path: Path, payload: dict) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    return path


# --- _resolve_mondo -------------------------------------------------------


def test_resolve_mondo_from_disease_term() -> None:
    data = {"disease_term": {"term": {"id": "MONDO:0007947", "label": "Marfan syndrome"}}}
    assert _resolve_mondo(data) == ("MONDO:0007947", "Marfan syndrome")


def test_resolve_mondo_excludes_ontology_root() -> None:
    """MONDO:0000001 (the 'disease' root) must never be emitted."""
    data = {"disease_term": {"term": {"id": "MONDO:0000001", "label": "disease"}}}
    assert _resolve_mondo(data) == ("", "")


def test_resolve_mondo_excludes_non_mondo_curie() -> None:
    data = {"disease_term": {"term": {"id": "ORPHA:558", "label": "Marfan syndrome"}}}
    assert _resolve_mondo(data) == ("", "")


def test_resolve_mondo_no_fallback_to_mappings() -> None:
    """Only disease_term is used; mappings.mondo_mappings is ignored."""
    data = {
        "disease_term": {"term": {"id": "", "label": ""}},
        "mappings": {
            "mondo_mappings": [
                {"predicate": "skos:exactMatch", "term": {"id": "MONDO:0007947", "label": "Marfan syndrome"}}
            ]
        },
    }
    assert _resolve_mondo(data) == ("", "")


def test_resolve_mondo_missing_disease_term() -> None:
    assert _resolve_mondo({}) == ("", "")


def test_resolve_mondo_strips_whitespace() -> None:
    data = {"disease_term": {"term": {"id": "  MONDO:0007947  ", "label": "  Marfan syndrome  "}}}
    assert _resolve_mondo(data) == ("MONDO:0007947", "Marfan syndrome")


# --- _collect_pmids -------------------------------------------------------


def test_collect_pmids_recursive_dedup_sorted() -> None:
    data = {
        "evidence": [
            {"reference": "PMID:222", "snippet": "b"},
            {"reference": "PMID:111", "snippet": "a"},
        ],
        "pathophysiology": [
            {"evidence": [{"reference": "PMID:222"}]},  # duplicate
            {"evidence": [{"reference": "PMID:333"}]},
        ],
    }
    assert _collect_pmids(data) == ["PMID:111", "PMID:222", "PMID:333"]


def test_collect_pmids_ignores_non_pmid_references() -> None:
    """Strict PMID matching: lowercase, DOI, NCT, and ORPHA refs are excluded."""
    data = {
        "evidence": [
            {"reference": "pmid:111"},
            {"reference": "DOI:10.1/x"},
            {"reference": "clinicaltrials:NCT00000000"},
            {"reference": "ORPHA:558"},
            {"reference": "PMID:111abc"},
            {"reference": "PMID:999"},
        ]
    }
    assert _collect_pmids(data) == ["PMID:999"]


def test_collect_pmids_empty_when_none() -> None:
    assert _collect_pmids({"description": "no refs here"}) == []


# --- _normalize_description ----------------------------------------------


def test_normalize_description_collapses_whitespace_and_newlines() -> None:
    raw = "Marfan syndrome is\n  an autosomal dominant\n\nconnective tissue disorder."
    assert (
        _normalize_description(raw)
        == "Marfan syndrome is an autosomal dominant connective tissue disorder."
    )


def test_normalize_description_none_and_empty() -> None:
    assert _normalize_description(None) == ""
    assert _normalize_description("") == ""


# --- emc_row_for_disorder -------------------------------------------------


def test_emc_row_for_disorder_full_row(tmp_path: Path) -> None:
    path = _write_yaml(
        tmp_path / "Marfan_Syndrome.yaml",
        {
            "name": "Marfan syndrome",
            "disease_term": {"term": {"id": "MONDO:0007947", "label": "Marfan syndrome"}},
            "description": "Marfan syndrome is\n  a connective tissue disorder.",
            "synonyms": ["MFS", "Marfan's syndrome"],
            "evidence": [{"reference": "PMID:11705149"}],
        },
    )
    row = emc_row_for_disorder(path)
    assert row == {
        "mondo_id": "MONDO:0007947",
        "mondo_label": "Marfan syndrome",
        "dismech_url": f"{DISMECH_BASE_URL}/Marfan_Syndrome.html",
        "dismech_definition": "Marfan syndrome is a connective tissue disorder.",
        "dismech_exact_synonyms": "MFS|Marfan's syndrome",
        "dismech_pmids": "PMID:11705149",
    }


def test_emc_row_for_disorder_returns_none_without_mondo(tmp_path: Path) -> None:
    path = _write_yaml(
        tmp_path / "No_Mondo.yaml",
        {"name": "x", "disease_term": {"term": {"id": "ORPHA:1", "label": "x"}}},
    )
    assert emc_row_for_disorder(path) is None


def test_emc_row_for_disorder_empty_cells(tmp_path: Path) -> None:
    """Disorders with no description/synonyms/PMIDs emit empty strings."""
    path = _write_yaml(
        tmp_path / "Sparse.yaml",
        {"name": "Sparse", "disease_term": {"term": {"id": "MONDO:0000123", "label": "sparse disease"}}},
    )
    row = emc_row_for_disorder(path)
    assert row is not None
    assert row["dismech_definition"] == ""
    assert row["dismech_exact_synonyms"] == ""
    assert row["dismech_pmids"] == ""


# --- build_emc_export -----------------------------------------------------


def test_build_emc_export_sorts_and_filters(tmp_path: Path) -> None:
    a = _write_yaml(
        tmp_path / "B_disease.yaml",
        {"name": "B", "disease_term": {"term": {"id": "MONDO:0000222", "label": "b"}}},
    )
    b = _write_yaml(
        tmp_path / "A_disease.yaml",
        {"name": "A", "disease_term": {"term": {"id": "MONDO:0000111", "label": "a"}}},
    )
    skipped = _write_yaml(
        tmp_path / "Skip.yaml",
        {"name": "skip", "disease_term": {"term": {"id": "MONDO:0000001", "label": "disease"}}},
    )
    rows = build_emc_export([a, b, skipped])
    assert [r["mondo_id"] for r in rows] == ["MONDO:0000111", "MONDO:0000222"]


# --- write_tsv ------------------------------------------------------------


def test_write_tsv_header_and_columns() -> None:
    buf = io.StringIO()
    write_tsv(
        [
            {
                "mondo_id": "MONDO:0000111",
                "mondo_label": "a",
                "dismech_url": "u",
                "dismech_definition": "d",
                "dismech_exact_synonyms": "s",
                "dismech_pmids": "PMID:1",
            }
        ],
        buf,
    )
    text = buf.getvalue()
    assert text.startswith("\t".join(TSV_COLUMNS) + "\n")
    reader = list(csv.DictReader(io.StringIO(text), delimiter="\t"))
    assert reader[0]["mondo_id"] == "MONDO:0000111"
    assert reader[0]["dismech_pmids"] == "PMID:1"
