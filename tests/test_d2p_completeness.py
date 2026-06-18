"""Tests for D2P phenotype-completeness audit helpers."""

from dismech.compare.d2p import (
    _is_genetic_disease,
    build_disease_audit_payload,
    build_comparison_table,
    build_completeness_audit,
    compute_audit_summary,
    extract_dismech_phenotypes,
)


def test_completeness_audit_flags_source_evidence_and_pathograph_gaps():
    disease = {
        "name": "Test Disease",
        "disease_term": {"term": {"id": "MONDO:0000001", "label": "test disease"}},
        "pathophysiology": [
            {
                "name": "Primary mechanism",
                "downstream": [{"target": "Connected phenotype"}],
                "evidence": [
                    {
                        "reference": "ORPHA:123",
                        "supports": "SUPPORT",
                        "snippet": "structured source row",
                    }
                ],
            }
        ],
        "phenotypes": [
            {
                "name": "Connected phenotype",
                "phenotype_term": {"term": {"id": "HP:0000001", "label": "All"}},
                "evidence": [
                    {
                        "reference": "PMID:1",
                        "supports": "SUPPORT",
                        "snippet": "quoted text",
                    }
                ],
            },
            {
                "name": "Floating phenotype",
                "phenotype_term": {
                    "term": {"id": "HP:0000002", "label": "Abnormality"}
                },
                "evidence": [
                    {
                        "reference": "PMID:2",
                        "supports": "NO_EVIDENCE",
                        "snippet": "quoted text",
                    }
                ],
            },
        ],
    }
    dismech_phenos = extract_dismech_phenotypes(disease)
    table = build_comparison_table(
        "MONDO:0000001",
        "Test Disease",
        dismech_phenos,
        omim_phenos=[
            {"hp_id": "HP:0000003", "label": "Missing phenotype", "pmids": []}
        ],
        ordo_phenos=[{"hp_id": "HP:0000002", "label": "Abnormality", "pmids": []}],
        resolver=None,
    )

    audit_rows = build_completeness_audit(disease, table)
    issues = {
        (row["issue_type"], row["phenotype_id"], row["phenotype_name"])
        for row in audit_rows
    }

    assert (
        "source_phenotype_missing_locally",
        "HP:0000003",
        "",
    ) in issues
    assert (
        "local_phenotype_missing_supporting_evidence",
        "HP:0000002",
        "Floating phenotype",
    ) in issues
    assert (
        "local_phenotype_unlinked_to_pathograph",
        "HP:0000002",
        "Floating phenotype",
    ) in issues
    assert (
        "local_phenotype_unlinked_to_pathograph",
        "HP:0000001",
        "Connected phenotype",
    ) not in issues
    missing_source_row = next(
        row
        for row in audit_rows
        if row["issue_type"] == "source_phenotype_missing_locally"
        and row["phenotype_id"] == "HP:0000003"
    )
    assert missing_source_row["source_evidence_refs"] == ""
    orphanet_backed_row = next(
        row
        for row in audit_rows
        if row["issue_type"] == "local_phenotype_missing_supporting_evidence"
    )
    assert orphanet_backed_row["source_evidence_refs"] == "ORPHA:123"

    summary = compute_audit_summary(audit_rows)
    assert summary["total_issues"] == 3
    assert summary["by_priority"] == {"high": 2, "medium": 1}


def test_completeness_audit_flags_source_term_covered_only_by_broader_local_term():
    row = {
        "disease_id": "MONDO:0000001",
        "disease_name": "Test Disease",
        "phenotype_id": "HP:0000004",
        "phenotype_label": "Specific source phenotype",
        "dismech": "broad:HP:0000118",
        "omim": "exact",
        "ordo": "-",
    }

    audit_rows = build_completeness_audit(
        {"name": "Test Disease", "pathophysiology": [], "phenotypes": []},
        [row],
    )

    assert len(audit_rows) == 1
    assert (
        audit_rows[0]["issue_type"]
        == "source_phenotype_covered_only_by_broader_local_term"
    )
    assert audit_rows[0]["priority"] == "medium"


def test_genetic_disease_filter_uses_genetic_section_or_category():
    assert _is_genetic_disease({"genetic": [{"name": "GENE1"}]})
    assert _is_genetic_disease({"category": "Mendelian"})
    assert _is_genetic_disease({"category": "Rare genetic disorder"})
    assert not _is_genetic_disease({"category": "Infectious"})


def test_disease_audit_payload_records_checkpoint_metadata():
    rows = [
        {
            "issue_type": "source_phenotype_missing_locally",
            "priority": "high",
            "disease_name": "Test Disease",
        }
    ]

    payload = build_disease_audit_payload(
        slug="Test_Disease",
        source_file="Test_Disease.yaml",
        disease_id="MONDO:0000001",
        disease_name="Test Disease",
        rows=rows,
    )

    assert payload["status"] == "ok"
    assert payload["slug"] == "Test_Disease"
    assert payload["source_file"] == "Test_Disease.yaml"
    assert payload["disease_id"] == "MONDO:0000001"
    assert payload["summary"]["total_issues"] == 1
    assert payload["issues"] == rows
