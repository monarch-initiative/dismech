"""Tests for the dismech-perturb results artifact and its rendering."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from dismech.perturb.results_export import (
    DEFAULT_OUTPUT_DIR,
    ROUNDING_DECIMALS,
    _fold_change,
    _round,
    build_observables,
    build_thresholds,
    load_results,
    run_config,
    threshold_kind,
)
from dismech.perturb.simulate import load_model_config

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
RESULTS_DIR = REPO_ROOT / DEFAULT_OUTPUT_DIR


def _committed():
    return sorted(RESULTS_DIR.glob("*.json"))


def test_fold_change_guards_against_a_zero_baseline():
    assert _fold_change(10.0, 5.0) == 2.0
    assert _fold_change(1.0, 0.0) is None


def test_rounding_collapses_integrator_noise_to_zero():
    # The Topp beta-cell-collapse scenarios land at ~1e-300; rounding makes
    # that a stable 0.0 instead of a value that churns the committed diff.
    assert _round(4.55e-303) == 0.0
    assert _round(None) is None
    assert _round(9.9800400001) == round(9.9800400001, ROUNDING_DECIMALS)


def test_rounding_normalises_negative_zero():
    """Assert the *sign*: `-0.0 == 0.0`, so a value comparison cannot catch it.

    json.dumps writes `-0.0` verbatim, and the sign of a denormal residual flips
    between machines — precisely the churn the rounding exists to prevent. It
    also renders as negative beta-cell mass.
    """
    assert math.copysign(1.0, _round(-4.55e-303)) == 1.0
    assert math.copysign(1.0, _round(-0.0)) == 1.0
    # Genuinely negative values keep their sign.
    assert math.copysign(1.0, _round(-3.5)) == -1.0


def test_threshold_kind_distinguishes_ratios_from_absolute_readings():
    assert threshold_kind("below") == "ratio_of_baseline"
    assert threshold_kind("above") == "absolute"


def test_observables_and_thresholds_come_from_the_curated_yaml():
    config = load_model_config(
        MODELS_DIR / "urate_homeostasis.config.yaml",
        disorder=json.loads(
            json.dumps(
                {
                    "computational_models": [
                        {
                            "model_id": "urate_homeostasis",
                            "variables": [
                                {
                                    "name": "Serum_Urate",
                                    "dataset_identifier": "U",
                                    "unit": "mg/dL",
                                    "mappings_list": [
                                        {
                                            "term": {
                                                "id": "HP:0002149",
                                                "label": "Hyperuricemia",
                                            },
                                            "threshold": 6.8,
                                            "threshold_direction": "above",
                                            "severity_scale": [
                                                {"threshold": 6.8, "name": "mild"}
                                            ],
                                        }
                                    ],
                                }
                            ],
                        }
                    ]
                }
            )
        ),
    )
    observables = build_observables(config)
    assert observables == [
        {
            "name": "Serum_Urate",
            "dataset_identifier": "U",
            "label": "Serum_Urate (mg/dL)",
        }
    ]
    thresholds = build_thresholds(config)
    assert thresholds[0]["hp_id"] == "HP:0002149"
    assert thresholds[0]["direction"] == "above"
    assert thresholds[0]["threshold_kind"] == "absolute"
    assert thresholds[0]["severity_scale"] == [[6.8, "mild"]]


def test_models_without_curated_variables_are_skipped(tmp_path):
    """Nothing to report is not the same as a run that produced nothing."""
    result = run_config(
        MODELS_DIR / "urate_homeostasis.config.yaml",
        tmp_path,
        disorders_dir=tmp_path / "no-disorders-here",
        write=False,
    )
    assert result.payload is None
    assert "no curated model variables" in result.skipped_reason


def test_committed_artifacts_exist_for_every_runnable_model():
    committed = {path.stem for path in _committed()}
    runnable = {
        path.name[: -len(".config.yaml")]
        for path in MODELS_DIR.glob("*.config.yaml")
    }
    assert committed == runnable, (
        "every model with a perturb config should have a committed run — "
        f"missing {sorted(runnable - committed)}, extra {sorted(committed - runnable)}. "
        "Regenerate with `just gen-model-results`, which needs tellurium "
        "(`uv pip install tellurium`)."
    )


@pytest.mark.parametrize("path", _committed(), ids=lambda path: path.stem)
def test_committed_artifact_is_well_formed(path):
    payload = json.loads(path.read_text())

    assert payload["model_id"] == path.stem
    provenance = payload["provenance"]
    for key in ("config_sha256", "sbml_sha256", "severity_dial", "duration_hours"):
        assert provenance.get(key), f"{path.name}: provenance.{key} missing"

    observable_names = {item["name"] for item in payload["observables"]}
    assert observable_names, f"{path.name}: no observables"
    assert set(payload["baseline"]) <= observable_names

    scenario_ids = [scenario["id"] for scenario in payload["scenarios"]]
    assert scenario_ids, f"{path.name}: no scenarios"
    assert len(scenario_ids) == len(set(scenario_ids))

    threshold_variables = {item["model_variable"] for item in payload["thresholds"]}
    assert threshold_variables <= observable_names

    # Every published threshold says whether its number is an absolute reading
    # or a ratio of baseline; without it, urate's Hypouricemia reads 5x off.
    for threshold in payload["thresholds"]:
        assert threshold["threshold_kind"] in {"absolute", "ratio_of_baseline"}

    for scenario in payload["scenarios"]:
        # `values` would be shadowed by the dict method in Jinja.
        assert "values" not in scenario
        assert set(scenario["final_values"]) <= observable_names
        assert set(scenario["fold_change"]) <= observable_names
        for phenotype in scenario["phenotypes"]:
            assert phenotype["hp_id"].startswith("HP:")
            assert phenotype["hp_label"]
            # A model that declares its scenarios not comparable in severity
            # publishes the activation without a tier.
            if not payload["severity_comparable"]:
                assert phenotype["severity"] is None

    # No negative zero anywhere in the committed numbers.
    for scenario in payload["scenarios"]:
        for value in list(scenario["final_values"].values()) + list(
            scenario["fold_change"].values()
        ):
            if value == 0:
                assert math.copysign(1.0, value) == 1.0, (
                    f"{path.name}/{scenario['id']}: negative zero in artifact"
                )


@pytest.mark.parametrize("path", _committed(), ids=lambda path: path.stem)
def test_committed_artifact_matches_its_inputs(path):
    """A stale run shows up as a hash mismatch, not a silently wrong table."""
    import hashlib

    payload = json.loads(path.read_text())
    provenance = payload["provenance"]

    config_path = MODELS_DIR / f"{payload['model_id']}.config.yaml"
    assert config_path.exists()
    actual = hashlib.sha256(config_path.read_bytes()).hexdigest()
    assert actual == provenance["config_sha256"], (
        f"{path.name} was generated from a different {config_path.name} — "
        "run `just gen-model-results`"
    )

    sbml_path = MODELS_DIR / provenance["sbml_file"]
    actual = hashlib.sha256(sbml_path.read_bytes()).hexdigest()
    assert actual == provenance["sbml_sha256"], (
        f"{path.name} was generated from a different {provenance['sbml_file']} — "
        "run `just gen-model-results`"
    )


@pytest.mark.parametrize("path", _committed(), ids=lambda path: path.stem)
def test_scenarios_match_the_config(path):
    payload = json.loads(path.read_text())
    config = load_model_config(MODELS_DIR / f"{payload['model_id']}.config.yaml")
    assert [scenario["id"] for scenario in payload["scenarios"]] == list(
        config.scenarios
    )


def test_load_results_returns_none_for_an_unrun_model():
    assert load_results("not-a-model", RESULTS_DIR) is None
    assert load_results("urate_homeostasis", RESULTS_DIR) is not None


def test_disorder_page_renders_the_results_table(tmp_path):
    """The Gout page must show the urate run, its phenotypes and provenance."""
    from dismech.render import render_disorder

    output = tmp_path / "Gout.html"
    render_disorder(REPO_ROOT / "kb" / "disorders" / "Gout.yaml", output)
    html = output.read_text()

    # The element, not the class name: the CSS rule ships on every page.
    assert '<details class="model-run-block"' in html
    assert "Simulation results" in html
    assert "Healthy baseline" in html
    # A scenario row, its activated phenotype, and the derived-artifact notice.
    assert "Allopurinol (xanthine oxidase inhibitor)" in html
    assert "Hyperuricemia" in html
    assert "just gen-model-results" in html
    # The causal_root should resolve to an in-page pathophysiology anchor.
    assert 'href="#pathophysiology-hyperuricemia"' in html


def test_disorder_page_without_a_run_has_no_results_table(tmp_path):
    from dismech.render import render_disorder

    output = tmp_path / "Asthma.html"
    render_disorder(REPO_ROOT / "kb" / "disorders" / "Asthma.yaml", output)
    assert '<details class="model-run-block"' not in output.read_text()


def test_bistable_model_suppresses_severity_and_carries_a_caveat():
    """Topp scenarios all land on one attractor, so a severity tier would lie.

    GCK loss-of-function is clinically mild, non-progressive MODY2; publishing
    it as "Hyperglycemia severe" alongside a genuine insulin-resistance lesion
    inverts the clinical picture. The config declares the scenarios
    non-comparable and the reason travels with the artifact.
    """
    payload = json.loads((RESULTS_DIR / "BIOMD0000000341.json").read_text())
    assert payload["severity_comparable"] is False
    assert payload["caveat"]
    assert "GCK" in payload["caveat"]

    gck = next(s for s in payload["scenarios"] if s["id"] == "GCK_LoF")
    assert gck["phenotypes"], "the activation itself is still published"
    assert all(p["severity"] is None for p in gck["phenotypes"])


def test_comparable_model_still_publishes_severity_tiers():
    payload = json.loads((RESULTS_DIR / "urate_homeostasis.json").read_text())
    assert payload["severity_comparable"] is True
    severities = [
        phenotype["severity"]
        for scenario in payload["scenarios"]
        for phenotype in scenario["phenotypes"]
    ]
    assert any(severity for severity in severities)


def test_disorder_page_renders_the_caveat_and_omits_suppressed_severity(tmp_path):
    from dismech.render import render_disorder

    output = tmp_path / "T2D.html"
    render_disorder(
        REPO_ROOT / "kb" / "disorders" / "Type_2_Diabetes_Mellitus.yaml", output
    )
    html = output.read_text()
    assert "model-run-caveat" in html
    assert "Interpretation caveat" in html
    assert "GCK-MODY" in html
    # The phenotype is still shown, but never with a severity tier.
    assert "Hyperglycemia" in html
    assert "&middot; severe" not in html.split("model-run-block")[-1]


def test_template_consumes_threshold_kind_rather_than_re_deriving_it(tmp_path):
    """The `x baseline` suffix must come from `threshold_kind`, not a second rule.

    Urate has one threshold of each kind, so a single page proves both branches:
    Hypouricemia (`below`, a ratio) carries the suffix and Hyperuricemia
    (`above`, an absolute mg/dL reading) does not.
    """
    from dismech.render import render_disorder

    output = tmp_path / "Gout.html"
    render_disorder(REPO_ROOT / "kb" / "disorders" / "Gout.yaml", output)
    html = output.read_text()

    assert "below 0.5&times; baseline" in html
    assert "above 6.8&times; baseline" not in html
    # The severity pills take the same discriminator.
    assert "moderate 0.35&times; baseline" in html
