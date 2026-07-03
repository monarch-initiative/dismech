---
reference_id: "ICEES:MONDO_0005002__MONDO_0005249"
title: "chronic obstructive pulmonary disease / pneumonia (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0005002__MONDO_0005249  chronic obstructive pulmonary disease ↔ pneumonia

**ICEES:MONDO_0005002__MONDO_0005249** - EHR correlation between chronic obstructive pulmonary disease (MONDO:0005002) and pneumonia (MONDO:0005249) in ICEES KG.

## Association

- Disorder A: chronic obstructive pulmonary disease (MONDO:0005002)
- Disorder B: pneumonia (MONDO:0005249)
- Predicate(s): correlated_with, positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| PCD_UNC_patient_2010_v6_binned_deidentified | 6.925480198964148e-06 | 1 | 0.9979002649095883 | 1311 |
| PCD_UNC_patient_2011_v6_binned_deidentified | 3.773035457940512e-06 | 1 | 0.9984501658303413 | 1392 |
| PCD_UNC_patient_2012_v6_binned_deidentified | 3.7846130867631542e-06 | 1 | 0.9984477898073072 | 1662 |
| PCD_UNC_patient_2013_v6_binned_deidentified | 2.0158055998712123e-06 | 1 | 0.9988671713104657 | 1766 |
| PCD_UNC_patient_2014_v6_binned_deidentified | 2.642624209721501e-06 | 1 | 0.9987029474409608 | 3312 |
| PCD_UNC_patient_2015_v6_binned_deidentified | 122.86804140834866 | 1 | 1.490386635913281e-28 | 4390 |
| PCD_UNC_patient_2016_v6_binned_deidentified | 261.3189090931642 | 1 | 8.851730839074057e-59 | 5688 |
| PCD_UNC_patient_2017_v6_binned_deidentified | 331.707743547728 | 1 | 4.0817029781289475e-74 | 6078 |
| PCD_UNC_patient_2018_v6_binned_deidentified | 230.89208149939242 | 1 | 3.808869466681937e-52 | 6146 |
| PCD_UNC_patient_2019_v6_binned_deidentified | 243.41870129212805 | 1 | 7.068016040436106e-55 | 5450 |
| PCD_UNC_patient_2020_v6_binned_deidentified | 189.21661013248743 | 1 | 4.713352702810791e-43 | 4753 |
| PCD_UNC_patient_2021_v6_binned_deidentified | 62.34586030032215 | 1 | 2.8813648175616225e-15 | 3526 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
