---
title: What a Classification of Pathograph Nodes Would Look Like
status: BRAINSTORM
description: >-
  Design brainstorm for classifying pathograph nodes. Surveys the 12,290
  pathophysiology nodes (plus ~52k nodes from the other eight linked sections)
  to show that "node type" is not one axis but five or six orthogonal facets,
  that two of them already exist, that one is being improvised in a 55-value
  free-text `role` vocabulary, and that most of what curators are hand-typing
  is derivable from graph topology. Proposes a facet model, a derivability
  test for deciding what earns a slot, and a feasibility survey as next step.
tags: [SCHEMA_EVOLUTION, PATHOGRAPH, PATHOPHYSIOLOGY, BRAINSTORM]
---

# What a Classification of Pathograph Nodes Would Look Like

**Status: brainstorm.** Nothing here is a schema proposal yet. The point is to
lay out the design space, show which parts of it are already occupied, and
identify the one facet that is genuinely missing.

## 1. What "node type" means today

There are two answers, and neither is a classification of what the node *is*.

**In the renderer,** `NodeInfo.node_type` (`src/dismech/graph.py`) records
**which YAML section the node came from** — `pathophysiology`, `phenotype`,
`environmental`, `genetic`, `treatment`, `biochemical`, `experimental_model`,
`animal_model`, `computational_model`, plus `orphan` for a dangling target. It
drives shape and colour in the D3 pathograph and nothing else. It is
provenance, not semantics: every one of the 12,290 pathophysiology nodes gets
the same blue rounded rectangle whether it denotes a kinase activity, a
granuloma, or organ failure.

**In the exporter,** there is no node type at all. `kgx_export.py` emits
Disease→X *associations* (`biolink:affects`, `biolink:has_participant`, …); the
pathophysiology node itself never becomes a KGX node, so it carries no
`biolink:` category. The pathograph is the one dismech artifact whose central
objects are invisible to the knowledge-graph layer.

So the honest baseline is: **pathograph nodes are currently classified by where
they were written down, not by what they are.**

## 2. What the corpus actually looks like

Counts across `kb/disorders/` + `kb/modules/` (2,094 files):

| Section | Entries |
|---|---:|
| phenotypes | 23,099 |
| **pathophysiology** | **12,290** |
| treatments | 8,363 |
| genetic | 4,854 |
| biochemical | 1,903 |
| environmental | 919 |
| animal_models | 488 |
| experimental_models | 231 |
| computational_models | 44 |

Pathophysiology is where the classification problem lives — the other sections
are already typed by their own class, and their nodes join the graph through
one explicit linking slot each. Within pathophysiology:

| Slot | Coverage |
|---|---:|
| `description` | 100.0% |
| `evidence` | 96.0% |
| `downstream` | 81.1% |
| `biological_processes` (GO BP) | 69.0% |
| `cell_types` (CL) | 52.2% |
| `biological_scale` | 30.1% |
| `locations` (UBERON) | 23.1% |
| `role` | 18.9% |
| `conforms_to` | 13.0% |
| `mechanism_confidence` | 6.6% |
| `molecular_functions` (GO MF) | 5.3% |

Two facts to carry forward. **14.3% of nodes carry no ontology grounding at
all** (no BP, MF, CL, UBERON, or CHEBI) — so any classification that is purely
*derived* from grounding leaves a seventh of the corpus untyped. And
`biological_scale`, the one deliberate classification slot, is at 30% adoption
after being added — a realistic ceiling to plan against.

## 3. The central claim

**"Node classification" is not one axis. It is five or six orthogonal facets,
and the failure mode is trying to make one enum carry all of them.**

The evidence for that failure mode is already in the repo. `role` is a free-text
`string` slot with an `examples: [Primary]` and no enum. 2,322 nodes use it,
with **55 distinct values after normalising case and spacing** (72 before —
`trigger`, `TRIGGER`, and `Trigger` all occur). The distribution is sharply
Zipfian:

| Value | n | | Value | n |
|---|---:|---|---|---:|
| trigger | 472 | | therapeutic_vulnerability | 91 |
| consequence | 384 | | intermediate | 34 |
| central_effector | 362 | | mechanism | 31 |
| effector | 327 | | driver | 30 |
| amplifier | 213 | | adaptive_escape | 30 |
| mediator | 122 | | modifier | 29 |
| outcome | 94 | | *(41 more, ≤13 each)* | 227 |

