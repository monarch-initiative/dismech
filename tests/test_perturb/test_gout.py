"""Tests for the urate homeostasis perturbation exemplar (Gout).

A single-compartment serum-urate balance with fractional excretion as the
disease-severity dial and three urate-lowering drug classes on distinct nodes.
"""

import subprocess
import sys
from pathlib import Path

import pytest

from dismech.perturb.simulate import load_model_config

CONFIG = Path("models/urate_homeostasis.config.yaml")
GOUT = "kb/disorders/Gout.yaml"


def _tellurium_available():
    import importlib.util

    return importlib.util.find_spec("tellurium") is not None


def test_urate_config_loads_excretion_dial():
    """The urate config uses fractional excretion as the severity dial."""
    config = load_model_config(CONFIG)
    assert config.model_id == "urate_homeostasis"
    assert config.coupling.gfr_parameter == "f_exc"
    assert config.coupling.baseline_gfr == pytest.approx(1.0)
    assert "ABCG2" in config.gene_effects
    assert "allopurinol" in config.scenarios


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_underexcretion_activates_hyperuricemia():
    """Reduced fractional excretion raises urate above the solubility limit."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", GOUT, "--scenario", "underexcretion_hyperuricemia"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0002149" in result.stdout  # Hyperuricemia


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_allopurinol_lowers_urate():
    """Xanthine oxidase inhibition returns urate below the solubility limit."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", GOUT, "--scenario", "allopurinol"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0002149" not in result.stdout  # no longer hyperuricemic


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_glut9_loss_is_protective_hypouricemia():
    """SLC2A9/GLUT9 loss increases excretion, causing protective hypouricemia."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", GOUT, "--scenario", "SLC2A9_LoF"],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "HP:0003537" in result.stdout  # Hypouricemia
    assert "HP:0002149" not in result.stdout  # not hyperuricemic
