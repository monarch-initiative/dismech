"""Tests for ODE simulation module."""

import importlib.util

import pytest
from pathlib import Path

from dismech.perturb.simulate import (
    ModelConfig,
    load_model_config,
    SimulationResult,
)


def _tellurium_available():
    return importlib.util.find_spec("tellurium") is not None


@pytest.fixture
def model_config():
    """Load the CKD-MBD model config."""
    config_path = Path("models/BIOMD0000000613.config.yaml")
    if not config_path.exists():
        pytest.skip("Model config not found")
    return load_model_config(config_path)


def test_load_model_config(model_config):
    """Test that model config loads correctly."""
    assert isinstance(model_config, ModelConfig)
    assert model_config.model_id == "BIOMD0000000613"
    assert "CASR" in model_config.gene_effects
    assert len(model_config.phenotype_thresholds) > 0
    assert len(model_config.variable_mappings) > 0
    assert model_config.coupling.dt_hours == 168


def test_gene_effects_loaded(model_config):
    """Test gene effects are parsed correctly."""
    casr = model_config.gene_effects["CASR"]
    assert casr.parameter == "ScaEffGam"
    assert casr.LoF == 0.4
    assert casr.GoF == 2.0
    assert not casr.in_extension

    kl = model_config.gene_effects["KL"]
    assert kl.in_extension is True
    assert kl.LoF == 0.2


def test_variable_mappings_loaded(model_config):
    """Test variable mappings are parsed correctly."""
    assert "PTH" in model_config.variable_mappings
    assert model_config.variable_mappings["PTH"].sbml_species == "PTH"
    assert model_config.variable_mappings["FGF23"].extension_species == "FGF23"
    assert (
        model_config.variable_mappings["CaPO4_product"].extension_assignment
        == "CaPO4_product"
    )


def test_phenotype_thresholds_loaded(model_config):
    """Test phenotype thresholds are parsed correctly."""
    assert len(model_config.phenotype_thresholds) == 9
    bmd = next(
        pt for pt in model_config.phenotype_thresholds if pt.hp_id == "HP:0004349"
    )
    assert bmd.model_variable == "Bone"
    assert bmd.direction == "below"
    assert bmd.threshold == 0.85
    assert len(bmd.severity_scale) == 3


def test_scenarios_loaded(model_config):
    """Test scenarios are loaded."""
    assert "CASR_LoF" in model_config.scenarios
    assert model_config.scenarios["CASR_LoF"]["gene"] == "CASR"
    assert "high_phosphate_diet" in model_config.scenarios


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_run_baseline(model_config):
    """Test running a healthy baseline simulation."""
    from dismech.perturb.simulate import run_perturbation

    result = run_perturbation(model_config, gfr=6.0)
    assert isinstance(result, SimulationResult)
    assert result.variables["PTH"] > 0
    assert result.variables["PO4"] > 0
    assert result.variables["Ca"] > 0


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_run_gene_perturbation(model_config):
    """Test CASR LoF perturbation changes PTH."""
    from dismech.perturb.simulate import run_perturbation

    baseline = run_perturbation(model_config, gfr=2.0)
    perturbed = run_perturbation(model_config, gfr=2.0, gene="CASR", effect="LoF")
    # CASR LoF should increase PTH (blunted calcium sensing)
    assert perturbed.variables["PTH"] > baseline.variables["PTH"]
