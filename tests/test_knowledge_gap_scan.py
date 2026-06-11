"""Tests for the mechanistic knowledge-gap scan packet generator."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "knowledge_gap_scan.py"
SPEC = importlib.util.spec_from_file_location("knowledge_gap_scan", SCRIPT_PATH)
assert SPEC and SPEC.loader
knowledge_gap_scan = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = knowledge_gap_scan
SPEC.loader.exec_module(knowledge_gap_scan)


def test_build_query_is_high_recall_and_not_review_only() -> None:
    query = knowledge_gap_scan.build_query("2026-05-08", "2026-05-15")

    assert "SRC:MED" in query
    assert "FIRST_PDATE:[2026-05-08 TO 2026-05-15]" in query
    assert 'TITLE_ABS:"knowledge gap"' in query
    assert 'TITLE_ABS:"remains unclear"' in query
    assert 'TITLE_ABS:"future studies"' in query
    assert "TITLE_ABS:controversial" in query
    assert "TITLE_ABS:pathogenesis" in query
    assert "TITLE_ABS:disease" in query
    assert "review[Publication Type]" not in query
    assert "NOT (TITLE:corrigendum" in query


def test_extract_gap_signals_preserves_abbreviations_and_categories() -> None:
    abstract = (
        "Critical knowledge gaps remain regarding the direct association between "
        "H. pylori internalization and eradication failure. Future research "
        "should focus on these gaps. The mechanism remains unclear."
    )

    signals = knowledge_gap_scan.extract_gap_signals(abstract)

    assert len(signals) == 3
    assert signals[0]["sentence"].startswith("Critical knowledge gaps")
    assert "H. pylori" in signals[0]["sentence"]
    assert signals[0]["categories"] == ["explicit_gap"]
    assert signals[1]["categories"] == ["future_work"]
    assert signals[2]["categories"] == ["unclear_unknown"]


def test_build_packet_adds_gap_signals_and_candidate_disease_matches(
    tmp_path: Path,
) -> None:
    kb_dir = tmp_path / "kb"
    kb_dir.mkdir()
    (kb_dir / "Erythromelalgia.yaml").write_text(
        "name: Erythromelalgia\n",
        encoding="utf-8",
    )
    records = [
        {
            "id": "42207226",
            "source": "MED",
            "pmid": "42207226",
            "title": "Erythromelalgia: Pathophysiology and Clinical Treatment Options",
            "abstractText": (
                "Erythromelalgia is a multifaceted neurovascular pain disorder. "
                "Future investigations should more clearly outline the diagnostic "
                "criteria and develop effective targeted treatments."
            ),
            "firstPublicationDate": "2026-05-28",
        }
    ]

    packet = knowledge_gap_scan.build_packet(
        records,
        hit_count=1,
        query="SRC:MED",
        date_from="2026-05-22",
        date_to="2026-05-29",
        kb_dir=kb_dir,
        max_matches=5,
        max_signals=8,
    )

    record = packet["records"][0]
    assert record["gap_signal_score"] == 2
    assert record["gap_signal_sentences"][0]["categories"] == ["future_work"]
    assert record["candidate_existing_diseases"][0]["path"] == str(
        kb_dir / "Erythromelalgia.yaml"
    )


def test_render_markdown_includes_handoff_scope() -> None:
    markdown = knowledge_gap_scan.render_markdown(
        {
            "generated_at": "2026-06-01T00:00:00+00:00",
            "profile": "mechanistic_knowledge_gaps",
            "date_from": "2026-05-22",
            "date_to": "2026-05-29",
            "query": "SRC:MED",
            "hit_count": 0,
            "record_count": 0,
            "records": [],
        }
    )

    assert "Mechanistic Knowledge-Gap Scan Packet" in markdown
    assert "deterministic high-recall lead generator" in markdown
    assert "does not curate disease YAML files" in markdown
