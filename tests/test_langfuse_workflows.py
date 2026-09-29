"""Guard trace coverage as new Claude workflows and local actions are added."""

import json
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = "langfuse-observability@langfuse-observability"
MARKETPLACE = "https://github.com/langfuse/Claude-Observability-Plugin.git"
# Include multiline CLI invocations, but exclude setup commands.
CLAUDE_CLI = re.compile(r"(?m)^\s*claude\s+(?!plugin\b|mcp\b)")


def _claude_steps(steps, inherited_env, location, uv=False, plugin=False):
    """Follow local composites so coverage is checked at the actual invocation."""
    for step in steps:
        env = {**inherited_env, **step.get("env", {})}
        uses = step.get("uses", "")
        run = step.get("run", "")
        label = f"{location}/{step.get('name', uses)}"
        if uses.startswith("astral-sh/setup-uv@"):
            uv = True
        if f"claude plugin install {PLUGIN}" in run:
            assert step.get("continue-on-error") is True, label
            assert f"claude plugin marketplace add {MARKETPLACE}" in run, label
            plugin = True
        if uses.startswith("./"):
            directory = ROOT / uses
            path = next(directory.glob("action.y*ml"))
            action = yaml.safe_load(path.read_text())
            if action["runs"]["using"] == "composite":
                yield from _claude_steps(
                    action["runs"]["steps"], env, label, uv, plugin
                )
        elif uses.startswith("anthropics/claude-code-action@") or CLAUDE_CLI.search(
            run
        ):
            yield label, step, env, uv, plugin


def _workflows():
    for path in sorted((ROOT / ".github/workflows").glob("*.y*ml")):
        workflow = yaml.safe_load(path.read_text())
        invocations = []
        for job_id, job in workflow["jobs"].items():
            env = {**workflow.get("env", {}), **job.get("env", {})}
            invocations.extend(
                _claude_steps(job.get("steps", []), env, f"{path.name}/{job_id}")
            )
        if invocations:
            yield pytest.param(path.stem, invocations, id=path.stem)


@pytest.mark.parametrize("stem,invocations", list(_workflows()))
def test_claude_invocations_have_tracing(stem, invocations):
    for location, step, env, uv, plugin in invocations:
        for key in ("LANGFUSE_PUBLIC_KEY", "LANGFUSE_SECRET_KEY", "LANGFUSE_BASE_URL"):
            assert env.get(key) == "${{ secrets." + key + " }}", location
        assert uv, f"{location}: the hook needs uv before Claude starts"
        raw_tags = env["CC_LANGFUSE_TRACE_TAGS"]
        assert "\n" not in raw_tags, location
        tags = json.loads(raw_tags)
        assert f"workflow:{stem}" in tags, location
        assert "run:${{ github.run_id }}" in tags, location
        if stem == "curation-scanner":
            assert "tier:${{ matrix.effort }}" in tags, location
        if step.get("uses", "").startswith("anthropics/claude-code-action@"):
            inputs = step["with"]
            assert PLUGIN in inputs.get("plugins", "").splitlines(), location
            assert MARKETPLACE in inputs.get("plugin_marketplaces", "").splitlines(), (
                location
            )
        else:
            assert plugin, f"{location}: CLI invocation lacks a prior plugin install"
