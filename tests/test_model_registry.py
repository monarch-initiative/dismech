"""The ``models/`` layout contract: one folder per model, fixed file names.

``dismech.model_registry`` is the only place that knows where a model's files
live, and every consumer (the models browser export, dismech-perturb, the
SED-ML export, the authored-model runners) goes through it. These tests keep
the committed tree in the shape the registry expects, so a branch still adding
a flat ``models/<id>.config.yaml`` fails here with a message instead of being
silently ignored by the folder globs.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from dismech import model_registry as reg

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"


def test_no_model_files_at_the_top_of_models():
    """Only folders (and a README) live directly under models/."""
    stray = sorted(
        p.name for p in MODELS_DIR.iterdir() if p.is_file() and p.name != "README.md"
    )
    assert not stray, (
        "models/ holds one folder per model; move these into models/<model_id>/ "
        f"with the file names in dismech.model_registry: {stray}"
    )


@pytest.mark.parametrize(
    "model_dir", reg.iter_model_dirs(MODELS_DIR), ids=lambda p: p.name
)
def test_each_model_folder_is_well_formed(model_dir: Path):
    files = {p.name for p in model_dir.iterdir() if p.is_file()}
    unknown = sorted(files - reg.KNOWN_FILES)
    assert not unknown, f"{model_dir.name}: unexpected files {unknown}"

    has_config = reg.CONFIG_NAME in files
    has_spec = reg.SPEC_NAME in files
    assert has_config != has_spec, (
        f"{model_dir.name}: a model folder holds exactly one of "
        f"{reg.CONFIG_NAME} (dismech-perturb) or {reg.SPEC_NAME} (authored runner)"
    )

    if has_config:
        config = yaml.safe_load((model_dir / reg.CONFIG_NAME).read_text())
        assert config["model_id"] == model_dir.name, (
            f"{model_dir.name}: config model_id {config['model_id']!r} must equal the folder name"
        )
        sbml = model_dir / config["sbml_file"]
        assert sbml.is_file(), (
            f"{model_dir.name}: sbml_file {config['sbml_file']!r} not found"
        )
        if config.get("extension_file"):
            assert (model_dir / config["extension_file"]).is_file()
    else:
        spec = yaml.safe_load((model_dir / reg.SPEC_NAME).read_text())
        assert spec["model_id"] == model_dir.name, (
            f"{model_dir.name}: spec model_id {spec['model_id']!r} must equal the folder name"
        )
        assert (model_dir / reg.RUNNER_NAME).is_file(), (
            f"{model_dir.name}: authored model needs {reg.RUNNER_NAME}"
        )
        assert (model_dir / reg.RESULTS_NAME).is_file(), (
            f"{model_dir.name}: authored model needs {reg.RESULTS_NAME}"
        )
        rel = model_dir.relative_to(REPO_ROOT)
        assert spec.get("runner") == str(rel / reg.RUNNER_NAME)
        assert spec.get("results") == str(rel / reg.RESULTS_NAME)


def test_registry_sees_the_committed_models():
    ids = {p.name for p in reg.iter_model_dirs(MODELS_DIR)}
    assert reg.runnable_model_ids(MODELS_DIR) <= ids
    assert {reg.model_id_of(p) for p in reg.iter_specs(MODELS_DIR)} <= ids
    assert (
        reg.runnable_model_ids(MODELS_DIR)
        | {reg.model_id_of(p) for p in reg.iter_specs(MODELS_DIR)}
        == ids
    )
    assert reg.find_config("not-a-model", MODELS_DIR) is None


@pytest.mark.parametrize(
    "spec_path", reg.iter_specs(MODELS_DIR), ids=lambda p: p.parent.name
)
def test_every_authored_runner_reports_its_results_current(spec_path: Path):
    """`run.py --check` is the contract every authored model honours."""
    runner = spec_path.parent / reg.RUNNER_NAME
    proc = subprocess.run(
        [sys.executable, str(runner), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=300,
    )
    assert proc.returncode == 0, f"{runner}: {proc.stdout}{proc.stderr}"
