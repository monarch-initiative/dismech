---
reference_id: "ICEES:MONDO_0000775__MONDO_0001475"
title: "drug allergy / neutropenia (ICEES KG)"
database: "ICEES KG"
content_type: "structured_record"
---

# ICEES:MONDO_0000775__MONDO_0001475  drug allergy ↔ neutropenia

**ICEES:MONDO_0000775__MONDO_0001475** - EHR correlation between drug allergy (MONDO:0000775) and neutropenia (MONDO:0001475) in ICEES KG.

## Association

- Disorder A: drug allergy (MONDO:0000775)
- Disorder B: neutropenia (MONDO:0001475)
- Predicate(s): correlated_with
- Direction of correlation: UNSIGNED

## Cohort statistics

Per-cohort chi-square contingency results. ICEES cohorts are condition-specific UNC Health patient sets (e.g. an asthma or primary-ciliary-dyskinesia cohort), so each statistic is conditioned on that base population, not a hospital-wide sample.

| Cohort | Chi-square | dof | p-value | N |
|---|---|---|---|---|
| Augmentin_DILI_patient_v4_binned_deidentified | 1.7339466756411096e-08 | 1 | 0.9998949350328814 | 265 |

## Source

ICEES KG (Integrated Clinical and Environmental Exposures Service), version **8-20-2024**, provenance `infores:automat-icees-kg`. Single-site UNC Health EHR integrated with environmental-exposure data; correlations are not multiple-testing corrected and are computed within condition-specific cohorts.

License: ICEES terms (https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt).

[ICEES KG](https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)
