# Glutamate Receptor, Ionotropic, Gene-Related Neurodevelopmental Disorders Curation Project

## Overview

This project organizes curation of Mendelian neurodevelopmental disorders caused
by ionotropic glutamate receptor subunit genes, starting with:

- GRIN1-related neurodevelopmental disorder
- GRIN2A-related neurodevelopmental disorder
- GRIN2B-related neurodevelopmental disorder
- GRIN2D-related neurodevelopmental disorder
- GRIA2-related neurodevelopmental disorder

These disorders sit at the overlap of neurodevelopmental disorder, epilepsy /
developmental and epileptic encephalopathy, language disorder, and movement
disorder curation. The shared biological theme is impaired ionotropic glutamate
receptor function at excitatory synapses, but the clinically useful pathograph
is not identical across genes. The goal in dismech is therefore not to create a
single generic "glutamate receptor disorder" entry, but to curate gene-centered
entries that preserve receptor-subunit-specific mechanisms and treatment
questions.

This document is a project-level organizing brief, not an assertion that all of
these entities should collapse into one umbrella disease file.

## Practical Modeling Decision For dismech

### Recommendation: gene-level files, project-level umbrella

| Structure | Pattern | Rationale |
|-----------|---------|-----------|
| `projects/GRIN_DISORDERS.md` | Project umbrella | Tracks shared curation rules, ordering, and family-level questions |
| `GRIN1-related_Neurodevelopmental_Disorder.yaml` | Gene-level disorder file | Obligatory NMDA receptor subunit with broad, severe neurodevelopmental phenotype |
| `GRIN2A-related_Neurodevelopmental_Disorder.yaml` | Gene-level disorder file | Distinct epilepsy-language / epilepsy-aphasia weighting |
| `GRIN2B-related_Neurodevelopmental_Disorder.yaml` | Gene-level disorder file | Strong developmental and synaptic-circuit framing, often broader than epilepsy alone |
| `GRIN2D-related_Neurodevelopmental_Disorder.yaml` | Gene-level disorder file | Distinct early DEE / movement-disorder-heavy branch |
| `GRIA2-related_Neurodevelopmental_Disorder.yaml` | Gene-level disorder file | AMPA receptor biology is related but not the same proximal module as GRIN/NMDA disorders |

### Why not one umbrella disease file by default?

- The affected receptor subunit changes the proximal biology, not just the
  severity label.
- NMDAR obligatory-subunit disease (`GRIN1`) is not equivalent to GluN2A,
  GluN2B, or GluN2D subunit disease.
- `GRIA2` belongs in the same project because it is an ionotropic glutamate
  receptor disorder, but its AMPA-receptor biology is distinct enough that it
  should not be forced under a GRIN/NMDA disease umbrella.
- The electroclinical pattern differs materially across genes: some are more
  epilepsy-aphasia weighted, some are broader developmental disorders with
  variable seizures, and some have a stronger hyperkinetic / infantile DEE
  profile.
- Variant-function-informed treatment logic may differ by gene and by
  gain-of-function vs loss-of-function direction, so over-lumping would hide
  clinically important distinctions.

### Why not split every syndrome label into its own file?

- Many named electroclinical labels in this space are downstream expressions of
  a shared gene/subunit mechanism rather than entirely different proximal
  pathobiology.
- Within a given gene, syndrome labels often differ more in age, seizure
  burden, language regression, or severity than in the earliest mechanistic
  trunk.
- Defaulting to gene-level entries keeps the pathograph coherent while still
  allowing `has_subtypes`, phenotype notes, or explicit variant-function notes
  where warranted.

## Working Granularity Rules

Split into separate top-level entries when:

- The causal gene or receptor family changes.
- The proximal receptor biology changes enough that the early pathograph would
  no longer be shared.
- Treatment logic is directionally different in a way that a shared file would
  obscure.
- The literature frames the entity as a distinct disease family with its own
  recurring clinical and mechanistic signal.

Keep within one gene-level entry when:

- The shared proximal mechanism is still altered function of the same receptor
  subunit.
- Reported phenotypic differences are mostly severity-weighting or downstream
  branch differences.
- The main curation problem is preserving functional direction
  (loss-of-function, gain-of-function, mixed effects), not inventing new root
  disease files.

Use `has_subtypes` or explicit within-file structure when:

- A gene has recurring functional subclasses with clear clinical value.
- A seizure-dominant branch and a developmental-dominant branch are both common
  enough to deserve internal organization.
- A gene has a well-recognized epilepsy-aphasia or movement-disorder-heavy
  branch that still shares the same proximal receptor mechanism.

## Existing KB Anchors

