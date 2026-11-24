---
reference_id: "HDRUK:PH4039"
title: "Myocardial infarction"
database: "HDR UK Phenotype Library"
source_snapshot: "PH4039 version 9990"
content_type: "structured_record"
---

# HDRUK:PH4039  Myocardial infarction

**PH4039** version 9990 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH4039 |
| Version | 9990 |
| Name | Myocardial infarction |
| Type | Disease or syndrome |
| Template | BHF Data Science Centre Phenotype |
| Author | Farrell J, Sherlock L, Lessels S, Mullen L, Akowuah E, Asselbergs F W, Gale C, Grant S, Harper C, Khunti K, MacArthur J, Mamas M, McConnachie A, Murphy G, Nadarajah R, Newby D, Nolan J, Petersen S, Quint J, Rahimi K, Stables R, Storey R, Denaxas S, Sydes M R |
| Collections | BHF Data Science Centre |
| Coding systems | ICD10 codes |
| Sex | Both |
| DOI | https://doi.org/10.48533/yzm3-k527 |
| Ontology | MONDO:0005068 myocardial infarction |

## Implementation

This code list was created as part of an algorithm to dectect myocardial infarction (MI), which was developed under the BHF Data Science Centre's Standardising Clinical Outcome measures in Routinely collected Electronic healthcare systems data (SCORE-CVD) project. It provides a pipeline for identifying MI events, including recurrent MIs, in HES APC and ONS deaths datasets. A ready to implement Databricks and R studio version of the MI algorithm, can be found on the BHF Data Science Centre Github here (https://github.com/BHFDSC/hds_phenotypes_score_cvd_mi)

## Codes

| Code | Description | Concept |
|---|---|---|
| ICD10:I21 | Acute myocardial infarction | Codelist 1 |
| ICD10:I22 | Subsequent myocardial infarction | Codelist 1 |

## Source

HDR UK Phenotype Library record PH4039 version 9990, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH4039/version/9990/detail/)
