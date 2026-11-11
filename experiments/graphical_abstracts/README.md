# Graphical Abstracts Experiment (`experiments/graphical_abstracts/`)

This experiment evaluates how to generate publication-grade graphical abstracts
(*Cell Press* / *Nature Reviews* / *BioRender* 2D vector style) from structured
`dismech` knowledge base records (`kb/modules/*.yaml` and `projects/*.md`)
using Gemini image generation.

## Core Finding: Why Structured Scene-Graph Prompts Beat Freeform Summaries

When an image model is handed a prose summary of a mechanism module, it
routinely introduces three classes of scientific error:

1. **Inverted or hallucinated causal arrows** — placing a disease gene downstream
   of the ligand it regulates (for example drawing `dsDNA + cGAS -> TREX1
   Deficiency` instead of `TREX1 loss -> undegraded cytosolic dsDNA`).
2. **Fabricated chemical and sequence detail** — drawing plausible-looking but
   chemically wrong small-molecule structures (such as an invented bicyclic ring
   for `2'3'-cGAMP`) or nonsense nucleotide strings (`ACCVCXCAGUGGGCGAC`).
3. **Compartment duplication across panel boundaries** — when a multi-step
   intracellular pathway is split across separate card containers without
   spatial continuity, the model redraws the same organelle (such as the Golgi)
   in multiple cards and misroutes cross-compartment branches (such as turning
   an activating `ER-STING -> PERK` arrow into an inhibitory `Golgi ⊣ PERK`
   bar).

## Five Prompt Engineering Styles Compared

| Iteration | Style Name | Layout Grammar | Strengths | Failure Modes Observed |
|---|---|---|---|---|
| **1** | **Narrative Summary** (`narrative`) | Unconstrained ("Nature Reviews style graphical abstract of...") | Rich organelle shading; spontaneous signal-strength gradient bar | Spelling error in header (`"Pativation"`), hallucinated `2'3'-cGAMP` chemical formula & DNA letters, inverted `dsDNA -> TREX1` arrow, wrong Breg cytokines (`IL-10, TGF-β` instead of `IL-35+`) |
| **2** | **3-Column Storyboard Grid** (`storyboard`) | Strict 3-column card layout (`Triggers` \| `Core` \| `Outcomes`) | Zero typos; clean visual hierarchy; accurate `TREX1` loss-of-function icon | Cards lack inter-column causal connectors; omits nuclear transcription step |
| **3** | **Anatomical Subcellular Cutaway** (`cutaway`) | Continuous 2D cutaway cell (65% left) + extracellular outcome tracks (35% right) | Authentic *Cell Press* / *BioRender* look; natural compartment flow (`Cytosol -> ER -> COPII/COPI -> Golgi -> Nucleus -> Secretion`) | Minor bracket-header alignment drift; no explicit Dismech module metadata header or symbol legend |
| **4** | **Dismech Scene-Graph + DSL Contract** (`dismech-dsl`) | 4 scale-tagged cards (`[TRIGGER • MOLECULAR]` etc.) + Dismech `#00838f` header + legend strip | Works on linear tissue cascades (`fibrotic_response`); clear role & ontology badges | Splitting a single cell's ER-to-Golgi shuttle across two separate cards caused duplicate Golgi illustrations and an inverted `Golgi ⊣ PERK` T-bar |
| **5** | **Hybrid Cutaway + Dismech DSL Contract** (`hybrid`, recommended for subcellular modules) | Unified cutaway cell card for intracellular steps + stacked outcome cards + Dismech header & symbol legend | Preserves continuous organelle topology while keeping Dismech header, category pills, explicit arrow grammar (`→`, `⊣`, `✕`, `⚡`, `⊕`), and zero hallucinated structures | Requires grouping intracellular nodes by shared cell/organelle context before emitting card boundaries |

## Choosing the Layout Archetype by Subject Type

A single visual style contract (Dismech `#00838f` teal header, `#e8f6f8` background,
`#ffffff` rounded cards, 2px `#1f2937` outlines, flat 2D vector icons, 2–4 word
labels, and a bottom symbol legend) supports three layout archetypes depending
on the structure of the `dismech` record:

1. **Subcellular Cutaway + Outcome Bifurcation** (for intracellular signaling
   modules like `cgas_sting_pathway_activation`):
   Keep all intracellular nodes (`Cytosol`, `ER`, `Vesicular Shuttle`, `Golgi`,
   `Nucleus`) inside **one** continuous cell cutaway card on the left 60–65% of
   the canvas, with multicellular/clinical consequence arms stacked on the right.
2. **Multi-Stage Horizontal Cascade** (for tissue-scale modules like
   `fibrotic_response`):
   Map each pathophysiology role (`TRIGGER` → `AMPLIFIER` → `CENTRAL EFFECTOR`
   → `EFFECTOR` → `CONSEQUENCE`) to its own vertical card from left to right,
   with `cell_types` ontology substitutions shown as pill callouts on the
   central effector and affected organs arranged as medallions in the final card.
3. **Radial Hub + Pathophysiology Cascade** (for multi-organelle or
   multi-disease projects like `projects/MEMBRANE_CONTACT_SITES.md`):
   Place the shared structural hub on the left 55% (for example the ER/SR
   network tethered to 6 distinct partner organelles, each with its own tether
   proteins and disease badge) and the conserved downstream cascade on the
   right 45%.

## Usage

Compile a prompt from any module YAML or project Markdown file:

```bash
python3 experiments/graphical_abstracts/compile_prompt.py \
  kb/modules/fibrotic_response.yaml --style dismech-dsl --dry-run
```

Generate a PNG via the Gemini API (`GEMINI_API_KEY` or `GOOGLE_API_KEY`):

```bash
python3 experiments/graphical_abstracts/compile_prompt.py \
  kb/modules/fibrotic_response.yaml --style dismech-dsl \
  --output experiments/graphical_abstracts/runs/fibrotic_response.png
```
