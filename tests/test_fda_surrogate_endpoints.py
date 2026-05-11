"""Regression tests for the FDA surrogate endpoint table import."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml


FDA_ENDPOINTS_PATH = Path("kb/surrogate_endpoints/fda_surrogate_endpoints.yaml")


def _collection() -> dict:
    return yaml.safe_load(FDA_ENDPOINTS_PATH.read_text())


def test_fda_surrogate_endpoint_table_counts() -> None:
    """All four FDA surrogate endpoint worksheets should be represented."""
    rows = _collection()["surrogate_endpoints"]

    assert len(rows) == 225
    assert Counter(row["source_table"] for row in rows) == {
        "ADULT_NONCANCER": 121,
        "ADULT_CANCER": 21,
        "PEDIATRIC_NONCANCER": 76,
        "PEDIATRIC_CANCER": 7,
    }


def test_fda_surrogate_endpoint_rows_have_required_provenance() -> None:
    """Each imported row should preserve row-level FDA source provenance."""
    collection = _collection()
    rows = collection["surrogate_endpoints"]
    required = {
        "row_id",
        "source_table",
        "source_sheet",
        "source_row_number",
        "disease_or_use",
        "patient_population",
        "surrogate_endpoint",
        "approval_type",
        "drug_mechanism_of_action",
        "endpoint_validation_level",
        "clinical_benefit_linkage",
        "clinical_benefit_linkage_basis",
        "context_of_use",
        "mapping_status",
        "source_url",
        "source_workbook_url",
        "source_workbook_sha256",
        "source_content_current_as_of",
        "retrieved_date",
    }

    assert collection["source_content_current_as_of"] == "2026-04-29"
    assert collection["source_workbook_sha256"]
    assert all(required <= row.keys() for row in rows)
    assert len({row["row_id"] for row in rows}) == len(rows)


def test_fda_surrogate_endpoint_approval_semantics() -> None:
    """Approval type should drive the BEST-aligned clinical-benefit linkage."""
    rows = _collection()["surrogate_endpoints"]
    by_id = {row["row_id"]: row for row in rows}

    alzheimer = by_id["FDA-SE-adult-noncancer-006"]
    assert alzheimer["surrogate_endpoint"] == "Reduction in amyloid beta plaques"
    assert alzheimer["approval_type"] == "ACCELERATED"
    assert (
        alzheimer["endpoint_validation_level"] == "REASONABLY_LIKELY_SURROGATE_ENDPOINT"
    )
    assert (
        alzheimer["clinical_benefit_linkage"]
        == "REASONABLY_LIKELY_TO_PREDICT_CLINICAL_BENEFIT"
    )

    tumor_burden = next(
        row
        for row in rows
        if row["source_table"] == "PEDIATRIC_CANCER"
        and row["surrogate_endpoint"] == "Progression-free survival(PFS)"
    )
    assert tumor_burden["approval_type"] == "ACCELERATED_OR_TRADITIONAL"
    assert tumor_burden["clinical_benefit_linkage"] == "CONTEXT_DEPENDENT"
    assert "TUMOR_BURDEN_CONTEXT_DEPENDENT" in tumor_burden["footnotes"]


def test_fda_surrogate_endpoint_target_disease_mappings() -> None:
    """The four surrogate-endpoint focus diseases should have mapped or candidate rows."""
    rows = _collection()["surrogate_endpoints"]

    dmd_rows = [
        row
        for row in rows
        if "Duchenne Muscular Dystrophy" in row.get("mapped_diseases", [])
    ]
    fabry_rows = [
        row for row in rows if "Fabry disease" in row.get("mapped_diseases", [])
    ]
    scd_rows = [
        row for row in rows if "Sickle Cell Disease" in row.get("mapped_diseases", [])
    ]
    thal_rows = [
        row for row in rows if "Beta Thalassemia" in row.get("mapped_diseases", [])
    ]

    assert len(dmd_rows) == 2
    assert len(fabry_rows) == 3
    assert len(scd_rows) == 2
    assert len(thal_rows) == 2
    assert {row["mapping_status"] for row in scd_rows} == {"CANDIDATE_DISMECH_MAPPING"}
    assert {row["mapping_status"] for row in thal_rows} == {"CANDIDATE_DISMECH_MAPPING"}
