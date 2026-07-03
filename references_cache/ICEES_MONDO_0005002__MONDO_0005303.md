---
reference_id: "ICEES:MONDO_0005002__MONDO_0005303"
title: "chronic obstructive pulmonary disease / drug dependence (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0005002__MONDO_0005303  chronic obstructive pulmonary disease ↔ drug dependence

**ICEES:MONDO_0005002__MONDO_0005303** - EHR correlation between chronic obstructive pulmonary disease (MONDO:0005002) and drug dependence (MONDO:0005303) in ICEES KG.

## Association

- Disorder A: chronic obstructive pulmonary disease (MONDO:0005002)
- Disorder B: drug dependence (MONDO:0005303)
- Predicate(s): correlated_with, positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| PCD_UNC_patient_2010_v6_binned_deidentified | 2.5868550484561916e-05 | 1 | 0.9959418860640677 | 1311 |
| PCD_UNC_patient_2011_v6_binned_deidentified | 2.0563772993113823e-05 | 1 | 0.9963818216259024 | 1392 |
| PCD_UNC_patient_2012_v6_binned_deidentified | 4.935271180353822e-05 | 1 | 0.994394788559694 | 1662 |
| PCD_UNC_patient_2013_v6_binned_deidentified | 3.490855227510447e-05 | 1 | 0.995285849386292 | 1766 |
| PCD_UNC_patient_2014_v6_binned_deidentified | 8.79479288318285e-06 | 1 | 0.9976337957337733 | 3312 |
| PCD_UNC_patient_2015_v6_binned_deidentified | 174.76054186090477 | 1 | 6.7530253504404305e-40 | 4390 |
| PCD_UNC_patient_2016_v6_binned_deidentified | 351.6421427724292 | 1 | 1.8601249169725476e-78 | 5688 |
| PCD_UNC_patient_2017_v6_binned_deidentified | 452.0767752792076 | 1 | 2.5477341193054187e-100 | 6078 |
| PCD_UNC_patient_2018_v6_binned_deidentified | 458.6400312059981 | 1 | 9.502653746027298e-102 | 6146 |
| PCD_UNC_patient_2019_v6_binned_deidentified | 381.72734723711676 | 1 | 5.234712374016827e-85 | 5450 |
| PCD_UNC_patient_2020_v6_binned_deidentified | 365.6432326681518 | 1 | 1.662694284060408e-81 | 4753 |
| PCD_UNC_patient_2021_v6_binned_deidentified | 84.49245398409613 | 1 | 3.8568405269048615e-20 | 3526 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
