"""Every place that runs ruff must use the same, pinned version (#9964).

CI used to run a bare ``uvx ruff check .``, which resolves to the newest ruff
release. Each release that changed ruff's default rules turned every open PR
red at once, PRs that touched no Python included. The version now lives in
three places that have to agree: the ``ruff==`` dev dependency (what
``uv run ruff`` and CI use), ``[tool.ruff] required-version``, and the
ruff-pre-commit ``rev``. This test fails when one is bumped without the others.
"""

from __future__ import annotations

import re
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def _pyproject() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text())


def _dev_dependency_version() -> str:
    pins = [
        dep
        for dep in _pyproject()["dependency-groups"]["dev"]
        if re.match(r"ruff\b", dep)
    ]
    assert len(pins) == 1, f"expected exactly one ruff dev dependency, found {pins}"
    match = re.fullmatch(r"ruff==(\S+)", pins[0])
    assert match, f"ruff dev dependency must be an exact == pin, got {pins[0]!r}"
    return match.group(1)


def test_required_version_matches_dev_dependency():
    required = _pyproject()["tool"]["ruff"]["required-version"]
    assert required == f"=={_dev_dependency_version()}"


def test_pre_commit_rev_matches_dev_dependency():
    config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
    revs = [
        repo["rev"]
        for repo in config["repos"]
        if repo.get("repo", "").endswith("astral-sh/ruff-pre-commit")
    ]
    assert revs == [f"v{_dev_dependency_version()}"]


def test_workflows_do_not_run_an_unpinned_ruff():
    offenders = []
    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.y*ml")):
        for lineno, line in enumerate(workflow.read_text().splitlines(), 1):
            # `uvx ruff` (no @version) resolves to the newest release.
            if re.search(r"\buvx\s+ruff(?!@)\b", line):
                offenders.append(f"{workflow.name}:{lineno}: {line.strip()}")
    assert not offenders, "use `uv run ruff`, which is pinned:\n" + "\n".join(offenders)
