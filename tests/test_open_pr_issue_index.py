"""Tests for the open-PR issue index the curation scanner uses (issue #5105).

Covers the pure parsing and indexing, the `--check` exit code with the `gh`
call stubbed out, and the scanner workflow's wiring. The script lives outside
any package (`.github/scripts/`), so it is loaded by path.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github/scripts/open_pr_issue_index.py"
SCANNER = ROOT / ".github/workflows/curation-scanner.yml"


def _load():
    spec = importlib.util.spec_from_file_location("open_pr_issue_index", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


index = _load()


@pytest.mark.parametrize(
    "body, expected",
    [
        ("Closes #7362", {7362}),
        ("fixes: #12", {12}),
        ("Resolved #5, and Fixed #6", {5, 6}),
        # The phrasing agent PRs used on #12842, which GitHub does not link.
        ("Addresses knowledge gap #12842", set()),
        ("Addresses #12842", {12842}),
        # Umbrella issues: a partial PR must leave the issue selectable.
        ("Refs #13103 (the issue stays open)", set()),
        ("Related: #4990, see also #360", set()),
        # Cross-repo references are not this repo's issues.
        ("Closes monarch-initiative/mondo#10836", set()),
        ("prefix#12 and closes#", set()),
    ],
)
def test_referenced_issues_reads_closing_and_addressing_keywords(body, expected):
    assert index.referenced_issues({"number": 1, "title": "", "body": body}) == expected


def test_referenced_issues_reads_the_title_and_ignores_self_and_null_body():
    pr = {"number": 99, "title": "Curate X (closes #7)", "body": None}
    assert index.referenced_issues(pr) == {7}
    assert (
        index.referenced_issues({"number": 99, "title": "", "body": "Closes #99"})
        == set()
    )


def test_build_index_groups_every_pr_per_issue_in_order():
    prs = [
        {"number": 8117, "title": "", "body": "Closes #7362"},
        {"number": 7989, "title": "", "body": "Closes #7362"},
        {"number": 7913, "title": "", "body": "Addresses #7372"},
        {"number": 16362, "title": "", "body": "Refs #13103"},
    ]
    assert index.build_index(prs) == {7362: [7989, 8117], 7372: [7913]}


def _stub(monkeypatch, prs):
    monkeypatch.setattr(index, "fetch_open_prs", lambda repo: prs)


def test_check_exits_1_when_an_open_pr_holds_the_issue(monkeypatch, capsys):
    _stub(monkeypatch, [{"number": 13537, "title": "", "body": "Closes #12842"}])
    assert index.main(["--repo", "o/r", "--check", "12842"]) == 1
    assert "#13537" in capsys.readouterr().out
    assert index.main(["--repo", "o/r", "--check", "1"]) == 0


def test_check_can_exclude_the_pr_being_updated(monkeypatch):
    _stub(monkeypatch, [{"number": 13537, "title": "", "body": "Closes #12842"}])
    assert (
        index.main(["--repo", "o/r", "--check", "12842", "--exclude-pr", "13537"]) == 0
    )


def test_list_prints_space_separated_issue_numbers(monkeypatch, capsys):
    _stub(
        monkeypatch,
        [
            {"number": 3, "title": "", "body": "Closes #20"},
            {"number": 4, "title": "", "body": "Fixes #10"},
        ],
    )
    assert index.main(["--repo", "o/r", "--list"]) == 0
    assert capsys.readouterr().out.strip() == "10 20"


def _scanner_job():
    workflow = yaml.safe_load(SCANNER.read_text())
    return workflow["jobs"]["curation-scan"]


def test_scanner_computes_the_index_before_the_agent_runs():
    steps = _scanner_job()["steps"]
    ids = [s.get("id") for s in steps]
    assert "open-pr-issues" in ids
    assert ids.index("open-pr-issues") < ids.index("curation-scanner")
    step = steps[ids.index("open-pr-issues")]
    assert "open_pr_issue_index.py --list" in step["run"]


def test_scanner_prompt_forbids_listed_issues_and_requires_the_check():
    steps = _scanner_job()["steps"]
    prompt = next(s for s in steps if s.get("id") == "curation-scanner")["with"][
        "prompt"
    ]
    assert "ISSUES WITH AN OPEN PR: ${{ steps.open-pr-issues.outputs.issues" in prompt
    assert "Never select\n            an issue on that list" in SCANNER.read_text()
    assert "open_pr_issue_index.py --check <issue-number>" in prompt


def test_scanner_runs_are_not_cancelled_mid_flight():
    assert _scanner_job()["concurrency"]["cancel-in-progress"] is False
