"""Where a model's files live: one folder per model under ``models/``.

Every model in the repository, whatever runs it, sits in ``models/<model_id>/``
and is identified by that folder name. The files inside carry fixed names, so
nothing that consumes a model has to know its id twice:

======================  =====================================================
File                    Meaning
======================  =====================================================
``config.yaml``         a dismech-perturb sidecar: the model is *runnable
                        in-repo* by ``dismech.perturb`` (SBML through
                        tellurium). ``sbml_file`` and ``extension_file`` in it
                        resolve relative to the folder.
``model.xml``           the SBML the config points at
``model.ant``           its Antimony source, where the model was authored here
``extension.ant``       an Antimony extension co-simulated with the base model
``spec.yaml``           a repository-authored model with its own runner (a
                        Boolean network, an agent-based model): the rule
                        specification, with per-rule provenance into ``kb/``
``run.py``              that model's runner; ``--check`` verifies ``results.json``
``results.json``        the runner's committed, deterministic output
======================  =====================================================

A folder holds exactly one of ``config.yaml`` or ``spec.yaml``. There are no
model files at the top of ``models/``; ``tests/test_model_registry.py`` keeps it
that way, so an in-flight branch still using the old flat
``models/<id>.config.yaml`` layout fails with a message rather than being
silently ignored by the globs below.

Only paths are decided here. Loading a config is ``dismech.perturb.simulate``'s
job, and running an authored model is its own ``run.py``'s.
"""

from __future__ import annotations

from pathlib import Path

MODELS_DIR = Path("models")

CONFIG_NAME = "config.yaml"
SPEC_NAME = "spec.yaml"
RUNNER_NAME = "run.py"
RESULTS_NAME = "results.json"
SBML_NAME = "model.xml"
ANTIMONY_NAME = "model.ant"
EXTENSION_NAME = "extension.ant"

#: Files a model folder may contain. Anything else is reported by the layout test.
KNOWN_FILES = frozenset(
    {
        CONFIG_NAME,
        SPEC_NAME,
        RUNNER_NAME,
        RESULTS_NAME,
        SBML_NAME,
        ANTIMONY_NAME,
        EXTENSION_NAME,
        "README.md",
    }
)


def model_dir(model_id: str, models_dir: Path = MODELS_DIR) -> Path:
    """The folder for ``model_id``, whether or not it exists."""
    return models_dir / model_id


def config_path(model_id: str, models_dir: Path = MODELS_DIR) -> Path:
    """The dismech-perturb sidecar for ``model_id``, whether or not it exists."""
    return model_dir(model_id, models_dir) / CONFIG_NAME


def find_config(model_id: str, models_dir: Path = MODELS_DIR) -> Path | None:
    """The sidecar for ``model_id`` when the model is runnable in-repo, else None."""
    path = config_path(model_id, models_dir)
    return path if path.is_file() else None


def iter_model_dirs(models_dir: Path = MODELS_DIR) -> list[Path]:
    """Every model folder, sorted by id."""
    if not models_dir.is_dir():
        return []
    return sorted(
        p
        for p in models_dir.iterdir()
        if p.is_dir() and not p.name.startswith((".", "_"))
    )


def iter_configs(models_dir: Path = MODELS_DIR) -> list[Path]:
    """Every dismech-perturb sidecar, sorted by model id."""
    return [
        d / CONFIG_NAME
        for d in iter_model_dirs(models_dir)
        if (d / CONFIG_NAME).is_file()
    ]


def iter_specs(models_dir: Path = MODELS_DIR) -> list[Path]:
    """Every repository-authored model spec, sorted by model id."""
    return [
        d / SPEC_NAME for d in iter_model_dirs(models_dir) if (d / SPEC_NAME).is_file()
    ]


def runnable_model_ids(models_dir: Path = MODELS_DIR) -> set[str]:
    """Ids of the models ``dismech.perturb`` can run: those with a sidecar."""
    return {path.parent.name for path in iter_configs(models_dir)}


def model_id_of(path: Path) -> str:
    """The model id a file under ``models/<id>/`` belongs to."""
    return path.parent.name
