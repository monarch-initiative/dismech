---
name: graphical-abstract
description: >
  Create, audit, and wire journal-grade graphical abstracts for dismech
  mechanism modules (kb/modules/*.yaml), curation projects (projects/*.md),
  disease entries (kb/disorders/*.yaml), groupings (kb/groupings/*.yaml), and
  module collections (kb/module_collections/*.yaml). Covers the three Dismech
  layout archetypes (Hybrid Subcellular Cutaway, Multi-Stage Horizontal Role
  Cascade, and Radial Hub + Pathophysiology Cascade), the Dismech House Style
  Contract, prompt compilation with experiments/graphical_abstracts/compile_prompt.py,
  mandatory pixel-level scientific auditing, and populating the graphical_abstract
  schema slot.
---

# Create a DisMech Graphical Abstract

## When to use

- The user asks to generate, refine, or update a **graphical abstract** for a
  mechanism module (`kb/modules/*.yaml`), curation project (`projects/*.md`),
  disease entry (`kb/disorders/*.yaml`), grouping (`kb/groupings/*.yaml`), or
  module collection (`kb/module_collections/*.yaml`).
- You are curating a new flagship module or project and want to populate its
  `graphical_abstract` slot so the rendered HTML page displays a visual summary
  below the header.

---

## Core principle: Scene-Graph DSL over freeform prompts

Never send a freeform narrative paragraph to an image generation model for a
scientific pathway. Unconstrained narrative prompts reliably fail in four ways:

1. **Garbled text & pseudo-Latin typos** when panel titles or callouts exceed
   4 words.
2. **Hallucinated chemical structures & nonsense DNA strings** (e.g., invented
   bicyclic sulfur rings for `2'3'-cGAMP` or invalid base strings like
   `ACCVCXCAGUGGGCGAC`).
3. **Inverted causal polarity** (drawing `dsDNA → TREX1 Deficiency` instead of
   `TREX1 ✕` removing the `⊣` degradation brake on cytosolic `dsDNA`).
4. **Duplicated organelles across panels** when a single intracellular pathway
   is split into separate boxed cards (causing the model to draw two Golgi
   stacks or invert `ER-STING → PERK` into `Golgi ⊣ PERK`).

Instead, compile the entry's structured `pathophysiology` graph (or project
frontmatter + architecture tables) into an **explicit spatial scene-graph
specification** using one of the three **Dismech Layout Archetypes** below.

---

## Step 1: Choose the right Layout Archetype

Match the biological topology of the target entry to one of three canonical
16:9 widescreen archetypes:

### Archetype 1 — Hybrid Subcellular Cutaway + Outcome Bifurcation (`--style hybrid`)
- **Best for**: Intracellular signaling, trafficking, and organelle-coupled
  modules (`cgas_sting_pathway_activation`, `autophagy_dysregulation`,
  `unfolded_protein_response`, `inflammasome_activation`).
- **Spatial architecture**:
  - **Left 68%**: A **single continuous rounded eukaryotic cell cutaway**
    subdivided into 3 vertical stage zones by subtle background tint bands and
    top stage pill badges (`[1. TRIGGER]`, `[2. AMPLIFIER]`,
    `[3. CENTRAL EFFECTOR]`) — **not** separate boxed cards. Each organelle
    (ER, COPII/COPI vesicles, Golgi cisternae, Nucleus) is drawn **once** so
    trafficking and signaling arrows cross zone boundaries continuously.
  - **Right 32%**: Stacked rounded outcome cards (`[4. SIGNAL-STRENGTH BIFURCATION]`)
    receiving arrows from the cell cutaway:
    - **Card 4A (Pathogenic — red border `#fecaca`)**: Chronic disease states,
      GOF/LOF genetic entries, and counter-regulatory tissue damage.
    - **Card 4B (Therapeutic — green border `#bbf7d0`)**: Controlled
      pharmacological agonism/antagonism (`⊕`) and adaptive clinical responses.

### Archetype 2 — Multi-Stage Horizontal Role Cascade (`--style dismech-dsl`)
- **Best for**: Tissue-scale, multi-cellular, or sequential cell-state cascades
  where stages occur across distinct cell populations or extracellular matrices
  (`fibrotic_response`, `granuloma_formation`, `atherogenesis`,
  `complement_mediated_injury`).
- **Spatial architecture**:
  - **5 equal-width vertical rounded cards** arranged left-to-right across the
    canvas, linked by bold `#00838f` chevron arrows (`→`):
    `[1. TRIGGER]` → `[2. AMPLIFIER]` → `[3. CENTRAL EFFECTOR ★]` →
    `[4. EFFECTOR]` → `[5. CONSEQUENCE]`.
  - Highlight `[3. CENTRAL EFFECTOR]` with a `#00838f` 2px border and
    `KEY CONFORMANCE TARGET` pill badge.
  - Include a compact bottom strip inside Card 5 showing **Organ-Specific
    Conformers** (e.g., `Liver: HSC • Lung: IPF Fibroblast • Kidney: Pericyte`)
    and a feedback loop arrow from Card 5 (`ECM Stiffening`) back to Card 3.

### Archetype 3 — Radial Structural Hub + Pathophysiology Cascade
- **Best for**: Multi-organelle or multi-disease curation projects
  (`projects/MEMBRANE_CONTACT_SITES.md`, `projects/CILIOPATHIES.md`) where a
  shared structural complex or anatomical hub branches into multiple genetic
  syndromes.
- **Spatial architecture**:
  - **Left 55% (`[A. STRUCTURAL HUB]`)**: Central anchor organelle/structure
    (e.g., Endoplasmic Reticulum hub) surrounded radially by 5–6 partner
    organelles at labeled tether bridges (`10–30 nm`), with each contact bridge
    carrying a crisp callout box naming its tether proteins and distinct
    disease bullets.
  - **Right 45% (`[B. SHARED PATHOPHYSIOLOGY CASCADE]`)**: 3 vertically stacked
    stage cards (`[1. TETHER & LIPID TRANSFER FAILURE]` →
    `[2. ORGANELLE STRESS & HOMEOSTATIC COLLAPSE]` →
    `[3. CELLULAR DEGENERATION & CLINICAL SPECTRUM]`) connected by downward
    `#00838f` arrows.

---

## Step 2: Enforce the Dismech House Style Contract

Every graphical abstract prompt must include these exact visual constraints so
all illustrations across the knowledge base share a unified *Cell Press* /
*Nature Reviews* 2D vector aesthetic:

1. **Color Palette** (matches `src/dismech/templates/_palette.css.j2`):
   - Canvas background: `#f8fafc` (`--gray-50`)
   - Top header banner: `#00838f` (`--teal`) with white bold title and category pills
   - Card surface: `#ffffff` with `1.5px solid #cbd5e1` border
   - Central effector / hub highlight: `#f0f9fa` (`--teal-50`) with `2px solid #00838f` border
   - Pathogenic / LOF / GOF accents: `#fee2e2` fill, `#991b1b` text, `#dc2626` T-bar/badge
   - Therapeutic / agonist accents: `#dcfce7` fill, `#166534` text
   - Organelle & protein fills: softamber `#fef3c7` (`#92400e` stroke), soft pink
     `#fce7f3` (`#9d174d` stroke), soft blue `#dbeafe` (`#1e40af` stroke), soft
     violet `#ede9fe` (`#5b21b6` stroke)
2. **Explicit Symbol Grammar & Bottom Legend Bar**:
   - `→` Solid dark-teal arrow (`#00838f`): Direct activation / forward trafficking / stimulation
   - `⊣` Flat red T-bar (`#dc2626`): Direct inhibition / repression / retrograde retrieval
   - `✕` Red badge (`#fee2e2` fill, `#991b1b` text): Loss-of-function (LOF) defect
   - `⚡` Red/orange star badge: Gain-of-function (GOF) constitutive activation
   - `⊕` Green pill badge (`#dcfce7` fill, `#166534` text): Pharmacological agonist / therapeutic intervention
3. **Typography & Label Density Budget**:
   - Maximum **2–4 words per text label**.
   - Never place full prose sentences inside the canvas.
   - All text must be strictly horizontal (`0°` rotation) in clean geometric
     sans-serif (`Inter` / `Helvetica Neue` style).
4. **Hard Negative Prompt Bans**:
   - **NO chemical structural formulas** (never draw purine/pyrimidine rings,
     bond lines, or atom letters `N, O, P, S, NH2`; represent small molecules
     like `2'3'-cGAMP` as a clean rounded geometric pill badge).
   - **NO nucleotide or amino-acid sequence strings** (never write `ATCG...`).
   - **NO 3D photorealistic rendering**, glossy spheres, lens flares, or dark
     neon backgrounds.

---

## Step 3: Compile the prompt and generate the image

Use `experiments/graphical_abstracts/compile_prompt.py` to inspect or customize
the structured prompt for a module YAML or project Markdown file:

```bash
# Preview the compiled Hybrid Cutaway + Dismech DSL prompt (Archetype 1)
python3 experiments/graphical_abstracts/compile_prompt.py \
  kb/modules/cgas_sting_pathway_activation.yaml \
  --style hybrid --dry-run

# Preview the Multi-Stage Horizontal Role Cascade prompt (Archetype 2)
python3 experiments/graphical_abstracts/compile_prompt.py \
  kb/modules/fibrotic_response.yaml \
  --style dismech-dsl --dry-run

# Generate PNG directly via Gemini REST API (requires GEMINI_API_KEY / GOOGLE_API_KEY)
python3 experiments/graphical_abstracts/compile_prompt.py \
  kb/modules/cgas_sting_pathway_activation.yaml \
  --style hybrid \
  --output assets/graphical_abstracts/cgas_sting_pathway_activation.png
```

When invoking an `image-generator` subagent or calling Gemini directly, pass the
compiled scene-graph specification verbatim and save the resulting 16:9 PNG to
`assets/graphical_abstracts/<slug>.png`.

---

## Step 4: Mandatory Pixel-Level Visual & Scientific Audit

**Never commit a generated graphical abstract without visually inspecting the
rendered PNG image.** Check every text label and arrow against these four gates:

1. **Zero Typos / Exact HGNC & Protein Symbols**:
   - Read every header, pill badge, protein label, and disease name in the PNG.
   - Reject and regenerate if any label has garbled characters, merged words,
     or misspelled gene symbols.
2. **Causal Arrow (`→`) and Inhibitory T-Bar (`⊣`) Polarity**:
   - Verify every arrow's source, target, and head (`→` vs `⊣`) against the
     YAML `pathophysiology` `downstream` edges and `notes`.
   - Confirm LOF defects (`✕`) are drawn on the enzyme/tether that fails (e.g.,
     `TREX1 ✕` removing its `⊣` brake on `dsDNA`), never as the target of the
     substrate.
3. **Anatomical Continuity (Archetype 1)**:
   - Confirm that the ER, Golgi, and Nucleus are each drawn **once** inside the
     unified cell cutaway, with no duplicate organelles across stage bands.
4. **Distinct Disease / Gene Bullets (Archetype 3)**:
   - Confirm that distinct disorders at the same contact site or node (e.g.,
     `VPS13A (ChAc)` and `XK (McLeod)`) are listed as separate lines and not
     collapsed into a single hybrid string.

---

## Step 5: Wire `graphical_abstract` with a checkable `legend` and verify sync

Every `graphical_abstract` block MUST include a structured `legend` whose panels
map the visual zones of the figure to the entry's pathograph nodes using
`<kind>#<name>` foreign-key entity references in `attaches_to`.

1. Save the verified PNG at `assets/graphical_abstracts/<slug>.png`.
2. Populate the structured `graphical_abstract` block on the entry:
   - In `kb/modules/<slug>.yaml`, `kb/disorders/<slug>.yaml`,
     `kb/groupings/<slug>.yaml`, or `kb/module_collections/<slug>.yaml`:
     ```yaml
     graphical_abstract:
       image_path: assets/graphical_abstracts/<slug>.png
       archetype: HORIZONTAL_ROLE_CASCADE
       caption: >-
         Concise summary of the mechanism and model alignment shown in the figure.
       legend:
       - panel: "1. Trigger"
         depicts: >-
           Visual description of Panel 1 and its outgoing causal arrow.
         attaches_to:
         - pathophysiology#Tissue Injury
       - panel: "Experimental Model"
         depicts: >-
           Assay platform and readouts recapitulating the central nodes.
         attaches_to:
         - experimental_models#Scar-in-a-Jar macromolecular-crowding fibroblast fibrosis assay
         - pathophysiology#Mesenchymal Cell Activation
     ```
   - In `projects/<SLUG>.md` YAML frontmatter, use `modules#<slug>`,
     `diseases#<slug>`, or `groupings#<slug>` in `attaches_to`.
3. Run the **bidirectional pathograph-to-figure sync checks**:
   ```bash
   # Forward FK check (every attaches_to resolves to a real node in the entry)
   python3 scripts/check_entity_refs.py kb/modules/<slug>.yaml

   # Bidirectional graphical abstract sync check (image exists, every attaches_to
   # resolves, AND every pathograph node is covered by at least one legend panel)
   python3 scripts/check_graphical_abstracts.py kb/modules/<slug>.yaml
   ```
4. When editing a curated file under `kb/` or `src/dismech/schema/`, record an
   append-only history entry via `just new-history`.
5. Validate and regenerate the HTML page:
   ```bash
   just validate-module kb/modules/<slug>.yaml
   just gen-module-pages
   # or for a project:
   just gen-project-page projects/<SLUG>.md
   ```

---

## Step 6: Escape Hatch When Editing a Module Without an Image Model (`todo`)

If you (or a curator) edit a module's or disorder's pathograph (adding,
renaming, or removing a `pathophysiology`, `treatments`, or model node) **without
access to an image generation model**, use the `todo` escape hatch on the
affected `GraphicalAbstractPanel` (or at the top level of `graphical_abstract`)
so the PR passes validation while flagging the exact visual update needed:

1. **Adding a new pathograph node**: Add a `TODO` legend panel (or add `todo:`
   to the existing panel where the node belongs):
   ```yaml
   - panel: "TODO"
     todo: "Add Myofibroblast Senescence node downstream of Mesenchymal Cell Activation"
     attaches_to:
     - pathophysiology#Myofibroblast Senescence
   ```
2. **Renaming or deleting a pathograph node shown in an existing panel**: Add
   `todo:` on that `GraphicalAbstractPanel` explaining the visual change needed:
   ```yaml
   - panel: "4. Effector (ECM Deposition)"
     depicts: "Dense collagen I/III and fibronectin fibrils..."
     todo: "Redraw Panel 4 to reflect renamed/updated ECM node"
     attaches_to:
     - pathophysiology#Extracellular Matrix Deposition
   ```
   Setting `todo` (or `panel: "TODO"`) on a legend panel bypasses strict
   foreign-key and coverage errors for that legend node in both
   `scripts/check_entity_refs.py` and `scripts/check_graphical_abstracts.py`,
   and renders a visible amber `⚠ Redraw TODO` badge in the HTML figure legend.
3. **Finding and clearing pending redraw TODOs** (when an image model is
   available):
   ```bash
   # List all graphical abstract panels across the KB with pending redraw TODOs
   python3 scripts/check_graphical_abstracts.py --list-todos

   # Audit strictly (exit 1 if any TODO escape hatch remains)
   python3 scripts/check_graphical_abstracts.py --fail-on-todo
   ```
