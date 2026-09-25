"""Guards for the `ci_step_twin` marker (see tests/conftest.py).

A twin is deselected from the pytest step in main.yaml because the same job
runs the same check as an ungated step. That is only sound while the step is
still there, still ungated, and still running the command the marker names.
These tests hold that line: delete or path-gate the step, and the twin fails
here until it is either restored to the lane or the step comes back.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
MAIN = WORKFLOWS / "main.yaml"
ENV = "DISMECH_SKIP_CI_STEP_TWINS"

TWIN_RE = re.compile(
    r'^@pytest\.mark\.ci_step_twin\("(?P<command>[^"]+)"\)\n'
    r"(?:@.*\n)*"
    r"def (?P<name>test_\w+)\(",
    re.MULTILINE,
)


def _twins() -> list[tuple[str, str, str]]:
    found = []
    for path in sorted((ROOT / "tests").glob("test_*.py")):
        for match in TWIN_RE.finditer(path.read_text(encoding="utf-8")):
            found.append((path.name, match["name"], match["command"]))
    return found


def _main_steps() -> list[dict]:
    workflow = yaml.safe_load(MAIN.read_text(encoding="utf-8"))
    return workflow["jobs"]["test"]["steps"]


def _command_lines(run: str) -> list[str]:
    """The lines of a run: block that execute, not the ones that explain."""
    return [
        line.strip()
        for line in run.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def test_twins_exist():
    # A regex that silently matched nothing would make every test below vacuous.
    assert len(_twins()) >= 9


def test_every_twin_names_an_ungated_step_in_main():
    ungated = [
        line
        for step in _main_steps()
        if "if" not in step
        for line in _command_lines(str(step.get("run", "")))
    ]
    missing = [
        f"{file}::{name} -> {command!r}"
        for file, name, command in _twins()
        if not any(command in line for line in ungated)
    ]
    assert not missing, (
        "these tests are deselected from the pytest step as twins of a main.yaml "
        "step, but no ungated step runs their command any more. Restore the "
        "step, or drop the ci_step_twin marker so the test runs in the lane:\n  "
        + "\n  ".join(missing)
    )


def test_only_main_yaml_pytest_step_deselects_twins():
    pytest_steps = [
        step
        for step in _main_steps()
        if str(step.get("run", "")).startswith("just test-python-code")
    ]
    assert len(pytest_steps) == 1
    assert str(pytest_steps[0].get("env", {}).get(ENV)) == "1"

    # Every other workflow keeps the twins. The nightly sweep in particular is
    # the backstop that still runs them against main.
    for path in sorted(WORKFLOWS.glob("*.y*ml")):
        if path == MAIN:
            continue
        assert ENV not in path.read_text(encoding="utf-8"), (
            f"{path.name} must not deselect ci_step_twin tests"
        )


def test_env_var_deselects_twins_and_nothing_else():
    target = "tests/test_folded_hyphens.py"

    def collected(skip: bool) -> set[str]:
        env = {k: v for k, v in os.environ.items() if k != ENV}
        if skip:
            env[ENV] = "1"
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "--collect-only", "-q",
             "-p", "no:cacheprovider", target],
            capture_output=True, text=True, cwd=ROOT, env=env, check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        return {line for line in result.stdout.splitlines() if "::" in line}

    everything, lane = collected(False), collected(True)
    twin = f"{target}::test_no_folded_scalar_hyphen_splits"
    assert twin in everything
    assert everything - lane == {twin}
