"""Integration tests for the full perturbation pipeline."""

import subprocess
import sys

import pytest


def _tellurium_available():
    import importlib.util

    return importlib.util.find_spec("tellurium") is not None


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_cli_gene_perturbation():
    """Test CLI with CASR LoF perturbation."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.perturb",
            "kb/disorders/CKD-Mineral_Bone_Disorder.yaml",
            "--gene",
            "CASR",
            "--effect",
            "LoF",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "PERTURBATION" in result.stdout
    assert "PTH" in result.stdout


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_cli_named_scenario():
    """Test CLI with a named scenario."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.perturb",
            "kb/disorders/CKD-Mineral_Bone_Disorder.yaml",
            "--scenario",
            "calcimimetic",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "PERTURBATION" in result.stdout


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_cli_param_perturbation():
    """Test CLI with parameter override."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.perturb",
            "kb/disorders/CKD-Mineral_Bone_Disorder.yaml",
            "--param",
            "OralPhos=2.0",
            "--gfr",
            "2.0",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "PERTURBATION" in result.stdout


@pytest.mark.skipif(not _tellurium_available(), reason="tellurium not installed")
def test_cli_phenotypes_activated():
    """Test that phenotypes are activated for severe CKD + gene perturbation."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "dismech.perturb",
            "kb/disorders/CKD-Mineral_Bone_Disorder.yaml",
            "--gene",
            "CASR",
            "--effect",
            "LoF",
            "--gfr",
            "1.0",
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert "ACTIVATED PHENOTYPES" in result.stdout


def test_cli_help():
    """Test --help works without tellurium."""
    result = subprocess.run(
        [sys.executable, "-m", "dismech.perturb", "--help"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0
    assert (
        "disorder-yaml" in result.stdout.lower()
        or "disorder_yaml" in result.stdout.lower()
    )
