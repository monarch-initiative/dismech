---
reference_id: "HDRUK:PH1"
title: "COVID-19 infection"
database: "HDR UK Phenotype Library"
source_snapshot: "PH1 version 2"
content_type: "structured_record"
---

# HDRUK:PH1  COVID-19 infection

**PH1** version 2 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH1 |
| Version | 2 |
| Name | COVID-19 infection |
| Type | Disease or syndrome |
| Template | BHF Data Science Centre Phenotype |
| Author | BHF CVD COVID UK Consortium |
| Organisation | BHF Data Science Centre |
| Collections | BHF Data Science Centre; Phenotype Library |
| Coding systems | ICD10 codes; SNOMED CT codes |
| Data sources | GPES Data for Pandemic Planning and Research (COVID-19); Hospital Episode Statistics Admitted Patient Care; Civil Registration - Deaths; Covid-19 Second Generation Surveillance System |
| Sex | Both |
| Event date range | 01/01/2020 - 31/10/2020 |
| DOI | https://doi.org/10.48533/wjmc-hh14 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/COVID-19-infection---0ad8bf70-16ea-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/COVID-19-infection.cwl |
| Ontology | MONDO:0100096 COVID-19 |

## Definition

We ascertained people with a confirmed or suspected Covid-19 diagnosis as follows:

1) a positive PCR or antigen test from the Covid-19 laboratory test data, with specimen date on or before 31 October 2020; or

2) a Covid-19 diagnosis SNOMED-CT concept code appearing in the primary care data, with event date on or before 31 October; or

3) a diagnosis ICD-10 code appearing in the hospital episodes (main or secondary diagnostic code position in the admitted patient care component of the hospital episode statistics), with admission date on or before 31 October or

4) death registration with a mention (as underlying on contributing cause) of a diagnosis ICD-10 code , with death registration date on or before 31 October 2020.

## Codes

| Code | Description | Concept |
|---|---|---|
| ICD10:U071 | COVID-19, virus identified | COVID-19 infection - Hospitalizations |
| ICD10:U072 | COVID-19, virus not identified | COVID-19 infection - Hospitalizations |

Not cached: 37 SNOMED CT codes. See the library record for those codes.

## Source

HDR UK Phenotype Library record PH1 version 2, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH1/version/2/detail/)
