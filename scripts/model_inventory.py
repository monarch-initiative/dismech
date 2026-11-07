#!/usr/bin/env python3
"""Inventory dismech's model systems and the links that reach the pathograph.

A model in `kb/` is only connected to disease mechanism through a
`ModelMechanismLink` -- the object carrying `target`, `relationship`,
`fidelity`, `model_scale`, `limitations`, `divergences`, `readouts` and
`evidence`. A model with no link renders on the page and no mechanism node
knows about it, so counting models alone overstates how much of the pathograph
has a model behind it.

This counts both, and keeps separate the two things a count can conflate.

**A link inside a proposed experiment is not a curated model.** A
`ModelMechanismLink` has four homes: the three top-level model sections, and
`model_systems` on a proposed experiment or its controls. The fourth describes
a system nobody has run. The walk comes from `dismech.model_links`, which is
the single place that reaches all four -- `tests/test_data.py` and
`scripts/model_scale_audit.py` each used to walk only the top three, and every
check on a link inside a proposal silently had no opinion (dismech#13427).

**An absent caveat is not the same as a clean one.** `fidelity`, `model_scale`,
`limitations` and `divergences` are all optional, so this reports how many
links carry each rather than treating a missing value as a verdict. A link with
neither scale is `UNDETERMINED`, which is the state of most of them, and the
scale comparison itself belongs to `just model-scale-audit` rather than here.

Usage:
    model_inventory.py
    model_inventory.py --format tsv --out models.tsv
    model_inventory.py --node "Neuronal Hyperexcitability"
    model_inventory.py --curated-only

Needs PyYAML; run it with uv from the repo root.
"""

from __future__ import annotations

import argparse
import datetime
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:
    sys.exit(
        "error: PyYAML not importable. Run it with uv, e.g.\n"
        "  uv run python scripts/model_inventory.py"
    )

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech.model_links import MODEL_SECTIONS, iter_model_links

# See the note in scripts/assay_inventory.py: the repo's loader prefers
# libyaml's CSafeLoader, which turns a six-minute corpus walk into about forty
# seconds without changing what is parsed.
from dismech.yaml_io import safe_load

REPO_ROOT = Path(__file__).resolve().parent.parent

#: The slot that types a model, per section. Each section names its own kind of
#: thing, so there is no single "model type" column to count.
TYPE_SLOT = {
    "experimental_models": "experimental_model_type",
    "animal_models": "species",
    "computational_models": "model_type",
}

#: Slots whose presence on a link is worth counting. `limitations` and
#: `divergences` are the two ways a translational caveat is recorded, and
#: `divergences` is the typed one.
LINK_DETAIL_SLOTS = ("limitations", "divergences", "readouts", "evidence")


def repo_commit(repo: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "not-a-git-checkout"


def model_name(model: dict, section: str) -> str:
    """The label a renderer would use for a model.

    `name` is optional on an animal model, where renderers fall back to
    genotype plus species -- so this mirrors that rather than reporting a blank.
    """
    name = model.get("name")
    if isinstance(name, str) and name:
        return name
    if section == "animal_models":
        parts = [model.get("genotype"), model.get("species")]
        fallback = " ".join(str(p) for p in parts if p)
        if fallback:
            return fallback
    return "(unnamed)"


def models_in_entry(doc: dict) -> list[dict]:
    """Every model in the three top-level sections, with its type and link count."""
    found = []
    for section in MODEL_SECTIONS:
        for index, model in enumerate(doc.get(section) or []):
            if not isinstance(model, dict):
                continue
            links = model.get("modeled_mechanisms")
            found.append(
                {
                    "section": section,
                    "path": f"{section}[{index}]",
                    "name": model_name(model, section),
                    "model_type": model.get(TYPE_SLOT[section]) or "",
                    "type_slot": TYPE_SLOT[section],
                    "links": len(links) if isinstance(links, list) else 0,
                }
            )
    return found


def links_in_entry(doc: dict) -> list[dict]:
    """Every `ModelMechanismLink`, from all four of its homes."""
    found = []
    for site in iter_model_links(doc):
        link = site.link
        section = (
            site.path_prefix
            if site.path_prefix in MODEL_SECTIONS
            else "proposed_experiment"
        )
        readouts = link.get("readouts")
        readouts = readouts if isinstance(readouts, list) else []
        divergences = link.get("divergences")
        divergences = divergences if isinstance(divergences, list) else []
        found.append(
            {
                "section": section,
                "proposed": site.proposed,
                "path": (
                    f"{site.path_prefix}[{site.model_index}]"
                    f".modeled_mechanisms[{site.link_index}]"
                ),
                "model": model_name(site.model, section),
                "target": link.get("target") or "",
                "relationship": link.get("relationship") or "",
                "fidelity": link.get("fidelity") or "",
                "model_scale": link.get("model_scale") or "",
                "limitations": bool(link.get("limitations")),
                "divergences": len(divergences),
                "readouts": len(readouts),
                "evidence": len(link.get("evidence") or []),
                "divergence_types": [
                    d.get("divergence_type") or ""
                    for d in divergences
                    if isinstance(d, dict)
                ],
            }
        )
    return found


def collect(repo: Path, globs: list[str], *, curated_only: bool) -> dict:
    files: list[Path] = []
    for pattern in globs:
        files += sorted(repo.glob(pattern))

    models: list[dict] = []
    links: list[dict] = []
    errors: list[dict] = []

    for path in files:
        rel = str(path.relative_to(repo))
        try:
            doc = safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError) as exc:
            errors.append({"file": rel, "error": str(exc)[:200]})
            continue
        if not isinstance(doc, dict):
            continue
        entry = doc.get("name") or rel

        for model in models_in_entry(doc):
            model["file"] = rel
            model["entry"] = entry
            models.append(model)
        for link in links_in_entry(doc):
            if curated_only and link["proposed"]:
                continue
            link["file"] = rel
            link["entry"] = entry
            links.append(link)

    return {
        "repo": str(repo),
        "commit": repo_commit(repo),
        "generated": datetime.datetime.now(datetime.UTC).date().isoformat(),
        "globs": globs,
        "curated_only": curated_only,
        "files_parsed": len(files) - len(errors),
        "parse_errors": errors,
        "models": models,
        "links": links,
    }


