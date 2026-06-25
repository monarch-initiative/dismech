"""Tests for D2P phenotype-completeness audit helpers."""

from dismech.compare.d2p import (
    _is_genetic_disease,
    _match_type,
    _parse_monarch_associations,
    _resolve_disease_ref,
    build_disease_audit_payload,
    build_comparison_table,
    build_completeness_audit,
    compute_audit_summary,
    compute_venn_summary,
    extract_dismech_phenotypes,
)


def test_parse_monarch_associations_skips_explicit_zero_frequency_rows():
    items = [
        {
            "object": "HP:0000001",
            "object_label": "Zero percent phenotype",
            "primary_knowledge_source": "infores:omim",
            "has_percentage": 0.0,
            "has_count": 0,
            "has_total": 20,
            "publications": ["PMID:1"],
        },
        {
            "object": "HP:0000002",
            "object_label": "Zero count phenotype",
            "primary_knowledge_source": "infores:omim",
            "has_count": 0,
            "has_total": 10,
            "publications": ["PMID:2"],
        },
        {
            "object": "HP:0000003",
            "object_label": "Observed phenotype",
            "primary_knowledge_source": "infores:orphanet",
            "has_count": 3,
            "has_total": 10,
            "publications": ["PMID:3"],
        },
    ]

    omim_phenos, ordo_phenos = _parse_monarch_associations(items)

    assert omim_phenos == []
    assert [record["hp_id"] for record in ordo_phenos] == ["HP:0000003"]


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


def test_match_type_uses_resolver_for_narrow_and_broad_matches():
    class FakeResolver:
        def ancestors(self, term_id: str) -> set[str]:
            return {
                "HP:child": {"HP:child", "HP:parent"},
                "HP:parent": {"HP:parent"},
            }[term_id]

    resolver = FakeResolver()

    narrow_match, narrow_record = _match_type(
        "HP:parent", [{"hp_id": "HP:child"}], resolver
    )
    assert narrow_match == "narrow:HP:child"
    assert narrow_record == {"hp_id": "HP:child"}

    broad_match, broad_record = _match_type(
        "HP:child", [{"hp_id": "HP:parent"}], resolver
    )
    assert broad_match == "broad:HP:parent"
    assert broad_record == {"hp_id": "HP:parent"}


def test_compute_venn_summary_counts_all_source_combinations():
    rows = [
        {"dismech": "exact", "omim": "-", "ordo": "-"},
        {"dismech": "-", "omim": "exact", "ordo": "-"},
        {"dismech": "-", "omim": "-", "ordo": "exact"},
        {"dismech": "exact", "omim": "exact", "ordo": "-"},
        {"dismech": "exact", "omim": "-", "ordo": "exact"},
        {"dismech": "-", "omim": "exact", "ordo": "exact"},
        {"dismech": "exact", "omim": "exact", "ordo": "exact"},
    ]

    assert compute_venn_summary(rows) == {
        "dismech_only": 1,
        "omim_only": 1,
        "ordo_only": 1,
        "dismech_omim": 1,
        "dismech_ordo": 1,
        "omim_ordo": 1,
        "all_three": 1,
        "total": 7,
    }


def test_resolve_disease_ref_uses_dismech_resolution_without_phenoagent():
    slug, path = _resolve_disease_ref("ANK2 Ankyrin-B Syndrome")

    assert slug == "ANK2_Ankyrin_B_Syndrome"
    assert path.name == "ANK2_Ankyrin_B_Syndrome.yaml"


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
