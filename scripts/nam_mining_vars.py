#!/usr/bin/env python3
"""Collect the variables a NAM-mining research prompt needs.

templates/nam_mining_research.md asks a provider to dissect one paper into its
biological systems, then to decide for each system which mechanism nodes it
bears on, with what relationship, fidelity and observed scale -- and what each
system does not model. Eight of its nine variables are written by hand and kept
in templates/nam_mining/<slug>.yaml, for the same reason the claim-confirmation
specs are (scripts/claim_confirmation_vars.py): nothing in the repository can
derive them. Which systems a paper contains, which of them are separable, and
which nodes are worth testing against are the screener's judgement, read off
the paper.

The ninth, `link_slot_definitions`, is generated from the schema. A run has to
return a `ModelMechanismLink` field by field, so the prompt has to say what each
field means -- and the schema already says, in wording the repository treats as
authoritative. Paraphrasing it into the template would create a second
definition of every slot, free to drift from the first; `just
template-version-audit` would then report the prompt as current while it
described a schema that had moved. So the definitions are read out of
src/dismech/schema/dismech.yaml at render time, enum values and all.

That also settles a question the hand-written version got wrong. Asking for
`limitations` and `divergences` as separate items invites the same caveat
written twice, because they are not separate content: the schema calls
`divergences` "the structured counterpart of the free-text `limitations`
summary", and the taxonomy was built by clustering the KB's existing
`limitations` prose (CLAUDE.md). Emitting both slots with their own descriptions
says that relationship plainly, where a paraphrase had to assert it.

A paper's screening issue states eight of these fields in prose, so a spec can
usually be lifted from one, but the two are not the same document: an issue also
carries provenance, the destination decision, the gap issues and the pull
requests, while a spec has to name node names that actually resolve. Committing
the spec is what makes a run reproducible rather than hand-assembled and lost --
the first one, zheng_2023_hmo_graft, had to be recovered from a committed
report's citations file because no prompt for it existed in the repository.
The `nam-mining` skill is the procedure for authoring one.

One field earns its place by what it prevents. `anchors_to_avoid` names the
nodes a run should not land on and says why, because a provider matching an
anchor on its name is the failure these runs actually produce: a module whose
title shares a word with the paper's wording, asserting a mechanism the paper
never measured. The screening issues name those traps; without a field for them
the prompt drops the warning.

This script only gathers the variables. `just nam-mining` passes each one to
deep-research-client as a `--var` and lets the client render the committed
template, so the run is staged, stamped and validated like every other research
recipe and no rendered prompt is ever written into research/.

    scripts/nam_mining_vars.py zheng_2023_hmo_graft --format entry
    scripts/nam_mining_vars.py zheng_2023_hmo_graft --format null
    scripts/nam_mining_vars.py zheng_2023_hmo_graft --format prompt

`--format prompt` renders the same template through the client's own
TemplateProcessor, so a preview cannot drift from what a run would send.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from dismech.yaml_io import safe_load_path

TEMPLATE = pathlib.Path("templates/nam_mining_research.md")
USE_CASES = pathlib.Path("templates/nam_mining")
SCHEMA = pathlib.Path("src/dismech/schema/dismech.yaml")
HAND_WRITTEN = (
    "reference",
    "access",
    "paper_summary",
    "systems",
    "candidate_nodes",
    "anchors_to_avoid",
    "claims_to_verify",
    "does_not_model",
)
GENERATED = ("link_slot_definitions",)

# The link object a run has to fill, and the slots worth spelling out in a
# prompt. `target` and `evidence` are omitted: the target is the node, which the
# prompt already supplies as `candidate_nodes`, and evidence is handled by the
# prompt's own quote-and-identifier discipline rather than by its schema shape.
LINK_CLASS = "ModelMechanismLink"
LINK_SLOTS = (
    "relationship",
    "description",
    "readouts",
    "fidelity",
    "limitations",
    "model_scale",
    "divergences",
)
# Ranges expanded one level, because a run cannot fill a structured slot from
# the slot's own description alone. The sub-slots are named rather than taken
# whole: a readout carries four optional ontology bindings a provider is in no
# position to choose, and listing them invites invented CURIEs.
NESTED = {
    "ModelDivergence": ("divergence_type", "description", "materiality"),
    "ExperimentalReadout": ("name", "direction", "interpretation"),
}


def _wrap(text: str, indent: str = "") -> str:
    """Collapse a schema description to one paragraph of readable width."""
    import textwrap

    collapsed = " ".join(str(text).split())
    return textwrap.fill(
        collapsed, width=78, initial_indent=indent, subsequent_indent=indent
    )


def _schema() -> dict:
    if not SCHEMA.is_file():
        raise SystemExit(f"{SCHEMA} not found. Run from a dismech checkout.")
    return safe_load_path(SCHEMA)


def _slot_description(schema: dict, cls: str, slot: str) -> str:
    """The description that applies to this slot on this class.

    `slot_usage` wins over the top-level slot, and has to: the top-level
    `relationship` and `readouts` descriptions are written for biomarkers, and
    quoting those at a model-mining run would describe the wrong object.
    """
    usage = schema["classes"][cls].get("slot_usage", {}).get(slot, {})
    if usage.get("description"):
        return usage["description"]
    return schema["slots"].get(slot, {}).get("description", "")


def _slot_range(schema: dict, cls: str, slot: str) -> str | None:
    usage = schema["classes"][cls].get("slot_usage", {}).get(slot, {})
    return usage.get("range") or schema["slots"].get(slot, {}).get("range")


def _enum_block(schema: dict, name: str) -> list[str]:
    """Every permitted value of an enum, with its own description."""
    values = schema["enums"][name].get("permissible_values") or {}
    lines = []
    for value, body in values.items():
        description = (body or {}).get("description", "")
        if description:
            lines.append(f"  - `{value}` — {' '.join(str(description).split())}")
        else:
            lines.append(f"  - `{value}`")
    return lines


def link_slot_definitions(schema: dict | None = None) -> str:
    """Render the link object's own definitions, straight from the schema.

    Everything here is the schema's wording, not a paraphrase of it, so the
    prompt and the object a curator has to fill cannot disagree.
    """
    schema = schema or _schema()
    cls = schema["classes"][LINK_CLASS]
    out: list[str] = []

    out.append(_wrap(cls["description"]))
    out.append("")
    for comment in cls.get("comments", []):
        out.append(_wrap(comment, indent="> "))
        out.append("")

    for slot in LINK_SLOTS:
        description = _slot_description(schema, LINK_CLASS, slot)
        range_ = _slot_range(schema, LINK_CLASS, slot)
        out.append(f"### `{slot}`")
        out.append("")
        out.append(_wrap(description))
        out.append("")

        if range_ in schema.get("enums", {}):
            out.append("One of:")
            out.extend(_enum_block(schema, range_))
            out.append("")
        elif range_ in NESTED:
            nested = schema["classes"][range_]
            out.append(_wrap(nested["description"]))
            out.append("")
            for comment in nested.get("comments", []):
                out.append(_wrap(comment, indent="> "))
                out.append("")
            for sub in NESTED[range_]:
                sub_description = _slot_description(schema, range_, sub)
                if not sub_description:
                    continue
                out.append(f"- **`{sub}`** — {' '.join(str(sub_description).split())}")
                sub_range = _slot_range(schema, range_, sub)
                if sub_range in schema.get("enums", {}):
                    out.extend("  " + line for line in _enum_block(schema, sub_range))
            out.append("")

    return "\n".join(out).rstrip()


def use_case(slug: str) -> dict:
    """Load one use-case spec, insisting on every variable the template needs."""
    spec_path = USE_CASES / f"{slug}.yaml"
    if not spec_path.is_file():
        available = (
            ", ".join(sorted(p.stem for p in USE_CASES.glob("*.yaml"))) or "none"
        )
        raise SystemExit(f"No use case {slug!r}. Available: {available}")
    spec = safe_load_path(spec_path)
    missing = [k for k in ("entry", *HAND_WRITTEN) if not spec.get(k)]
    if missing:
        raise SystemExit(f"{spec_path} is missing: {', '.join(missing)}")
    return spec


def variables(spec: dict) -> dict[str, str]:
    """Return every template variable for a use case."""
    values = {k: str(spec[k]).rstrip() for k in HAND_WRITTEN}
    values["link_slot_definitions"] = link_slot_definitions()
    return values


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("slug", help="use case in templates/nam_mining/, without .yaml")
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