def _counted_table(out: list[str], header: str, counts: Counter, total: int) -> None:
    """A value/count/share table, with absent values named as such."""
    out += [f"### {header}", "", "| Value | Links | Share |", "|---|---|---|"]
    for value, count in counts.most_common():
        shown = value if value else "(not recorded)"
        share = f"{100 * count / total:.1f}%" if total else "--"
        out.append(f"| {shown} | {count} | {share} |")
    out.append("")


def render_md(res: dict, nodes: list[str]) -> str:
    models, links = res["models"], res["links"]
    linked_models = sum(1 for m in models if m["links"])
    proposed = sum(1 for link in links if link["proposed"])

    out = [
        "# Model systems and mechanism links in dismech",
        "",
        f"- Repo: `{res['repo']}`",
        f"- Commit: `{res['commit']}`",
        f"- Run on: {res['generated']}",
        f"- Files parsed: {res['files_parsed']} from "
        + ", ".join("`" + g + "`" for g in res["globs"]),
        f"- Models: {len(models)}, of which {linked_models} reach the pathograph",
        f"- Mechanism links: {len(links)}"
        + (
            f", of which {proposed} sit inside a proposed experiment"
            if not res["curated_only"]
            else " (curated models only)"
        ),
        "",
        (
            "A model with no `modeled_mechanisms` link renders on its entry's "
            "page but no mechanism node knows about it."
        ),
        "",
        "## Models by section",
        "",
        "| Section | Models | With a link | Links | Entries |",
        "|---|---|---|---|---|",
    ]
    for section in MODEL_SECTIONS:
        rows = [m for m in models if m["section"] == section]
        out.append(
            f"| `{section}` | {len(rows)} "
            f"| {sum(1 for m in rows if m['links'])} "
            f"| {sum(m['links'] for m in rows)} "
            f"| {len({m['entry'] for m in rows})} |"
        )
    out.append("")

    for section in MODEL_SECTIONS:
        rows = [m for m in models if m["section"] == section]
        if not rows:
            continue
        counts = Counter(m["model_type"] for m in rows)
        out += [f"### `{section}` by `{TYPE_SLOT[section]}`", ""]
        if section == "animal_models":
            out += [
                (
                    "`species` is free text, so these are the strings as "
                    "curated and one animal appears under several of them. "
                    "For species normalised into clades, use "
                    "`just model-taxon-census`, which owns that mapping -- a "
                    "second normaliser here could disagree with it."
                ),
                "",
            ]
        out += ["| Value | Models |", "|---|---|"]
        for value, count in counts.most_common(20):
            out.append(f"| {value if value else '(not recorded)'} | {count} |")
        out.append("")

    out += [
        "## Links by where they sit",
        "",
        "| Home | Links | Entries | Distinct targets |",
        "|---|---|---|---|",
    ]
    for section in (*MODEL_SECTIONS, "proposed_experiment"):
        rows = [link for link in links if link["section"] == section]
        if not rows and section == "proposed_experiment":
            continue
        out.append(
            f"| `{section}` | {len(rows)} "
            f"| {len({r['entry'] for r in rows})} "
            f"| {len({(r['entry'], r['target']) for r in rows})} |"
        )
    out.append("")

    out.append("## What the links record")
    out.append("")
    total = len(links)
    for slot in ("relationship", "fidelity", "model_scale"):
        _counted_table(out, slot, Counter(link[slot] for link in links), total)

    out += [
        "### Detail carried on a link",
        "",
        "| Slot | Links carrying it | Share |",
        "|---|---|---|",
    ]
    for slot in LINK_DETAIL_SLOTS:
        carrying = sum(1 for link in links if link[slot])
        share = f"{100 * carrying / total:.1f}%" if total else "--"
        out.append(f"| `{slot}` | {carrying} | {share} |")
    out.append("")

    divergence_types = Counter(
        t for link in links for t in link["divergence_types"] if t
    )
    if divergence_types:
        out += ["### `divergence_type` values", "", "| Value | Uses |", "|---|---|"]
        for value, count in divergence_types.most_common():
            out.append(f"| {value} | {count} |")
        out.append("")

    for wanted in nodes:
        hits = [link for link in links if link["target"].lower() == wanted.lower()]
        out += [f"## Reverse lookup: {wanted} -- {len(hits)} link(s)", ""]
        if not hits:
            out += [
                (
                    "No model targets a node with that name in the files "
                    "parsed. A link's `target` is a bare node name, matched "
                    "verbatim."
                ),
                "",
            ]
            continue
        out += [
            "| Entry | Model | Home | Relationship | Fidelity | Scale | Proposed |",
            "|---|---|---|---|---|---|---|",
        ]
        for hit in sorted(hits, key=lambda h: (h["entry"], h["path"])):
            out.append(
                f"| {hit['entry']} | {hit['model']} | `{hit['section']}` "
                f"| {hit['relationship'] or '--'} | {hit['fidelity'] or '--'} "
                f"| {hit['model_scale'] or '--'} "
                f"| {'yes' if hit['proposed'] else 'no'} |"
            )
        out.append("")

    if res["parse_errors"]:
        out += ["## Files that would not parse", ""]
        out += [f"- `{e['file']}`: {e['error']}" for e in res["parse_errors"]]
        out.append("")
    return "\n".join(out)


