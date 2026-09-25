"""Guards for the repository-authored radial neuronal migration agent-based model.

The model in ``models/neuronal_migration_abm.yaml`` is a transcription of the
causal chain curated in
``kb/modules/microtubule_dependent_neuronal_migration_failure.yaml``. The same
two things can silently rot here as in the rosacea Boolean model: the committed
results can fall behind the spec, and a node rename in the module can strand
the model's ``maps_to`` provenance. Two further guards are specific to a
stochastic model: the wild-type scenario must lay the cortex down inside-out,
and a stronger perturbation must never land more neurons in the plate.
"""

from __future__ import annotations

import importlib.util
import json
import pathlib
import sys

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL_DIR = REPO_ROOT / "models"
SPEC_PATH = MODEL_DIR / "neuronal_migration_abm.yaml"
RESULTS_PATH = MODEL_DIR / "neuronal_migration_abm.results.json"
RUNNER_PATH = MODEL_DIR / "neuronal_migration_abm.py"
MODULE_PATH = (
    REPO_ROOT
    / "kb"
    / "modules"
    / "microtubule_dependent_neuronal_migration_failure.yaml"
)

# `maps_to` prefix -> (KB section, key holding the item's name)
SECTIONS = {
    "pathophysiology": ("pathophysiology", "name"),
    "treatments": ("treatments", "name"),
}


def load_runner():
    spec = importlib.util.spec_from_file_location("neuronal_migration_abm", RUNNER_PATH)
    module = importlib.util.module_from_spec(spec)
    # Registered before execution: the runner's dataclasses use postponed
    # annotations, which dataclasses resolves through sys.modules.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def spec_dict():
    return yaml.safe_load(SPEC_PATH.read_text())


@pytest.fixture(scope="module")
def module_entry():
    return yaml.safe_load(MODULE_PATH.read_text())


@pytest.fixture(scope="module")
def results():
    return json.loads(RESULTS_PATH.read_text())


def test_committed_results_match_the_spec():
    """`python models/neuronal_migration_abm.py` must be a no-op on a clean tree."""
    runner = load_runner()
    expected = (
        json.dumps(runner.build_results(runner.load_spec()), indent=2, sort_keys=True)
        + "\n"
    )
    assert RESULTS_PATH.read_text() == expected, (
        "committed agent-based-model results are stale; "
        "re-run `uv run python models/neuronal_migration_abm.py`"
    )


def test_wild_type_lays_the_cortex_down_inside_out(results):
    """With no perturbation every neuron settles and birth order is laminar order."""
    wt = results["scenarios"]["wild_type"]["readouts"]
    assert wt["cortical_plate_fraction"] == 1.0
    assert wt["ectopic_fraction"] == 0.0
    assert wt["lamination_fidelity"] >= 0.99
    assert wt["pattern"] == "normal"


def test_stronger_perturbation_never_lands_more_neurons_in_the_plate(results):
    """The slowed_nucleokinesis rule is monotone in the perturbation, so its
    consequence must be too, up to the sampling noise of a 600-agent run."""
    for name in ("perturbation_no_arrest", "perturbation_with_arrest"):
        rows = results["sweeps"][name]["rows"]
        fractions = [row["cortical_plate_fraction"] for row in rows]
        for earlier, later in zip(fractions, fractions[1:]):
            assert later <= earlier + 0.02, (
                f"{name}: plate fraction rises along the sweep: {fractions}"
            )


def test_band_requires_mosaicism(results):
    """A heterotopic band appears only when unaffected neurons can build a
    cortex above the arrested affected ones, never from a constitutional
    perturbation. This is the model's central implication and the reason the
    `affected_fraction` input exists."""
    constitutional = results["sweeps"]["perturbation_with_arrest"]["rows"]
    assert all(row["pattern"] != "band_heterotopia" for row in constitutional)
    mosaic = results["sweeps"]["affected_fraction_severe"]["rows"]
    assert any(row["pattern"] == "band_heterotopia" for row in mosaic)
    assert (
        results["scenarios"]["mosaic_severe"]["readouts"]["pattern"]
        == "band_heterotopia"
    )


def test_every_node_maps_to_a_node_that_exists_in_the_module(spec_dict, module_entry):
    """A rename in the module must not silently strand the model's provenance."""
    names = {
        prefix: {item[key] for item in (module_entry.get(section) or [])}
        for prefix, (section, key) in SECTIONS.items()
    }
    broken = []
    holders = []
    holders += list(spec_dict["agents"].items())
    holders += list(spec_dict["inputs"].items())
    holders += list(spec_dict["rules"].items())
    holders += list(spec_dict["interventions"].items())
    for node, body in holders:
        ref = body.get("maps_to") if isinstance(body, dict) else None
        if not ref:
            continue
        prefix, _, target = ref.partition("#")
        if prefix not in names:
            broken.append(f"{node}: unknown section {prefix!r}")
        elif target not in names[prefix]:
            broken.append(f"{node}: {ref} does not resolve")
    assert not broken, "agent-based-model provenance is stale:\n  " + "\n  ".join(
        broken
    )


def test_the_one_uncurated_rule_is_labelled_as_such(spec_dict):
    """Inside-out settling is a background assumption, and must stay declared
    as one rather than acquiring a fabricated provenance line."""
    settling = spec_dict["rules"]["inside_out_settling"]
    assert settling["provenance"] == "background_assumption"
    for name, rule in spec_dict["rules"].items():
        if name == "inside_out_settling":
            continue
        assert isinstance(rule["provenance"], list) and rule["provenance"], name


def test_scenario_and_sweep_inputs_are_declared(spec_dict):
    """Catches a typo in a scenario key before it silently falls back to a default."""
    declared = set(spec_dict["inputs"])
    for name, body in spec_dict["scenarios"].items():
        unknown = set(body) - declared - {"description"}
        assert not unknown, f"scenario {name} sets undeclared inputs {sorted(unknown)}"
    for name, body in spec_dict["sweeps"].items():
        assert body["vary"] in declared, (
            f"sweep {name} varies undeclared input {body['vary']!r}"
        )
        unknown = set(body.get("fixed", {})) - declared
        assert not unknown, f"sweep {name} fixes undeclared inputs {sorted(unknown)}"
