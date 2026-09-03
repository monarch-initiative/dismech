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
  - Juvenile_Myoclonic_Epilepsy
  - DNM1_Encephalopathy
  - SNAP25_Encephalopathy
  - Epilepsy_of_Infancy_with_Migrating_Focal_Seizures
  - Pyridoxine-Dependent_Epilepsy
  - PCDH19_Clustering_Epilepsy
  - PNPO_Deficiency
  - Epilepsy_with_Myoclonic_Atonic_Seizures
  - Mesial_Temporal_Lobe_Epilepsy_with_Hippocampal_Sclerosis
  - KCNQ2_Developmental_and_Epileptic_Encephalopathy
  - Febrile_Infection-Related_Epilepsy_Syndrome
  - CPLX1-Related_DEE
  - Tetralogy_of_Fallot
  - Pericarditis
  - Infective_Endocarditis
  - Rheumatic_Heart_Disease
  - Hypoplastic_Left_Heart_Syndrome
  - Familial_Atrial_Fibrillation
  - Uveal_Melanoma
  - FGFR_Altered_Cholangiocarcinoma
  - Diffuse_Large_B_Cell_Lymphoma
  - Kaposi_Sarcoma
  - IDH_Mutant_Cholangiocarcinoma
  - IDH_Mutant_Astrocytoma
  - RET_Fusion_Thyroid_Cancer
  - Li-Fraumeni_Syndrome
  - Sturge-Weber_Syndrome
  - Beare-Stevenson_Cutis_Gyrata_Syndrome
  - Pituitary_Tumor
  - Cushing_Disease
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
  - corticotroph_egfr_pomc_acth_activation
  - somatotroph_camp_pka_overactivation
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

> ### How fast this decays
>
> All four workstreams were rebuilt against `main` @ `48bd0eb60c` (2026-09-03).
> Treat that date as a short expiry, not a footnote: **61 of workstream 1's
> candidates were curated in the four days** between two rebuilds, and the KB
> grew from 1,937 to 2,535 disorder entries over three weeks.
>
> The first version of this file was assembled from a tree 9,389 commits behind
> `main`. The dashboards were regenerated at the time and came back
> byte-identical, which was read as confirmation the figures were current. It was
> not: both the committed and the regenerated dashboards derived from the same
> stale tree, so the check established self-consistency and nothing about
> currency. `git log -1 origin/main` settles it in one command — run that before
> trusting any count here.

## Where the KB stands

Verified against `main` @ `48bd0eb60c` (2026-09-03):

| Measure | Value |
|---|---|
| Disorder entries | 2,535 |
| …with a MONDO-anchored `disease_term` | 2,499 |
| Distinct curated MONDO IDs (primary, subtype, exact/narrow mapping) | 3,857 |
| MONDO human-disease terms with an exact dismech page | 2,469 of 23,213 (10.6%) |
| …covered exactly **or** by a parent page | 48.3% |
| Average weighted compliance | 90.0% (684 violations) |
| Entries declaring any module conformance | 1,001 (39.5%) |
| Comorbidity entries | 26 |
| Mechanism modules | 164 |
| Groupings | 98 |

Pathophysiology and phenotype coverage are effectively complete. The gaps are
everywhere else.

## A prior question: is the candidate genuinely uncovered?

Before curating anything from these lists, check that a curated entry does not
already cover the concept under a **different MONDO term** — usually the target's
parent. The lexical preflight cannot see this, which is how issue #10069 was
filed against a concept `Pituitary_Tumor.yaml` had covered for ten days.

```bash
uv run python scripts/audit_curation_queue_coverage.py --max-descendants 20
```

Over the 1,338-stub queue that check finds 3 stubs already curated exactly and
**641 with a curated ancestor**. Those 641 are mostly not duplicates — they are
lump/split rulings the queue is presenting as "curate a new entry" (mevalonic
aciduria and hyper-IgD both under `Mevalonate_Kinase_Deficiency`; sclerosteosis 2
under `Sclerosteosis`). Curating one as a fresh entry creates a contradiction
rather than resolving it. Details and the over-broad-anchor finding are in #10679.

---

## Workstream 1 — MONDO terms already linked from existing pages

**397 candidates** (552 → 458 → 397 across three rebuilds; **61 curated in the
last four days alone**). Data: `linked-but-uncurated.tsv`.

These diseases are already referenced *by* curated entries — as differentials,
comorbidities, or related conditions — but have no entry of their own. Demand is
therefore already demonstrated, which makes this the cheapest breadth work in the
repo: no need to argue the disease is worth curating, only to curate it.

