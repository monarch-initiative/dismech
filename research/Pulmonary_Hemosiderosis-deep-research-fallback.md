# Pulmonary Hemosiderosis Deep-Research Fallback

Date: 2026-05-09

Automated deep-research providers were attempted after local evidence-backed
curation, but both stayed silent and were stopped by bounded timeouts:

- `timeout 120s just research-disorder falcon Pulmonary_Hemosiderosis` returned 124 / signal 15.
- `timeout 60s just research-disorder openai Pulmonary_Hemosiderosis` returned 124 / signal 15.

The curation therefore used generated local caches only:

- ORPHA:99931 for definition, age of onset, epidemiology, cross-references, and HPO phenotype coverage.
- PMID:30278795 for the 107-patient pediatric cohort, clinical frequencies, diagnosis, prognosis, and glucocorticoid treatment.
- PMID:24125570 for the French RespiRare pediatric cohort, autoimmunity signals, diagnosis, fibrosis, and severe hemorrhage outcomes.
- PMID:15293620 for recurrent diffuse alveolar hemorrhage, siderophages, alveolar hemosiderin deposition, and biopsy exclusion of vasculitis.
- PMID:26289251 for physician-practice treatment patterns.
- PMID:33184706 and PMID:30806370 for corticosteroid and steroid-sparing immunosuppressive treatment scope.
