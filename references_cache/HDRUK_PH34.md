---
reference_id: "HDRUK:PH34"
title: "Abdominal aortic aneurysm"
database: "HDR UK Phenotype Library"
source_snapshot: "PH34 version 68"
content_type: "structured_record"
---

# HDRUK:PH34  Abdominal aortic aneurysm

**PH34** version 68 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH34 |
| Version | 68 |
| Name | Abdominal aortic aneurysm |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/wqb7-wk59 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Abdominal-aortic-aneurysm---a587a710-1709-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Abdominal-aortic-aneurysm.cwl |
| Ontology | MONDO:0005350 abdominal aortic aneurysm |

## Definition

Use MODIFIED CALIBER 'Abdominal aortic aneurysm' phenotyping algorithm:

At the specified date, a patient is considered to have an 'Abdominal aortic aneurysm' IF they meet any of the criteria below on or before the specified date.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

1. Primary care

1. Diagnosis of AAA during a consultation: arterial_gprd: category 4

2. Performance of emergency AAA repair procedure recording during a consultation: aaa_ops_gprd: category 3

3. History of AAA during a consultation. The following Read code from CPRD:

1. Read:14AE.00 Medcode:16993 Descr:H/O: aortic aneurysm

2. Secondary care

1. Diagnosis of AAA as the primary or secondary diagnosis of any hospitalization: arterial_hes: category 4

2. Performance of emergency AAA repair procedure recorded: aaa_ops_opcs: category 3

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:14AE.00 | H/O: aortic aneurysm | Abdominal aortic aneurysm - Primary care |
| READ2:7A11000 | Emerg repl aneurysm bifurc aorta by anast aorta to fem art | Abdominal aortic aneurysm - Primary care |
| READ2:7A11200 | Emerg repl aneurysm bifurc aorta by anast aorta to iliac a | Abdominal aortic aneurysm - Primary care |
| READ2:7A11211 | Y graft of abdominal Aortic aneurysm (emergency) | Abdominal aortic aneurysm - Primary care |
| READ2:7A13.00 | Emergency replacement of aneurysmal segment of aorta | Abdominal aortic aneurysm - Primary care |
| READ2:7A13.11 | Emergency repair of aortic aneurysm | Abdominal aortic aneurysm - Primary care |
| READ2:7A13300 | Emerg replace aneurysm infrarenal aorta by anast aorta/aorta | Abdominal aortic aneurysm - Primary care |
| READ2:7A13400 | Emerg replace aneurysm abdom aorta by anast aorta/aorta NEC | Abdominal aortic aneurysm - Primary care |
| READ2:7A13411 | Tube graft abdominal Aortic aneurysm (emergency) | Abdominal aortic aneurysm - Primary care |
| READ2:7A13y00 | Emergency replacement of aneurysmal segment of aorta OS | Abdominal aortic aneurysm - Primary care |
| READ2:7A13z00 | Emergency replacement of aneurysmal segment of aorta NOS | Abdominal aortic aneurysm - Primary care |
| READ2:G714.00 | Abdominal aortic aneurysm without mention of rupture | Abdominal aortic aneurysm - Primary care |
| READ2:G714.11 | AAA - Abdominal aortic aneurysm without mention of rupture | Abdominal aortic aneurysm - Primary care |
| READ2:G716.00 | Aortic aneurysm without mention of rupture NOS | Abdominal aortic aneurysm - Primary care |
| READ2:G716000 | Thoracoabdominal aortic aneurysm, without mention of rupture | Abdominal aortic aneurysm - Primary care |
| 16034 (Med codes) | AAA without leak or rupture (4) | Abdominal aortic aneurysm - Primary care |
| 16993 (Med codes) | History of AAA (1) | Abdominal aortic aneurysm - Primary care |
| 17220 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 17345 (Med codes) | AAA without leak or rupture (4) | Abdominal aortic aneurysm - Primary care |
| 1867 (Med codes) | AAA without leak or rupture (4) | Abdominal aortic aneurysm - Primary care |
| 31613 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 40787 (Med codes) | AAA without leak or rupture (4) | Abdominal aortic aneurysm - Primary care |
| 45474 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 45477 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 54192 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 63408 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 66232 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 69922 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 92925 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| 96654 (Med codes) | Emergency AAA repair (3) | Abdominal aortic aneurysm - Primary care |
| ICD10:I714 | Abdominal aortic aneurysm, without mention of rupture | Abdominal aortic aneurysm - Secondary care - Diagnoses |
| ICD10:I716 | Thoracoabdominal aortic aneurysm, without mention of rupture | Abdominal aortic aneurysm - Secondary care - Diagnoses |
| ICD10:I719 | Aortic aneurysm of unspecified site, without mention of rupture | Abdominal aortic aneurysm - Secondary care - Diagnoses |

## Source

HDR UK Phenotype Library record PH34 version 68, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH34/version/68/detail/)
