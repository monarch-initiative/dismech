---
reference_id: "HDRUK:PH215"
title: "Myocardial infarction"
database: "HDR UK Phenotype Library"
source_snapshot: "PH215 version 430"
content_type: "structured_record"
---

# HDRUK:PH215  Myocardial infarction

**PH215** version 430 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH215 |
| Version | 430 |
| Name | Myocardial infarction |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/8smg-ga13 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Myocardial-infarction---b32f9260-1795-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Myocardial-infarction.cwl |
| Ontology | MONDO:0005068 myocardial infarction |

## Definition

Use MODIFIED CALIBER 'Myocardial infarction' phenotyping algorithm:

At the specified date, a patient is considered to have had a 'Myocardial infarction' IF they meet any of the criteria below on or before the specified date.

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date.

1. Primary care diagnosis of MI: myo_infarct_gprd: category 1, category 2, category 3, category 4, category 5, category 6, category 7

2. Secondary care diagnosis of MI: myo_infarct_hes: category 1, category 5, category 6, category 7

3. Secondary care procedure code for coronary thrombolysis: lysis_opcs category 2

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:14A3.00 | H/O: myocardial infarct <60 | Myocardial infarction - Primary care |
| READ2:14A4.00 | H/O: myocardial infarct >60 | Myocardial infarction - Primary care |
| READ2:14AH.00 | H/O: Myocardial infarction in last year | Myocardial infarction - Primary care |
| READ2:323..00 | ECG: myocardial infarction | Myocardial infarction - Primary care |
| READ2:3233 | ECG: antero-septal infarct. | Myocardial infarction - Primary care |
| READ2:3234 | ECG:posterior/inferior infarct | Myocardial infarction - Primary care |
| READ2:3235 | ECG: subendocardial infarct | Myocardial infarction - Primary care |
| READ2:3236 | ECG: lateral infarction | Myocardial infarction - Primary care |
| READ2:323Z.00 | ECG: myocardial infarct NOS | Myocardial infarction - Primary care |
| READ2:889A.00 | Diab mellit insulin-glucose infus acute myocardial infarct | Myocardial infarction - Primary care |
| READ2:G30..00 | Acute myocardial infarction | Myocardial infarction - Primary care |
| READ2:G30..11 | Attack - heart | Myocardial infarction - Primary care |
| READ2:G30..12 | Coronary thrombosis | Myocardial infarction - Primary care |
| READ2:G30..13 | Cardiac rupture following myocardial infarction (MI) | Myocardial infarction - Primary care |
| READ2:G30..14 | Heart attack | Myocardial infarction - Primary care |
| READ2:G30..15 | MI - acute myocardial infarction | Myocardial infarction - Primary care |
| READ2:G30..16 | Thrombosis - coronary | Myocardial infarction - Primary care |
| READ2:G30..17 | Silent myocardial infarction | Myocardial infarction - Primary care |
| READ2:G300.00 | Acute anterolateral infarction | Myocardial infarction - Primary care |
| READ2:G301.00 | Other specified anterior myocardial infarction | Myocardial infarction - Primary care |
| READ2:G301000 | Acute anteroapical infarction | Myocardial infarction - Primary care |
| READ2:G301100 | Acute anteroseptal infarction | Myocardial infarction - Primary care |
| READ2:G301z00 | Anterior myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G302.00 | Acute inferolateral infarction | Myocardial infarction - Primary care |
| READ2:G303.00 | Acute inferoposterior infarction | Myocardial infarction - Primary care |
| READ2:G304.00 | Posterior myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G305.00 | Lateral myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G306.00 | True posterior myocardial infarction | Myocardial infarction - Primary care |
| READ2:G307.00 | Acute subendocardial infarction | Myocardial infarction - Primary care |
| READ2:G307000 | Acute non-Q wave infarction | Myocardial infarction - Primary care |
| READ2:G307100 | Acute non-ST segment elevation myocardial infarction | Myocardial infarction - Primary care |
| READ2:G308.00 | Inferior myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G309.00 | Acute Q-wave infarct | Myocardial infarction - Primary care |
| READ2:G30A.00 | Mural thrombosis | Myocardial infarction - Primary care |
| READ2:G30B.00 | Acute posterolateral myocardial infarction | Myocardial infarction - Primary care |
| READ2:G30X.00 | Acute transmural myocardial infarction of unspecif site | Myocardial infarction - Primary care |
| READ2:G30X000 | Acute ST segment elevation myocardial infarction | Myocardial infarction - Primary care |
| READ2:G30y.00 | Other acute myocardial infarction | Myocardial infarction - Primary care |
| READ2:G30y000 | Acute atrial infarction | Myocardial infarction - Primary care |
| READ2:G30y100 | Acute papillary muscle infarction | Myocardial infarction - Primary care |
| READ2:G30y200 | Acute septal infarction | Myocardial infarction - Primary care |
| READ2:G30yz00 | Other acute myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G30z.00 | Acute myocardial infarction NOS | Myocardial infarction - Primary care |
| READ2:G310.00 | Postmyocardial infarction syndrome | Myocardial infarction - Primary care |
| READ2:G310.11 | Dressler's syndrome | Myocardial infarction - Primary care |
| READ2:G31y100 | Microinfarction of heart | Myocardial infarction - Primary care |
| READ2:G32..00 | Old myocardial infarction | Myocardial infarction - Primary care |
| READ2:G32..11 | Healed myocardial infarction | Myocardial infarction - Primary care |
| READ2:G32..12 | Personal history of myocardial infarction | Myocardial infarction - Primary care |
| READ2:G33z500 | Post infarct angina | Myocardial infarction - Primary care |
| READ2:G35..00 | Subsequent myocardial infarction | Myocardial infarction - Primary care |
| READ2:G350.00 | Subsequent myocardial infarction of anterior wall | Myocardial infarction - Primary care |
| READ2:G351.00 | Subsequent myocardial infarction of inferior wall | Myocardial infarction - Primary care |
| READ2:G353.00 | Subsequent myocardial infarction of other sites | Myocardial infarction - Primary care |
| READ2:G35X.00 | Subsequent myocardial infarction of unspecified site | Myocardial infarction - Primary care |
| READ2:G36..00 | Certain current complication follow acute myocardial infarct | Myocardial infarction - Primary care |
| READ2:G360.00 | Haemopericardium/current comp folow acut myocard infarct | Myocardial infarction - Primary care |
| READ2:G361.00 | Atrial septal defect/curr comp folow acut myocardal infarct | Myocardial infarction - Primary care |
| READ2:G362.00 | Ventric septal defect/curr comp fol acut myocardal infarctn | Myocardial infarction - Primary care |
| READ2:G363.00 | Ruptur cardiac wall w'out haemopericard/cur comp fol ac MI | Myocardial infarction - Primary care |
| READ2:G364.00 | Ruptur chordae tendinae/curr comp fol acute myocard infarct | Myocardial infarction - Primary care |
| READ2:G365.00 | Rupture papillary muscle/curr comp fol acute myocard infarct | Myocardial infarction - Primary care |
| READ2:G366.00 | Thrombosis atrium,auric append&vent/curr comp foll acute MI | Myocardial infarction - Primary care |
| READ2:G38..00 | Postoperative myocardial infarction | Myocardial infarction - Primary care |
| READ2:G380.00 | Postoperative transmural myocardial infarction anterior wall | Myocardial infarction - Primary care |
| READ2:G381.00 | Postoperative transmural myocardial infarction inferior wall | Myocardial infarction - Primary care |
| READ2:G384.00 | Postoperative subendocardial myocardial infarction | Myocardial infarction - Primary care |
| READ2:G38z.00 | Postoperative myocardial infarction, unspecified | Myocardial infarction - Primary care |
| READ2:G501.00 | Post infarction pericarditis | Myocardial infarction - Primary care |
| READ2:Gyu3400 | [X]Acute transmural myocardial infarction of unspecif site | Myocardial infarction - Primary care |
| 10562 (Med codes) | NSTEMI (4) | Myocardial infarction - Primary care |
| 1204 (Med codes) | Possible MI or uncertain date (2) | Myocardial infarction - Primary care |
| 12139 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 12229 (Med codes) | STEMI (3) | Myocardial infarction - Primary care |
| 13566 (Med codes) | Possible MI or uncertain date (2) | Myocardial infarction - Primary care |
| 13571 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 14658 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 14897 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 14898 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 15661 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 16408 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 1677 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 1678 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 17133 (Med codes) | Possible MI or uncertain date (2) | Myocardial infarction - Primary care |
| 17464 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 17689 (Med codes) | Possible MI or uncertain date (2) | Myocardial infarction - Primary care |
| 17872 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 18842 (Med codes) | Subsequent MI (6) | Myocardial infarction - Primary care |
| 23579 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 23708 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 23892 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 241 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 24126 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 2491 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 26972 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 26975 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 28736 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 29553 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 29643 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 29758 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 30330 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 30421 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 32272 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 32854 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 34803 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 35119 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 35674 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 36423 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 3704 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 37657 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 38609 (Med codes) | Subsequent MI (6) | Myocardial infarction - Primary care |
| 4017 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 40399 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 40429 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 41221 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 41835 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 45809 (Med codes) | Subsequent MI (6) | Myocardial infarction - Primary care |
| 46017 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 46112 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 46166 (Med codes) | Subsequent MI (6) | Myocardial infarction - Primary care |
| 46276 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 50372 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 52705 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 5387 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 55401 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 59032 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 59189 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 59940 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 61670 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 62626 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 63467 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 68357 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 68748 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 69474 (Med codes) | Complications of MI (7) | Myocardial infarction - Primary care |
| 72562 (Med codes) | Subsequent MI (6) | Myocardial infarction - Primary care |
| 7783 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 8935 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 9507 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| 9555 (Med codes) | History of MI (1) | Myocardial infarction - Primary care |
| 96838 (Med codes) | Acute MI not further specified (5) | Myocardial infarction - Primary care |
| ICD10:I21 | Acute myocardial infarction | Myocardial infarction - Secondary care - Diagnoses |
| ICD10:I22 | Subsequent myocardial infarction | Myocardial infarction - Secondary care - Diagnoses |
| ICD10:I23 | Certain current complications following acute myocardial infarction | Myocardial infarction - Secondary care - Diagnoses |
| ICD10:I241 | Dressler's syndrome | Myocardial infarction - Secondary care - Diagnoses |
| ICD10:I252 | Old myocardial infarction | Myocardial infarction - Secondary care - Diagnoses |

## Source

HDR UK Phenotype Library record PH215 version 430, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH215/version/430/detail/)
