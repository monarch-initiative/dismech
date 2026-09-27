"""Guards for the repository-authored rosacea innate-immune Boolean model.

The model in ``models/rosacea_innate_boolean.yaml`` is a transcription of causal
edges curated in ``kb/disorders/Rosacea.yaml``. Two things can silently rot: the
committed results can fall behind the spec, and a node rename in the KB entry can
strand the model's ``maps_to`` provenance - the same dangling-reference hazard the
pathograph itself has.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_DIR = REPO_ROOT / "models"
SPEC_PATH = MODEL_DIR / "rosacea_innate_boolean.yaml"
RESULTS_PATH = MODEL_DIR / "rosacea_innate_boolean.results.json"
RUNNER_PATH = MODEL_DIR / "rosacea_innate_boolean.py"
ENTRY_PATH = REPO_ROOT / "kb" / "disorders" / "Rosacea.yaml"

# `maps_to` prefix -> (KB section, key holding the item's name)
SECTIONS = {
    "pathophysiology": ("pathophysiology", "name"),
    "phenotypes": ("phenotypes", "name"),
    "environmental": ("environmental", "name"),
    "treatments": ("treatments", "name"),
}


def load_runner():
    spec = importlib.util.spec_from_file_location("rosacea_boolean", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def spec_dict():
    return yaml.safe_load(SPEC_PATH.read_text())


@pytest.fixture(scope="module")
def entry():
    return yaml.safe_load(ENTRY_PATH.read_text())


def test_committed_results_match_the_spec():
    """`python models/rosacea_innate_boolean.py` must be a no-op on a clean tree."""
    runner = load_runner()
    model = runner.BooleanModel(yaml.safe_load(SPEC_PATH.read_text()))
    expected = json.dumps(runner.build_results(model), indent=2, sort_keys=True) + "\n"
    assert RESULTS_PATH.read_text() == expected, (
        "committed Boolean-model results are stale; "
        "re-run `uv run python models/rosacea_innate_boolean.py`"
    )


def test_healthy_scenario_is_silent(spec_dict):
    """With no active input no phenotype may fire, or the wiring is wrong."""
    results = json.loads(RESULTS_PATH.read_text())
    assert results["scenarios"]["healthy"]["active_phenotypes"] == []


def test_every_node_maps_to_a_node_that_exists_in_the_entry(spec_dict, entry):
    """A rename in Rosacea.yaml must not silently strand the model's provenance."""
    names = {
        prefix: {item[key] for item in (entry.get(section) or [])}
        for prefix, (section, key) in SECTIONS.items()
    }
    broken = []
    for section in ("inputs", "rules", "outputs"):
        for node, body in spec_dict[section].items():
            ref = body.get("maps_to")
            if not ref:
                continue
            prefix, _, target = ref.partition("#")
            if prefix not in names:
                broken.append(f"{node}: unknown section {prefix!r}")
            elif target not in names[prefix]:
                broken.append(f"{node}: {ref} does not resolve")
    assert not broken, "Boolean model provenance is stale:\n  " + "\n  ".join(broken)


def test_intervention_targets_are_model_nodes(spec_dict):
    """Each intervention must inhibit a node the network actually has."""
    known = set(spec_dict["inputs"]) | set(spec_dict["rules"]) | set(spec_dict["outputs"])
    for name, body in spec_dict["interventions"].items():
        assert body["inhibits"] in known, f"{name} inhibits unknown node {body['inhibits']!r}"


def test_rules_only_reference_declared_nodes(spec_dict):
    """Catches a typo in a rule before it silently changes the attractor."""
    runner = load_runner()
    declared = (
        set(spec_dict["inputs"])
        | set(spec_dict["rules"])
        | set(spec_dict["outputs"])
        | set(spec_dict["interventions"])
    )
    for section in ("rules", "outputs"):
        for node, body in spec_dict[section].items():
            for token in runner.tokenize(body["rule"]):
                if token in {"and", "or", "not", "(", ")"}:
                    continue
                assert token in declared, f"rule for {node} references unknown node {token!r}"
