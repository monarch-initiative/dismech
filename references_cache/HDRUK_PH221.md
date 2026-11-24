---
reference_id: "HDRUK:PH221"
title: "Obesity"
database: "HDR UK Phenotype Library"
source_snapshot: "PH221 version 442"
content_type: "structured_record"
---

# HDRUK:PH221  Obesity

**PH221** version 442 — computable phenotype record from the HDR UK Phenotype Library.

## Record

| Field | Value |
|---|---|
| Phenotype ID | PH221 |
| Version | 442 |
| Name | Obesity |
| Type | Disease or syndrome |
| Template | Clinical-Coded Phenotype |
| Author | Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A |
| Collections | CALIBER; Phenotype Library |
| Coding systems | ICD10 codes; Read codes v2; Med codes |
| Data sources | CPRD GOLD; HES Admitted Patient Care data for CPRD GOLD |
| Sex | Both |
| Event date range | 01/01/1999 - 01/07/2016 |
| DOI | https://doi.org/10.48533/nst9-hf80 |
| Phenoflow | https://kclhi.org/phenoflow/workflows/github.com/phenoflow/Obesity---4c978140-1798-11ef-9de4-4d4ea830ad16/blob/read-potential-cases-fhir/Obesity.cwl |
| Ontology | MONDO:0011122 obesity disorder |

## Definition

At the specified date, a patient is defined as having had 'Obesity' IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care

1. 'Obesity' diagnosis or history of diagnosis or procedure during a consultation

OR

2. IF enttype = 13 (Weight) available on or before specified date AND data3 not missing, BMI = data3. If BMI > 30, patient is defined as having had 'Obesity'. OR

3. If enttype = 13 (Weight) available on or before specified date AND data3 missing, BMI = data1 (enttype 13) /(data2 ^2) (enttype 14 = Height). If BMI > 30, patient is defined as having had 'Obesity'. IF height not available on same eventdate as weight, use most recent height for age > 18 years. OR Secondary care (ICD10)

1. ALL diagnoses of 'Obesity' or history of diagnosis during a hospitalization

## Publications

- Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI 10.1016/S2589-7500(19)30012-3

## Codes