The top eight cover 90% of usage. The tail is where the conflation shows: a
single slot is being asked to encode **causal position** (`upstream`, `root`,
`endpoint`, `convergence_point`), **epistemic status**
(`provisional_effector`, `emerging_mechanism`, `disputed_branch`,
`provisional_trigger`), **causal direction** (`protective`, `host_defense`),
and **therapeutic interface** (`therapeutic_vulnerability`,
`intrinsic_resistance`, `resistance_mechanism`). Those are four different
questions. Curators reached for one slot because it was the only one there.

## 4. The facets

### F1 — Section / provenance *(exists; derived; leave alone)*

`NodeInfo.node_type`. Computed, never curated, drives shape and colour. Its one
gap is that it has no `biolink:` counterpart in the export layer.

### F2 — Biological scale *(exists; curated; `BiologicalScaleEnum`)*

`MOLECULAR` / `CELLULAR` / `TISSUE` / `ORGANISM`, 30.1% populated. The
[feasibility survey](../../../projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md)
established that four values suffice and that forcing a single assignment
surfaces bundled nodes (~41% of the sample were split candidates). Crucially,
that survey **deliberately declined the state-vs-process distinction** — the
enum was renamed from `kind:` to `biological_scale:` precisely because its
values encode scale only. That decision is what leaves F3 open.

### F3 — Ontological character *(MISSING — this is the real gap)*

What *kind of thing* is the node: an occurrent, a state, a structure, a
substance, a disposition? This is the facet with no slot, and the one where
dismech already has a house convention it has not generalised.

The **Xogenesis** module convention (`granuloma_formation`, `thrombogenesis`,
`atherogenesis`, `amyloidogenesis`, `renal_cystogenesis`) already anchors
pathological-structure formation against OGMS:

- `OGMS:0000061` pathological bodily process
- `OGMS:0000078` pathological anatomical structure (granuloma, atheroma, cyst)
- `OGMS:0000079` portion of pathological body substance (amyloid deposit)
- `OGMS:0000080` pathological transformation
- `OGMS:0000081` pathological derivation

That is a ready-made upper-ontology typology, already vetted by this project —
but it lives in **prose, in five files**. Generalising it to a node slot is the
obvious move. A candidate enum:

| Value | Anchor | Reads as | Example node |
|---|---|---|---|
| `PROCESS` | OGMS:0000061 / GO BP / GO MF | something occurring | *Amyloid Fibril Formation and Extracellular Deposition* |
| `STATE` | PATO quality | a persisting condition | *Biallelic HMGCL loss of function* |
| `STRUCTURE` | OGMS:0000078 / MPATH | a pathological thing that now exists | *Platelet-rich intraluminal thrombus* |
| `SUBSTANCE` | OGMS:0000079 | a pathological portion of matter | *Progressive Multi-Organ Amyloid Accumulation* |
| `DISPOSITION` | BFO disposition | a latent tendency, not yet realised | *Increased Seizure Susceptibility* |

Crude lexical proxies over node names give a rough sense of the population —
~11% state-shaped (`deficiency`, `haploinsufficiency`, `accumulation`), ~13%
process-shaped (`activation`, `signaling`, `degeneration`), ~2%
disposition-shaped (`susceptibility`, `substrate`, `vulnerability`), ~1.4%
structure-shaped. **Do not trust those numbers.** The head-noun distribution
(`dysfunction` 4.7%, `activation` 3.1%, `deficiency` 3.0%, `failure` 2.4%,
`dysregulation` 2.1%) shows how many names are ambiguous by construction —
"dysfunction" is a state, a process, and an outcome depending on the node. Name
lexicon can seed a survey; it cannot substitute for one.

`DISPOSITION` is the value that earns its keep. It is the only way to say that
*Arrhythmogenic Substrate and Triggered Activity* or *Exon-Skipping-Addressable
Reading-Frame Lesion* is a **standing vulnerability** rather than an event —
which is exactly what a therapy-targetable node is, and exactly what the
`therapeutic_vulnerability` role value has been improvising.

