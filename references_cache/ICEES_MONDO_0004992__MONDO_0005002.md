---
reference_id: "ICEES:MONDO_0004992__MONDO_0005002"
title: "cancer / chronic obstructive pulmonary disease (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0004992__MONDO_0005002  cancer ↔ chronic obstructive pulmonary disease

**ICEES:MONDO_0004992__MONDO_0005002** - EHR correlation between cancer (MONDO:0004992) and chronic obstructive pulmonary disease (MONDO:0005002) in ICEES KG.

## Association

- Disorder A: cancer (MONDO:0004992)
- Disorder B: chronic obstructive pulmonary disease (MONDO:0005002)
- Predicate(s): positively_correlated_with
- Direction of correlation: POSITIVE

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| COVID_UNC_EPR_patient_APR2021_v2_binned_deidentified | 2303.168208224234 | 1 | 0 | 98619 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
