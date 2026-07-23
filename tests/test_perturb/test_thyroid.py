"""Tests for the HPT (hypothalamic-pituitary-thyroid) perturbation exemplar.

A minimal two-state feedback model wired to Congenital Hypothyroidism, with
thyroid secretory capacity as the disease-severity dial and levothyroxine as a
drug-target parameter.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from dismech.perturb.simulate import load_model_config

CONFIG = Path("models/hpt_feedback_axis.config.yaml")
CH = "kb/disorders/Congenital_Hypothyroidism.yaml"


def _tellurium_available():
    import importlib.util

    return importlib.util.find_spec("tellurium") is not None


def test_hpt_config_loads_thyroid_dial():
    """The HPT config uses thyroid secretory capacity as the severity dial."""
    config = load_model_config(CONFIG)
    assert config.model_id == "hpt_feedback_axis"
    assert config.coupling.gfr_parameter == "S_thy"
    assert config.coupling.baseline_gfr == pytest.approx(1.0)
    assert "TPO" in config.gene_effects
    assert "levothyroxine_full_replacement" in config.scenarios


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_overt_hypothyroidism_activates_phenotypes():
    """Overt primary hypothyroidism elevates TSH and lowers free T4."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", CH, "--scenario", "overt_hypothyroidism"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0002925" in result.stdout  # Elevated TSH
    assert "HP:0000821" in result.stdout  # Hypothyroidism


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_levothyroxine_full_replacement_rescues():
    """Full levothyroxine replacement restores euthyroidism (no phenotypes)."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", CH, "--scenario", "levothyroxine_full_replacement"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0002925" not in result.stdout  # TSH normalized
    assert "HP:0000821" not in result.stdout  # euthyroid


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_levothyroxine_over_replacement_causes_thyrotoxicosis():
    """Over-replacement suppresses TSH and drives free T4 into thyrotoxicosis."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", CH, "--scenario", "levothyroxine_over_replacement"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0000836" in result.stdout  # Hyperthyroidism


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_central_hypothyroidism_has_no_elevated_tsh():
    """Central hypothyroidism gives low free T4 with inappropriately normal TSH."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", CH, "--scenario", "central_hypothyroidism"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0000821" in result.stdout  # Hypothyroidism (low free T4)
    assert "HP:0002925" not in result.stdout  # TSH NOT elevated (unlike primary)
