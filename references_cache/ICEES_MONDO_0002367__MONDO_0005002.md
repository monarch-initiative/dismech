---
reference_id: "ICEES:MONDO_0002367__MONDO_0005002"
title: "kidney cancer / chronic obstructive pulmonary disease (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0002367__MONDO_0005002  kidney cancer ↔ chronic obstructive pulmonary disease

**ICEES:MONDO_0002367__MONDO_0005002** - EHR correlation between kidney cancer (MONDO:0002367) and chronic obstructive pulmonary disease (MONDO:0005002) in ICEES KG.

## Association

- Disorder A: kidney cancer (MONDO:0002367)
- Disorder B: chronic obstructive pulmonary disease (MONDO:0005002)
- Predicate(s): correlated_with, positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| PCD_UNC_patient_2010_v6_binned_deidentified | 2.5868550484561916e-05 | 1 | 0.9959418860640677 | 1311 |
| PCD_UNC_patient_2011_v6_binned_deidentified | 2.7477867793434034e-05 | 1 | 0.9958175612714824 | 1392 |
| PCD_UNC_patient_2012_v6_binned_deidentified | 4.935271180353822e-05 | 1 | 0.994394788559694 | 1662 |
| PCD_UNC_patient_2013_v6_binned_deidentified | 3.490855227510447e-05 | 1 | 0.995285849386292 | 1766 |
| PCD_UNC_patient_2014_v6_binned_deidentified | 1.298216260245773e-05 | 1 | 0.9971251668506923 | 3312 |
| PCD_UNC_patient_2015_v6_binned_deidentified | 0.9609443205404642 | 1 | 0.3269490715441098 | 4390 |
| PCD_UNC_patient_2016_v6_binned_deidentified | 0.19958619039164485 | 1 | 0.6550550687207357 | 5688 |
| PCD_UNC_patient_2017_v6_binned_deidentified | 0.16005770813939532 | 1 | 0.6891033918741429 | 6078 |
| PCD_UNC_patient_2018_v6_binned_deidentified | 0.10821565340631877 | 1 | 0.7421848057771645 | 6146 |
| PCD_UNC_patient_2019_v6_binned_deidentified | 4.168368062161712 | 1 | 0.041185451310167744 | 5450 |
| PCD_UNC_patient_2020_v6_binned_deidentified | 2.2932833448297165 | 1 | 0.12993479830447424 | 4753 |
| PCD_UNC_patient_2021_v6_binned_deidentified | 0.006012914034280419 | 1 | 0.9381915996135209 | 3526 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
