---
title: Fanconi Anemia Phenotype Gap Analysis
status: IN_PROGRESS
description: >-
  Close the FA phenotype-annotation gap identified by the Connelly et al. custom
  HPO profile (PMID:41728284); 203 profile terms were absent from the dismech
  entry. Batch 1 added 17; ~186 remain.
tags: [PHENOTYPE_COVERAGE, HPO, RARE_DISEASE, DNA_REPAIR]
diseases:
  - Fanconi_Anemia
modules:
  - dna_repair_synthetic_lethality
phenotypes:
  - id: HP:0001199
    label: Triphalangeal thumb
  - id: HP:0000027
    label: Azoospermia
  - id: HP:0008551
    label: Microtia
---

# Fanconi Anemia Phenotype Gap Analysis

## Overview

Connelly E, Laraway B, Mullen KR, Mungall CJ, Haendel MA, Hurwitz EG.
*A custom phenotypic profile for Fanconi anemia: Addressing gaps in existing
disease annotations.* medRxiv, 2026. **PMID:41728284**, PMCID:PMC12919158,
DOI:10.64898/2026.02.10.26346018.

The paper publishes a 264-term custom HPO profile for Fanconi anemia, curated
from the Fanconi Cancer Foundation Clinical Care Guidelines (5th Edition, 2020)
via OntoGPT extraction plus manual review, and shows existing OMIM/Orphanet
annotations under-represent musculoskeletal, genitourinary, and limb phenotypes.
This project diffs that profile against the dismech `Fanconi_Anemia` entry and
tracks closing the gap with snippet-verified evidence.

## Scope and Method

- **Profile data** (CC-BY-4.0): https://github.com/ehurwitz/FA-custom-profile
  (`FA-custom-profile.hpoa`, HPO release 2026-02-16) — mirrored as
  `custom_profile.hpoa` below.
- Extracted the 264 custom-profile HP IDs and the 446-term OMIM/Orphanet/custom
  comparison table (`FA-custom-profile.xlsx`) with anatomical-system labels.
- Diffed against the HP IDs already present in `kb/disorders/Fanconi_Anemia.yaml`.
- **Evidence policy:** the `.hpoa` annotations cite the FCF guideline URL
  (evidence code `TAS`), which does **not** satisfy the dismech PMID/structured
  snippet policy. Every added term is independently sourced and snippet-verified
  against `ORPHA:84` (Orphanet structured record) or a fetched PubMed abstract.

## Result (at project start)

| Set | HP terms |
|-----|----------|
| Connelly custom profile | 264 |
| `Fanconi_Anemia` (before batch 1) | 98 |
| Shared | 61 |
| In profile, missing from dismech | 203 (150 novel — absent from OMIM *and* Orphanet) |
| In dismech, absent from profile | 37 |

Many of the 203 are finer-grained children of terms `Fanconi_Anemia` already
carries (e.g. dismech has generic "Radial Ray Defects"; the profile enumerates
absent radius/scaphoid/trapezium), so the gap is partly granularity, not pure
absence.

## Catalog Artifacts

| Artifact | Description | Rows |
|----------|-------------|------|
| `projects/FANCONI_ANEMIA_GAP_ANALYSIS/custom_profile_comparison.tsv` | Full 446-term OMIM/Orphanet/custom comparison with anatomical system | 446 |
| `projects/FANCONI_ANEMIA_GAP_ANALYSIS/missing_terms_by_system.tsv` | The 203 profile terms missing from dismech, with system, prior source, status, batch-1 evidence | 203 |
| `projects/FANCONI_ANEMIA_GAP_ANALYSIS/batch1_added.tsv` | The 17 phenotypes added in batch 1 with evidence sources | 17 |
| `projects/FANCONI_ANEMIA_GAP_ANALYSIS/batch2_added.tsv` | The 32 phenotypes added in batch 2 (Orphanet record) | 32 |
| `projects/FANCONI_ANEMIA_GAP_ANALYSIS/custom_profile.hpoa` | Verbatim mirror of the published 264-term `.hpoa` | 264 |

## Batch 1 — added (raises `Fanconi_Anemia` from 98 → 115 HP terms)

Prioritised the paper's emphasis systems. Sources are deterministic and
snippet-verified (see `batch1_added.tsv`).

