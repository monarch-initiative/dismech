"""Tests for the centralized agent-config model resolution (issue #5218)."""

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from dismech.yaml_io import safe_load_path

REPO_ROOT = Path(__file__).resolve().parents[1]
ACTION_DIR = REPO_ROOT / ".github" / "actions" / "resolve-agent-config"
CONFIG_PATH = REPO_ROOT / ".github" / "agent-config.yaml"
WORKFLOW_DIR = REPO_ROOT / ".github" / "workflows"

_SPEC = importlib.util.spec_from_file_location(
    "resolve_agent_config", ACTION_DIR / "resolve_agent_config.py"
)
resolver = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = resolver
_SPEC.loader.exec_module(resolver)


@pytest.fixture
def config() -> dict:
    return resolver.load_config(CONFIG_PATH)


def test_single_model_resolves_from_config(config):
    assert resolver.resolve_model(config, "literature-scan") == "haiku"
    assert resolver.resolve_model(config, "pr-shepherd") == "opus"


def test_override_wins(config):
    assert (
        resolver.resolve_model(config, "literature-scan", "claude-sonnet-5")
        == "claude-sonnet-5"
    )
    # whitespace-only override is treated as no override
    assert resolver.resolve_model(config, "pr-shepherd", "  ") == "opus"


def test_default_model_fallback():
    cfg = {"default_model": "opus", "workflows": {"x": {}}}
    assert resolver.resolve_model(cfg, "x") == "opus"


def test_unknown_workflow_errors(config):
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(config, "does-not-exist")


def test_missing_model_and_default_errors():
    cfg = {"workflows": {"x": {}}}
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(cfg, "x")


def test_matrix_mode(config):
    matrix = resolver.resolve_matrix(config, "curation-scanner")
    assert [entry["model"] for entry in matrix] == [
        "haiku",
        "sonnet",
        "opus",
    ]
    # each entry carries the effort tier and label selector for the fan-out
    assert {entry["effort"] for entry in matrix} == {
        "low_effort",
        "medium_effort",
        "high_effort",
    }
    assert all(entry.get("selector") for entry in matrix)


def test_single_model_mode_rejects_matrix_workflow(config):
    with pytest.raises(resolver.ConfigError):
        resolver.resolve_model(config, "curation-scanner")


def test_every_config_workflow_file_exists(config):
    """Each key under workflows: must map to a real workflow file."""
    for stem in config["workflows"]:
        candidates = [WORKFLOW_DIR / f"{stem}.yml", WORKFLOW_DIR / f"{stem}.yaml"]
        assert any(c.exists() for c in candidates), f"no workflow file for '{stem}'"


def _workflow_texts() -> dict[str, str]:
    return {path.stem: path.read_text() for path in WORKFLOW_DIR.glob("*.y*ml")}


def test_no_workflow_hardcodes_a_model_inline():
    """After centralization, no managed workflow should hardcode a model in
    its agent invocation; models must come from the resolve-agent-config action.

    Only flag model invocations, not manual input examples or choices.
    """
    offenders = []
    model_argument = re.compile(
        r"--model(?:\s+|=)['\"]?(?:claude-[\w.-]+|opus|sonnet|haiku|fable|best|default)\b"
    )
    for stem, text in _workflow_texts().items():
        for line in text.splitlines():
            if model_argument.search(line):
                offenders.append(f"{stem}: {line.strip()}")
    assert not offenders, (
        "hardcoded --model found (should use AGENT_MODEL):\n" + "\n".join(offenders)
    )


def test_managed_agents_use_latest_cli_instead_of_bundled_runtime(config):
    """An alias only follows releases when the runtime carrying its mapping does."""
    setup_path = REPO_ROOT / ".github/actions/setup-claude-code/action.yml"
    setup = safe_load_path(setup_path)
    assert setup["inputs"]["version"]["default"] == "latest"
    for stem in config["workflows"]:
        path = next(WORKFLOW_DIR.glob(f"{stem}.y*ml"))
        workflow = safe_load_path(path)
        agent_count = 0
        for job in workflow["jobs"].values():
            setups = {}
            for step in job.get("steps", []):
                if step.get("uses") == "./.github/actions/setup-claude-code":
                    assert "version" not in step.get("with", {}), stem
                    setups[step["id"]] = step
                if step.get("uses", "").startswith("anthropics/claude-code-action@"):
                    agent_count += 1
                    executable = step.get("with", {}).get(
                        "path_to_claude_code_executable"
                    )
                    assert executable in {
                        "${{ steps." + step_id + ".outputs.executable }}"
                        for step_id in setups
                    }, f"{stem} bypasses the shared CLI setup"
                    setup_id = executable.split(".")[1]
                    assert setups[setup_id].get("if") == step.get("if"), stem
        assert agent_count, stem


@pytest.mark.parametrize("download_fails", [True, False])
def test_cli_setup_stops_on_download_or_install_failure(tmp_path, download_fails):
    """Never continue with an old SDK runtime after a failed latest install."""
    setup = safe_load_path(REPO_ROOT / ".github/actions/setup-claude-code/action.yml")
    script = setup["runs"]["steps"][0]["run"]
    curl = tmp_path / "curl"
    curl.write_text(
        "#!/bin/sh\nexit 22\n"
        if download_fails
        else "#!/bin/sh\nprintf '%s\\n' 'test \"$1\" = latest || exit 99' 'exit 42'\n"
    )
    curl.chmod(0o755)
    output = tmp_path / "output"
    env = {
        **os.environ,
        "PATH": str(tmp_path) + os.pathsep + os.environ["PATH"],
        "CLAUDE_INSTALL_VERSION": "latest",
        "GITHUB_OUTPUT": str(output),
        "GITHUB_PATH": str(tmp_path / "path"),
        "GITHUB_STEP_SUMMARY": str(tmp_path / "summary"),
    }
    result = subprocess.run(
        ["bash", "-c", script], env=env, capture_output=True, check=False
    )
    assert result.returncode == (22 if download_fails else 42)
    assert not output.exists(), "failed install must not publish an executable"


def test_managed_workflows_use_the_resolver_action():
    """Every workflow in agent-config.yaml must actually source its model from
    the config: single-model workflows must `uses:` the composite action;
    matrix workflows (curation-scanner) instead call the resolver script from a
    setup job, so they're checked for that path."""
    config = safe_load_path(CONFIG_PATH)
    texts = _workflow_texts()
    for stem, entry in config["workflows"].items():
        text = texts.get(stem, "")
        if isinstance(entry, dict) and entry.get("matrix"):
            assert (
                "resolve-agent-config/resolve_agent_config.py" in text
                and "--matrix" in text
            ), f"matrix workflow '{stem}' does not emit its matrix from the config"
        else:
            assert "uses: ./.github/actions/resolve-agent-config" in text, (
                f"workflow '{stem}' is in agent-config.yaml but does not `uses:` "
                f"the resolve-agent-config action"
            )


def test_duplicate_search_tool_allowlists_stay_in_sync():
    command = (REPO_ROOT / ".claude/commands/dedupe.md").read_text()
    workflow = (WORKFLOW_DIR / "claude-dedupe-issues.yml").read_text()
    command_tools = re.search(r"^allowed-tools: (.+)$", command, re.MULTILINE)
    workflow_tools = re.search(r'--allowedTools "([^"]+)"', workflow)
    assert command_tools and workflow_tools
    assert {tool.strip() for tool in command_tools[1].split(",")} == {
        tool.strip() for tool in workflow_tools[1].split(",")
    }
