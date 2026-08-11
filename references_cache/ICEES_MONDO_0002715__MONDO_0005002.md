---
reference_id: "ICEES:MONDO_0002715__MONDO_0005002"
title: "uterine cancer / chronic obstructive pulmonary disease (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0002715__MONDO_0005002  uterine cancer ↔ chronic obstructive pulmonary disease

**ICEES:MONDO_0002715__MONDO_0005002** - EHR correlation between uterine cancer (MONDO:0002715) and chronic obstructive pulmonary disease (MONDO:0005002) in ICEES KG.

## Association

- Disorder A: uterine cancer (MONDO:0002715)
- Disorder B: chronic obstructive pulmonary disease (MONDO:0005002)
- Predicate(s): correlated_with, positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| PCD_UNC_patient_2010_v6_binned_deidentified | 2.5868550484561916e-05 | 1 | 0.9959418860640677 | 1311 |
| PCD_UNC_patient_2011_v6_binned_deidentified | 1.6415333257331312e-05 | 1 | 0.9967673124895872 | 1392 |
| PCD_UNC_patient_2012_v6_binned_deidentified | 1.6331887978335505e-05 | 1 | 0.9967755393931181 | 1662 |
| PCD_UNC_patient_2013_v6_binned_deidentified | 5.2452148728514664e-05 | 1 | 0.9942214628873574 | 1766 |
| PCD_UNC_patient_2014_v6_binned_deidentified | 2.1755857177156143e-05 | 1 | 0.9962784266226181 | 3312 |
| PCD_UNC_patient_2015_v6_binned_deidentified | 0.9110371672018511 | 1 | 0.33983937744569115 | 4390 |
| PCD_UNC_patient_2016_v6_binned_deidentified | 0.408272021729832 | 1 | 0.5228478643544576 | 5688 |
| PCD_UNC_patient_2017_v6_binned_deidentified | 1.498601590944864e-07 | 1 | 0.999691124724842 | 6078 |
| PCD_UNC_patient_2018_v6_binned_deidentified | 2.353800963082758 | 1 | 0.12497794707829543 | 6146 |
| PCD_UNC_patient_2019_v6_binned_deidentified | 0.41477070352554574 | 1 | 0.519557962655387 | 5450 |
| PCD_UNC_patient_2020_v6_binned_deidentified | 0.20090104960872474 | 1 | 0.6539945256799555 | 4753 |
| PCD_UNC_patient_2021_v6_binned_deidentified | 4.36827320467632e-07 | 1 | 0.99947265488641 | 3526 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