- **`ORPHA:84`** (exact phenotype-table row substrings): Triphalangeal thumb
  (HP:0001199), Spina bifida (HP:0002414), Tetralogy of Fallot (HP:0001636),
  High palate (HP:0000218), Frontal bossing (HP:0002007), Short palpebral
  fissure (HP:0012745), Azoospermia (HP:0000027), Hydroureter (HP:0000072),
  Hyperreflexia (HP:0001347).
- **PMID:19622403** (Auerbach AD, *Fanconi anemia and its diagnosis*, Mutat Res
  2009 — IFAR series; exact-substring quotes): Microtia (HP:0008551), Low-set
  ears (HP:0000369), Posteriorly rotated ears (HP:0000358), Fusion of middle ear
  ossicles (HP:0005473), Aplastic clavicle (HP:0006660), Oligozoospermia
  (HP:0000798), Obesity (HP:0001513), Abnormal circulating lipid concentration
  (HP:0003119).

## Batch 2 — added (raises `Fanconi_Anemia` from 115 → 147 HP terms)

Curating phenotypes **as recorded in the authoritative Orphanet record**
(`ORPHA:84`): every uncovered phenotype-table row was added, skipping only
top-of-hierarchy "Abnormality of the [system]" umbrellas, exact concept
duplicates of existing entries, and one clinically implausible Orphanet
annotation (pyridoxine-responsive sideroblastic anemia — not characteristic of
FA, likely a mapping artifact). All 32 carry an exact `ORPHA:84` row snippet
(see `batch2_added.tsv`). Spans renal/GU (recurrent UTI, renal
insufficiency/hypoplasia, abnormal kidney position, decreased male fertility,
preputial anomaly), craniofacial (dolichocephaly, facial asymmetry, sloping
forehead, choanal atresia, uvular hypoplasia), ocular (astigmatism, visual
impairment, proptosis, upslanted fissures, nystagmus, iris hypoplasia), cardiac/
vascular (HCM, carotid anomaly, AVM), skeletal/limb (hip dislocation, finger
syndactyly, finger aplasia/hypoplasia, pes planus, toe clubbing), GI (umbilical
hernia, Meckel diverticulum, Hirschsprung, duodenal stenosis), plus cranial
nerve paralysis, weight loss, and oligohydramnios.

**Cross-source finding:** **none** of these 32 Orphanet-recorded phenotypes
appear in the Connelly 264-term custom profile — a direct illustration of the
paper's thesis that no single source is complete. The custom profile and the
Orphanet record are *complementary*, not nested.

## Remaining work — ~186 unmapped profile terms

Counts per anatomical system (from `missing_terms_by_system.tsv`, status `TODO`):

| System | TODO | System | TODO |
|--------|------|--------|------|
| Musculoskeletal | 53 | Immune | 6 |
| Genitourinary | 29 | Ear | 5 |
| Digestive | 17 | Cardiovascular | 5 |
| Neoplasm | 12 | Blood/blood-forming | 3 |
| Nervous | 11 | Eye | 2 |
| Integument | 11 | Musculature | 2 |
| Head or neck | 9 | Respiratory | 2 |
| Metabolism/homeostasis | 8 | Endocrine | 2 |
| Growth abnormality | 6 | (other singletons) | 3 |

### Next batches (proposed)

- [ ] **Batch 2 — renal/genitourinary structural** (horseshoe/ectopic kidney,
      hydronephrosis, renal dysplasia/hypoplasia, chordee, phimosis): source
      from GeneReviews/IFAR and Orphanet xref literature.
- [ ] **Batch 3 — radial-ray granularity** (absent radius/scaphoid/trapezium,
      thumb-hypoplasia grading, carpal hypoplasia, ulnar bowing): map to the
      existing generic radial-ray nodes.
- [ ] **Batch 4 — oral-mucosal / head-and-neck** (oral ulcer, gingivitis,
      periodontitis, xerostomia, leukoplakia-adjacent): relevant to the FA
      head-and-neck SCC surveillance context.
- [ ] **Batch 5 — GI-functional and metabolic** (GERD, dysphagia, constipation,
      diabetes mellitus, insulin resistance).
- [ ] Re-run the diff after each batch and update `missing_terms_by_system.tsv`
      status flags.

## Notes

- Every future addition must carry a verified `ORPHA:`/`PMID:` snippet; do not
  import the OntoGPT `TAS` annotations as evidence.
- Watch the `Fanconi_Anemia` vs Fanconi *renotubular* syndrome named-entity
  confusion when sourcing literature (the renotubular disorder shares "Fanconi"
  but has an unrelated phenotype set).
