---
reference_id: "HDRUK:PH36"
title: "Atrial fibrillation"
database: "HDR UK Phenotype Library"
source_snapshot: "PH36 version 72"
content_type: "structured_record"
---

# HDRUK:PH36  Atrial fibrillation

**PH36** version 72 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH36 |
| Version | 72 |
| Name | Atrial fibrillation |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/2r1r-n230 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Atrial-fibrillation---34e3c970-170a-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Atrial-fibrillation.cwl |
| Ontology | MONDO:0004981 atrial fibrillation |

## Definition

Use MODIFIED CALIBER 'Atrial fibrillation' phenotyping algorithm:

At the specified date, a patient is considered to have had 'Atrial fibrillation' or flutter IF they meet any of the criteria below on or before the specified date.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

1. 1. Historical & Diagnosed: first recorded AF code indicates monitoring of an existing condition, or reference to a previous AF diagnosis, or a diagnosis code for AF; preference given to the earliest dated record rather than diagnosis source (i.e. no preference for primary versus secondary care).

1. af_gprd: category 1, 2, 3, 4, 5, 6, 7

2. af_hes: category 6

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:14AN.00 | H/O: atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:14AR.00 | History of atrial flutter | Atrial fibrillation - Primary care |
| READ2:212R.00 | Atrial fibrillation resolved | Atrial fibrillation - Primary care |
| READ2:3272.00 | ECG: atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:3273.00 | ECG: atrial flutter | Atrial fibrillation - Primary care |
| READ2:662S.00 | Atrial fibrillation monitoring | Atrial fibrillation - Primary care |
| READ2:6A9..00 | Atrial fibrillation annual review | Atrial fibrillation - Primary care |
| READ2:9Os..00 | Atrial fibrillation monitoring administration | Atrial fibrillation - Primary care |
| READ2:9Os0.00 | Atrial fibrillation monitoring first letter | Atrial fibrillation - Primary care |
| READ2:9Os1.00 | Atrial fibrillation monitoring second letter | Atrial fibrillation - Primary care |
| READ2:9Os2.00 | Atrial fibrillation monitoring third letter | Atrial fibrillation - Primary care |
| READ2:9Os3.00 | Atrial fibrillation monitoring verbal invite | Atrial fibrillation - Primary care |
| READ2:9Os4.00 | Atrial fibrillation monitoring telephone invite | Atrial fibrillation - Primary care |
| READ2:9hF..00 | Exception reporting: atrial fibrillation quality indicators | Atrial fibrillation - Primary care |
| READ2:9hF1.00 | Excepted from atrial fibrillation qual indic: Inform dissent | Atrial fibrillation - Primary care |
| READ2:G573.00 | Atrial fibrillation and flutter | Atrial fibrillation - Primary care |
| READ2:G573000 | Atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:G573100 | Atrial flutter | Atrial fibrillation - Primary care |
| READ2:G573200 | Paroxysmal atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:G573300 | Non-rheumatic atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:G573400 | Permanent atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:G573500 | Persistent atrial fibrillation | Atrial fibrillation - Primary care |
| READ2:G573z00 | Atrial fibrillation and flutter NOS | Atrial fibrillation - Primary care |
| 1268 (Med codes) | Paroxysmal atrial fibrillation (3) | Atrial fibrillation - Primary care |
| 1664 (Med codes) | Atrial fibrillation, not otherwise specified (5) | Atrial fibrillation - Primary care |
| 1757 (Med codes) | Atrial flutter (7) | Atrial fibrillation - Primary care |
| 18746 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 2212 (Med codes) | Atrial fibrillation or flutter (6) | Atrial fibrillation - Primary care |
| 23437 (Med codes) | Atrial fibrillation or flutter (6) | Atrial fibrillation - Primary care |
| 28994 (Med codes) | History of atrial fibrillation or flutter (1) | Atrial fibrillation - Primary care |
| 35127 (Med codes) | Atrial fibrillation, not otherwise specified (5) | Atrial fibrillation - Primary care |
| 3757 (Med codes) | Atrial fibrillation, not otherwise specified (5) | Atrial fibrillation - Primary care |
| 39114 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 45773 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 57832 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 63350 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 6345 (Med codes) | History of atrial fibrillation or flutter (1) | Atrial fibrillation - Primary care |
| 6771 (Med codes) | Atrial flutter (7) | Atrial fibrillation - Primary care |
| 90187 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 90188 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 90189 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 90190 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 90191 (Med codes) | Atrial fibrillation monitoring (2) | Atrial fibrillation - Primary care |
| 93460 (Med codes) | History of atrial fibrillation or flutter (1) | Atrial fibrillation - Primary care |
| 96076 (Med codes) | Persistent or permanent atrial fibrillation (4) | Atrial fibrillation - Primary care |
| 96277 (Med codes) | Persistent or permanent atrial fibrillation (4) | Atrial fibrillation - Primary care |
| ICD10:I48 | Atrial fibrillation and flutter | Atrial fibrillation - Secondary care - Diagnoses |

## Source

HDR UK Phenotype Library record PH36 version 72, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH36/version/72/detail/)