The churn is the argument for re-deriving before picking. Myocarditis, once top of
this queue at 4 inbound links, was curated in
[#9954](https://github.com/monarch-initiative/dismech/pull/9954). Pituitary gland
adenoma left the list not by being curated but by being *recognised* — a
`skos:narrowMatch` on the entry that already covered it (#10069). And several
resolved to existing entries the lexical check had missed: `velocardiofacial
syndrome` → `22q11.2_Deletion_Syndrome`, `proximal spinal muscular atrophy` →
`Spinal_Muscular_Atrophy`, `RASopathy` → `RASopathies`.

Ranked by inbound links from existing pages. Top of the queue, with the
coverage check from the section above already applied:

| Links | MONDO | Disease | Status |
|---:|---|---|---|
| 3 | MONDO:0044970 | mitochondrial disease | scope decision needed — likely a Grouping |
| 2 | MONDO:0018564 | 3p25.3 microdeletion syndrome | |
| 2 | MONDO:0003709 | agoraphobia | clear |
| 2 | MONDO:0011786 | allergic rhinitis | clear |
| 2 | MONDO:0001164 | antisocial personality disorder | clear |
| 2 | MONDO:0024557 | ataxia-telangiectasia-like disorder 1 | |
| 2 | MONDO:0005230 | cellulitis | clear |
| 2 | MONDO:0017843 | congenital pulmonary sequestration | clear |
| 2 | MONDO:0008021 | Cowden syndrome | NEC risk: eponym + numbered series |
| 2 | MONDO:0015474 | cryptosporidiosis | |
| 2 | MONDO:0015612 | Dent disease | clear |
| 2 | MONDO:0001521 | intermittent explosive disorder | clear |

**Recommended next tranche — the psychiatric trio.** `agoraphobia`,
`antisocial personality disorder` and `intermittent explosive disorder`: two
inbound links each, all `CURATE_ROOT`, none in the stub queue, none blocked by a
curated ancestor, none with an open issue. Psychiatry is thin in the KB and the
three share a DSM/epidemiology literature base, so they cost less together than
apart.

**Second tranche — the pituitary follow-on.** `acromegaly` (MONDO:0019933) and
`hypopituitarism` (MONDO:0005152), both clear and unclaimed, both sitting on work
already in place: `Pituitary_Tumor.yaml` is now anchored, the
`somatotroph_camp_pka_overactivation` module exists, and
`Somatotroph_cAMP_PKA_Pituitary_Tumor_Syndromes` groups them. Acromegaly should be
its own entry that *conforms to* that module rather than a subtype of pituitary
tumour — ectopic GHRH-driven acromegaly involves no pituitary tumour at all.

- [x] Curate myocarditis (MONDO:0004496) — done in #9954
- [x] Anchor pituitary gland adenoma (MONDO:0006373) — narrowMatch on `Pituitary_Tumor.yaml`, #10069
- [ ] Curate the psychiatric trio: agoraphobia, antisocial personality disorder, intermittent explosive disorder
- [ ] Curate acromegaly and hypopituitarism as the pituitary follow-on
- [ ] Decide scope for mitochondrial disease (MONDO:0044970)
- [ ] Curate Cowden syndrome (MONDO:0008021) — **run `just preflight-dr` first**: NEC flags for numbered series (`type 1`), eponym collision (`Cowden`) and synonym aliasing (`Duclos`, `Lhermitte`)
- [ ] Work down the remainder of `linked-but-uncurated.tsv` by inbound-link count

**Do not claim off a stale copy of this list.** Regenerate with
`just gen-dashboard`, drop rows curated on current `main`, then run the coverage
audit. Skipping the first step is how the myocarditis miss happened; skipping the
third is how #10069 happened.

---

## Workstream 2 — Module-conformance suggestions awaiting triage

**66 suggestions at cosine ≥ 0.90; 55 still actionable** — 8 have been wired
since, and 3 name a node that no longer exists. Data:
`conformance-suggestions.tsv` (full set of 1,128 in
`research/conforms_to_suggestions.tsv`).

**The suggestion set itself is stale and cannot currently be regenerated.**
`research/conforms_to_suggestions.tsv` dates from 2026-08-12 and has no committed
generator, so it predates roughly 600 entries. Only each suggestion's *status* is
re-derived here. Recovering or rewriting the node-embedding generator would be
worth more than triaging what it produced a month ago.

39.5% of entries declare a `conforms_to` (up from 31.2%), and a node-embedding
pass proposed links for some of the rest. The high-confidence tail is small enough to
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

**Three coherent clusters in the bottom 30.** Data: `low-compliance-entries.tsv`
(bottom 60, with the exact missing sections per file). Scores are weighted
compliance against 2,535 entries; the KB average is 90.0%.

The epilepsy and cardiac clusters have both improved since the first pass — the
worst entry was 53.7% and is now 61.9% — but both persist, and a third has
appeared.

### Epilepsy and developmental epileptic encephalopathy (12 of the bottom 30)

`Juvenile_Myoclonic_Epilepsy` (65.8), `DNM1_Encephalopathy` (67.2),
`SNAP25_Encephalopathy` (69.1), `Epilepsy_of_Infancy_with_Migrating_Focal_Seizures`
(69.3), `Pyridoxine-Dependent_Epilepsy` (69.8), `PCDH19_Clustering_Epilepsy` (69.9),
`PNPO_Deficiency` (69.9), `Epilepsy_with_Myoclonic_Atonic_Seizures` (69.9),
`Mesial_Temporal_Lobe_Epilepsy_with_Hippocampal_Sclerosis` (70.3),
`KCNQ2_Developmental_and_Epileptic_Encephalopathy` (70.3),
`Febrile_Infection-Related_Epilepsy_Syndrome` (70.5), `CPLX1-Related_DEE` (70.8).

Shared gaps: `environmental`, `histopathology`, `definitions`, `epidemiology`,
`experimental_models`, `classifications`, `datasets`, `biochemical`. The cluster
shares a literature base and the ILAE classification vocabulary, so it is far
cheaper as one tranche — `classifications` in particular is near-mechanical once
the ILAE mapping is settled once.

- [ ] Settle the ILAE classification mapping once, then backfill `classifications` across all 12
- [ ] Backfill `definitions` (EHR/OMOP phenotype algorithms) — see the `create-definitions-from-ohdsi` skill
- [ ] Backfill `epidemiology` + `prevalence` from a shared incidence source
- [ ] Sweep `datasets` with `just discover-datasets`, then `just verify-datasets`
- [ ] Add `animal_models` with `modeled_mechanisms` links — **blocked on #8320**, which invalidates 229 files carrying unnamed animal models

### Structural and inflammatory cardiac (6 of the bottom 30)

`Tetralogy_of_Fallot` (61.9 — now the lowest-scoring entry in the KB),
`Pericarditis` (63.9), `Infective_Endocarditis` (64.4),
`Rheumatic_Heart_Disease` (66.1), `Hypoplastic_Left_Heart_Syndrome` (67.9),
`Familial_Atrial_Fibrillation` (69.8).

Shared gaps: `datasets`, `clinical_trials`, `histopathology`, `definitions`,
`biochemical`. Congenital-heart trials are well registered on ClinicalTrials.gov,
so `clinical_trials` is the cheapest win here.

- [ ] Backfill `clinical_trials` across the cluster
- [ ] Backfill `histopathology` — valve and myocardial pathology is well described
- [ ] `Tetralogy_of_Fallot` first: it is the lowest-scoring entry in the KB

### Molecularly stratified oncology (8 of the bottom 30) — new

`Uveal_Melanoma` (65.9), `FGFR_Altered_Cholangiocarcinoma` (69.3),
`Diffuse_Large_B_Cell_Lymphoma` (69.7), `Kaposi_Sarcoma` (69.9),
`IDH_Mutant_Cholangiocarcinoma` (70.3), `IDH_Mutant_Astrocytoma` (70.6),
`RET_Fusion_Thyroid_Cancer` (70.8), `Li-Fraumeni_Syndrome` (70.9).

This cluster did not exist at the first pass and is worth reading together with
the over-broad-anchor finding in #10679: the L4 biomarker-stratum entries
(`IDH_Mutant_AML`, and the three colorectal strata) are exactly the entries that
anchor a parent MONDO term without the `skos:narrowMatch` mapping design decisions
L4 requires. Low compliance and loose anchoring look like the same underlying
thing — these entries were split out of a parent quickly and not finished.

- [ ] Audit the molecular-stratum entries against design decisions L4 — anchor plus `narrowMatch` mapping, or fold back into the parent
- [ ] Then backfill the shared gaps rather than treating them as eight separate jobs

`Sturge-Weber_Syndrome` (62.7) and `Beare-Stevenson_Cutis_Gyrata_Syndrome` (65.9)
sit in the bottom 10 and belong to no cluster; each needs its own pass.

---

## Workstream 4 — Outstanding entries from the original disease list

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
