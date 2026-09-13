"""Behaviour of scripts/run_term_validator.sh, exercised against a fake ``uv``.

The wrapper wraps ``linkml-term-validator validate-data`` and turns WARN
output or a missing success line into a non-zero exit. It must not spend an
extra interpreter start probing ``--help`` on every call (dismech#11004).
"""

from __future__ import annotations

import os
import stat
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
WRAPPER = ROOT / "scripts" / "run_term_validator.sh"
MAIN_WORKFLOW = ROOT / ".github" / "workflows" / "main.yaml"


def test_wrapper_does_not_probe_help() -> None:
    """No per-call capability probe: one validator start per validate-data call."""
    code = "\n".join(
        line
        for line in WRAPPER.read_text().splitlines()
        if not line.lstrip().startswith("#")
    )
    assert "--help" not in code
    assert code.count("uv run linkml-term-validator") == 2, (
        "expected exactly one exec passthrough and one validate-data invocation"
    )


def _fake_uv(tmp_path: Path, stdout: str, exit_code: int = 0) -> Path:
    """Write a ``uv`` shim that logs its argv and prints canned output."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    log = tmp_path / "calls.log"
    shim = bin_dir / "uv"
    shim.write_text(
        "#!/usr/bin/env bash\n"
        f'printf \'%s\\n\' "$*" >> "{log}"\n'
        f"cat <<'CANNED'\n{stdout}\nCANNED\n"
        f"exit {exit_code}\n"
    )
    shim.chmod(shim.stat().st_mode | stat.S_IXUSR)
    return log


def _run(tmp_path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ, PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}")
    return subprocess.run(
        [str(WRAPPER), *args], capture_output=True, text=True, env=env, check=False
    )


@pytest.mark.parametrize(
    ("stdout", "exit_code", "expected"),
    [
        ("✅ Validation passed", 0, 0),
        ("✅ All 2 files passed validation", 0, 0),
        ("⚠️  WARN: Label mismatch for 'HP:1'\n✅ Validation passed", 0, 1),
        ("❌ ERROR: Term 'HP:1' not found in ontology", 1, 1),
        ("something else entirely", 0, 1),
    ],
    ids=["single-pass", "multi-pass", "warn-is-fatal", "error-exit", "no-success-line"],
)
def test_validate_data_exit_codes(
    tmp_path: Path, stdout: str, exit_code: int, expected: int
) -> None:
    log = _fake_uv(tmp_path, stdout, exit_code)
    result = _run(tmp_path, "validate-data", "x.yaml", "-t", "Disease")
    assert result.returncode == expected, result.stdout + result.stderr
    assert stdout.splitlines()[0] in result.stdout
    calls = log.read_text().splitlines()
    assert calls == ["run linkml-term-validator validate-data x.yaml -t Disease"]


def test_other_subcommands_pass_straight_through(tmp_path: Path) -> None:
    log = _fake_uv(tmp_path, "usage", 3)
    result = _run(tmp_path, "some-other-command", "--flag")
    assert result.returncode == 3
    assert log.read_text().splitlines() == [
        "run linkml-term-validator some-other-command --flag"
    ]


def test_no_arguments_prints_usage_and_exits_2(tmp_path: Path) -> None:
    log = _fake_uv(tmp_path, "should not run")
    result = _run(tmp_path)
    assert result.returncode == 2
    assert "Usage:" in result.stderr
    assert not log.exists()


def test_wrapper_edits_trigger_the_pytest_lane() -> None:
    """A PR touching only the wrapper must still run this file (#11479 review)."""
    assert "- 'scripts/run_term_validator.sh'" in MAIN_WORKFLOW.read_text()
