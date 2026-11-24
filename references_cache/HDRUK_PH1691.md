---
reference_id: "HDRUK:PH1691"
title: "Chronic paediatric conditions: Cystic Fibrosis"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1691 version 3622"
content_type: "structured_record"
---

# HDRUK:PH1691  Chronic paediatric conditions: Cystic Fibrosis

**PH1691** version 3622 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1691 |
| Version | 3622 |
| Name | Chronic paediatric conditions: Cystic Fibrosis |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Swann OV, Williams TC, Fraser LK, Farrell J, Parker M, Kennedy J, Seabourne M, Brophy S, Harrison EM, Docherty AB, Pollock L |
| Collections | Phenotype Library |
| Coding systems | SNOMED CT codes; ICD10 codes; Read codes v2 |
| Data sources | Hospital Episode Statistics Admitted Patient Care; OpenSAFELY SNOMED CT; Patient Episode Dataset for Wales (PEDW); Welsh Longitudinal General Practice Dataset (WLGP) - Welsh Primary Care |
| Sex | Both |
| Event date range | 2021/01/01 - 2021/01/01 |
| DOI | https://doi.org/10.48533/z0df-2110 |
| Ontology | MONDO:0009061 cystic fibrosis |

## Definition

This code list is part of a set of harmonised code lists to identify chronic paediatric conditions across primary and secondary care datasets across the UK.

Published ICD-10 and Read v2 code lists were combined with SNOMED codes derived using CALIBERas below:

- Read v2 cystic fibrosis code list: https://phenotypes.healthdatagateway.org/phenotypes/PH14/version/28/detail/ (https://phenotypes.healthdatagateway.org/phenotypes/PH14/version/28/detail/) - ICD-10 cystic fibrosis diagnoses as per Hardelid 2014 mapped through CALIBER to produce SNOMED code list.

### Methods

Chronic paediatric conditions were defined as health problems requiring medical follow-up for more than 12 months in 50% or more of cases. Code lists were produced by mapping existing ICD-10 codes for chronic paediatric conditions to SNOMED and Read v2 codes using the CALIBER R package, with review by paediatric sub-specialists.

An established ICD-10 code list of chronic paediatric conditions (Hardelid 2014) was used as the basis for the new lists.1 Chronic paediatric conditions were defined as any health problem requiring medical follow-up (hospital admission, outpatient follow up or use of support services such as physiotherapy) for more than 12 months in 50% or more of cases.[1] A Chronic Paediatric Conditions Committee of paediatric sub-specialists was established. The original ICD-10 list was screened by two paediatricians and acute conditions removed, with disagreements resolved by a third paediatrician. Conditions which were likely acute and would not fulfil our chronic disease definition were excluded, including skeletal injuries and self-harm. Drug-induced conditions were excluded as chronicity was not known. Infections other than human immunodeficiency virus (HIV), hepatitis B or C, or congenital infections (syphilis / toxoplasmosis / rubella / herpes simplex virus / cytomegalovirus) were excluded. Chronic sequelae of infections were retained.

Published code lists were then identified for Read v2 and SNOMED codes for well-characterised conditions including asthma, diabetes, cystic fibrosis and cancer. The remaining ICD-10 codes were mapped to SNOMED and Read v2 codes using the CALIBER R package and Technology Reference Update Distribution NHS Data Migration tables [2] to produce new code lists suitable for primary care data. These resulting code lists were screened by two sub-specialists to ensure conditions were chronic and in the correct subgroup with disagreements resolved by a third clinician.

### References:

1. Hardelid P, Dattani N, Gilbert R. Estimating the prevalence of chronic conditions in children who die in England, Scotland and Wales: a data linkage cohort study. BMJ Open 2014; 4: e005331. 2. CALIBER codelists-package: Generate ICD, Read and OPCS codelists in CALIBER codelists: Generate ICD10, Read and OPCS codelists, https://rdrr.io/rforge/CALIBERcodelists/man/CALIBERcodelists-package.html (https://rdrr.io/rforge/CALIBERcodelists/man/CALIBERcodelists-package.html) (accessed 19 October 2022).

## Implementation

We have considered conditions to be active if they had been coded for in the preceding five years. In addition, conditions from the following subgroups were considered to be permanent, therefore active if coded for at any time: metabolic, diabetes, cystic fibrosis, transplant, receiving palliative care, other congenital multisystem syndromes and chromosomal abnormalities, immunological and cerebral palsy / paralysis (a subgroup of "Other neurology" code list).

## Codes

| Code | Description | Concept |
|---|---|---|
| ICD10:E84 | Cystic fibrosis | Cystic Fibrosis (ICD-10) |
| ICD10:E840 | Cystic fibrosis with pulmonary manifestations | Cystic Fibrosis (ICD-10) |
| ICD10:E841 | Cystic fibrosis with intestinal manifestations | Cystic Fibrosis (ICD-10) |
| ICD10:E848 | Cystic fibrosis with other manifestations | Cystic Fibrosis (ICD-10) |
| ICD10:E849 | Cystic fibrosis, unspecified | Cystic Fibrosis (ICD-10) |
| READ2:C10N100 | Cystic fibrosis related diabetes mellitus | Cystic Fibrosis (Read v2) |
| READ2:C370.00 | Cystic fibrosis | Cystic Fibrosis (Read v2) |
| READ2:C370000 | Cystic fibrosis with no meconium ileus | Cystic Fibrosis (Read v2) |
| READ2:C370100 | Cystic fibrosis with meconium ileus | Cystic Fibrosis (Read v2) |
| READ2:C370111 | Meconium ileus in cystic fibrosis | Cystic Fibrosis (Read v2) |
| READ2:C370200 | Cystic fibrosis with pulmonary manifestations | Cystic Fibrosis (Read v2) |
| READ2:C370300 | Cystic fibrosis with intestinal manifestations | Cystic Fibrosis (Read v2) |
| READ2:C370400 | Arthropathy in cystic fibrosis | Cystic Fibrosis (Read v2) |
| READ2:C370500 | Cystic fibrosis with distal intestinal obstruction syndrome | Cystic Fibrosis (Read v2) |
| READ2:C370700 | Liver disease due to cystic fibrosis | Cystic Fibrosis (Read v2) |
| READ2:C370800 | Cystic fibrosis related cirrhosis | Cystic Fibrosis (Read v2) |
| READ2:C370900 | Exacerbation of cystic fibrosis | Cystic Fibrosis (Read v2) |
| READ2:C370y00 | Cystic fibrosis with combined manifestations | Cystic Fibrosis (Read v2) |
| READ2:C370z00 | Cystic fibrosis NOS | Cystic Fibrosis (Read v2) |

Not cached: 28 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH1691 version 3622, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1691/version/3622/detail/)
