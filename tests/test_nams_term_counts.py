"""Tests for scripts/nams_term_counts.py (no network)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import httpx
import pytest

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "nams_term_counts.py"
_spec = importlib.util.spec_from_file_location("nams_term_counts", SCRIPT_PATH)
nams = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = nams  # dataclasses look the module up here
_spec.loader.exec_module(nams)


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


def test_reported_counts_match_the_report_table():
    reported = {
        t.label: t.reported_count for t in nams.TERMS if t.reported_count is not None
    }
    assert len(reported) == 22
    assert reported["in silico"] == 107016
    assert reported["FDA Modernization Act"] == 136


def test_labels_are_unique():
    labels = [t.label for t in nams.TERMS]
    assert len(labels) == len(set(labels))


def test_pubmed_count_reads_esearch_count():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["term"] == '"in silico"[tiab]'
        assert request.url.params["retmax"] == "0"
        return httpx.Response(200, json={"esearchresult": {"count": "123"}})

    with _client(handler) as client:
        assert nams.pubmed_count(client, '"in silico"[tiab]') == 123


def test_pubmed_count_raises_on_query_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"esearchresult": {"ERROR": "bad query"}})

    with _client(handler) as client, pytest.raises(RuntimeError, match="bad query"):
        nams.pubmed_count(client, "x")


def test_build_rows_computes_change_and_leaves_new_terms_blank():
    terms = [
        nams.Term("old", "q1", 200, "report"),
        nams.Term("new", "q2", None, "added"),
    ]
    rows = nams.build_rows(terms, [250, 7], "2026-10-19")
    assert rows[0]["change"] == "+50"
    assert rows[0]["percent_change"] == "+25.0"
    assert rows[1]["reported_count"] == ""
    assert rows[1]["change"] == ""
    assert rows[1]["current_count"] == "7"
