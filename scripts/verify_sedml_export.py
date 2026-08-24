#!/usr/bin/env python3
"""Verify the exported SED-ML archives reproduce dismech-perturb's own results.

The exporter in ``dismech.perturb.sedml_export`` re-encodes each scenario as
absolute SED-ML model changes. That re-encoding is only worth anything if a
third-party SED-ML engine, running the archive with no dismech code in the
loop, lands on the same numbers as ``dismech-perturb``.

This script runs both sides and diffs them:

* **dismech side** — ``simulate.run_perturbation`` with the scenario's
  gene/effect/gfr/param_overrides, exactly as the CLI invokes it.
* **standards side** — the ``.omex`` archive, extracted and executed through
  tellurium's SED-ML interpreter (``SEDMLCodeFactory``), which reads the
  archive's own ``changeAttribute`` targets and integrator settings.

Usage::

    uv run python scripts/verify_sedml_export.py
    uv run python scripts/verify_sedml_export.py --id urate_homeostasis --tolerance 1e-6

Requires tellurium (``uv pip install tellurium``). Exits non-zero if any
scenario disagrees beyond the relative tolerance.
"""

from __future__ import annotations

import argparse
import os
import tempfile
import zipfile
from pathlib import Path

# Run this through `uv run` (or `just verify-sedml-export`) so the installed
# dismech package is on the path. No sys.path manipulation is needed, which is
# what keeps every import below at the top of the file.
from dismech.perturb.sedml_export import (
    export_config,
    find_disorder_for_model,
    read_sbml_model_info,
    sanitize_sid,
)
from dismech.perturb.simulate import (
    load_model_config,
    resolve_scenario_dial,
    run_perturbation,
)
from dismech.yaml_io import safe_load

REPO_ROOT = Path(__file__).resolve().parents[1]


def run_archive(omex_path: Path) -> dict[str, object]:
    """Execute an OMEX archive through tellurium's SED-ML interpreter."""
    import matplotlib

    matplotlib.use("Agg")
    from tellurium.sedml.tesedml import SEDMLCodeFactory

    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(omex_path) as archive:
            archive.extractall(tmp)
        code = SEDMLCodeFactory(
            os.path.join(tmp, "simulation.sedml"), workingDir=tmp
        ).toPython()
        # Drop plotting: the numbers are what matter, and headless plot calls
        # are slow and noisy.
        source = "\n".join(line for line in code.split("\n") if "plt." not in line)
        namespace: dict[str, object] = {}
        exec(compile(source, str(omex_path), "exec"), namespace)
        return namespace


def column_index(colnames: list[str], symbol_id: str) -> int | None:
    """Locate a symbol in a roadrunner result array (species use [brackets])."""
    for candidate in (f"[{symbol_id}]", symbol_id):
        if candidate in colnames:
            return colnames.index(candidate)
    return None


def verify_model(
    config_path: Path, tolerance: float, atol: float, output_root: Path
) -> list[str]:
    """Compare both execution paths for one model. Returns failure messages."""
    with open(config_path) as handle:
        raw = safe_load(handle) or {}
    model_id = str(raw.get("model_id") or config_path.stem)

    result = export_config(
        config_path,
        output_root,
        disorders_dir=REPO_ROOT / "kb" / "disorders",
        write_archive=True,
    )
    if result.skipped_reason:
        print(f"SKIP  {model_id}: {result.skipped_reason}")
        return []

    disorder = find_disorder_for_model(model_id, REPO_ROOT / "kb" / "disorders")
    config = load_model_config(config_path, disorder=disorder)
    info = read_sbml_model_info(config_path.parent / config.sbml_file)

    print(f"\n=== {model_id} ({len(config.scenarios)} scenarios) ===")
    namespace = run_archive(result.omex_path)

    failures: list[str] = []
    for scenario_id, scenario in config.scenarios.items():
        scenario = scenario or {}
        dismech = run_perturbation(
            config,
            gfr=resolve_scenario_dial(config, scenario),
            gene=scenario.get("gene"),
            effect=scenario.get("effect"),
            param_overrides=scenario.get("param_overrides"),
        ).variables

        # Must use the exporter's own mapping: a local re-implementation
        # diverges silently, surfacing as a missing task rather than an error.
        task = namespace.get(f"task_{sanitize_sid(scenario_id)}")
        if task is None:
            failures.append(f"{model_id}/{scenario_id}: task missing from archive run")
            continue
        array = task[0]
        colnames = list(array.colnames)

        for var_name, mapping in config.variable_mappings.items():
            symbol_id = mapping.dataset_identifier or mapping.sbml_species
            if not symbol_id or symbol_id not in info.symbols:
                continue
            index = column_index(colnames, symbol_id)
            if index is None:
                failures.append(
                    f"{model_id}/{scenario_id}: {symbol_id} not in archive output"
                )
                continue

            expected = dismech.get(var_name)
            actual = float(array[-1][index])
            if expected is None:
                continue

            # Combined absolute + relative tolerance. A pure relative test is
            # meaningless where a variable has converged to zero: the Topp
            # beta-cell-collapse scenarios land on ~1e-300 via dismech-perturb
            # (which restarts the integrator every dt) and ~1e-13 via the
            # archive (one continuous integration). Both are zero for a state
            # whose healthy value is O(10); only an absolute floor says so.
            delta = abs(actual - expected)
            allowed = atol + tolerance * abs(expected)
            status = "ok " if delta <= allowed else "FAIL"
            if delta > allowed:
                failures.append(
                    f"{model_id}/{scenario_id}/{symbol_id}: "
                    f"dismech={expected:.9g} archive={actual:.9g} abs={delta:.3g} "
                    f"allowed={allowed:.3g}"
                )
            print(
                f"  {status} {scenario_id:42} {symbol_id:>6} "
                f"dismech={expected:12.6f} archive={actual:12.6f} abs={delta:.2e}"
            )

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models-dir", default=str(REPO_ROOT / "models"))
    parser.add_argument(
        "--id", help="Verify only this model_id (default: every exportable config)"
    )
    parser.add_argument(
        "--tolerance",
        type=float,
        default=1e-6,
        help="Relative tolerance on the final value of each observable",
    )
    parser.add_argument(
        "--atol",
        type=float,
        default=1e-6,
        help="Absolute floor, so variables converged to zero compare equal",
    )
    args = parser.parse_args()

    paths = sorted(Path(args.models_dir).glob("*.config.yaml"))
    if args.id:
        paths = [path for path in paths if path.name == f"{args.id}.config.yaml"]
        if not paths:
            parser.error(f"no config found for model_id '{args.id}'")

    failures: list[str] = []
    with tempfile.TemporaryDirectory() as tmp:
        for path in paths:
            failures.extend(
                verify_model(path, args.tolerance, args.atol, Path(tmp))
            )

    print()
    if failures:
        print(f"{len(failures)} MISMATCH(ES):")
        for failure in failures:
            print(f"  {failure}")
        return 1
    print("All exported scenarios reproduce dismech-perturb within tolerance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
