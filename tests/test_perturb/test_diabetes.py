"""Tests for the Topp beta-cell/insulin/glucose diabetes perturbation exemplar.

Covers the disease-agnostic generalization of the perturb framework (a
configurable disease-severity dial via ``coupling.gfr_parameter`` /
``baseline_gfr`` and integrator tolerances) and the Type 2 Diabetes wiring to
BioModels BIOMD0000000341.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from dismech.perturb.simulate import load_model_config

CONFIG = Path("models/BIOMD0000000341.config.yaml")
T2DM = "kb/disorders/Type_2_Diabetes_Mellitus.yaml"


def _tellurium_available():
    import importlib.util

    return importlib.util.find_spec("tellurium") is not None


def test_diabetes_config_loads_severity_dial():
    """The diabetes config repurposes the severity dial to insulin sensitivity."""
    config = load_model_config(CONFIG)
    assert config.model_id == "BIOMD0000000341"
    # Disease-severity dial generalized away from the CKD-specific GFR default.
    assert config.coupling.gfr_parameter == "si"
    assert config.coupling.baseline_gfr == pytest.approx(0.72)
    # Stiff beta-cell-mass collapse needs a looser absolute tolerance.
    assert config.coupling.abs_tol == pytest.approx(1e-6)
    assert "PPARG" in config.gene_effects
    assert "sglt2_inhibitor" in config.scenarios


def test_ckd_config_defaults_preserved():
    """The generalization keeps the CKD defaults (GFR dial, tight tolerance)."""
    config = load_model_config(Path("models/BIOMD0000000613.config.yaml"))
    assert config.coupling.gfr_parameter == "GFR"
    assert config.coupling.baseline_gfr == pytest.approx(6.0)
    assert config.coupling.abs_tol == pytest.approx(1e-12)


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_diabetes_insulin_resistance_activates_hyperglycemia():
    """Severe insulin resistance decompensates to overt hyperglycemia."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", T2DM, "--scenario", "insulin_resistance"],
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "ACTIVATED PHENOTYPES" in result.stdout
    assert "HP:0003074" in result.stdout  # Hyperglycemia


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_diabetes_sglt2_inhibitor_rescues():
    """An insulin-independent therapy (SGLT2i) returns glucose to euglycemia."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", T2DM, "--scenario", "sglt2_inhibitor"],
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    # Rescued: hyperglycemia is NOT among the activated phenotypes.
    assert "HP:0003074" not in result.stdout


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_diabetes_sulfonylurea_fails_after_collapse():
    """A pure secretagogue fails once beta-cell mass has collapsed."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", T2DM, "--scenario", "sulfonylurea"],
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    # Not rescued: hyperglycemia remains activated.
    assert "HP:0003074" in result.stdout
