# Chronic Disease Curation Project

## Overview

This project aims to curate comprehensive pathophysiology entries for major chronic diseases in the Disorder Mechanisms Knowledge Base. Chronic diseases represent long-term conditions that require ongoing management and significantly impact quality of life.

This is an evergreen project: beyond the initial phases, "Other" expansion categories capture related conditions that share mechanisms and can be unfolded as curation continues.

## Goals

- Document disease mechanisms with evidence-backed pathophysiology
- Map phenotypes to HPO terms
- Annotate treatments with MAXO terms
- Provide PMID-supported evidence for all claims

## Target Diseases - Phase 1 (Complete)

- [x] Type 2 Diabetes Mellitus - `Type_2_Diabetes_Mellitus.yaml`
- [x] Hypertension - `Essential_Hypertension.yaml`
- [x] Chronic Obstructive Pulmonary Disease (COPD) - `Chronic_Obstructive_Pulmonary_Disease.yaml`
- [x] Coronary Artery Disease - `Coronary_Artery_Disease.yaml`
- [x] Chronic Kidney Disease - `Chronic_Kidney_Disease.yaml`
- [x] Heart Failure - `Heart_Failure.yaml`
- [x] Osteoarthritis - `Osteoarthritis.yaml`
- [x] Rheumatoid Arthritis - `Rheumatoid_Arthritis.yaml`
- [x] Asthma - `Asthma.yaml`
- [x] Inflammatory Bowel Disease - `Crohn_Disease.yaml` (Ulcerative Colitis pending)
- [x] Alzheimer's Disease - `Alhzeimer_Disease.yaml`
- [x] Parkinson's Disease - `Parkinsons_Disease.yaml`
- [x] Multiple Sclerosis - `Multiple_Sclerosis.yaml`
- [x] Systemic Lupus Erythematosus - `Systemic_Lupus_Erythematosus.yaml`
- [x] Chronic Liver Disease / Cirrhosis - `Liver_Cirrhosis.yaml`
- [x] Atrial Fibrillation - `Atrial_Fibrillation.yaml`
- [x] Obesity - `Obesity.yaml`
- [x] Depression (Major Depressive Disorder) - `Major_Depressive_Disorder.yaml`
- [x] Epilepsy - `Epilepsy.yaml`
- [x] Psoriasis - `Psoriasis.yaml`

## Target Diseases - Phase 2 (Complete)

