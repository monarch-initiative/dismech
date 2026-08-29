---
title: Curation Backlog (Cross-Cutting)
status: IN_PROGRESS
tags: [META, BACKLOG, COVERAGE]
description: >-
  A cross-cutting worklist of what still needs curating in dismech, assembled
  from the KB itself plus the QC dashboards. Four workstreams: outstanding
  entries from the original disease list, MONDO terms already linked from
  existing pages but never curated, high-confidence module-conformance
  suggestions awaiting triage, and the lowest-compliance existing entries.
diseases:
  - SCN2A-Related_Developmental_and_Epileptic_Encephalopathy
  - Lennox-Gastaut_Syndrome
  - Self-Limited_Epilepsy_with_Centrotemporal_Spikes
  - Childhood_Absence_Epilepsy
  - SCN8A-Related_Developmental_and_Epileptic_Encephalopathy
  - PCDH19_Clustering_Epilepsy
  - Epilepsy_of_Infancy_with_Migrating_Focal_Seizures
  - Febrile_Infection-Related_Epilepsy_Syndrome
  - GNAO1-Related_Developmental_and_Epileptic_Encephalopathy
  - STX1B-Related_Epilepsy
  - Juvenile_Myoclonic_Epilepsy
  - CPLX1-Related_DEE
  - Coarctation_of_the_Aorta
  - Aortic_Valve_Stenosis
  - Mitral_Valve_Prolapse
  - Tetralogy_of_Fallot
  - Ventricular_Septal_Defect
  - Pericarditis
  - Infective_Endocarditis
  - Sturge-Weber_Syndrome
modules:
  - cerebellar_purkinje_degeneration
  - immune_checkpoint_blockade
  - fgfr_gain_of_function_skeletal_dysplasia
  - rtk_grb2_signaling_adaptation
  - fibrotic_response
  - ciliopathy_dysfunction
  - cardiac_ion_channel_repolarization
  - hemolytic_anemia_erythrocyte_destruction
  - hypothyroidism_thyroid_hormone_deficiency
  - glaucoma_optic_neuropathy
---

# Curation Backlog (Cross-Cutting)

## Overview

Most dismech project files are *thematic* — a disease domain, a drug class, a
mechanism. This one is **orthogonal**: it collects what is outstanding across the
whole KB, so that "what should I curate next?" has an answer that does not depend
on picking a theme first.

Four workstreams, ordered by yield per unit of effort rather than by size. The
first three are **triage** work — the candidates already exist and need judgement,
not fresh literature search. The fourth is genuine curation volume.

