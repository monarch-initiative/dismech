"""Unit tests for the deterministic duplicate-claim guard (issue #16202).

Covers the pure functions only — the MONDO-ID extraction, the same-MONDO
grouping, the lowest-number keeper rule, and the exact-match used by the
pre-PR check. The `gh`-calling functions are not exercised here.

Both modules live outside any package (`.github/scripts/` and `scripts/`), so
they are loaded by path.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


guard = _load(ROOT / ".github/scripts/claim_dedupe_guard.py", "claim_dedupe_guard")
preflight = _load(ROOT / "scripts/preflight_claim_conflict.py", "preflight_claim_conflict")


def test_mondo_of_extracts_the_id():
    assert guard.mondo_of("Curate complex lethal osteochondrodysplasia (MONDO:0014821)") == "MONDO:0014821"
    assert guard.mondo_of("curate peripartum cardiomyopathy") is None


def test_groups_by_mondo_groups_only_keyed_titles():
    claims = [
        {"number": 1, "title": "A (MONDO:0000001)"},
        {"number": 2, "title": "B (MONDO:0000001)"},
        {"number": 3, "title": "C (MONDO:0000002)"},
        {"number": 4, "title": "unkeyed title"},
    ]
    groups = guard.groups_by_mondo(claims)
    assert set(groups) == {"MONDO:0000001", "MONDO:0000002"}
    assert [c["number"] for c in groups["MONDO:0000001"]] == [1, 2]


def test_keeper_is_lowest_number_regardless_of_order():
    members = [{"number": 16098}, {"number": 16096}, {"number": 16100}]
    keeper, dups = guard.keeper_and_duplicates(members)
    assert keeper == 16096
    assert sorted(d["number"] for d in dups) == [16098, 16100]


def test_keeper_is_stable_under_reordering():
    # The two parallel runs the guard serializes must agree on the loser.
    a = [{"number": 16096}, {"number": 16098}]
    b = list(reversed(a))
    assert guard.keeper_and_duplicates(a)[0] == guard.keeper_and_duplicates(b)[0] == 16096


def test_already_flagged_reads_labels():
    assert guard.already_flagged({"labels": [{"name": "duplicate-claim"}]}) is True
    assert guard.already_flagged({"labels": [{"name": "claim"}]}) is False
    assert guard.already_flagged({}) is False


@pytest.mark.parametrize(
    "text, mondo, expected",
    [
        ("Curate X (MONDO:0014821)", "MONDO:0014821", True),
        ("Curate X (MONDO:00148210)", "MONDO:0014821", False),  # exact, not prefix
        ("Curate X (MONDO:0014821) in branch", "MONDO:0014821", True),
        ("no id here", "MONDO:0014821", False),
        ("", "MONDO:0014821", False),
    ],
)
def test_preflight_has_mondo_is_exact(text, mondo, expected):
    assert preflight.has_mondo(text, mondo) is expected
