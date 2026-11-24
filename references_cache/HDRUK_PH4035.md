---
reference_id: "HDRUK:PH4035"
title: "Chronic Kidney Disease (CKD)"
database: "HDR UK Phenotype Library"
source_snapshot: "PH4035 version 9988"
content_type: "structured_record"
---

# HDRUK:PH4035  Chronic Kidney Disease (CKD)

**PH4035** version 9988 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH4035 |
| Version | 9988 |
| Name | Chronic Kidney Disease (CKD) |
| Type | Disease or syndrome |
| Template | BHF Data Science Centre Phenotype |
| Author | Samira Bell, Amy Coombe, Ross Forsyth, Anna Stevenson, Jadene Lewis, Laura Sherlock |
| Organisation | BHF Data Science Centre |
| Collections | BHF Data Science Centre |
| Coding systems | SNOMED CT codes; ICD10 codes; OPCS4 codes |
| Data sources | GPES Data for Pandemic Planning and Research (COVID-19); Hospital Episode Statistics Admitted Patient Care |
| Sex | Both |
| DOI | https://doi.org/10.48533/2ecn-8119 |
| Ontology | MONDO:0005300 chronic kidney disease |

## Definition

This phenotype is a rule-based Chronic Kidney Disease (CKD) phenotyping algorithm designed for use in electronic health records (EHR) to identify and stage people with CKD and from routinely collected health data. The algorithm was developed by a multidisciplinary working group to translate established clinical definitions of CKD into operational definitions that can be consistently applied to large-scale health datasets. The algorithm has been developed iteratively, and multiple versions are available to reflect updates and refinements over time.