### F4 — Causal position *(exists as free-text `role`; mostly derivable)*

Here is the finding that should shape the proposal. Cross-tabulating curated
`role` against pure graph topology (in-degree/out-degree within the
pathophysiology subgraph):

| role | n | source | internal | sink | isolated |
|---|---:|---:|---:|---:|---:|
| trigger | 352 | **89%** | 11% | 0% | 0% |
| mediator | 122 | 1% | **99%** | 0% | 0% |
| central_effector | 257 | 4% | **96%** | 0% | 0% |
| amplifier | 140 | 4% | **95%** | 1% | 0% |
| intermediate | 34 | 0% | **100%** | 0% | 0% |
| effector | 224 | 2% | 82% | 15% | 1% |
| consequence | 270 | 0% | 55% | **44%** | 1% |
| outcome | 86 | 0% | 56% | **44%** | 0% |
| therapeutic_vulnerability | 67 | 16% | 15% | 13% | **55%** |

`trigger` is 89% graph sources. `mediator`/`intermediate`/`central_effector`/
`amplifier` are 95–100% interior. `consequence` and `outcome` are
indistinguishable from each other. **Most of `role` is re-typing what the edges
already say** — which is why 41 tail values drifted: nothing anchored them.

Two things follow:

1. **Compute the position, don't curate it.** `SOURCE` / `INTERMEDIATE` /
   `SINK` / `ISOLATED` are free, exact, and never drift. Render them; query on
   them; don't ask a curator for them.
2. **The residue is the interesting part.** What topology *cannot* tell you is
   the distinction between `mediator` (passes signal through) and `amplifier`
   (increases magnitude) and `central_effector` (the convergence hub the
   disease turns on) — all three are 95–100% interior. That is a real curatorial
   judgement about *causal function*, and it is the only part of `role` worth
   keeping as a curated slot.

`therapeutic_vulnerability` at 55% **isolated** is its own signal: those nodes
have no pathophysiology edges at all, and exist purely as targets of
`treatments.target_mechanisms`. They are not causal-position claims — they are
F6 claims wearing F4's clothes.

### F5 — Epistemic status *(exists; scattered across three mechanisms)*

Already expressible three different ways: `mechanism_confidence`
(`ESTABLISHED` 373 / `PROVISIONAL` 348 / `HYPOTHETICAL` 89 — 6.6% coverage),
edge-level `hypothesis_groups` → `mechanistic_hypotheses[].status`, and
`discussions` of kind `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH`. Plus the
improvised `role` values (`provisional_effector`, `emerging_mechanism`,
`disputed_branch`). Not a missing facet — an **un-unified** one. Worth a
consolidation pass, not a new enum.

### F6 — Interface / actionability *(fully derivable; should never be curated)*

Whether a node is targeted by a treatment (`target_mechanisms`), measured by a
model (`modeled_mechanisms`), read out by a biomarker (`biochemical.readouts`),
modifiable by an exposure (`influences_mechanisms`), or conformant to a module
(`conforms_to`). All of it is already in the edges. This is a **rendering and
query facet**, and the fact that curators hand-typed `therapeutic_vulnerability`
91 times for something the graph already knows is the argument for computing it.

## 5. A test for what earns a slot

Proposed rule, which the data above motivates:

> **Derivability test.** If a facet is computable from graph topology plus
> already-populated slots, compute it. Only ask a curator for what no
> computation can recover.

Applied:

| Facet | Verdict |
|---|---|
| F1 provenance | derive (already does) |
| F2 scale | **curate** — not recoverable from grounding alone |
| F3 ontological character | **curate**, partly seedable from GO BP vs PATO vs OGMS grounding |
| F4 causal position | derive; **curate only** the mediator/amplifier/hub residue |
| F5 epistemic status | curate, but unify the three existing mechanisms first |
| F6 actionability | derive |

This turns a 55-value free-text slot into roughly **one new curated enum (F3),
one narrowed curated enum (F4-residue), and two computed properties**.

## 6. What it would buy