### Endocrine/Metabolic
- [x] Hypothyroidism (Hashimoto's Thyroiditis) - `Hashimotos_Thyroiditis.yaml`
- [x] Polycystic Ovary Syndrome (PCOS) - `Polycystic_Ovary_Syndrome.yaml`
- [x] Gout - `Gout.yaml`
- [ ] Other endocrine/metabolic; e.g. Cushing syndrome, acromegaly, hyperparathyroidism

### Musculoskeletal
- [x] Osteoporosis - `Osteoporosis.yaml`
- [x] Fibromyalgia - `Fibromyalgia.yaml`
- [ ] Other musculoskeletal; e.g. Paget disease, osteogenesis imperfecta, ankylosing spondylitis

### Gastrointestinal
- [x] Gastroesophageal Reflux Disease (GERD) - `Gastroesophageal_Reflux_Disease.yaml`
- [x] Irritable Bowel Syndrome (IBS) - `Irritable_Bowel_Syndrome.yaml`
- [x] Ulcerative Colitis - `Ulcerative_Colitis.yaml`
- [x] Celiac Disease - `Celiac_Disease.yaml`
- [x] Chronic Pancreatitis - `Chronic_Pancreatitis.yaml`
- [ ] Other gastrointestinal; e.g. Barrett esophagus, diverticular disease, chronic constipation

### Psychiatric/Neurological
- [x] Bipolar Disorder - `Bipolar_Disorder.yaml`
- [x] Generalized Anxiety Disorder - `Generalized_Anxiety_Disorder.yaml`
- [x] Migraine - `Migraine.yaml`
- [ ] Other psychiatric; e.g. schizophrenia, OCD, PTSD, eating disorders
- [ ] Other neurological; e.g. ALS, Huntington disease, essential tremor, neuropathies

### Cardiovascular
- [x] Peripheral Artery Disease - `Peripheral_Artery_Disease.yaml`
- [ ] Other cardiovascular; e.g. cardiomyopathies, valvular heart disease, aortic aneurysm

### Respiratory
- [x] Obstructive Sleep Apnea - `Obstructive_Sleep_Apnea.yaml`
- [ ] Other respiratory; e.g. pulmonary fibrosis, bronchiectasis, pulmonary hypertension

### Reproductive/Urological
- [x] Endometriosis - `Endometriosis.yaml`
- [x] Benign Prostatic Hyperplasia - `Benign_Prostatic_Hyperplasia.yaml`
- [ ] Other reproductive/urological; e.g. chronic pelvic pain, interstitial cystitis, male infertility

### Ophthalmological
- [x] Glaucoma - `Glaucoma.yaml`
- [x] Age-related Macular Degeneration - `Age_Related_Macular_Degeneration.yaml`
- [ ] Other ophthalmological; e.g. diabetic retinopathy, cataracts, dry eye disease

### Hematological
- [x] Sickle Cell Disease - `Sickle_Cell_Disease.yaml`
- [ ] Other hematological; e.g. thalassemias, hemophilia, myelodysplastic syndromes

## Curation Workflow

1. Research disease pathophysiology using primary literature
2. Create YAML file in `kb/disorders/`
3. Validate with `just validate` and `just validate-references`
4. Run `just qc` before committing

---

# STATUS

**Phase 1:** 20/20 (100%) Complete
**Phase 2:** 20/20 (100%) Complete
**Core diseases:** 40/40 (100%)

Both phases complete. All 40 target chronic diseases have been curated with:
- Evidence-backed pathophysiology mechanisms
- HPO phenotype annotations
- PMID-supported evidence items
- Schema-validated YAML files

## Expansion Categories
- [ ] Other endocrine/metabolic; e.g. Cushing syndrome, acromegaly, hyperparathyroidism
- [ ] Other musculoskeletal; e.g. Paget disease, osteogenesis imperfecta
- [ ] Other gastrointestinal; e.g. Barrett esophagus, diverticular disease
- [ ] Other psychiatric; e.g. schizophrenia, OCD, PTSD, eating disorders
- [ ] Other neurological; e.g. ALS, Huntington disease, essential tremor
- [ ] Other cardiovascular; e.g. cardiomyopathies, valvular heart disease
- [ ] Other respiratory; e.g. pulmonary fibrosis, bronchiectasis, pulmonary hypertension
- [ ] Other reproductive/urological; e.g. chronic pelvic pain, interstitial cystitis
- [ ] Other ophthalmological; e.g. diabetic retinopathy, cataracts, dry eye disease
- [ ] Other hematological; e.g. thalassemias, hemophilia, myelodysplastic syndromes

# NOTES

## 2025-12-17

Initial status review completed. Cross-referenced target diseases against existing KB files:
- 7 of 20 target diseases already have entries
- Identified priority queue starting with Type 2 Diabetes (highest prevalence chronic disease)
- Note: Alzheimer file has typo in name (`Alhzeimer_Disease.yaml`)

## 2025-12-17 (later)

**Bulk curation completed for 13 remaining diseases:**

| Disease | File | Evidence Items |
|---------|------|----------------|
| Type 2 Diabetes Mellitus | `Type_2_Diabetes_Mellitus.yaml` | 14 |
| Essential Hypertension | `Essential_Hypertension.yaml` | 29 |
| Coronary Artery Disease | `Coronary_Artery_Disease.yaml` | Multiple |
| Parkinson's Disease | `Parkinsons_Disease.yaml` | 13 |
| Heart Failure | `Heart_Failure.yaml` | Multiple |
| Chronic Kidney Disease | `Chronic_Kidney_Disease.yaml` | Multiple |
| Osteoarthritis | `Osteoarthritis.yaml` | 7 |
| Liver Cirrhosis | `Liver_Cirrhosis.yaml` | 11 |
| Atrial Fibrillation | `Atrial_Fibrillation.yaml` | Multiple |
| Obesity | `Obesity.yaml` | Multiple |
| Major Depressive Disorder | `Major_Depressive_Disorder.yaml` | 18 |
| Epilepsy | `Epilepsy.yaml` | 12 |
| Psoriasis | `Psoriasis.yaml` | Multiple |

Workflow used:
1. Created initial YAML files with complete structure
2. Ran deep research (falcon) for all 13 diseases
3. Enhanced with PMID-backed evidence items
4. Validated all files against schema

All files pass `just validate` checks.

## 2025-12-18

**Phase 2 bulk curation completed for 20 additional chronic diseases:**

| Disease | File | Key Mechanisms |
|---------|------|----------------|
| Hashimoto's Thyroiditis | `Hashimotos_Thyroiditis.yaml` | Autoimmune thyroid destruction, TPO antibodies |
| Polycystic Ovary Syndrome | `Polycystic_Ovary_Syndrome.yaml` | Hyperandrogenism, insulin resistance |
| Gout | `Gout.yaml` | MSU crystal deposition, inflammasome activation |
| Osteoporosis | `Osteoporosis.yaml` | RANKL/OPG imbalance, osteoclast activity |
| Fibromyalgia | `Fibromyalgia.yaml` | Central sensitization, neuroinflammation |
| GERD | `Gastroesophageal_Reflux_Disease.yaml` | LES dysfunction, acid reflux |
| IBS | `Irritable_Bowel_Syndrome.yaml` | Gut-brain axis, visceral hypersensitivity |
| Ulcerative Colitis | `Ulcerative_Colitis.yaml` | Barrier dysfunction, mucosal inflammation |
| Celiac Disease | `Celiac_Disease.yaml` | tTG-mediated gluten immune response |
| Chronic Pancreatitis | `Chronic_Pancreatitis.yaml` | Pancreatic stellate cell fibrosis |
| Bipolar Disorder | `Bipolar_Disorder.yaml` | CACNA1C/ANK3 variants, GSK3 signaling |
| Generalized Anxiety Disorder | `Generalized_Anxiety_Disorder.yaml` | GABAergic dysfunction, amygdala hyperactivity |
| Migraine | `Migraine.yaml` | CSD, CGRP pathway |
| Peripheral Artery Disease | `Peripheral_Artery_Disease.yaml` | Atherosclerosis, endothelial dysfunction |
| Obstructive Sleep Apnea | `Obstructive_Sleep_Apnea.yaml` | Intermittent hypoxia, oxidative stress |
| Endometriosis | `Endometriosis.yaml` | Ectopic endometrium, estrogen dependence |
| Benign Prostatic Hyperplasia | `Benign_Prostatic_Hyperplasia.yaml` | EMT, ROCK-mediated fibrosis |
| Glaucoma | `Glaucoma.yaml` | RGC death, trabecular dysfunction |
| Age-related Macular Degeneration | `Age_Related_Macular_Degeneration.yaml` | Complement dysregulation, RPE loss |
| Sickle Cell Disease | `Sickle_Cell_Disease.yaml` | HbS polymerization, vaso-occlusion |

Workflow:
1. Created 20 initial YAML files with MONDO IDs and basic structure
2. Ran deep research (falcon) for all 20 diseases
3. Enhanced with PMID-backed evidence items using parallel agents
4. Validated all files against schema

All 20 files pass `just validate` checks with schema, term, and reference validation.
