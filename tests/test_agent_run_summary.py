"""Tests for the agent run-report extractor.

`.github/actions/agent-run-summary` exists because claude-code-action v1 has no
`result` output — every workflow that wrote `${{ steps.<id>.outputs.result }}`
was rendering an empty fenced block. The report has to be read out of the
`execution_file` stream log instead.
"""

import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTION_DIR = REPO_ROOT / ".github" / "actions" / "agent-run-summary"

_SPEC = importlib.util.spec_from_file_location(
    "extract_result_mod", ACTION_DIR / "extract_result.py"
)
assert _SPEC is not None and _SPEC.loader is not None
mod = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = mod
_SPEC.loader.exec_module(mod)

extract_result = mod.extract_result


def test_returns_the_last_result_events_report():
    events = [
        {"type": "system", "subtype": "init"},
        {"type": "result", "subtype": "success", "result": "first"},
        {
            "type": "result",
            "subtype": "success",
            "result": "Scanned 4 PRs; merged #123.",
            "num_turns": 12,
            "total_cost_usd": 0.42,
        },
    ]
    out = extract_result(events)
    assert "Scanned 4 PRs; merged #123." in out
    assert "first" not in out
    assert "turns=12" in out


def test_reports_errors_from_a_failed_run():
    events = [
        {
            "type": "result",
            "subtype": "error_during_execution",
            "is_error": True,
            "errors": ["usage limit reached", "aborted"],
        }
    ]
    out = extract_result(events)
    assert "usage limit reached" in out
    assert "aborted" in out


def test_names_the_quota_case_when_there_is_no_result_event():
    out = extract_result([{"type": "system", "subtype": "init"}])
    assert "did not complete" in out
    assert "usage limit" in out


def test_explains_a_result_event_with_no_report():
    out = extract_result([{"type": "result", "subtype": "success", "is_error": False}])
    assert "no closing report" in out


def test_reads_a_real_execution_file(tmp_path):
    path = tmp_path / "execution.json"
    path.write_text(
        json.dumps([{"type": "result", "subtype": "success", "result": "done"}])
    )
    assert mod.main(["extract_result.py", str(path)]) == 0
