"""Tests for the weekly literature-scan packet generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "literature_scan.py"
SPEC = importlib.util.spec_from_file_location("literature_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
literature_scan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = literature_scan
SPEC.loader.exec_module(literature_scan)


def test_build_query_is_pubmed_title_focused_and_not_cancer_hardwired() -> None:
    query = literature_scan.build_query("2026-05-08", "2026-05-15")

    assert "SRC:MED" in query
    assert "FIRST_PDATE:[2026-05-08 TO 2026-05-15]" in query
    assert "TITLE:pathogenesis" in query
    assert "TITLE:treatment" in query
    assert "NOT (TITLE:corrigendum" in query
    assert "cancer" not in query.lower()


def test_load_disease_terms_and_references(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    (kb_dir / "Wilsons_Disease.yaml").write_text(
        """
name: Wilson Disease
synonyms:
- Hepatolenticular degeneration
pathophysiology:
- name: Copper Accumulation
  evidence:
  - reference: PMID:12345
    snippet: copper
""".strip()
        + "\n",
        encoding="utf-8",
    )

    terms, references_by_path = literature_scan.load_disease_terms(kb_dir)

    labels = {term.label for term in terms}
    assert "Wilson Disease" in labels
    assert "Hepatolenticular degeneration" in labels
    assert references_by_path[str(kb_dir / "Wilsons_Disease.yaml")] == {"PMID:12345"}


def test_match_publication_marks_already_cited(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    yaml_path = kb_dir / "Wilsons_Disease.yaml"
    yaml_path.write_text(
        """
name: Wilson Disease
pathophysiology:
- name: Copper Transport Defect
  evidence:
  - reference: PMID:42126658
    snippet: ATP7B
""".strip()
        + "\n",
        encoding="utf-8",
    )
    terms, references_by_path = literature_scan.load_disease_terms(kb_dir)
    publication = literature_scan.Publication(
        id="42126658",
        source="MED",
        pmid="42126658",
        doi="10.1007/example",
        title="Exploring a compound heterozygous variant in ATP7B associated with Wilson disease",
        journal="Example Journal",
        publication_date="2026-05-13",
        authors="A. Author",
        abstract="This paper reports Wilson disease in an Iranian family.",
        europe_pmc_url="https://europepmc.org/article/MED/42126658",
        pubmed_url="https://pubmed.ncbi.nlm.nih.gov/42126658/",
    )

    matches = literature_scan.match_publication(
        publication,
        terms,
        references_by_path,
        max_matches=5,
    )

    assert matches
    assert matches[0]["path"] == str(yaml_path)
    assert matches[0]["already_cited"] is True


def test_build_packet_includes_candidate_existing_diseases(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    (kb_dir / "Maple_Syrup_Urine_Disease.yaml").write_text(
        "name: Maple Syrup Urine Disease\n",
        encoding="utf-8",
    )
    records = [
        {
            "id": "42127902",
            "source": "MED",
            "pmid": "42127902",
            "title": "Trial-ready external controls for gene therapy in maple syrup urine disease",
            "abstractText": "A cohort relevant to maple syrup urine disease.",
            "firstPublicationDate": "2026-05-12",
        }
    ]

    packet = literature_scan.build_packet(
        records,
        hit_count=1,
        query="SRC:MED",
        date_from="2026-05-08",
        date_to="2026-05-15",
        profile="mechanisms",
        kb_dir=kb_dir,
        max_matches=5,
    )

    matches = packet["records"][0]["candidate_existing_diseases"]
    assert matches[0]["path"] == str(kb_dir / "Maple_Syrup_Urine_Disease.yaml")
