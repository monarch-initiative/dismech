"""Tests for the preprint scan packet generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "preprint_scan.py"
SPEC = importlib.util.spec_from_file_location("preprint_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
preprint_scan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = preprint_scan
SPEC.loader.exec_module(preprint_scan)


def test_build_query_scans_preprints_without_fulltext_filter() -> None:
    query = preprint_scan.build_query("2026-05-08", "2026-05-15")

    # Preprint source, not the PubMed/MEDLINE source the sibling scanners use.
    assert "SRC:PPR" in query
    assert "SRC:MED" not in query
    # No HAS_FT filter: it would empty a weekly window (ingestion lag).
    assert "HAS_FT" not in query
    assert "FIRST_PDATE:[2026-05-08 TO 2026-05-15]" in query
    assert "TITLE:pathogenesis" in query
    assert "NOT (TITLE:corrigendum" in query


def test_build_packet_emits_ppr_reference_and_disease_matches(tmp_path: Path) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    (kb_dir / "Fragile_X_Syndrome.yaml").write_text(
        "name: Fragile X Syndrome\n",
        encoding="utf-8",
    )
    records = [
        {
            "id": "PPR1253390",
            "source": "PPR",
            "doi": "10.64898/2026.06.12.731901",
            "title": "FMR1 gene therapy in Fragile X Syndrome restores inhibition",
            "journalTitle": "bioRxiv",
            "abstractText": (
                "Fragile X Syndrome is caused by FMR1 silencing. Gene therapy "
                "restored activity-driven inhibition in a disease model."
            ),
            "firstPublicationDate": "2026-06-12",
        }
    ]

    packet = preprint_scan.build_packet(
        records,
        hit_count=1,
        query="SRC:PPR",
        date_from="2026-06-08",
        date_to="2026-06-15",
        profile="mechanisms",
        kb_dir=kb_dir,
        max_matches=5,
    )

    record = packet["records"][0]
    assert record["is_preprint"] is True
    assert record["ppr_id"] == "PPR1253390"
    assert record["suggested_reference"] == "PPR:PPR1253390"
    assert record["pmid"] == ""  # preprints carry no PMID
    assert record["candidate_existing_diseases"][0]["path"] == str(
        kb_dir / "Fragile_X_Syndrome.yaml"
    )
    assert packet["source"] == "preprints"


def test_build_packet_marks_already_cited_when_ppr_reference_present(
    tmp_path: Path,
) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    (kb_dir / "Fragile_X_Syndrome.yaml").write_text(
        "name: Fragile X Syndrome\n"
        "evidence:\n"
        "- reference: PPR:PPR1253390\n",
        encoding="utf-8",
    )
    records = [
        {
            "id": "PPR1253390",
            "source": "PPR",
            "doi": "10.64898/2026.06.12.731901",
            "title": "FMR1 gene therapy in Fragile X Syndrome restores inhibition",
            "abstractText": "Fragile X Syndrome FMR1 gene therapy.",
            "firstPublicationDate": "2026-06-12",
        }
    ]

    packet = preprint_scan.build_packet(
        records,
        hit_count=1,
        query="SRC:PPR",
        date_from="2026-06-08",
        date_to="2026-06-15",
        profile="mechanisms",
        kb_dir=kb_dir,
        max_matches=5,
    )

    match = packet["records"][0]["candidate_existing_diseases"][0]
    assert match["already_cited"] is True


def test_render_markdown_flags_not_peer_reviewed() -> None:
    markdown = preprint_scan.render_markdown(
        {
            "generated_at": "2026-06-01T00:00:00+00:00",
            "profile": "mechanisms",
            "date_from": "2026-05-22",
            "date_to": "2026-05-29",
            "query": "SRC:PPR",
            "hit_count": 0,
            "record_count": 0,
            "records": [],
        }
    )

    assert "Weekly Preprint Scan Packet" in markdown
    assert "NOT peer-reviewed" in markdown
    assert "just fetch-reference PPR:<id>" in markdown
    assert "does not curate disease YAML files" in markdown