Supporting data lives in
[`projects/CURATION_BACKLOG/`](https://github.com/monarch-initiative/dismech/tree/main/projects/CURATION_BACKLOG);
regenerate it from the dashboards rather than hand-editing.

> ### ⚠️ Mixed provenance — read before using the numbers
>
> This file was first assembled from a working tree that turned out to be
> **9,389 commits behind `main`** (tree of 2026-08-13; the KB had grown from
> 1,937 to 2,462 disorder entries in the interval). The dashboards were
> regenerated at the time and came back byte-identical, which was mistaken for
> confirmation that the figures were current — in fact both the committed and
> the regenerated dashboards were derived from that same stale tree, so the
> check only established self-consistency.
>
> **Workstream 1 has since been re-derived against `main` @ `9cb071deca`
> (2026-08-29) and is current.** Workstreams 2, 3 and 4 have **not** been, and
> their counts should be treated as lower bounds pending a rebuild. The lesson
> generalizes: regenerating a derived artifact from a stale input proves
> nothing about currency. Check `git log -1 origin/main` first.

## Where the KB stands

Verified against `main` @ `9cb071deca` (2026-08-29):

| Measure | Value |
|---|---|
| Disorder entries | 2,462 |
| Distinct curated MONDO IDs (primary, subtype, exact/narrow mapping) | 2,503 |
| Comorbidity entries | 25 |
| Mechanism modules | 164 |
| Groupings | 98 |

The following are from the **stale** 2026-08-13 tree and are not yet re-derived —
directionally useful, numerically wrong: MONDO exact-page coverage 8.1% (45.1%
including parent-page coverage); average weighted compliance 89.5% with 597
violations; 31.2% of entries declaring module conformance.

Phenotypes and pathophysiology were effectively complete (99.9% / 99.7%) at the
stale snapshot and are unlikely to have regressed. The gaps are everywhere else.

---

## Workstream 1 — MONDO terms already linked from existing pages

**458 candidates** (was 552 at the stale snapshot; **94 have been curated since**).
Data: `linked-but-uncurated.tsv`. ✅ **Current as of `main` @ `9cb071deca`.**

These diseases are already referenced *by* curated entries — as differentials,
comorbidities, or related conditions — but have no entry of their own. Demand is
therefore already demonstrated, which makes this the cheapest breadth work in the
repo: no need to argue the disease is worth curating, only to curate it.

That 94 closed in ~two weeks is itself the argument for re-deriving this list
before picking from it: myocarditis, the former top of this queue at 4 inbound
links, was curated in [#9954](https://github.com/monarch-initiative/dismech/pull/9954)
and is gone from the list. Several more resolved not as new entries but as
*existing* ones the lexical check had missed — `velocardiofacial syndrome` →
`22q11.2_Deletion_Syndrome`, `proximal spinal muscular atrophy` →
`Spinal_Muscular_Atrophy`, `RASopathy` → `RASopathies`.

Ranked by inbound links from existing pages. Top of the queue:

| Links | MONDO | Disease | Status |
|---:|---|---|---|
| 3 | MONDO:0044970 | mitochondrial disease | scope decision needed |
| 3 | MONDO:0006373 | pituitary gland adenoma | **claimed — [#10069](https://github.com/monarch-initiative/dismech/issues/10069)** |
| 2 | MONDO:0018564 | 3p25.3 microdeletion syndrome | |
| 2 | MONDO:0003709 | agoraphobia | |
| 2 | MONDO:0011786 | allergic rhinitis | |
| 2 | MONDO:0001164 | antisocial personality disorder | |
| 2 | MONDO:0024557 | ataxia-telangiectasia-like disorder 1 | |
| 2 | MONDO:0005230 | cellulitis | |
| 2 | MONDO:0017843 | congenital pulmonary sequestration | |
| 2 | MONDO:0008021 | Cowden syndrome | NEC risk: eponym + numbered series |
| 2 | MONDO:0015474 | cryptosporidiosis | |
| 2 | MONDO:0015612 | Dent disease | |

- [x] Curate myocarditis (MONDO:0004496) — done in #9954
- [ ] Curate pituitary gland adenoma (MONDO:0006373) — claimed, #10069
- [ ] Decide scope for mitochondrial disease (MONDO:0044970) — likely a Grouping, not a Disease
- [ ] Curate agoraphobia (MONDO:0003709) and allergic rhinitis (MONDO:0011786) — both `CURATE_ROOT`, no NEC risk
- [ ] Curate Cowden syndrome (MONDO:0008021) — **run `just preflight-dr` first**: NEC flags for numbered series (`type 1`), eponym collision (`Cowden`) and synonym aliasing (`Duclos`, `Lhermitte`)
- [ ] Work down the remainder of `linked-but-uncurated.tsv` by inbound-link count

**Before claiming from this list, re-derive it.** Regenerate the underlying data
with `just gen-dashboard` (writes `dashboard/not_yet_curated.json`), then drop
rows whose MONDO ID is curated on current `main`. Do not claim off a stale copy —
that is how the myocarditis miss happened.

---

## Workstream 2 — Module-conformance suggestions awaiting triage

> ⚠️ **Stale — derived from the 2026-08-13 tree, not re-derived against current `main`.** Counts are lower bounds; entries named here may already be curated.

**66 suggestions at cosine ≥ 0.90; 58 of them actionable.** Data:
`conformance-suggestions.tsv` (full set of 1,128 lives in
`research/conforms_to_suggestions.tsv`).

Only 31.2% of entries declare any `conforms_to`, and a node-embedding pass has
already proposed links for the rest. The high-confidence tail is small enough to
review by hand.

**These are suggestions, not findings.** The embedding matches on *node label
similarity*, so it is blind to direction and to disease context. Two failure modes
are already visible in the ≥0.90 set and must be rejected, not applied:

- **Direction-blind:** `Graves_Disease :: Thyroid Overactivity` → `hypothyroidism_thyroid_hormone_deficiency#Thyroid Hormone Insufficiency` (cosine 0.914). Hyperthyroidism is not hypothyroidism.
- **Context-blind:** a generic `MAPK Pathway Activation` node in `Uveal_Melanoma`, `KIT_Mutant_Melanoma`, `HER2_Positive_Gastric_Cancer`, `HER2_Positive_Colorectal_Cancer` and `FGFR_Altered_Cholangiocarcinoma` → `fgfr_gain_of_function_skeletal_dysplasia#Sustained MAPK/STAT Signaling`. The MAPK claim is right; the *skeletal-dysplasia* module is not the home for it. If these need a shared anchor, that is an argument for a new module, not for conforming a melanoma to a chondrodysplasia.

Highest-confidence candidates that do look right:

- [ ] `Autosomal_Dominant_Cerebellar_Ataxia_Type_I :: Purkinje Cell Degeneration and Cerebellar Cortical Atrophy` → `cerebellar_purkinje_degeneration#Purkinje Neuron Degeneration` (1.000)
- [ ] `HPV_Positive_Head_and_Neck_Cancer :: Immune Evasion` → `immune_checkpoint_blockade#Adaptive Immune Resistance` (1.000)
- [ ] `Hypotonia-Cystinuria_Syndrome :: Urinary cystine supersaturation` → `nephrolithiasis_crystal_nucleation#Urinary Supersaturation` (1.000)
- [ ] `Duchenne_Muscular_Dystrophy :: Myocardial Fibrosis` → `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling` (0.971)
- [ ] `Glaucoma :: Trabecular Meshwork Dysfunction` → `glaucoma_optic_neuropathy#Trabecular Meshwork Outflow Dysfunction` (0.954)
- [ ] `Meckel_Syndrome` (two ciliogenesis nodes) → `ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction` (0.954, 0.942)
- [ ] `Systemic_Sclerosis :: Fibroblast Activation and Fibrosis` → `fibrotic_response#Mesenchymal Cell Activation` (0.946)
- [ ] Triage the remaining ≥0.90 rows in `conformance-suggestions.tsv`, recording rejects
- [ ] Decide whether the RTK/MAPK oncogene cluster warrants its own module rather than 15 near-miss suggestions

Each accepted link must satisfy the module's stated conformance bar — the
biological processes and causal edges the module expects — not just a matching
node name.

---

## Workstream 3 — Lowest-compliance existing entries

> ⚠️ **Stale — derived from the 2026-08-13 tree, not re-derived against current `main`.** Counts are lower bounds; entries named here may already be curated.

**Two coherent clusters in the bottom 30.** Data: `low-compliance-entries.tsv`
(bottom 60, with the exact missing sections per file).

### Pediatric epilepsy (14 of the bottom 30)

`SCN2A-Related_Developmental_and_Epileptic_Encephalopathy` (53.7% weighted),
`Lennox-Gastaut_Syndrome` (53.7), `Self-Limited_Epilepsy_with_Centrotemporal_Spikes`
(54.7), `Childhood_Absence_Epilepsy` (56.5),
`SCN8A-Related_Developmental_and_Epileptic_Encephalopathy` (58.4),
`PCDH19_Clustering_Epilepsy` (60.5),
`Epilepsy_of_Infancy_with_Migrating_Focal_Seizures` (60.6),
`Febrile_Infection-Related_Epilepsy_Syndrome` (61.8),
`GNAO1-Related_Developmental_and_Epileptic_Encephalopathy` (64.8),
`STX1B-Related_Epilepsy` (65.3), `Juvenile_Myoclonic_Epilepsy` (65.8),
`CPLX1-Related_DEE` (66.7).

Shared gaps (missing in 10-12 of the 12): `environmental`, `histopathology`,
`definitions`, `epidemiology`, `experimental_models`, `classifications`,
`datasets`, `biochemical`. The cluster shares a literature base and an ILAE
classification vocabulary, so curating them as one tranche is far cheaper than
one at a time — and `classifications` in particular is close to mechanical once
the ILAE mapping is settled.

- [ ] Settle the ILAE classification mapping once, then backfill `classifications` across all 12
- [ ] Backfill `definitions` (EHR/OMOP phenotype algorithms) for the cluster — see the `create-definitions-from-ohdsi` skill
- [ ] Backfill `epidemiology` + `prevalence` from a shared incidence source
- [ ] Sweep `datasets` with `just discover-datasets` per entry, then `just verify-datasets`
- [ ] Add `experimental_models` / `animal_models` with `modeled_mechanisms` links (the SCN2A/SCN8A/GNAO1 entries have well-known mouse models)

### Structural cardiac (7 of the bottom 30)

`Coarctation_of_the_Aorta` (59.7), `Aortic_Valve_Stenosis` (63.9),
`Mitral_Valve_Prolapse` (64.3), `Tetralogy_of_Fallot` (65.8),
`Ventricular_Septal_Defect` (66.0), `Pericarditis` (66.0),
`Infective_Endocarditis` (65.9).

Shared gaps: `datasets`, `clinical_trials`, `histopathology`, `definitions`,
`biochemical`. `Mitral_Valve_Prolapse` is the weakest (14 sections absent,
including `diagnosis`, `inheritance` and `prevalence`).

- [ ] Bring `Mitral_Valve_Prolapse` up to the cluster baseline first
- [ ] Backfill `clinical_trials` across the cluster — congenital-heart trials are well registered on ClinicalTrials.gov
- [ ] Backfill `histopathology` (valve/myocardial pathology is well described)

`Sturge-Weber_Syndrome` (56.1) sits in the bottom 10 but belongs to neither
cluster; it needs its own pass.

---

## Workstream 4 — Outstanding entries from the original disease list

> ⚠️ **Stale — derived from the 2026-08-13 tree, not re-derived against current `main`.** Counts are lower bounds; entries named here may already be curated.

**177 rows still outstanding** of the 431 on `initial-diseases.tsv`
(207 were flagged as candidates; 30 have been curated since that file was
written). Data: `outstanding-initial-diseases.tsv`.

Split by whether a related entry already exists:

- **Tier 1 — no entry at all (~82).** Genuine gaps. Notable: paroxysmal nocturnal
  haemoglobinuria (open as #6906), Glanzmann thrombasthenia, Bernard-Soulier
  syndrome, cold agglutinin disease, Evans syndrome, hyper-IgM syndrome,
  leukocyte adhesion deficiency (and types 1/II), Creutzfeldt-Jakob disease,
  corticobasal degeneration, normal pressure hydrocephalus, Werner syndrome,
  Sotos syndrome, Birt-Hogg-Dubé syndrome, NF2-related schwannomatosis, Pendred
  syndrome, acromegaly, hypopituitarism, MODY types 1 and 2, MRKH syndrome, HELLP
  syndrome, Hodgkin lymphoma (only the *classic* subtype is curated).
- **Tier 2 — a related entry exists (~95).** Usually a missing
  `mappings.mondo_mappings` `exactMatch`/`narrowMatch` or a `has_subtypes` term
  rather than a new file — e.g. beta-thalassaemia major vs `Beta_Thalassemia`,
  hereditary retinoblastoma vs `Retinoblastoma`, Cockayne types 1-3 vs
  `Cockayne_Syndrome`, thoracic aortic aneurysm vs
  `Familial_Thoracic_Aortic_Aneurysm_and_Aortic_Dissection`.

- [ ] Decide the **Usher syndrome** subtype policy — 15 of the 177 rows are Usher molecular subtypes (1B-1K, 2A/2C/2D, 3A/3B, type 4) against a single `Usher_Syndrome` entry. One decision closes ~9% of this list.
- [ ] Sweep Tier 2 for mappings that can be added without new entries
- [ ] Open curation issues for the Tier 1 haematology block (7 entries, one literature base)
- [ ] Open curation issues for the Tier 1 immunodeficiency block (LAD 1/II, hyper-IgM, hyper-IgD)

---

## Not in scope here (tracked elsewhere)

These are real backlogs but have their own homes:

- **Comorbidities** — 25 entries against 2,462 disorders, proportionally the
  largest structural hole. Tracked in
  [`projects/COMORBIDITIES.md`](https://github.com/monarch-initiative/dismech/blob/main/projects/COMORBIDITIES.md).
- **Evidence-quality debt** — 8,114 evidence items with `UNSPECIFIED`
  `evidence_source` and 18,211 tagged `OTHER`; 295 grandfathered title-as-snippet
  items in `tests/title_snippet_baseline.txt`; issue #8296 (182 environmental
  exposures with no evidence) and #8185 (environmental entries that are disease
  states, not exposures).
- **Live regression** — issue #8320: `AnimalModel.name` became implicitly
  required, invalidating 224 entries. This blocks animal-model backfill in
  Workstream 3 and should be fixed first.
- **Thematic projects** with large open checklists: `REACTOME_DISEASES` (659
  open), `CANCER` (79), `NICU` (40), `GWAS_MECHANISMS` (35), `CHILDHOOD_CANCER`
  (35), `MONDO_EHR_MAPPINGS` (35).

## Regenerating this backlog

```bash
just gen-dashboard        # refreshes dashboard/{capability_metrics,not_yet_curated,priority,reports}.json
```

The four TSVs under `projects/CURATION_BACKLOG/` are derived from those dashboards
plus `research/conforms_to_suggestions.tsv`. Note that
`dashboard/priority.json` reports `already_curated: 0` / `coverage_percent: 0.0`
even though the generator log says it excluded 2,932 already-curated roots — the
summary appears to count *after* exclusion, so do not read that 0% as a coverage
statement.
