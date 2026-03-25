# Dismech and Individual/Case-Level Data

## Overview

Dismech is a **disease-level knowledge layer** — it captures general mechanistic
knowledge about disorders (pathophysiology, phenotypes, genetics, treatments,
trajectories). It deliberately does not store individual patient records, cohort
datasets, or per-patient variant calls.

The question is: how does this knowledge model inform interpretation of
individual-level observations?

## Existing schema touchpoints

The schema already has several hooks into case-level data, though they are not
fully developed:

- **Phenopacket-store prefix** — a `phenopacket-store:` CURIE prefix exists for
  linking to GA4GH Phenopacket collections.
- **PHENOPACKETS dataset type** — datasets can be typed as case-level phenotype
  collections.
- **DIGITAL_TWIN computational model type** — patient-specific computational
  models are recognized as a model category.
- **Frequency enums** — phenotype frequencies (OBLIGATE through VERY_RARE)
  describe how often a phenotype appears across individuals with a given
  disorder.
- **Variants with clinical significance** — ACMG-style pathogenic/benign
  classification connects to individual variant interpretation.

## Use cases

### 1. Phenotype-driven differential diagnosis

A patient presents with a set of HPO-coded phenotypes. Dismech entries annotate
phenotypes with frequencies, categories, and mechanism links. An interpretation
system could:

- Match patient phenotypes against dismech phenotype lists.
- Rank candidate disorders by the proportion and frequency of matching
  phenotypes.
- Highlight *diagnostic* phenotypes (the `diagnostic: true` flag exists in the
  schema).
- Use the pathophysiology graph to check whether the patient's phenotype
  constellation is mechanistically coherent (i.e., the observed phenotypes can
  all be traced to a common upstream mechanism).

### 2. Variant interpretation in mechanistic context

A patient has a VUS (variant of uncertain significance) in gene X. Dismech
captures:

- Which genes are involved in which diseases (the `genetic` section with
  `GeneDescriptor`).
- How those genes participate in pathophysiology (pathway membership, downstream
  causal edges).
- Known variants and their clinical significance.
- Penetrance and expressivity estimates.

This lets you ask: *"Does this patient's variant sit in a gene whose known
mechanistic role explains their phenotype pattern?"* — going beyond simple
gene-disease association to mechanistic plausibility.

### 3. Treatment selection guided by pathophysiology subtype

Dismech links treatments to the pathophysiology mechanisms they target via
`TreatmentEffectEnum` (INHIBITS, ACTIVATES, BYPASSES, RESTORES). For a patient
whose subtype is known:

- Match the patient's subtype to the relevant pathophysiology branch.
- Identify treatments that target that specific mechanism.
- Use clinical trial data (already modeled in dismech) to assess evidence
  strength.
- Flag treatments that target the wrong mechanism for the patient's subtype.

### 4. Comorbidity trajectory prediction

The schema has a full comorbidity/trajectory model (`ComorbidityDirectionEnum`,
`AssociationSignalSourceEnum`, `CausalEdge` with `sequelae`). For an individual
with disease A:

- Query dismech for directed comorbidity pairs where A precedes B.
- Estimate risk based on population-level metrics (OR, HR, RR — all in
  `AssociationMetricTypeEnum`).
- Prioritize surveillance for downstream conditions.
- This is the "digital twin" use case — projecting a patient's disease
  trajectory from population-level mechanistic knowledge.

### 5. Phenopacket enrichment and annotation

A GA4GH Phenopacket describes an individual case. Dismech could enrich it by:

- Annotating each phenotype with its mechanistic context (which pathophysiology
  node produces it).
- Flagging phenotypes that are unexplained by the diagnosed disease's known
  mechanisms.
- Suggesting missing phenotypes that should be screened for given the mechanisms
  involved.
- Adding biological process and cell type context to raw HPO terms.

### 6. Case-cohort comparison

Compare an individual's phenotype profile against the "expected" profile from
dismech:

- Identify phenotypes the patient has that are VERY_RARE for their diagnosis
  (possible alternate or additional diagnosis).
- Identify OBLIGATE phenotypes they lack (possible misdiagnosis).
- Flag discordance between observed and expected severity or progression.

## Architectural model

The cleanest integration pattern treats dismech as an interpretive scaffold that
sits alongside — not within — individual data systems:

```
Individual data (Phenopackets / OMOP / FHIR)
        │
        ▼
   ┌─────────────────┐
   │  Interpretation  │  ← match, score, explain
   │     Engine       │
   └────────┬────────┘
            │
            ▼
   dismech knowledge base
   (mechanisms, phenotypes,
    frequencies, treatments,
    trajectories)
```

Dismech already has the ontology bindings (HP, MONDO, CL, GO, MAXO, CHEBI) that
make this interoperable — a Phenopacket's HPO terms directly match dismech's
`PhenotypeDescriptor` terms. The `datasets` section with `PHENOPACKETS` type
already supports linking to case-level collections.

## What dismech is NOT

Dismech should not attempt to become an individual-data store. The boundary is:

| Concern | Belongs in dismech | Belongs elsewhere |
|---|---|---|
| Disease mechanisms | Yes | — |
| Phenotype frequencies | Yes | — |
| Treatment-mechanism links | Yes | — |
| Gene-disease associations | Yes | — |
| Individual patient records | — | Phenopackets, EHR |
| Cohort-level datasets | — | OMOP, FHIR |
| Per-patient variant calls | — | VCF, GA4GH VRS |
| Clinical decision support rules | — | CDS systems |

The gap to fill is primarily an **interpretation layer** that queries dismech
programmatically and applies its knowledge to individual observations — not
changes to dismech's own data model.
