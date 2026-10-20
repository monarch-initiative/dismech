#!/usr/bin/env python3
"""Render and optionally run an alternative-model deep-research prompt.

templates/disease_alternative_models_research.md asks a provider which model
systems, beyond the ones already curated, could support an entry's pathograph
nodes. Four of its eight variables are a per-use-case search plan written by
hand and kept in templates/alternative_models/<slug>.yaml; two are generated
from the entry itself by scripts/model_taxon_census.py, so the prompt always
states the record's real current state rather than a remembered one.

This script joins the two and either prints the rendered prompt or hands it to
deep-research-client. Print it first: the prompt is the whole experiment, and a
run costs real time and credit.

    just alternative-models-research mdd_alternative_systems --dry-run
    just alternative-models-research mdd_alternative_systems --provider openscientist

Output goes to research/<Entry>-alternative-models-deep-research-<provider>.md,
which cannot collide with the disorder-wide report that `just research-disorder`
writes.
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


def render(slug: str) -> tuple[str, str]:
    """Return (entry, rendered prompt) for a use case."""
    spec_path = USE_CASES / f"{slug}.yaml"
    if not spec_path.is_file():
        available = ", ".join(sorted(p.stem for p in USE_CASES.glob("*.yaml"))) or "none"
        raise SystemExit(f"No use case {slug!r}. Available: {available}")
    spec = safe_load_path(spec_path)

    missing = [k for k in ("entry", "disease_name", "mondo_id", *HAND_WRITTEN) if not spec.get(k)]
    if missing:
        raise SystemExit(f"{spec_path} is missing: {', '.join(missing)}")

    entry = spec["entry"]
    variables = {
        "disease_name": spec["disease_name"],
        "mondo_id": spec["mondo_id"],
        **{k: str(spec[k]).rstrip() for k in HAND_WRITTEN},
        **{k: generated_var(entry, k) for k in GENERATED},
    }
    return entry, TEMPLATE.read_text().format(**variables)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="use case in templates/alternative_models/, without .yaml")
    ap.add_argument("--dry-run", action="store_true", help="print the rendered prompt and stop")
    ap.add_argument(
        "--provider", default="openscientist", help="deep-research provider (default: openscientist)"
    )
    ap.add_argument("--out", help="override the output report path")
    args = ap.parse_args()

    if not TEMPLATE.is_file():
        print(f"{TEMPLATE} not found. Run from a dismech checkout.", file=sys.stderr)
        return 1

    entry, prompt = render(args.slug)
    if args.dry_run:
        print(prompt)
        return 0

    out = pathlib.Path(args.out or f"research/{entry}-alternative-models-deep-research-{args.provider}.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    # The client takes a template path, not a prompt string, so the rendered
    # prompt is written beside the report. It is the exact text sent, which is
    # worth keeping: the use-case YAML plus a later curation PR would not
    # reconstruct it, because the generated blocks move with the record.
    rendered = out.with_suffix(".prompt.md")
    rendered.write_text(prompt)
    print(f"Rendered prompt: {rendered}")

    cmd = [
        "scripts/run_deep_research_client.sh",
        "research",
        "--template",
        str(rendered),
        "--provider",
        args.provider,
        "--output",
        str(out),
        "--separate-citations",
        f"{out}.citations.md",
    ]
    print("Running:", " ".join(cmd))
    return subprocess.run(cmd, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