Documentation relating to algorithm development, flowchart and implementation are available here (https://github.com/BHFDSC/hds_phenotypes_ckd/blob/main/docs/CKD_algorithm_markdown_updated.md)

Further code lists related to the CKD phenotyping algorithm implementation are also on the Phenotype Library:

• Dialysis available here (https://phenotypes.healthdatagateway.org/phenotypes/PH4036/version/9238/detail/) (PH4036)

• Transplant available here (https://phenotypes.healthdatagateway.org/phenotypes/PH4037/version/9239/detail/) (PH4037)

• Congenital kidney disease available here (https://phenotypes.healthdatagateway.org/phenotypes/PH4038/version/9240/detail/) (PH4038)

## Implementation

This phenotype is implemented as a rule-based algorithm for application to electronic health records, using structured logic applied to diagnosis, and laboratory data to identify CKD status and staging. The implementation coded in PySpark is publicly available through the BHF Data Science Centre [GitHub.](/https://github.com/BHFDSC/hds_phenotypes_ckd/tree/main).

## Codes

| Code | Description | Concept |
|---|---|---|
| OPCS4:M012 | Allotransplantation of kidney from live donor | Chronic Kidney Disease (CKD) |
| OPCS4:M013 | Allotransplantation of kidney from cadaver NEC | Chronic Kidney Disease (CKD) |
| OPCS4:M014 | Allotransplantation of kidney from cadaver heart beating | Chronic Kidney Disease (CKD) |
| OPCS4:M015 | Allotransplantation of kidney from cadaver heart non-beating | Chronic Kidney Disease (CKD) |
| OPCS4:M018 | Other specified transplantation of kidney | Chronic Kidney Disease (CKD) |
| OPCS4:M019 | Unspecified transplantation of kidney | Chronic Kidney Disease (CKD) |
| OPCS4:M026 | Excision of rejected transplanted kidney | Chronic Kidney Disease (CKD) |
| OPCS4:M027 | Excision of transplanted kidney NEC | Chronic Kidney Disease (CKD) |
| OPCS4:M172 | Pre-transplantation of kidney work-up - recipient | Chronic Kidney Disease (CKD) |
| OPCS4:M174 | Post-transplantation of kidney examination - recipient | Chronic Kidney Disease (CKD) |
| OPCS4:M178 | Other specified interventions associated with transplantation of kidney | Chronic Kidney Disease (CKD) |
| OPCS4:M179 | Unspecified interventions associated with transplantation of kidney | Chronic Kidney Disease (CKD) |
| OPCS4:X401 | Renal dialysis | Chronic Kidney Disease (CKD) |
| OPCS4:X402 | Peritoneal dialysis | Chronic Kidney Disease (CKD) |
| OPCS4:X403 | Haemodialysis NEC | Chronic Kidney Disease (CKD) |
| OPCS4:X405 | Automated peritoneal dialysis | Chronic Kidney Disease (CKD) |
| OPCS4:X406 | Continuous ambulatory peritoneal dialysis | Chronic Kidney Disease (CKD) |
| OPCS4:X408 | Other specified compensation for renal failure | Chronic Kidney Disease (CKD) |
| OPCS4:X409 | Unspecified compensation for renal failur | Chronic Kidney Disease (CKD) |
| ICD10:E102 | Type 1 diabetes mellitus with renal complications​ | Chronic Kidney Disease (CKD) |
| ICD10:E112 | Type 2 diabetes mellitus with renal complications​ | Chronic Kidney Disease (CKD) |
| ICD10:E122 | Malnutrition-related diabetes mellitus with renal complications​ | Chronic Kidney Disease (CKD) |
| ICD10:E132 | Other specified diabetes mellitus with renal complications​ | Chronic Kidney Disease (CKD) |
| ICD10:E142 | Unspecified diabetes mellitus with renal complications​ | Chronic Kidney Disease (CKD) |
| ICD10:I120 | Hypertensive renal disease with renal failure​ | Chronic Kidney Disease (CKD) |
| ICD10:I129 | Hypertensive renal disease without renal failure​ | Chronic Kidney Disease (CKD) |
| ICD10:I130 | Hypertensive heart and renal disease with (congestive) heart failure​ | Chronic Kidney Disease (CKD) |
| ICD10:I131 | Hypertensive heart and renal disease with renal failure​ | Chronic Kidney Disease (CKD) |
| ICD10:I132 | Hypertensive heart and renal disease with both (congestive) heart failure and renal failure​ | Chronic Kidney Disease (CKD) |
| ICD10:I139 | Hypertensive heart and renal disease | Chronic Kidney Disease (CKD) |
| ICD10:I770 | Arteriovenuous fistula | Chronic Kidney Disease (CKD) |
| ICD10:M103 | Gout due to impairment of renal function | Chronic Kidney Disease (CKD) |
| ICD10:N00 | Acute nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N01 | Rapidly progressive nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N03 | Chronic nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N04 | Nephrotic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N052 | Unspecified nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N053 | Unspecified nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N054 | Unspecified nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N055 | Unspecified nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N056 | Unspecified nephritic syndrome | Chronic Kidney Disease (CKD) |
| ICD10:N072 | Hereditary nephropathy | Chronic Kidney Disease (CKD) |
| ICD10:N073 | Hereditary nephropathy | Chronic Kidney Disease (CKD) |
| ICD10:N074 | Hereditary nephropathy | Chronic Kidney Disease (CKD) |
| ICD10:N08 | Glomerular disorders in diseases classified elsewhere | Chronic Kidney Disease (CKD) |
| ICD10:N165 | Renal tubulo-interstitial disorders in transplant rejection​ | Chronic Kidney Disease (CKD) |
| ICD10:N180 | End-stage renal disease | Chronic Kidney Disease (CKD) |
| ICD10:N181 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N182 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N183 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N184 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N185 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N186 | Patients with CKD requiring dialysis​ | Chronic Kidney Disease (CKD) |
| ICD10:N189 | Chronic kidney disease | Chronic Kidney Disease (CKD) |
| ICD10:N19 | Unspecified kidney failure | Chronic Kidney Disease (CKD) |
| ICD10:T824 | Mechanical complication of vascular dialysis catheter​ | Chronic Kidney Disease (CKD) |
| ICD10:T861 | Kidney transplant failure and rejection | Chronic Kidney Disease (CKD) |
| ICD10:Y602 | During kidney dialysis or other perfusion​ | Chronic Kidney Disease (CKD) |
| ICD10:Y612 | During kidney dialysis or other perfusion​ | Chronic Kidney Disease (CKD) |
| ICD10:Y622 | During kidney dialysis or other perfusion​ | Chronic Kidney Disease (CKD) |
| ICD10:Y841 | Kidney dialysis | Chronic Kidney Disease (CKD) |
| ICD10:Z49 | Care involving dialysis | Chronic Kidney Disease (CKD) |
| ICD10:Z490 | Preparatory care for dialysis​ | Chronic Kidney Disease (CKD) |
| ICD10:Z491 | Extracorporeal dialysis​ | Chronic Kidney Disease (CKD) |
| ICD10:Z492 | Other dialysis​ | Chronic Kidney Disease (CKD) |
| ICD10:Z940 | Kidney transplant status | Chronic Kidney Disease (CKD) |
| ICD10:Z992 | Dependence on renal dialysis | Chronic Kidney Disease (CKD) |

Not cached: 441 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH4035 version 9988, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH4035/version/9988/detail/)