- `kb/disorders/CTCF-related_Neurodevelopmental_Disorder.yaml`
  - Useful precedent for a gene-first neurodevelopmental disorder entry rather
    than a broad syndrome bucket.
- `kb/disorders/Dravet_syndrome.yaml`
  - Useful precedent for a gene-driven developmental and epileptic
    encephalopathy entry with a clear circuit-level mechanistic chain.
- `kb/disorders/Epilepsy.yaml`
  - Useful umbrella precedent showing that broad epilepsy should not absorb all
    mechanism-specific subtype content.
- `projects/EPILEPSY.md`
  - Useful precedent for writing down split/lump rules before subtype curation.
- `projects/RETINOPATHIES.md`
  - Useful precedent for using a project document to distinguish project labels,
    family umbrellas, and true standalone disease entries.

Current state:

- There are no existing GRIN1 / GRIN2A / GRIN2B / GRIN2D / GRIA2 disorder files
  in `kb/disorders/`.
- A local MONDO search already resolves `GRIN1-related complex
  neurodevelopmental disorder`; exact MONDO labels and IDs for the other working
  targets should be confirmed during YAML creation rather than guessed here.

## Initial Target Set

| Disorder | Receptor class | Why it merits its own entry | Proposed file | Status |
|----------|----------------|-----------------------------|---------------|--------|
| GRIN1-related neurodevelopmental disorder | NMDA receptor, GluN1 subunit | Obligatory NMDAR subunit; broad and often severe developmental phenotype with seizures and movement abnormalities | `GRIN1-related_Neurodevelopmental_Disorder.yaml` | [ ] |
| GRIN2A-related neurodevelopmental disorder | NMDA receptor, GluN2A subunit | Distinct language / epilepsy-aphasia / focal epilepsy framing makes it more than a generic seizure branch | `GRIN2A-related_Neurodevelopmental_Disorder.yaml` | [ ] |
| GRIN2B-related neurodevelopmental disorder | NMDA receptor, GluN2B subunit | Strong neurodevelopmental and synaptic-plasticity framing, often broader than epilepsy alone | `GRIN2B-related_Neurodevelopmental_Disorder.yaml` | [ ] |
| GRIN2D-related neurodevelopmental disorder | NMDA receptor, GluN2D subunit | Early severe DEE and hyperkinetic movement signal is distinct enough to justify a dedicated file | `GRIN2D-related_Neurodevelopmental_Disorder.yaml` | [ ] |
| GRIA2-related neurodevelopmental disorder | AMPA receptor, GluA2 subunit | Related glutamatergic synaptopathy, but a different receptor family with distinct trafficking / excitatory-transmission questions | `GRIA2-related_Neurodevelopmental_Disorder.yaml` | [ ] |

## Shared Mechanistic Backbone To Capture

1. Pathogenic variants alter receptor subunit abundance, assembly, trafficking,
   agonist response, or channel gating.
2. Ionotropic glutamate receptor signaling becomes quantitatively or
   qualitatively abnormal at excitatory synapses.
3. Synaptic plasticity, dendritic maturation, and activity-dependent circuit
   refinement are disrupted during development.
4. Cortical, hippocampal, and thalamocortical network balance is altered,
   increasing risk of epileptiform activity and seizures.
5. Persistent circuit dysfunction contributes to developmental delay,
   intellectual disability, language impairment, autism-related features,
   hypotonia, and/or movement abnormalities.

This shared trunk should guide project-level consistency, but it should not
erase subunit-specific differences in receptor physiology.

## Gene-Specific Modeling Emphasis

### GRIN1

- Treat as the most general NMDAR-core entry in the set because GluN1 is an
  obligatory receptor subunit.
- Expect broad neurologic involvement: developmental delay / intellectual
  disability, epilepsy, hypotonia, and movement-disorder signal.
- Do not assume a single therapeutic direction across all variants; functional
  effect matters.

### GRIN2A

- Expect stronger language and epilepsy weighting than in several other GRIN
  disorders.
- Keep epilepsy-aphasia-style labels inside the gene-centered file unless a
  truly separate proximal mechanism emerges.
- Capture speech and language regression carefully as a major downstream branch,
  not as a substitute for pathophysiology.

### GRIN2B

- Expect a broader developmental-neurobiology framing, often with severe global
  delay / intellectual disability and variable epilepsy burden.
- Emphasize synaptic development, cortical circuit maturation, and plasticity
  disruption.
- Avoid over-centering epilepsy if the literature for a given branch is more
  developmental than electroclinical.

### GRIN2D

- Expect a relatively sharp infantile DEE / movement-disorder profile.
- Capture hyperkinetic or abnormal-movement features as a major downstream
  consequence of receptor dysfunction when supported.
