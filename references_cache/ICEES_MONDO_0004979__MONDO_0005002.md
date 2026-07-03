---
reference_id: "ICEES:MONDO_0004979__MONDO_0005002"
title: "asthma / chronic obstructive pulmonary disease (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0004979__MONDO_0005002  asthma ↔ chronic obstructive pulmonary disease

**ICEES:MONDO_0004979__MONDO_0005002** - EHR correlation between asthma (MONDO:0004979) and chronic obstructive pulmonary disease (MONDO:0005002) in ICEES KG.

## Association

- Disorder A: asthma (MONDO:0004979)
- Disorder B: chronic obstructive pulmonary disease (MONDO:0005002)
- Predicate(s): correlated_with, positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| PCD_UNC_patient_2010_v6_binned_deidentified | 9.408579765999117e-07 | 1 | 0.9992260693809875 | 1311 |
| PCD_UNC_patient_2011_v6_binned_deidentified | 1.0443894678545964e-06 | 1 | 0.9991845990226738 | 1392 |
| PCD_UNC_patient_2012_v6_binned_deidentified | 1.0941585705098131e-06 | 1 | 0.99916539666545 | 1662 |
| PCD_UNC_patient_2013_v6_binned_deidentified | 1.1734505958277916e-06 | 1 | 0.9991356843406515 | 1766 |
| PCD_UNC_patient_2014_v6_binned_deidentified | 2.799761939630324e-07 | 1 | 0.9995778171436037 | 3312 |
| PCD_UNC_patient_2015_v6_binned_deidentified | 45.304219158501155 | 1 | 1.686853427417526e-11 | 4390 |
| PCD_UNC_patient_2016_v6_binned_deidentified | 168.58533016733276 | 1 | 1.5071340388291068e-38 | 5688 |
| PCD_UNC_patient_2017_v6_binned_deidentified | 146.1707628254436 | 1 | 1.191269396669518e-33 | 6078 |
| PCD_UNC_patient_2018_v6_binned_deidentified | 74.32073118649157 | 1 | 6.6402506212762226e-18 | 6146 |
| PCD_UNC_patient_2019_v6_binned_deidentified | 42.584064139665145 | 1 | 6.770877481238625e-11 | 5450 |
| PCD_UNC_patient_2020_v6_binned_deidentified | 52.72467171975637 | 1 | 3.837402567878219e-13 | 4753 |
| PCD_UNC_patient_2021_v6_binned_deidentified | 21.134663569398946 | 1 | 4.281136565940172e-06 | 3526 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
