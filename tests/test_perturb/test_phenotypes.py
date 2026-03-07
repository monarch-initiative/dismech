"""Tests for phenotype mapping."""

import pytest

from dismech.perturb.phenotypes import evaluate_phenotypes
from dismech.perturb.simulate import PhenotypeThreshold


@pytest.fixture
def thresholds():
    return [
        PhenotypeThreshold(
            hp_id="HP:0004349",
            hp_label="Reduced bone mineral density",
            model_variable="Bone",
            direction="below",
            threshold=0.85,
            severity_scale=[(0.85, "mild"), (0.70, "moderate"), (0.50, "severe")],
        ),
        PhenotypeThreshold(
            hp_id="HP:0002653",
            hp_label="Bone pain",
            model_variable="PTH",
            direction="above",
            threshold=70,
            severity_scale=[(70, "mild"), (100, "moderate"), (150, "severe")],
        ),
    ]


def test_no_activation_at_baseline(thresholds):
    """Baseline values should not activate phenotypes."""
    baseline = {"Bone": 5000.0, "PTH": 55.0}
    result = {"Bone": 5000.0, "PTH": 55.0}
    activated = evaluate_phenotypes(result, baseline, thresholds)
    assert len(activated) == 0


def test_bone_loss_activates_bmd(thresholds):
    """Bone loss below threshold should activate reduced BMD."""
    baseline = {"Bone": 5000.0, "PTH": 55.0}
    result = {"Bone": 3500.0, "PTH": 55.0}  # 70% of baseline
    activated = evaluate_phenotypes(result, baseline, thresholds)
    assert any(a.hp_id == "HP:0004349" for a in activated)


def test_high_pth_activates_bone_pain(thresholds):
    """High PTH should activate bone pain."""
    baseline = {"Bone": 5000.0, "PTH": 55.0}
    result = {"Bone": 5000.0, "PTH": 120.0}
    activated = evaluate_phenotypes(result, baseline, thresholds)
    assert any(a.hp_id == "HP:0002653" for a in activated)
    pain = next(a for a in activated if a.hp_id == "HP:0002653")
    assert pain.severity == "moderate"


def test_severity_scaling(thresholds):
    """Severity should scale with value."""
    baseline = {"Bone": 5000.0, "PTH": 55.0}
    result = {"Bone": 2000.0, "PTH": 55.0}  # 40% of baseline = severe
    activated = evaluate_phenotypes(result, baseline, thresholds)
    bmd = next(a for a in activated if a.hp_id == "HP:0004349")
    assert bmd.severity == "severe"


def test_missing_variable_skipped(thresholds):
    """Variables not in result should be silently skipped."""
    baseline = {"PTH": 55.0}
    result = {"PTH": 120.0}  # Bone is missing
    activated = evaluate_phenotypes(result, baseline, thresholds)
    # Only PTH-based phenotype should activate
    assert len(activated) == 1
    assert activated[0].hp_id == "HP:0002653"