- This may become the cleanest use case for an internal subtype split if
  recurrent functional subclasses prove treatment-relevant.

### GRIA2

- Keep in the same project because it belongs to the same ionotropic glutamate
  receptor mechanistic neighborhood.
- Model separately from the GRIN/NMDAR branch because AMPA receptor composition,
  trafficking, and excitatory-synaptic-strength effects are distinct.
- Treat it as the main adjacent-family test case for whether project-level
  curation rules generalize beyond NMDA receptor disorders.

## Family-Specific Curation Rules

- Do not create one disease file per named seizure syndrome by default.
- Do not generalize treatment response across genes or across functional
  directions within a gene.
- Where functional studies are central to interpretation, make the evidence type
  explicit (`HUMAN_CLINICAL` vs `IN_VITRO` vs `MODEL_ORGANISM`).
- Prefer exact receptor-function language in pathophysiology nodes
  ("altered NMDA receptor gating", "reduced surface expression", "impaired
  excitatory synaptic transmission") rather than vague "synaptic dysfunction"
  wording.
- Keep phenotypes downstream from mechanism nodes. Do not collapse "seizures",
  "language disorder", or "autism" into proximal mechanism descriptions.
- Revisit within-gene subtype structure only when there is enough repeated
  evidence that it improves curation clarity rather than creating ontology noise.

## Initial Execution Plan

1. Confirm exact MONDO label and ID for each target disorder before creating
   YAML files.
2. Start with `GRIN1-related_Neurodevelopmental_Disorder.yaml` as the anchor
   NMDAR-core entry.
3. Follow with `GRIN2A-related_Neurodevelopmental_Disorder.yaml` to establish
   the epilepsy-language branch pattern.
4. Curate `GRIN2B-related_Neurodevelopmental_Disorder.yaml` as the
   development-heavy counterpart.
5. Add `GRIN2D-related_Neurodevelopmental_Disorder.yaml` once the GRIN family
   template is stable.
6. Add `GRIA2-related_Neurodevelopmental_Disorder.yaml` as the adjacent AMPA
   receptor comparison case.
7. After the first 2-3 entries, decide whether a reusable project module or
   checklist is warranted for receptor-function direction, electrophysiology
   evidence, and precision-treatment notes.

## Open Curation Questions

- Should recurring gain-of-function vs loss-of-function branches be represented
  as `has_subtypes`, or is that too variant-specific for current dismech
  disease-level files?
- When a gene-specific disorder is strongly framed by an epilepsy-aphasia
  syndrome in the literature, should that syndrome live only in phenotypes /
  notes, or as an explicit subtype?
- Is there enough shared proximal biology across GRIN1 / GRIN2A / GRIN2B /
  GRIN2D to justify a future reusable pathophysiology module, even if no
  umbrella disease file is created?
- Should precision pharmacology observations be modeled only in treatments, or
  also summarized in pathophysiology notes when variant function directly
  determines response?

---
# STATUS

## Scope and Modeling
- [x] Defined the project as a gene-family curation program rather than a single
  umbrella disease entry
- [x] Identified five initial target disorders spanning NMDA and AMPA receptor
  biology
- [x] Recorded default modeling rule: gene-level files first, subtype structure
  only when mechanistically justified
- [x] Recorded the main family-specific curation risks: over-lumping, syndrome
  proliferation, and treatment overgeneralization

## Next Curation Steps
- [ ] Confirm exact MONDO mappings for GRIN2A / GRIN2B / GRIN2D / GRIA2 working
  targets
- [ ] Create `GRIN1-related_Neurodevelopmental_Disorder.yaml`
- [ ] Create `GRIN2A-related_Neurodevelopmental_Disorder.yaml`
- [ ] Create `GRIN2B-related_Neurodevelopmental_Disorder.yaml`
- [ ] Create `GRIN2D-related_Neurodevelopmental_Disorder.yaml`
- [ ] Create `GRIA2-related_Neurodevelopmental_Disorder.yaml`
- [ ] Reassess whether reusable within-family subtype conventions are needed

# NOTES

## 2026-04-09

- Added an ionotropic glutamate receptor neurodevelopmental disorders project
  brief to guide future dismech curation.
- Chose a project-level umbrella with gene-level disease files as the default
  pattern.
- Kept `GRIA2` in scope because it is mechanistically adjacent and useful for
  comparison, while explicitly not forcing it into a GRIN/NMDA disease umbrella.
- Recorded the main curation stance that named electroclinical syndromes should
  not automatically become separate root entries when the proximal receptor
  mechanism is still gene-centered.
