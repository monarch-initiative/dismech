---
reference_id: "HDRUK:PH1709"
title: "Chronic paediatric conditions: Diabetes"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1709 version 3634"
content_type: "structured_record"
---

# HDRUK:PH1709  Chronic paediatric conditions: Diabetes

**PH1709** version 3634 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1709 |
| Version | 3634 |
| Name | Chronic paediatric conditions: Diabetes |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Swann OV, Williams TC, Fraser LK, Farrell J, Parker M, Kennedy J, Seabourne M, Brophy S, Harrison EM, Docherty AB, Pollock L |
| Collections | Phenotype Library |
| Coding systems | SNOMED CT codes; ICD10 codes; Read codes v2 |
| Data sources | Hospital Episode Statistics Admitted Patient Care; OpenSAFELY SNOMED CT; Patient Episode Dataset for Wales (PEDW); Welsh Longitudinal General Practice Dataset (WLGP) - Welsh Primary Care |
| Sex | Both |
| Event date range | 2021/01/01 - 2021/01/01 |
| DOI | https://doi.org/10.48533/stbh-je21 |
| Ontology | MONDO:0005015 diabetes mellitus |

## Definition

This code list is part of a set of harmonised code lists to identify chronic paediatric conditions across primary and secondary care datasets across the UK.

- ICD-10 diagnoses as per Hardelid 2014. - Read v2 code list for diabetes: https://phenotypes.healthdatagateway.org/phenotypes/PH8/version/16/detail/ (https://phenotypes.healthdatagateway.org/phenotypes/PH8/version/16/detail/) - SNOMED code list diabetes: https://phenotypes.healthdatagateway.org/phenotypes/PH1006/version/2184/detail/ (https://phenotypes.healthdatagateway.org/phenotypes/PH1006/version/2184/detail/)

### Methods

Chronic paediatric conditions were defined as health problems requiring medical follow-up for more than 12 months in 50% or more of cases. Code lists were produced by mapping existing ICD-10 codes for chronic paediatric conditions to SNOMED and Read v2 codes using the CALIBER R package, with review by paediatric sub-specialists.

An established ICD-10 code list of chronic paediatric conditions (Hardelid 2014) was used as the basis for the new lists.[1] Chronic paediatric conditions were defined as any health problem requiring medical follow-up (hospital admission, outpatient follow up or use of support services such as physiotherapy) for more than 12 months in 50% or more of cases.[1] A Chronic Paediatric Conditions Committee of paediatric sub-specialists was established. The original ICD-10 list was screened by two paediatricians and acute conditions removed, with disagreements resolved by a third paediatrician. Conditions which were likely acute and would not fulfil our chronic disease definition were excluded, including skeletal injuries and self-harm. Drug-induced conditions were excluded as chronicity was not known. Infections other than human immunodeficiency virus (HIV), hepatitis B or C, or congenital infections (syphilis / toxoplasmosis / rubella / herpes simplex virus / cytomegalovirus) were excluded. Chronic sequelae of infections were retained.

Published code lists were then identified for Read v2 and SNOMED codes for well-characterised conditions including asthma, diabetes, cystic fibrosis and cancer. The remaining ICD-10 codes were mapped to SNOMED and Read v2 codes using the CALIBER R package and Technology Reference Update Distribution NHS Data Migration tables [2] to produce new code lists suitable for primary care data. These resulting code lists were screened by two sub-specialists to ensure conditions were chronic and in the correct subgroup with disagreements resolved by a third clinician.

### References:

1. Hardelid P, Dattani N, Gilbert R. Estimating the prevalence of chronic conditions in children who die in England, Scotland and Wales: a data linkage cohort study. BMJ Open 2014; 4: e005331. 2. CALIBER codelists-package: Generate ICD, Read and OPCS codelists in CALIBER codelists: Generate ICD10, Read and OPCS codelists, https://rdrr.io/rforge/CALIBERcodelists/man/CALIBERcodelists-package.html (https://rdrr.io/rforge/CALIBERcodelists/man/CALIBERcodelists-package.html) (accessed 19 October 2022).

## Implementation