def render_tsv(res: dict) -> str:
    cols = [
        "entry",
        "section",
        "proposed",
        "model",
        "target",
        "relationship",
        "fidelity",
        "model_scale",
        "has_limitations",
        "divergences",
        "readouts",
        "evidence",
        "path",
        "file",
    ]
    rows = ["\t".join(cols)]
    for link in res["links"]:
        rows.append(
            "\t".join(
                [
                    link["entry"],
                    link["section"],
                    str(link["proposed"]),
                    link["model"],
                    link["target"],
                    link["relationship"],
                    link["fidelity"],
                    link["model_scale"],
                    str(link["limitations"]),
                    str(link["divergences"]),
                    str(link["readouts"]),
                    str(link["evidence"]),
                    link["path"],
                    link["file"],
                ]
            )
        )
    return "\n".join(rows) + "\n"


def render_models_tsv(res: dict) -> str:
    cols = [
        "entry",
        "section",
        "model",
        "type_slot",
        "model_type",
        "links",
        "path",
        "file",
    ]
    rows = ["\t".join(cols)]
    for model in res["models"]:
        rows.append(
            "\t".join(
                [
                    model["entry"],
                    model["section"],
                    model["name"],
                    model["type_slot"],
                    str(model["model_type"]),
                    str(model["links"]),
                    model["path"],
                    model["file"],
                ]
            )
        )
    return "\n".join(rows) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--repo", default=REPO_ROOT, type=Path)
    ap.add_argument(
        "--glob",
        action="append",
        dest="globs",
        help="KB glob, repeatable (default: disorders, modules, comorbidities)",
    )
    ap.add_argument(
        "--node",
        action="append",
        dest="nodes",
        default=[],
        help="reverse-lookup the models targeting this node name, repeatable",
    )
    ap.add_argument(
        "--curated-only",
        action="store_true",
        help="drop links that sit inside a proposed experiment",
    )
    ap.add_argument(
        "--table",
        choices=("links", "models"),
        default="links",
        help="which table --format tsv emits (default: links)",
    )
    ap.add_argument("--format", choices=("md", "tsv", "json"), default="md")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if not args.repo.is_dir():
        print(f"error: no such repo: {args.repo}", file=sys.stderr)
        return 1

    globs = args.globs or [
        "kb/disorders/*.yaml",
        "kb/modules/*.yaml",
        "kb/comorbidities/*.yaml",
    ]
    res = collect(args.repo, globs, curated_only=args.curated_only)

    if args.format == "md":
        text = render_md(res, args.nodes)
    elif args.format == "tsv":
        text = render_models_tsv(res) if args.table == "models" else render_tsv(res)
    else:
        text = json.dumps(res, indent=2)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
