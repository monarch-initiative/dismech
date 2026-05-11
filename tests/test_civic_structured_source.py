"""Tests for the CIViC structured-database reference source."""

from __future__ import annotations

from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.civic import CivicSource


ASSERTION_HEADER = (
    "molecular_profile\tmolecular_profile_id\tdisease\tdoid\tphenotypes\t"
    "therapies\tassertion_type\tassertion_direction\tsignificance\t"
    "acmg_codes\tamp_category\tclingen_codes\tnccn_guideline\t"
    "nccn_guideline_version\tregulatory_approval\tfda_companion_test\t"
    "assertion_summary\tassertion_description\tassertion_id\t"
    "evidence_item_ids\tlast_review_date\tassertion_civic_url\t"
    "evidence_items_civic_url\tmolecular_profile_civic_url\tis_flagged\n"
)

EVIDENCE_HEADER = (
    "molecular_profile\tmolecular_profile_id\tdisease\tdoid\tphenotypes\t"
    "therapies\ttherapy_interaction_type\tevidence_type\t"
    "evidence_direction\tevidence_level\tsignificance\tevidence_statement\t"
    "citation_id\tsource_type\tasco_abstract_id\tcitation\tnct_ids\t"
    "rating\tevidence_status\tevidence_id\tvariant_origin\t"
    "last_review_date\tevidence_civic_url\tmolecular_profile_civic_url\t"
    "is_flagged\n"
)


@pytest.fixture()
def civic_source(tmp_path: Path) -> CivicSource:
    (tmp_path / "accepted_assertion_summaries.tsv").write_text(
        ASSERTION_HEADER
        + "BCR::ABL1 Fusion\t1\tChronic Myeloid Leukemia\t8552\t\t\t"
        + "Diagnostic\tSupports\tPositive\t\tTier I - Level A\t\t\t\t\t\t"
        + "BCR::ABL1 fusion is a diagnostic criterion for CML.\t"
        + "CML is characterized by the BCR::ABL1 fusion.\t188\t12589,12526\t"
        + "2025-11-18 20:46:50 UTC\t"
        + "https://civicdb.org/links/assertions/188\t"
        + "https://civicdb.org/links/evidence_items/12589,"
        + "https://civicdb.org/links/evidence_items/12526\t"
        + "https://civicdb.org/links/molecular_profiles/1\tfalse\n",
        encoding="utf-8",
    )
    (tmp_path / "accepted_clinical_evidence_summaries.tsv").write_text(
        EVIDENCE_HEADER
        + "BCR::ABL1 Fusion\t1\tChronic Myeloid Leukemia\t8552\t\t"
        + "Imatinib\t\tPredictive\tSupports\tA\tSensitivity/Response\t"
        + "Imatinib improves prognosis in patients with CML.\t20537386\t"
        + "PubMed\t\tAn et al., 2010\t\t5\taccepted\t260\tSomatic\t"
        + "2023-01-09 21:46:24 UTC\t"
        + "https://civicdb.org/links/evidence_items/260\t"
        + "https://civicdb.org/links/molecular_profiles/1\tfalse\n",
        encoding="utf-8",
    )
    return CivicSource(tmp_path)


def test_serialize_civic_assertion(civic_source: CivicSource):
    text = civic_source.serialize("CIViC_ASSERTION:188").render()

    assert 'reference_id: "CIViC_ASSERTION:188"' in text
    assert 'database: "CIViC"' in text
    assert 'content_type: "structured_record"' in text
    assert (
        "**CIViC_ASSERTION:188** — BCR::ABL1 Fusion / Chronic Myeloid Leukemia" in text
    )
    assert "- Evidence item IDs: CIViC_EID:12589, CIViC_EID:12526" in text
    assert "BCR::ABL1 fusion is a diagnostic criterion for CML." in text


def test_serialize_civic_evidence_item(civic_source: CivicSource):
    text = civic_source.serialize("CIViC_EID:260").render()

    assert 'reference_id: "CIViC_EID:260"' in text
    assert 'title: "BCR::ABL1 Fusion / Chronic Myeloid Leukemia' in text
    assert "- Citation: An et al., 2010 (PMID:20537386)" in text
    assert "Imatinib improves prognosis in patients with CML." in text


def test_civic_cache_file_passes_frontmatter_contract(
    civic_source: CivicSource, tmp_path: Path
):
    path = civic_source.write_cache_file("CIViC_EID:260", tmp_path)
    assert path.name == "CIViC_EID_260.md"
    assert check_cache_file(path) is None


@pytest.mark.parametrize(
    "identifier", ["CIViC_EID:260", "CIVIC_EID:260", "civic.eid:260"]
)
def test_serialize_accepts_evidence_identifier_variants(
    civic_source: CivicSource, identifier: str
):
    assert civic_source.serialize(identifier).reference_id == "CIViC_EID:260"


@pytest.mark.parametrize(
    "identifier", ["CIViC_ASSERTION:188", "CIVIC_ASSERTION:188", "civic.aid:188"]
)
def test_serialize_accepts_assertion_identifier_variants(
    civic_source: CivicSource, identifier: str
):
    assert civic_source.serialize(identifier).reference_id == "CIViC_ASSERTION:188"


def test_civic_serialization_is_byte_deterministic(civic_source: CivicSource):
    assert (
        civic_source.serialize("CIViC_EID:260").render()
        == civic_source.serialize("CIViC_EID:260").render()
    )
