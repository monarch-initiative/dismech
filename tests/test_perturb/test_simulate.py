"""Tests for ODE simulation module."""

import importlib.util

import pytest
from pathlib import Path

from dismech.perturb.simulate import (
    ModelConfig,
    extract_model_variables,
    load_model_config,
    SimulationResult,
)


def _tellurium_available():
    return importlib.util.find_spec("tellurium") is not None


@pytest.fixture
def ckd_disorder():
    """Load the CKD-MBD disorder YAML."""
    import yaml as _yaml

    yaml_path = Path("kb/disorders/CKD-Mineral_Bone_Disorder.yaml")
    if not yaml_path.exists():
        pytest.skip("CKD-MBD YAML not found")
    with open(yaml_path) as f:
        return _yaml.safe_load(f)


@pytest.fixture
def model_config(ckd_disorder):
    """Load the CKD-MBD model config with disorder YAML."""
    config_path = Path("models/BIOMD0000000613.config.yaml")
    if not config_path.exists():
        pytest.skip("Model config not found")
    return load_model_config(config_path, disorder=ckd_disorder)


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
    assert casr.parameter == "T61"
    assert casr.LoF == 3.0
    assert casr.GoF == 0.3
    assert not casr.in_extension

    kl = model_config.gene_effects["KL"]
    assert kl.in_extension is True
    assert kl.LoF == 0.2


def test_variable_mappings_loaded(model_config):
    """Test variable mappings from YAML are parsed correctly."""
    assert "Plasma_PTH" in model_config.variable_mappings
    assert model_config.variable_mappings["Plasma_PTH"].dataset_identifier == "PTH"
    assert model_config.variable_mappings["FGF23"].dataset_identifier == "FGF23"
    assert (
        model_config.variable_mappings["CaPO4_Product"].dataset_identifier
        == "CaPO4_product"
    )


def test_phenotype_thresholds_loaded(model_config):
    """Test phenotype thresholds extracted from YAML mappings_list."""
    assert len(model_config.phenotype_thresholds) == 9
    bmd = next(
        pt for pt in model_config.phenotype_thresholds if pt.hp_id == "HP:0004349"
    )
    assert bmd.model_variable == "BMD"
    assert bmd.direction == "below"
    assert bmd.threshold == 0.85
    assert len(bmd.severity_scale) == 3


def test_scenarios_loaded(model_config):
    """Test scenarios are loaded."""
    assert "CASR_LoF" in model_config.scenarios
    assert model_config.scenarios["CASR_LoF"]["gene"] == "CASR"
    assert "high_phosphate_diet" in model_config.scenarios


def test_extract_variables_from_yaml():
    """Test extracting variable mappings and thresholds from disorder YAML."""
    yaml_path = Path("kb/disorders/CKD-Mineral_Bone_Disorder.yaml")
    if not yaml_path.exists():
        pytest.skip("CKD-MBD YAML not found")
    import yaml as _yaml

    with open(yaml_path) as f:
        disorder = _yaml.safe_load(f)
    var_mappings, thresholds = extract_model_variables(disorder, "BIOMD0000000613")
    assert len(var_mappings) > 0
    # Check dataset_identifier is populated
    assert var_mappings["Plasma_Ca"].dataset_identifier == "P"
    assert var_mappings["Plasma_PO4"].dataset_identifier == "ECCPhos"
    assert var_mappings["BMD"].dataset_identifier == "Qbone"
    assert var_mappings["FGF23"].dataset_identifier == "FGF23"
    assert var_mappings["Vascular_Calcification"].dataset_identifier == "VascCa"
    # Check phenotype thresholds extracted from mappings_list
    assert len(thresholds) > 0
    bmd_thresh = [t for t in thresholds if t.hp_id == "HP:0004349"]
    assert len(bmd_thresh) == 1
    assert bmd_thresh[0].direction == "below"
    assert bmd_thresh[0].threshold == 0.85
    assert len(bmd_thresh[0].severity_scale) == 3


def test_load_config_with_disorder_yaml():
    """Test that load_model_config with disorder YAML uses YAML variables."""
    yaml_path = Path("kb/disorders/CKD-Mineral_Bone_Disorder.yaml")
    config_path = Path("models/BIOMD0000000613.config.yaml")
    if not yaml_path.exists() or not config_path.exists():
        pytest.skip("CKD-MBD files not found")
    import yaml as _yaml

    with open(yaml_path) as f:
        disorder = _yaml.safe_load(f)
    config = load_model_config(config_path, disorder=disorder)
    # Should use YAML-derived mappings (dataset_identifier populated)
    assert config.variable_mappings["Plasma_Ca"].dataset_identifier == "P"
    # Should have phenotype thresholds from YAML
    assert any(t.hp_id == "HP:0003207" for t in config.phenotype_thresholds)
    # Should still have gene_effects from sidecar
    assert "CASR" in config.gene_effects


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_run_baseline_with_yaml_variables():
    """Test simulation using YAML-derived variable mappings."""
    from dismech.perturb.simulate import run_perturbation
    import yaml as _yaml

    yaml_path = Path("kb/disorders/CKD-Mineral_Bone_Disorder.yaml")
    config_path = Path("models/BIOMD0000000613.config.yaml")
    if not yaml_path.exists() or not config_path.exists():
        pytest.skip("CKD-MBD files not found")
    with open(yaml_path) as f:
        disorder = _yaml.safe_load(f)
    config = load_model_config(config_path, disorder=disorder)
    result = run_perturbation(config, gfr=6.0)
    assert result.variables["Plasma_PTH"] > 0
    assert result.variables["Plasma_PO4"] > 0
    assert result.variables["Plasma_Ca"] > 0
    assert result.variables["FGF23"] > 0
    assert result.variables["Vascular_Calcification"] >= 0


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_run_baseline(model_config):
    """Test running a healthy baseline simulation."""
    from dismech.perturb.simulate import run_perturbation

    result = run_perturbation(model_config, gfr=6.0)
    assert isinstance(result, SimulationResult)
    assert result.variables["Plasma_PTH"] > 0
    assert result.variables["Plasma_PO4"] > 0
    assert result.variables["Plasma_Ca"] > 0


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_run_gene_perturbation(model_config):
    """Test CASR LoF perturbation changes PTH."""
    from dismech.perturb.simulate import run_perturbation

    baseline = run_perturbation(model_config, gfr=2.0)
    perturbed = run_perturbation(model_config, gfr=2.0, gene="CASR", effect="LoF")
    # CASR LoF should increase PTH (blunted calcium sensing)
    assert perturbed.variables["Plasma_PTH"] > baseline.variables["Plasma_PTH"]
