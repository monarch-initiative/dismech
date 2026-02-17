# Epilepsy Granularity and Mechanism Curation Project

## Overview

This project records a practical curation plan for representing epilepsy in dismech at a level where mechanisms are coherent and clinically useful.

It is based on current dismech granularity discussions and pathophysiology debundling work:
- https://github.com/monarch-initiative/dismech/issues/272
- https://github.com/monarch-initiative/dismech/issues/306
- https://github.com/monarch-initiative/dismech/issues/164
- https://github.com/monarch-initiative/dismech/issues/332
- https://github.com/monarch-initiative/dismech/pull/210

## Core Granularity Rules

Split into separate entries when:
- Pathophysiology is distinct.
- Treatment response differs (especially precision/targeted treatment implications).
- Prognosis or disease course differs materially.
- External disease resources treat entities as distinct.

Lump into one entry (with `has_subtypes`) when:
- Core mechanism is shared.
- Phenotypes and management substantially overlap.
- Splitting does not add practical curation/clinical value.

Pathophysiology modeling rule:
- Keep mechanisms atomic and causally linked.
- Do not mix phenotypes into mechanism events.

## Current KB Anchors

- Umbrella entry: `kb/disorders/Epilepsy.yaml` (`MONDO:0005027`)
  - Has broad subtype list at `kb/disorders/Epilepsy.yaml:10`.
  - Contains mechanism blocks that are partially subtype-specific (for example TLE/mTOR evidence), see `kb/disorders/Epilepsy.yaml:44`, `kb/disorders/Epilepsy.yaml:48`, `kb/disorders/Epilepsy.yaml:136`.
- Existing mechanistically coherent subtype-level entries:
  - `kb/disorders/Dravet_syndrome.yaml` (`MONDO:0100135`) with a clear SCN1A -> interneuron dysfunction -> hyperexcitability chain at `kb/disorders/Dravet_syndrome.yaml:17` and `kb/disorders/Dravet_syndrome.yaml:50`.
  - `kb/disorders/Jeavons_Syndrome.yaml` (`MONDO:0015346`) with phenotype coherence but mixed-quality mechanism evidence (examples at `kb/disorders/Jeavons_Syndrome.yaml:50`, `kb/disorders/Jeavons_Syndrome.yaml:105`, `kb/disorders/Jeavons_Syndrome.yaml:149`).

## Starting Points (Mechanism-Coherent Lumps)

### 1. Temporal lobe epilepsy (TLE) as its own entry
- Why: current umbrella epilepsy evidence is partly TLE-specific.
- Evidence anchors: `kb/disorders/Epilepsy.yaml:44`, `kb/disorders/Epilepsy.yaml:48`, `kb/disorders/Epilepsy.yaml:189`.
- Proposed initial target file: `kb/disorders/Temporal_Lobe_Epilepsy.yaml`
- Status: [ ] Planned

### 2. mTOR-related focal epilepsy
- Why: coherent pathway-level mechanism with therapeutic relevance (mTOR inhibition).
- Evidence anchors: `kb/disorders/Epilepsy.yaml:122`, `kb/disorders/Epilepsy.yaml:136`, `kb/disorders/Epilepsy.yaml:144`.
- Proposed initial target file: `kb/disorders/mTOR_related_focal_epilepsy.yaml`
- Status: [ ] Planned

### 3. BBB-disruption-associated drug-resistant focal epilepsy
- Why: coherent endothelial/BBB mechanism with translational signal.
- Evidence anchors: `kb/disorders/Epilepsy.yaml:50`, `kb/disorders/Epilepsy.yaml:66`, `kb/disorders/Epilepsy.yaml:69`.
- Proposed initial target file: `kb/disorders/BBB_disruption_associated_focal_epilepsy.yaml`
- Status: [ ] Planned

### 4. SCN1A-related epileptic encephalopathy (Dravet spectrum)
- Why: already coherent and mostly in place; use as reference model for future sodium-channel DEE entries.
- Current anchor: `kb/disorders/Dravet_syndrome.yaml`
- Status: [ ] Consolidate and template

### 5. Photosensitive eyelid-myoclonia epilepsy family (Jeavons/EMA)
- Why: coherent electroclinical phenotype family; good candidate after evidence cleanup.
- Current anchor: `kb/disorders/Jeavons_Syndrome.yaml`
- Status: [ ] Cleanup first, then consider family-level structure

## Practical Modeling Decision for dismech

- Keep `Epilepsy` (`MONDO:0005027`) as umbrella/index-level entry.
- Move mechanism-specific causal chains into subtype-level entries where coherence is better.
- Keep umbrella entry concise and focused on cross-cutting mechanisms only.

## Initial Execution Plan

1. Create `Temporal_Lobe_Epilepsy.yaml` by refactoring TLE-specific content out of umbrella epilepsy.
2. Create `mTOR_related_focal_epilepsy.yaml` using the mTOR and dysmorphic neuron chain.
3. Keep `Dravet_syndrome.yaml` as the template for mechanistically coherent epilepsy subtype modeling.
4. Perform evidence quality pass on `Jeavons_Syndrome.yaml` before additional splitting.

## Notes

### 2026-02-16
- Recorded initial epilepsy granularity strategy and starting candidates.
- Strategy aligns with active granularity issues and prior pathophysiology debundling direction.