- **Cross-disease queries that don't work today.** "Every pathological
  structure formed across the KB" (F3 = STRUCTURE), "every standing therapeutic
  vulnerability" (F3 = DISPOSITION ∧ F6 targeted), "every hypothetical
  convergence hub" (F4-residue = hub ∧ F5 = HYPOTHETICAL).
- **A KGX/biolink category for pathograph nodes.** F3 maps almost directly:
  PROCESS → `biolink:BiologicalProcess` / `biolink:MolecularActivity`,
  STRUCTURE → `biolink:AnatomicalEntity`, SUBSTANCE →
  `biolink:ChemicalEntity`. That would let the pathograph's central objects
  exist in the exported graph at all.
- **QC rules with teeth.** A `STRUCTURE` node with no UBERON site, a
  `DISPOSITION` node with outgoing `causes` edges (a disposition that is
  already realised is a modelling error), a `PROCESS` node grounded only in
  PATO.
- **Better layout.** Shape by character rather than by section would let a
  reader distinguish a granuloma from the process that forms it — currently
  both are blue rounded rectangles.
- **Sharper module conformance.** A disorder node conforming to a module node
  of a different ontological character is a likely mis-mapping.
- **Bundle detection, again.** The scale survey found 41% split candidates. A
  node that is genuinely both PROCESS and STRUCTURE (*"Amyloid Fibril Formation
  and Extracellular Deposition"* — the forming and the formed) is exactly the
  bundle the Xogenesis convention already splits by hand.

## 7. Risks and open questions

- **Adoption ceiling.** `biological_scale` sits at 30% after being added. A
  second optional facet plausibly lands lower. Seeding F3 from existing GO/PATO
  grounding (69% have GO BP) could bootstrap it — but 14.3% of nodes have no
  grounding at all and would stay untyped.
- **Process/state really is hard.** The scale survey walked away from this
  distinction deliberately. Pass 1 of that survey, which used process-suffixed
  enum names, produced 29% ambiguity and 4% "propose a new kind"; renaming to
  scale-only drove both to near zero. F3 walks straight back into the problem
  the rename solved. That is a reason to survey it carefully, not a reason to
  skip it — but the burden of proof is on F3.
- **`role` migration is not free.** 2,322 nodes, 55 values. The mapping is
  mostly mechanical for the top eight but the 41-value tail needs judgement,
  and some values (`adaptive_escape`, `intrinsic_resistance`, `immune_evasion`)
  are arguably domain content that belongs in `description`, not any enum.
- **Do phenotype nodes need F3 too?** 23,099 phenotype entries dwarf
  pathophysiology. HP terms carry their own character implicitly. Probably out
  of scope for a first pass — but "disease-like phenotype" modules
  (`osteoporosis_bone_resorption` et al.) blur the line.
- **Single-value discipline.** F2 enforces it and uses violations as a split
  signal. F3 should do the same, for the same reason.

## 8. Suggested next step

Mirror what worked for `biological_scale`: a **three-pass LLM classification
survey** over a stratified sample of ~100 pathophysiology nodes, testing the
F3 enum (5 values, OGMS-anchored) with split-detection as a co-equal task. The
pass-1/pass-2/pass-3 structure of the scale survey is directly reusable, and
its lesson — that enum *naming* drove the ambiguity rate more than enum
*content* did — is the specific thing to control for here.

Cheap and independent of that survey, and worth doing regardless:

1. **Normalise `role` casing** (`TRIGGER`/`Trigger` → `trigger`) — 3 variants
   of one value today.
2. **Compute and expose F4 position and F6 actionability** in
   `graph_to_json`. No schema change, no curation, immediate query value.
3. **Enumerate `role`** at the top eight values with the tail mapped or moved
   to `description`, *after* deciding how much of it F4-derivation absorbs.

## Appendix — reproducing the numbers

Every figure above comes from reading `kb/disorders/*.yaml` and
`kb/modules/*.yaml` with `dismech.yaml_io.safe_load` and counting: slot
presence per `pathophysiology` node; `role` values normalised with
`.strip().lower().replace(' ', '_')`; and in-/out-degree computed over
`downstream[].target` edges restricted to targets that resolve to a
pathophysiology node in the same file (so cross-section targets are excluded
from the topology cross-tab). Section counts are `len()` of each top-level list.
