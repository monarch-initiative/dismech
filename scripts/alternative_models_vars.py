#!/usr/bin/env python3
"""Collect the variables an alternative-model research prompt needs.

templates/disease_alternative_models_research.md asks a provider which model
systems, beyond the ones already curated, could support an entry's pathograph
nodes. Two of its eight variables name the disease, four are a per-use-case
search plan written by hand and kept in templates/alternative_models/<slug>.yaml,
and two are generated from the entry itself by scripts/model_taxon_census.py, so
the prompt always states the record's real current state rather than a remembered
one.

This script only gathers them. `just alternative-models-research` passes each
one to deep-research-client as a `--var` and lets the client render the
committed template, so the run is staged, stamped and validated like every other
research recipe and no rendered prompt is ever written into research/.

    scripts/alternative_models_vars.py mdd_alternative_systems --format entry
    scripts/alternative_models_vars.py mdd_alternative_systems --format null
    scripts/alternative_models_vars.py mdd_alternative_systems --format prompt

`--format prompt` renders the same template through the client's own
TemplateProcessor, so a preview cannot drift from what a run would send.
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from dismech.yaml_io import safe_load_path

TEMPLATE = pathlib.Path("templates/disease_alternative_models_research.md")
USE_CASES = pathlib.Path("templates/alternative_models")
CENSUS = pathlib.Path("scripts/model_taxon_census.py")
NAMED = ("disease_name", "mondo_id")
HAND_WRITTEN = ("model_scope", "nodes_of_interest", "substitution_constraint", "systems_to_cover")
GENERATED = ("existing_models", "mechanism_nodes")


def generated_var(entry: str, name: str) -> str:
    """Run the census script for one injectable block."""
    proc = subprocess.run(
        [sys.executable, str(CENSUS), "--entry", entry, "--template-vars", name],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"{CENSUS} failed for {name}: {proc.stderr.strip()}")
    return proc.stdout.rstrip()


def use_case(slug: str) -> dict:
    """Load one use-case spec, insisting on every hand-written variable."""
    spec_path = USE_CASES / f"{slug}.yaml"
    if not spec_path.is_file():
        available = ", ".join(sorted(p.stem for p in USE_CASES.glob("*.yaml"))) or "none"
        raise SystemExit(f"No use case {slug!r}. Available: {available}")
    spec = safe_load_path(spec_path)
    missing = [k for k in ("entry", *NAMED, *HAND_WRITTEN) if not spec.get(k)]
    if missing:
        raise SystemExit(f"{spec_path} is missing: {', '.join(missing)}")
    return spec


def variables(spec: dict) -> dict[str, str]:
    """Return every template variable for a use case, generated blocks included."""
    entry = spec["entry"]
    return {
        **{k: str(spec[k]).rstrip() for k in (*NAMED, *HAND_WRITTEN)},
        **{k: generated_var(entry, k) for k in GENERATED},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="use case in templates/alternative_models/, without .yaml")
    ap.add_argument(
        "--format",
        choices=("null", "entry", "prompt"),
        default="null",
        help="NUL-separated name=value records (default), the entry name, or the rendered prompt",
    )
    args = ap.parse_args()

    if not TEMPLATE.is_file():
        print(f"{TEMPLATE} not found. Run from a dismech checkout.", file=sys.stderr)
        return 1

    spec = use_case(args.slug)
    if args.format == "entry":
        print(spec["entry"])
        return 0

    values = variables(spec)
    if args.format == "prompt":
        from deep_research_client.processing.template_processor import TemplateProcessor

        print(TemplateProcessor().render_template(TEMPLATE, values))
        return 0

    for name, value in values.items():
        sys.stdout.write(f"{name}={value}\0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
