#!/usr/bin/env python3
"""Compile a dismech module YAML or project Markdown file into structured Gemini graphical-abstract prompts.

Supports five prompt engineering styles explored in the graphical-abstracts pilot:
  1. narrative    — Style A: Journal-style prose summary prompt
  2. storyboard   — Style B: Multi-column left-to-right zoned storyboard grid
  3. cutaway      — Style C: Spatial compartment / anatomical cutaway blueprint
  4. dismech-dsl  — Style D: Multi-card Dismech Scene-Graph + Visual Grammar Contract
  5. hybrid       — Style E: Unified Subcellular Cutaway + Dismech DSL Header/Legend (recommended for intracellular modules)

Can either emit the compiled prompt (--dry-run) or call the Gemini API directly
using GEMINI_API_KEY / GOOGLE_API_KEY to save a 16:9 PNG image.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import urllib.request
from pathlib import Path
from typing import Any

import yaml

# Canonical Dismech editorial palette (from src/dismech/templates/_palette.css.j2)
DISMECH_STYLE_CONTRACT = """\
HOUSE STYLE CONTRACT (Dismech Editorial Vector System):
- Aspect ratio: 16:9 widescreen journal graphical abstract.
- Rendering style: Crisp 2D flat vector scientific illustration (Cell Press / Nature Reviews / BioRender aesthetic).
  Flat cel-shaded biological icons with uniform 2px dark slate outlines (#1f2937), subtle clean gradients only.
- Color palette:
  • Canvas background: pale cool teal-gray (#e8f6f8) or crisp off-white (#f9fafb)
  • Container cards: pure white (#ffffff) with rounded corners (12px radius) and thin borders (#e5e7eb)
  • Header bar & primary structural accents: Dismech deep teal (#00838f) and mid-teal (#008c99)
  • Triggers & stress signals: warm amber (#f59e0b)
  • Pathogenic consequences & loss-of-function lesions: coral rose (#f43f5e)
  • Protective / therapeutic / rescue pathways: emerald-teal (#0d9488) and sky blue (#0ea5e9)
  • Counter-regulatory / signaling feedback: violet (#8b5cf6)
- Typography discipline:
  • Clean geometric sans-serif labels ONLY (maximum 2–4 words per label).
  • NO multi-sentence paragraphs, NO prose descriptions, NO pseudo-Latin or garbled small text.
- Arrow & symbol grammar:
  • Solid directional arrow (→): direct causal progression (downstream target)
  • Dashed directional arrow (⇢): indirect / multi-step causal link or retrograde retrieval
  • Flat T-bar arrow (⊣): inhibition, blockade, or suppression
  • Red circle-X badge (✕): loss-of-function genetic lesion or deleted enzyme
  • Coral lightning badge (⚡): constitutive gain-of-function variant
  • Blue capsule/plus badge (⊕): pharmacologic agonist or therapeutic intervention
- Strictly forbidden: 3D photorealistic rendering, glowing neon sci-fi spheres, lens flares, decorative DNA strands unrelated to the mechanism, or dense text blocks."""

ROLE_ORDER = {
    "trigger": 1,
    "amplifier": 2,
    "central_effector": 3,
    "effector": 4,
    "consequence": 5,
    "counter_regulatory": 6,
}


def load_yaml_or_frontmatter(path: Path) -> tuple[str, dict[str, Any], str]:
    """Return (kind, data, markdown_body) where kind is 'module' or 'project'."""
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".md":
        if text.startswith("---\n"):
            parts = text.split("---\n", 2)
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip() if len(parts) > 2 else ""
            return "project", meta, body
        return "project", {"title": path.stem}, text
    data = yaml.safe_load(text) or {}
    return "module", data, ""


def short_label(name: str, max_words: int = 4) -> str:
    """Shorten a verbose dismech node name into a crisp 2-4 word graphical label."""
    cleaned = re.sub(
        r"\b(Activation|Induction|Dependent|Mediated|From|Between|And|Of|The|In|At|A|With|To|By|For)\b",
        " ",
        name,
        flags=re.IGNORECASE,
    )
    cleaned = re.sub(r"-\s+", " ", cleaned)
    words = [w.strip("-") for w in cleaned.split() if w.strip("-")]
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words])


def extract_module_scene_graph(data: dict[str, Any]) -> dict[str, Any]:
    """Extract structured visual zones from a dismech module YAML dict."""
    nodes = data.get("pathophysiology", []) or []
    zones: list[dict[str, Any]] = []
    for idx, node in enumerate(nodes, 1):
        name = node.get("name", f"Node {idx}")
        role = node.get("role", "effector")
        scale = node.get("biological_scale", "CELLULAR")
        cells = [
            c.get("preferred_term") or c.get("term", {}).get("label", "")
            for c in (node.get("cell_types") or [])
        ]
        comps = [
            c.get("preferred_term") or c.get("term", {}).get("label", "")
            for c in (node.get("cellular_components") or [])
        ]
        procs = [
            f"{p.get('preferred_term') or p.get('term', {}).get('label', '')}"
            + (f" [{p['modifier']}]" if p.get("modifier") else "")
            for p in (node.get("biological_processes") or [])
        ]
        downstream = [
            d.get("target", "")
            for d in (node.get("downstream") or [])
            if d.get("target")
        ]
        zones.append(
            {
                "index": idx,
                "name": name,
                "short_label": short_label(name),
                "role": role.upper(),
                "scale": scale,
                "cells": [c for c in cells if c],
                "compartments": [c for c in comps if c],
                "processes": [p for p in procs if p],
                "downstream": downstream,
            }
        )
    treatments = []
    for t in data.get("treatments", []) or []:
        t_name = t.get("name", "")
        targets = [
            tm.get("target", "")
            for tm in (t.get("target_mechanisms") or [])
            if tm.get("target")
        ]
        if t_name:
            treatments.append({"name": t_name, "targets": targets})

    return {
        "title": data.get("name", "Mechanism Module"),
        "categories": data.get("module_categories", []) or [],
        "description": data.get("description", ""),
        "zones": zones,
        "treatments": treatments,
    }


def compile_module_prompt(data: dict[str, Any], style: str = "dismech-dsl") -> str:
    """Compile a module YAML into one of the four prompt engineering styles."""
    sg = extract_module_scene_graph(data)
    title = sg["title"]
    cats = (
        " | ".join(sg["categories"]) if sg["categories"] else "PATHOPHYSIOLOGY MODULE"
    )

    if style == "narrative":
        node_names = " -> ".join(z["name"] for z in sg["zones"])
        return (
            f"A scientific graphical abstract in the style of Nature Reviews or Cell Press "
            f"illustrating '{title}'. {sg['description']} "
            f"Show the causal pathway progression: {node_names}. "
            f"Clean 2D flat vector scientific illustration on a white background."
        )

    if style == "storyboard":
        lines = [
            "A clean 2D flat vector scientific graphical abstract (16:9 widescreen) structured as a "
            "strict left-to-right multi-column storyboard grid on a light off-white background (#f9fafb) "
            "with crisp dark slate outlines (#1f2937) and teal (#00838f) accents, zero 3D effects, "
            "and concise sans-serif labels (maximum 3-4 words per label, no paragraphs):",
            f"\nTOP HEADER BANNER: '{title}' ({cats})",
        ]
        for z in sg["zones"]:
            meta = ", ".join(z["compartments"] + z["cells"]) or z["scale"]
            arrows = ", ".join(f"-> '{short_label(t)}'" for t in z["downstream"])
            lines.append(
                f"- STAGE {z['index']} [{z['role']} • {z['scale']}]: Card titled '{z['short_label']}' "
                f"(Visual focus: {meta}; Processes: {', '.join(z['processes'][:2]) or 'core step'}) "
                f"{arrows}"
            )
        return "\n".join(lines)

    if style == "cutaway":
        compartments = []
        for z in sg["zones"]:
            for c in z["compartments"] + z["cells"]:
                if c not in compartments:
                    compartments.append(c)
        comp_str = (
            " -> ".join(compartments)
            if compartments
            else "Subcellular -> Cellular -> Tissue compartments"
        )
        lines = [
            "A flagship Cell Press / BioRender style 2D flat vector scientific illustration "
            "(16:9 widescreen, white background, crisp thin dark outlines, flat cel-shaded vector "
            "organelles and cells, no 3D rendering, no glowing sci-fi effects, concise labels only):",
            f"\nSUBJECT: '{title}'",
            f"SPATIAL ARCHITECTURE: A continuous anatomical/cellular cutaway spanning: {comp_str}.",
            "MECHANISTIC NODES TO ILLUSTRATE IN SPATIAL ORDER:",
        ]
        for z in sg["zones"]:
            loc = ", ".join(z["compartments"] + z["cells"]) or z["scale"]
            lines.append(
                f"  {z['index']}. [{loc}] '{z['short_label']}': illustrate {', '.join(z['processes'][:2]) or z['name']} "
                f"leading to {', '.join(short_label(t) for t in z['downstream']) or 'terminal outcome'}."
            )
        return "\n".join(lines)

    if style == "hybrid":
        intracellular = [
            z for z in sg["zones"] if z["scale"] == "MOLECULAR" or z["compartments"]
        ]
        outcomes = [z for z in sg["zones"] if z not in intracellular]
        lines = [
            DISMECH_STYLE_CONTRACT,
            "Additional strict constraint: Do NOT draw chemical structural formulas or raw nucleotide letter sequences.",
            "\n1. TOP HEADER BAR (Full-width deep teal #00838f banner with bold white text):",
            f"   Left title: 'MODULE: {title.upper()}'",
            f"   Right category pills: '{cats}'",
            "\n2. LEFT MAIN PANEL (62% width, single continuous white card showing a unified cutaway cell interior with clearly labeled sub-zones):",
        ]
        for z in intracellular:
            comp = ", ".join(z["compartments"]) or "intracellular compartment"
            proc = ", ".join(z["processes"][:2]) or z["name"]
            edges = "; ".join(
                f"solid arrow (→) to '{short_label(t)}'" for t in z["downstream"]
            )
            lines.append(
                f"   - SUB-ZONE {z['index']} [{z['role']} • {comp}]: '{z['short_label']}' — "
                f"illustrate {proc} ({edges})."
            )
        lines.append(
            "\n3. RIGHT PANEL (38% width, stacked outcome cards branching from the cell cutaway):"
        )
        for z in outcomes:
            border = (
                "violet border"
                if z["role"] == "COUNTER_REGULATORY"
                else "coral or emerald border"
            )
            cells = ", ".join(z["cells"]) or z["scale"]
            lines.append(
                f"   - OUTCOME CARD [{z['role']} • {z['scale']}] ({border}): '{z['short_label']}' "
                f"(Icons: {cells}; Process: {', '.join(z['processes'][:2]) or z['name']})."
            )
        lines.append(
            "\n4. BOTTOM LEGEND STRIP (Slim white bar across bottom):\n"
            "   '→ Direct Activation / Flux'   '⊣ Inhibits / Blocks'   '✕ Loss-of-Function Lesion'   '⚡ Gain-of-Function'   '⊕ Pharmacologic Agonist'"
        )
        return "\n".join(lines)

    # Default: style == "dismech-dsl"
    lines = [
        DISMECH_STYLE_CONTRACT,
        "\n1. TOP HEADER BAR (Full-width deep teal #00838f banner with bold white text):",
        f"   Title: '{title.upper()}'",
        f"   Right-aligned category pills: '{cats}'",
        "\n2. SCENE GRAPH (Linked horizontal zones flowing left-to-right across the 16:9 canvas):",
    ]
    for z in sg["zones"]:
        border = (
            "double teal border (#00838f)"
            if z["role"] == "CENTRAL_EFFECTOR"
            else "coral border (#f43f5e)"
            if z["role"] == "CONSEQUENCE"
            else "violet border (#8b5cf6)"
            if z["role"] == "COUNTER_REGULATORY"
            else "amber accent (#f59e0b)"
            if z["role"] == "TRIGGER"
            else "clean slate-gray border"
        )
        visual_entities = (
            ", ".join(z["cells"] + z["compartments"])
            or f"{z['scale'].lower()} structure"
        )
        proc_summary = ", ".join(z["processes"][:2]) or z["name"]
        edges = (
            "; ".join(f"solid arrow (→) to '{short_label(t)}'" for t in z["downstream"])
            or "terminal outcome node"
        )
        lines.append(
            f"   - ZONE {z['index']} [{z['role']} • {z['scale']}] (White card with {border}):\n"
            f"     • Card Header Label: '{z['short_label']}'\n"
            f"     • Vector Iconography: Draw flat 2D vector {visual_entities} depicting {proc_summary}.\n"
            f"     • Outgoing Connectors: {edges}."
        )
    if sg["treatments"]:
        t_items = "; ".join(
            f"'{t['name']}' -> {', '.join(short_label(x) for x in t['targets'])}"
            for t in sg["treatments"][:4]
        )
        lines.append(
            f"\n3. THERAPEUTIC INTERVENTION CALLOUTS (Sky-blue badges ⊕ / T-bars ⊣):\n   {t_items}"
        )
    lines.append(
        "\n4. BOTTOM LEGEND STRIP (Slim white bar across bottom):\n"
        "   '→ Direct Causal Edge'   '⊣ Inhibits / Blocks'   '✕ Loss-of-Function'   '⚡ Gain-of-Function'   '⊕ Therapeutic Agent'"
    )
    return "\n".join(lines)


def generate_via_gemini_api(
    prompt: str, output_path: Path, model: str = "gemini-2.5-flash-image"
) -> None:
    """Call the Gemini generateContent REST API to generate an image and write it to output_path."""
    api_key = (
        os.environ.get("GEMINI_API_KEY")
        or os.environ.get("GOOGLE_API_KEY")
        or os.environ.get("LLM_GEMINI_KEY")
    )
    if not api_key:
        raise RuntimeError("No GEMINI_API_KEY or GOOGLE_API_KEY found in environment.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    for cand in body.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                img_bytes = base64.b64decode(inline["data"])
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(img_bytes)
                print(
                    f"Saved generated image ({len(img_bytes)} bytes) to {output_path}"
                )
                return
    raise RuntimeError(f"No image returned in response: {json.dumps(body)[:500]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "input_path", type=Path, help="Path to kb/modules/*.yaml or projects/*.md"
    )
    parser.add_argument(
        "--style",
        choices=["narrative", "storyboard", "cutaway", "dismech-dsl", "hybrid"],
        default="hybrid",
        help="Prompt engineering style to compile",
    )
    parser.add_argument(
        "--output", "-o", type=Path, help="Output PNG path (if generating)"
    )
    parser.add_argument(
        "--model", default="gemini-2.5-flash-image", help="Gemini image model name"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print compiled prompt without calling API",
    )
    args = parser.parse_args()

    kind, data, _ = load_yaml_or_frontmatter(args.input_path)
    if kind == "project":
        modules = data.get("modules", [])
        if modules:
            mod_path = (
                args.input_path.parent.parent / "kb" / "modules" / f"{modules[0]}.yaml"
            )
            if mod_path.exists():
                _, mod_data, _ = load_yaml_or_frontmatter(mod_path)
                mod_data["name"] = f"Project: {data.get('title', args.input_path.stem)}"
                mod_data["module_categories"] = [
                    t.upper() for t in data.get("tags", [])
                ]
                data = mod_data

    prompt = compile_module_prompt(data, style=args.style)
    if args.dry_run or not args.output:
        print(prompt)
        return

    generate_via_gemini_api(prompt, args.output, model=args.model)


if __name__ == "__main__":
    main()
