"""Behaviour of scripts/run_ci_gates.sh, the runner behind "Run whole-repo gates".

The runner replaced ~20 separate workflow steps, so it has to keep the two
things a step gave for free: a failing gate fails the build, and its output
can be found under its own name. It also must not trade either away for speed:
one gate failing must not stop the others running.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_ci_gates.sh"


def _run(gates: str, *args: str, tmp_path: Path | None = None, env=None):
    return subprocess.run(
        ["bash", str(RUNNER), *args],
        input=gates, capture_output=True, text=True, check=False,
        cwd=tmp_path or ROOT, env=env,
    )


def test_all_passing_gates_exit_zero_and_print_in_list_order():
    # The first gate finishes last, so completion order and list order differ.
    result = _run(
        "# a rationale comment is ignored\n"
        "Slow one :: sleep 0.4; echo slow-output\n"
        "\n"
        "Fast one :: echo fast-output\n",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    out = result.stdout
    assert "::group::PASS Slow one" in out and "::group::PASS Fast one" in out
    assert out.index("slow-output") < out.index("fast-output")
    assert out.index("::group::PASS Slow one") < out.index("slow-output")
    assert "::error" not in out
    assert "All 2 gates passed." in out


def test_a_failing_gate_fails_the_run_without_stopping_the_others(tmp_path):
    result = _run(
        "Breaks :: echo broken-output; exit 3\n"
        "Still runs :: touch ran-anyway\n",
        tmp_path=tmp_path,
    )
    assert result.returncode == 1
    assert (tmp_path / "ran-anyway").exists()
    out = result.stdout
    assert "::group::FAIL Breaks" in out and "broken-output" in out
    assert "::error title=Breaks::Breaks failed with exit code 3" in out
    assert "::group::PASS Still runs" in out
    assert "1 of 2 gate(s) failed:" in out


def test_concurrency_is_capped(tmp_path):
    # Each gate records how many gates are running when it starts. With -j 2
    # that must never exceed 2.
    gate = (
        "mkdir -p live && touch live/$$ && ls live | wc -l >> peaks && "
        "sleep 0.3 && rm live/$$"
    )
    gates = "".join(f"Gate {i} :: {gate}\n" for i in range(6))
    result = _run(gates, "-j", "2", tmp_path=tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    peaks = [int(x) for x in (tmp_path / "peaks").read_text().split()]
    assert len(peaks) == 6
    assert max(peaks) <= 2


def test_gates_see_the_step_environment():
    result = _run(
        "Reads env :: test \"$BASE_REF\" = main\n",
        env={"BASE_REF": "main", "PATH": "/usr/bin:/bin"},
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_summary_table_is_written_when_github_provides_one(tmp_path):
    summary = tmp_path / "summary.md"
    _run(
        "Good :: true\nBad :: false\n",
        env={"GITHUB_STEP_SUMMARY": str(summary), "PATH": "/usr/bin:/bin"},
    )
    text = summary.read_text()
    assert "| Good | PASS |" in text and "| Bad | FAIL |" in text


def test_malformed_lists_are_refused():
    assert _run("").returncode == 2
    assert _run("# only comments\n").returncode == 2
    assert _run("no separator here\n").returncode == 2
    assert _run("Same :: true\nSame :: true\n").returncode == 2
    assert _run("Fine :: true\n", "-j", "0").returncode == 2


def test_list_mode_prints_without_running(tmp_path):
    result = _run("Would write :: touch should-not-exist\n", "--list", tmp_path=tmp_path)
    assert result.returncode == 0
    assert result.stdout == "Would write\ttouch should-not-exist\n"
    assert not (tmp_path / "should-not-exist").exists()