| Code | Description | Concept |
|---|---|---|
| READ2:1444.00 | H/O: obesity | Obesity - Primary care |
| READ2:212Q.00 | Obesity resolved | Obesity - Primary care |
| READ2:222A.00 | O/E - obese | Obesity - Primary care |
| READ2:22A5.11 | O/E - obese | Obesity - Primary care |
| READ2:22K5.00 | Body mass index 30+ - obesity | Obesity - Primary care |
| READ2:22K7.00 | Body mass index 40+ - severely obese | Obesity - Primary care |
| READ2:66C..00 | Obesity monitoring | Obesity - Primary care |
| READ2:66C1.00 | Initial obesity assessment | Obesity - Primary care |
| READ2:66C2.00 | Follow-up obesity assessment | Obesity - Primary care |
| READ2:66C4.00 | Has seen dietician - obesity | Obesity - Primary care |
| READ2:66C5.00 | Treatment of obesity changed | Obesity - Primary care |
| READ2:66C6.00 | Treatment of obesity started | Obesity - Primary care |
| READ2:66CE.00 | Reason for obesity therapy - occupational | Obesity - Primary care |
| READ2:66CZ.00 | Obesity monitoring NOS | Obesity - Primary care |
| READ2:7611400.0 | Sleeve gastrectomy and duodenal switch | Obesity - Primary care |
| READ2:7611500.0 | Sleeve gastrectomy NEC | Obesity - Primary care |
| READ2:7611600.0 | Laparoscopic sleeve gastrectomy | Obesity - Primary care |
| READ2:7613100.0 | Partitioning of stomach | Obesity - Primary care |
| READ2:7613111.0 | Mason vertical banded gastroplasty | Obesity - Primary care |
| READ2:7613200.0 | Laparoscopic adjustable gastric banding | Obesity - Primary care |
| READ2:7613300.0 | Partitioning of stomach using band | Obesity - Primary care |
| READ2:7613400.0 | Partitioning of stomach using staples | Obesity - Primary care |
| READ2:7613500.0 | Partitioning of stomach NEC | Obesity - Primary care |
| READ2:7613600.0 | Maintenance of gastric band | Obesity - Primary care |
| READ2:7614100.0 | Bypass of stomach by anastomosis of stomach to duodenum | Obesity - Primary care |
| READ2:7615000.0 | Bypass stomach by anastomosis stomach to transposed jejunum | Obesity - Primary care |
| READ2:7616000.0 | Bypass of stomach by anastomosis of stomach to jejunum NEC | Obesity - Primary care |
| READ2:7616013.0 | Mason high gastric bypass | Obesity - Primary care |
| READ2:7616015.0 | Printer high gastric bypass | Obesity - Primary care |
| READ2:7616600.0 | Laparoscopic gastric bypass | Obesity - Primary care |
| READ2:761A500 | Removal of gastric band | Obesity - Primary care |
| READ2:7633.00 | Bypass of jejunum | Obesity - Primary care |
| READ2:7633000.0 | Bypass of jejunum by anastomosis of jejunum to jejunum | Obesity - Primary care |
| READ2:7633100.0 | Bypass of jejunum by anastomosis of jejunum to ileum | Obesity - Primary care |
| READ2:7633200.0 | Bypass of jejunum by anastomosis of jejunum to colon | Obesity - Primary care |
| READ2:7633y00 | Other specified bypass of jejunum | Obesity - Primary care |
| READ2:7633z00 | Bypass of jejunum NOS | Obesity - Primary care |
| READ2:7642500.0 | Duodenal switch | Obesity - Primary care |
| READ2:9OK..00 | Obesity monitoring admin. | Obesity - Primary care |
| READ2:9OK..11 | Obesity clinic administration | Obesity - Primary care |
| READ2:9OK1.00 | Attends obesity monitoring | Obesity - Primary care |
| READ2:9OK2.00 | Refuses obesity monitoring | Obesity - Primary care |
| READ2:9OK3.00 | Obesity monitoring default | Obesity - Primary care |
| READ2:9OK4.00 | Obesity monitoring 1st letter | Obesity - Primary care |
| READ2:9OK5.00 | Obesity monitoring 2nd letter | Obesity - Primary care |
| READ2:9OK6.00 | Obesity monitoring 3rd letter | Obesity - Primary care |
| READ2:9OK7.00 | Obesity monitoring verbal inv. | Obesity - Primary care |
| READ2:9OK8.00 | Obesity monitor phone invite | Obesity - Primary care |
| READ2:9OKA.00 | Obesity monitoring check done | Obesity - Primary care |
| READ2:9OKZ.00 | Obesity monitoring admin.NOS | Obesity - Primary care |
| READ2:C38..00 | Obesity and other hyperalimentation | Obesity - Primary care |
| READ2:C380.00 | Obesity | Obesity - Primary care |
| READ2:C380000 | Obesity due to excess calories | Obesity - Primary care |
| READ2:C380100 | Drug-induced obesity | Obesity - Primary care |
| READ2:C380200 | Extreme obesity with alveolar hypoventilation | Obesity - Primary care |
| READ2:C380300 | Morbid obesity | Obesity - Primary care |
| READ2:C380400 | Central obesity | Obesity - Primary care |
| READ2:C380500 | Generalised obesity | Obesity - Primary care |
| READ2:C380600 | Adult-onset obesity | Obesity - Primary care |
| READ2:C380700 | Lifelong obesity | Obesity - Primary care |
| READ2:C38y.11 | Pickwickian syndrome | Obesity - Primary care |
| READ2:C38y000 | Pickwickian syndrome | Obesity - Primary care |
| READ2:C38y011 | Obesity hypoventilation syndrome | Obesity - Primary care |
| READ2:C38z.00 | Obesity and other hyperalimentation NOS | Obesity - Primary care |
| READ2:C38z000 | Simple obesity NOS | Obesity - Primary care |
| READ2:Cyu7.00 | [X]Obesity and other hyperalimentation | Obesity - Primary care |
| READ2:Cyu7000 | [X]Other obesity | Obesity - Primary care |
| READ2:ZC2CM00 | Dietary advice for obesity | Obesity - Primary care |
| READ2:ZV45P00 | [V]Presence of gastric bypass | Obesity - Primary care |
| READ2:ZV65319 | [V]Dietary counselling in obesity | Obesity - Primary care |
| 103574.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 104129.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 104421.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 10728.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 11401.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 11461.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 13278.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 16196.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 17444.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 17477.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 18863.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 19929.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 21744.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 22556.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 22695.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 24755.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 25968.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 29538.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 3176.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 32843.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 34119.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 38059.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 38294.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 38632.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 38658.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 38799.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 39123.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 39797.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 40153.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 40977.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 430.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 47439.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 48417.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 49250.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 49409.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 52034.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 52036.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 52703.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 52735.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 52782.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 55585.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 55586.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 56107.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 56926.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 59622.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 59780.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 60421.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 62848.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 64123.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 64712.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 66406.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 67516.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 67517.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 69757.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 7082.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 70898.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 70950.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 7984.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 88474.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 8854.0 (Med codes) | Diagnosis of Obesity | Obesity - Primary care |
| 89148.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 89259.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 90454.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 90517.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 90600.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 92957.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 93378.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 95929.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| 97014.0 (Med codes) | History of Obesity | Obesity - Primary care |
| 97691.0 (Med codes) | Procedure for Obesity | Obesity - Primary care |
| ICD10:E66 | Obesity | Obesity - Secondary care - Diagnoses |

## Source

HDR UK Phenotype Library record PH221 version 442, from the library's public API (resolved code export, include/exclude rules applied). User-submitted library content is CC BY-SA 4.0 for non-commercial use unless the Definition states a record-specific licence.

[HDR UK record](https://phenotypes.healthdatagateway.org/phenotypes/PH221/version/442/detail/)
