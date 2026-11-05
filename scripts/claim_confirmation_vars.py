#!/usr/bin/env python3
"""Collect the variables a claim-confirmation research prompt needs.

templates/claim_confirmation_research.md asks a provider whether each claim
drawn from a single source is independently confirmed, contradicted, or simply
untested elsewhere. All three of its variables are written by hand and kept in
templates/claim_confirmation/<slug>.yaml, because nothing in the repository can
derive a claim list: deciding which assertions of a source are worth checking is
the curator's judgement, not something computable from the entry.

That is the one way this differs from its sibling, scripts/alternative_models_vars.py,
whose prompt is mostly generated from the entry's own current state. Here the
spec file *is* the input, which is why it is committed: a run is then
reproducible and reviewable rather than hand-assembled and lost.

This script only gathers the variables. `just claim-confirmation` passes each one
to deep-research-client as a `--var` and lets the client render the committed
template, so the run is staged, stamped and validated like every other research
recipe and no rendered prompt is ever written into research/.

    scripts/claim_confirmation_vars.py paul_2023_pesticides --format entry
    scripts/claim_confirmation_vars.py paul_2023_pesticides --format null
    scripts/claim_confirmation_vars.py paul_2023_pesticides --format prompt

`--format prompt` renders the same template through the client's own
TemplateProcessor, so a preview cannot drift from what a run would send.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from dismech.yaml_io import safe_load_path

TEMPLATE = pathlib.Path("templates/claim_confirmation_research.md")
USE_CASES = pathlib.Path("templates/claim_confirmation")
HAND_WRITTEN = ("source_citation", "context", "claims")


def use_case(slug: str) -> dict:
    """Load one use-case spec, insisting on every variable the template needs."""
    spec_path = USE_CASES / f"{slug}.yaml"
    if not spec_path.is_file():
        available = ", ".join(sorted(p.stem for p in USE_CASES.glob("*.yaml"))) or "none"
        raise SystemExit(f"No use case {slug!r}. Available: {available}")
    spec = safe_load_path(spec_path)
    missing = [k for k in ("entry", *HAND_WRITTEN) if not spec.get(k)]
    if missing:
        raise SystemExit(f"{spec_path} is missing: {', '.join(missing)}")
    return spec


def variables(spec: dict) -> dict[str, str]:
    """Return every template variable for a use case."""
    return {k: str(spec[k]).rstrip() for k in HAND_WRITTEN}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("slug", help="use case in templates/claim_confirmation/, without .yaml")
    ap.add_argument(
        "--format",
        choices=("null", "entry", "prompt"),
        default="null",
        help="NUL-separated name=value records (default), the entry name, or the rendered prompt",
    )
    args = ap.parse_args(argv)

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
