"""Tests for the centralized agent-config model resolution (issue #5218)."""

import importlib.util
import re
import sys
from pathlib import Path

import pytest
import yaml

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
    assert resolver.resolve_model(config, "literature-scan") == (
        "claude-haiku-4-5-20251001"
    )
    assert resolver.resolve_model(config, "pr-shepherd") == "claude-opus-4-8"


def test_override_wins(config):
    assert (
        resolver.resolve_model(config, "literature-scan", "claude-sonnet-4-6")
        == "claude-sonnet-4-6"
    )
    # whitespace-only override is treated as no override
    assert resolver.resolve_model(config, "pr-shepherd", "  ") == "claude-opus-4-8"


def test_default_model_fallback():
    cfg = {"default_model": "claude-opus-4-8", "workflows": {"x": {}}}
    assert resolver.resolve_model(cfg, "x") == "claude-opus-4-8"


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
        "claude-haiku-4-5-20251001",
        "claude-sonnet-4-6",
        "claude-opus-4-8",
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
    return {
        path.stem: path.read_text()
        for path in WORKFLOW_DIR.glob("*.y*ml")
    }


def test_no_workflow_hardcodes_a_model_inline():
    """After centralization, no managed workflow should pin a claude-* model in
    its agent invocation; models must come from the resolve-agent-config action.

    A workflow_dispatch `model:` dropdown may still *list* models as choices, so
    only flag hardcoded models on `--model` invocation lines.
    """
    offenders = []
    # Covers every current and anticipated Claude model family (haiku/sonnet/
    # opus/fable) so a future hardcoded model is also caught.
    model_family = re.compile(r"claude-(haiku|sonnet|opus|fable)-")
    for stem, text in _workflow_texts().items():
        for line in text.splitlines():
            if "--model" in line and model_family.search(line):
                offenders.append(f"{stem}: {line.strip()}")
    assert not offenders, "hardcoded --model found (should use AGENT_MODEL):\n" + "\n".join(
        offenders
    )


def test_managed_workflows_use_the_resolver_action():
    """Every workflow in agent-config.yaml must actually source its model from
    the config: single-model workflows must `uses:` the composite action;
    matrix workflows (curation-scanner) instead call the resolver script from a
    setup job, so they're checked for that path."""
    config = yaml.safe_load(CONFIG_PATH.read_text())
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
