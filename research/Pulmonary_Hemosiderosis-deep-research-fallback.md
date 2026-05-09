---
title: Pulmonary Hemosiderosis Deep-Research Fallback
disorder: Pulmonary_Hemosiderosis
date: 2026-05-09
status: provider_timeout_fallback
attempted_providers:
  - falcon
  - openai
---

# Pulmonary Hemosiderosis Deep-Research Fallback

Automated deep-research providers were attempted after local evidence-backed
curation, but both stayed silent and were stopped by bounded timeouts:

- `timeout 120s just research-disorder falcon Pulmonary_Hemosiderosis` returned 124 / signal 15.
- `timeout 60s just research-disorder openai Pulmonary_Hemosiderosis` returned 124 / signal 15.

Because provider runs were unavailable, the curation used generated local caches
and the disease-specific literature already fetched into `references_cache/`.
The reviewed scope is idiopathic pulmonary hemosiderosis as represented by
ORPHA:99931 and MONDO:0008346, with secondary diffuse alveolar hemorrhage causes
and Lane-Hamilton syndrome kept outside the core disease definition.

## Scope Confirmation

- ORPHA:99931 supplied the disease definition, childhood onset, epidemiology,
  cross-references, and HPO phenotype rows.
- PMID:30278795 supplied the large 107-patient pediatric cohort, clinical
  frequencies, diagnosis, prognosis, and glucocorticoid treatment evidence.
- PMID:24125570 supplied the French RespiRare pediatric cohort, autoimmunity
  signals, Down syndrome comorbidity signal, diagnosis, fibrosis, and severe
  hemorrhage outcomes.
- PMID:15293620 supplied recurrent diffuse alveolar hemorrhage, siderophages,
  alveolar hemosiderin deposition, and biopsy exclusion of vasculitis.
- PMID:26289251 supplied physician-practice treatment patterns.
- PMID:33184706 and PMID:30806370 supplied corticosteroid and steroid-sparing
  immunosuppressive treatment scope.

## Review Follow-Up

The provider fallback was explicitly cross-checked for obvious curation gaps.
PMID:24125570 supports autoimmune contribution in a subset through ANCA, ANA,
and coeliac antibody positivity and through the authors' conclusion that
autoimmunity contributes to disease development. The YAML now models this as an
atomic modifier node rather than replacing the idiopathic upstream trigger.

The same cohort reported Down syndrome in 5 of 25 pediatric IPH cases. Because
the current disease schema has no top-level `comorbidities` slot, the YAML
represents this as a `Comorbidity` phenotype entry with a MONDO term binding and
an exact cohort snippet.

PMID:33184706 names cyclophosphamide and mycophenolate mofetil among attempted
steroid-sparing therapies. The YAML treatment entry now includes those
therapeutic-agent bindings alongside hydroxychloroquine and azathioprine.