We have considered conditions to be active if they had been coded for in the preceding five years. In addition, conditions from the following subgroups were considered to be permanent, therefore active if coded for at any time: metabolic, diabetes, cystic fibrosis, transplant, receiving palliative care, other congenital multisystem syndromes and chromosomal abnormalities, immunological and cerebral palsy / paralysis (a subgroup of "Other neurology" code list).

## Codes

| Code | Description | Concept |
|---|---|---|
| ICD10:E10 | Type 1 diabetes mellitus | Diabetes (ICD-10) |
| ICD10:E100 | With coma | Diabetes (ICD-10) |
| ICD10:E101 | With ketoacidosis | Diabetes (ICD-10) |
| ICD10:E102 | With renal complications | Diabetes (ICD-10) |
| ICD10:E103 | With ophthalmic complications | Diabetes (ICD-10) |
| ICD10:E104 | With neurological complications | Diabetes (ICD-10) |
| ICD10:E105 | With peripheral circulatory complications | Diabetes (ICD-10) |
| ICD10:E106 | With other specified complications | Diabetes (ICD-10) |
| ICD10:E107 | With multiple complications | Diabetes (ICD-10) |
| ICD10:E108 | With unspecified complications | Diabetes (ICD-10) |
| ICD10:E109 | Without complications | Diabetes (ICD-10) |
| ICD10:E11 | Type 2 diabetes mellitus | Diabetes (ICD-10) |
| ICD10:E110 | With coma | Diabetes (ICD-10) |
| ICD10:E111 | With ketoacidosis | Diabetes (ICD-10) |
| ICD10:E112 | With renal complications | Diabetes (ICD-10) |
| ICD10:E113 | With ophthalmic complications | Diabetes (ICD-10) |
| ICD10:E114 | With neurological complications | Diabetes (ICD-10) |
| ICD10:E115 | With peripheral circulatory complications | Diabetes (ICD-10) |
| ICD10:E116 | With other specified complications | Diabetes (ICD-10) |
| ICD10:E117 | With multiple complications | Diabetes (ICD-10) |
| ICD10:E118 | With unspecified complications | Diabetes (ICD-10) |
| ICD10:E119 | Without complications | Diabetes (ICD-10) |
| ICD10:E12 | Malnutrition-related diabetes mellitus | Diabetes (ICD-10) |
| ICD10:E120 | With coma | Diabetes (ICD-10) |
| ICD10:E121 | With ketoacidosis | Diabetes (ICD-10) |
| ICD10:E122 | With renal complications | Diabetes (ICD-10) |
| ICD10:E123 | With ophthalmic complications | Diabetes (ICD-10) |
| ICD10:E124 | With neurological complications | Diabetes (ICD-10) |
| ICD10:E125 | With peripheral circulatory complications | Diabetes (ICD-10) |
| ICD10:E126 | With other specified complications | Diabetes (ICD-10) |
| ICD10:E127 | With multiple complications | Diabetes (ICD-10) |
| ICD10:E128 | With unspecified complications | Diabetes (ICD-10) |
| ICD10:E129 | Without complications | Diabetes (ICD-10) |
| ICD10:E13 | Other specified diabetes mellitus | Diabetes (ICD-10) |
| ICD10:E130 | With coma | Diabetes (ICD-10) |
| ICD10:E131 | With ketoacidosis | Diabetes (ICD-10) |
| ICD10:E132 | With renal complications | Diabetes (ICD-10) |
| ICD10:E133 | With ophthalmic complications | Diabetes (ICD-10) |
| ICD10:E134 | With neurological complications | Diabetes (ICD-10) |
| ICD10:E135 | With peripheral circulatory complications | Diabetes (ICD-10) |
| ICD10:E136 | With other specified complications | Diabetes (ICD-10) |
| ICD10:E137 | With multiple complications | Diabetes (ICD-10) |
| ICD10:E138 | With unspecified complications | Diabetes (ICD-10) |
| ICD10:E139 | Without complications | Diabetes (ICD-10) |
| ICD10:E14 | Unspecified diabetes mellitus | Diabetes (ICD-10) |
| ICD10:E140 | With coma | Diabetes (ICD-10) |
| ICD10:E141 | With ketoacidosis | Diabetes (ICD-10) |
| ICD10:E142 | With renal complications | Diabetes (ICD-10) |
| ICD10:E143 | With ophthalmic complications | Diabetes (ICD-10) |
| ICD10:E144 | With neurological complications | Diabetes (ICD-10) |
| ICD10:E145 | With peripheral circulatory complications | Diabetes (ICD-10) |
| ICD10:E146 | With other specified complications | Diabetes (ICD-10) |
| ICD10:E147 | With multiple complications | Diabetes (ICD-10) |
| ICD10:E148 | With unspecified complications | Diabetes (ICD-10) |
| ICD10:E149 | Without complications | Diabetes (ICD-10) |
| READ2:C100011 | Insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C100112 | Non-insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C103y00 | Other specified diabetes mellitus with coma | Diabetes (Read v2) |
| READ2:C108.00 | Insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C108.11 | IDDM-Insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C108.12 | Type 1 diabetes mellitus | Diabetes (Read v2) |
| READ2:C108.13 | Type I diabetes mellitus | Diabetes (Read v2) |
| READ2:C108000 | Insulin-dependent diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C108011 | Type I diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C108012 | Type 1 diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C108100 | Insulin-dependent diabetes mellitus with ophthalmic comps | Diabetes (Read v2) |
| READ2:C108112 | Type 1 diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C108200 | Insulin-dependent diabetes mellitus with neurological comps | Diabetes (Read v2) |
| READ2:C108211 | Type I diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C108212 | Type 1 diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C108300 | Insulin dependent diabetes mellitus with multiple complicatn | Diabetes (Read v2) |
| READ2:C108311 | Type I diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C108411 | Unstable type I diabetes mellitus | Diabetes (Read v2) |
| READ2:C108412 | Unstable type 1 diabetes mellitus | Diabetes (Read v2) |
| READ2:C108500 | Insulin dependent diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C108511 | Type I diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C108512 | Type 1 diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C108600 | Insulin dependent diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C108700 | Insulin dependent diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C108711 | Type I diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C108712 | Type 1 diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C108800 | Insulin dependent diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C108811 | Type I diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C108812 | Type 1 diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C108911 | Type I diabetes mellitus maturity onset | Diabetes (Read v2) |
| READ2:C108A00 | Insulin-dependent diabetes without complication | Diabetes (Read v2) |
| READ2:C108A11 | Type I diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C108B00 | Insulin dependent diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C108B11 | Type I diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C108C00 | Insulin dependent diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C108D00 | Insulin dependent diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C108D11 | Type I diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C108E00 | Insulin dependent diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C108E11 | Type I diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C108E12 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C108F00 | Insulin dependent diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C108F11 | Type I diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C108F12 | Type 1 diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C108G00 | Insulin dependent diab mell with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C108H00 | Insulin dependent diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C108H11 | Type I diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C108J00 | Insulin dependent diab mell with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C108J11 | Type I diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C108J12 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C109.00 | Non-insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C109.11 | NIDDM - Non-insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C109.12 | Type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C109.13 | Type II diabetes mellitus | Diabetes (Read v2) |
| READ2:C109000 | Non-insulin-dependent diabetes mellitus with renal comps | Diabetes (Read v2) |
| READ2:C109011 | Type II diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C109012 | Type 2 diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C109100 | Non-insulin-dependent diabetes mellitus with ophthalm comps | Diabetes (Read v2) |
| READ2:C109111 | Type II diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C109112 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C109200 | Non-insulin-dependent diabetes mellitus with neuro comps | Diabetes (Read v2) |
| READ2:C109211 | Type II diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C109212 | Type 2 diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C109300 | Non-insulin-dependent diabetes mellitus with multiple comps | Diabetes (Read v2) |
| READ2:C109312 | Type 2 diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C109400 | Non-insulin dependent diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C109411 | Type II diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C109412 | Type 2 diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C109500 | Non-insulin dependent diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C109511 | Type II diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C109512 | Type 2 diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C109600 | Non-insulin-dependent diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C109611 | Type II diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C109612 | Type 2 diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C109700 | Non-insulin dependent diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C109711 | Type II diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C109712 | Type 2 diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C109900 | Non-insulin-dependent diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C109911 | Type II diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C109912 | Type 2 diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C109A00 | Non-insulin dependent diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C109A11 | Type II diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C109B00 | Non-insulin dependent diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C109B11 | Type II diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C109B12 | Type 2 diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C109C00 | Non-insulin dependent diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C109C11 | Type II diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C109C12 | Type 2 diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C109D00 | Non-insulin dependent diabetes mellitus with hypoglyca coma | Diabetes (Read v2) |
| READ2:C109D11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C109D12 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C109E00 | Non-insulin depend diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C109E11 | Type II diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C109E12 | Type 2 diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C109F11 | Type II diabetes mellitus with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C109F12 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C109G00 | Non-insulin dependent diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C109G11 | Type II diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C109G12 | Type 2 diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C109H11 | Type II diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C109H12 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C109J00 | Insulin treated Type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C109J11 | Insulin treated non-insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C109J12 | Insulin treated Type II diabetes mellitus | Diabetes (Read v2) |
| READ2:C109K00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E.00 | Type 1 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E.11 | Type I diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E.12 | Insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E000 | Type 1 diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C10E011 | Type I diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C10E012 | Insulin-dependent diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C10E100 | Type 1 diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C10E111 | Type I diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C10E112 | Insulin-dependent diabetes mellitus with ophthalmic comps | Diabetes (Read v2) |
| READ2:C10E200 | Type 1 diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C10E212 | Insulin-dependent diabetes mellitus with neurological comps | Diabetes (Read v2) |
| READ2:C10E300 | Type 1 diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C10E311 | Type I diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C10E312 | Insulin dependent diabetes mellitus with multiple complicat | Diabetes (Read v2) |
| READ2:C10E400 | Unstable type 1 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E411 | Unstable type I diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E412 | Unstable insulin dependent diabetes mellitus | Diabetes (Read v2) |
| READ2:C10E500 | Type 1 diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C10E511 | Type I diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C10E512 | Insulin dependent diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C10E600 | Type 1 diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C10E611 | Type I diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C10E612 | Insulin dependent diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C10E700 | Type 1 diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C10E711 | Type I diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C10E712 | Insulin dependent diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C10E800 | Type 1 diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C10E811 | Type I diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C10E812 | Insulin dependent diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C10EA00 | Type 1 diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C10EA11 | Type I diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C10EA12 | Insulin-dependent diabetes without complication | Diabetes (Read v2) |
| READ2:C10EB00 | Type 1 diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C10EC00 | Type 1 diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C10EC11 | Type I diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C10EC12 | Insulin dependent diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C10ED00 | Type 1 diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C10ED12 | Insulin dependent diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C10EE00 | Type 1 diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C10EE12 | Insulin dependent diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C10EF00 | Type 1 diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C10EF12 | Insulin dependent diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C10EG00 | Type 1 diabetes mellitus with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C10EH00 | Type 1 diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C10EJ00 | Type 1 diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C10EK00 | Type 1 diabetes mellitus with persistent proteinuria | Diabetes (Read v2) |
| READ2:C10EL00 | Type 1 diabetes mellitus with persistent microalbuminuria | Diabetes (Read v2) |
| READ2:C10EL11 | Type I diabetes mellitus with persistent microalbuminuria | Diabetes (Read v2) |
| READ2:C10EM00 | Type 1 diabetes mellitus with ketoacidosis | Diabetes (Read v2) |
| READ2:C10EM11 | Type I diabetes mellitus with ketoacidosis | Diabetes (Read v2) |
| READ2:C10EN00 | Type 1 diabetes mellitus with ketoacidotic coma | Diabetes (Read v2) |
| READ2:C10EN11 | Type I diabetes mellitus with ketoacidotic coma | Diabetes (Read v2) |
| READ2:C10EP00 | Type 1 diabetes mellitus with exudative maculopathy | Diabetes (Read v2) |
| READ2:C10EP11 | Type I diabetes mellitus with exudative maculopathy | Diabetes (Read v2) |
| READ2:C10EQ00 | Type 1 diabetes mellitus with gastroparesis | Diabetes (Read v2) |
| READ2:C10EQ11 | Type I diabetes mellitus with gastroparesis | Diabetes (Read v2) |
| READ2:C10F.00 | Type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10F.11 | Type II diabetes mellitus | Diabetes (Read v2) |
| READ2:C10F000 | Type 2 diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C10F011 | Type II diabetes mellitus with renal complications | Diabetes (Read v2) |
| READ2:C10F100 | Type 2 diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C10F111 | Type II diabetes mellitus with ophthalmic complications | Diabetes (Read v2) |
| READ2:C10F200 | Type 2 diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C10F211 | Type II diabetes mellitus with neurological complications | Diabetes (Read v2) |
| READ2:C10F300 | Type 2 diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C10F311 | Type II diabetes mellitus with multiple complications | Diabetes (Read v2) |
| READ2:C10F400 | Type 2 diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C10F411 | Type II diabetes mellitus with ulcer | Diabetes (Read v2) |
| READ2:C10F500 | Type 2 diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C10F511 | Type II diabetes mellitus with gangrene | Diabetes (Read v2) |
| READ2:C10F600 | Type 2 diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C10F611 | Type II diabetes mellitus with retinopathy | Diabetes (Read v2) |
| READ2:C10F700 | Type 2 diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C10F711 | Type II diabetes mellitus - poor control | Diabetes (Read v2) |
| READ2:C10F900 | Type 2 diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C10F911 | Type II diabetes mellitus without complication | Diabetes (Read v2) |
| READ2:C10FA00 | Type 2 diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C10FA11 | Type II diabetes mellitus with mononeuropathy | Diabetes (Read v2) |
| READ2:C10FB00 | Type 2 diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C10FB11 | Type II diabetes mellitus with polyneuropathy | Diabetes (Read v2) |
| READ2:C10FC00 | Type 2 diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C10FC11 | Type II diabetes mellitus with nephropathy | Diabetes (Read v2) |
| READ2:C10FD00 | Type 2 diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C10FD11 | Type II diabetes mellitus with hypoglycaemic coma | Diabetes (Read v2) |
| READ2:C10FE00 | Type 2 diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C10FE11 | Type II diabetes mellitus with diabetic cataract | Diabetes (Read v2) |
| READ2:C10FF00 | Type 2 diabetes mellitus with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C10FF11 | Type II diabetes mellitus with peripheral angiopathy | Diabetes (Read v2) |
| READ2:C10FG11 | Type II diabetes mellitus with arthropathy | Diabetes (Read v2) |
| READ2:C10FH00 | Type 2 diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C10FH11 | Type II diabetes mellitus with neuropathic arthropathy | Diabetes (Read v2) |
| READ2:C10FJ00 | Insulin treated Type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10FJ11 | Insulin treated Type II diabetes mellitus | Diabetes (Read v2) |
| READ2:C10FK00 | Hyperosmolar non-ketotic state in type 2 diabetes mellitus | Diabetes (Read v2) |
| READ2:C10FK11 | Hyperosmolar non-ketotic state in type II diabetes mellitus | Diabetes (Read v2) |
| READ2:C10FL00 | Type 2 diabetes mellitus with persistent proteinuria | Diabetes (Read v2) |
| READ2:C10FL11 | Type II diabetes mellitus with persistent proteinuria | Diabetes (Read v2) |
| READ2:C10FM00 | Type 2 diabetes mellitus with persistent microalbuminuria | Diabetes (Read v2) |
| READ2:C10FM11 | Type II diabetes mellitus with persistent microalbuminuria | Diabetes (Read v2) |
| READ2:C10FN00 | Type 2 diabetes mellitus with ketoacidosis | Diabetes (Read v2) |
| READ2:C10FN11 | Type II diabetes mellitus with ketoacidosis | Diabetes (Read v2) |
| READ2:C10FP00 | Type 2 diabetes mellitus with ketoacidotic coma | Diabetes (Read v2) |
| READ2:C10FQ00 | Type 2 diabetes mellitus with exudative maculopathy | Diabetes (Read v2) |
| READ2:C10FR00 | Type 2 diabetes mellitus with gastroparesis | Diabetes (Read v2) |

Not cached: 268 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH1709 version 3634, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1709/version/3634/detail/)
