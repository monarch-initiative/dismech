---
provider: fallback
status: provider_timeout
date: "2026-05-09"
disorder: Hereditary_Pulmonary_Alveolar_Proteinosis
attempted_providers:
  - provider: falcon
    command: timeout 120s just research-disorder falcon Hereditary_Pulmonary_Alveolar_Proteinosis
    result: timeout_signal_15
  - provider: openai
    command: timeout 90s just research-disorder openai Hereditary_Pulmonary_Alveolar_Proteinosis
    result: timeout_signal_15
---

# Hereditary Pulmonary Alveolar Proteinosis Deep-Research Fallback

Initial Falcon deep-research could not run before a draft existed because
`just research-disorder` requires the target YAML path. After the draft was in
place, bounded provider attempts were retried:

- `timeout 120s just research-disorder falcon Hereditary_Pulmonary_Alveolar_Proteinosis`
  terminated with signal 15 after the timeout.
- `timeout 90s just research-disorder openai Hereditary_Pulmonary_Alveolar_Proteinosis`
  terminated with signal 15 after the timeout.

No provider artifact was produced by either bounded retry. The local curation
therefore used generated caches only:

- ORPHA:264675 for definition, inheritance, age of onset, epidemiology, genes,
  phenotype frequencies, and cross-references.
- PMID:20622029 for CSF2RA-associated hereditary PAP, GM-CSF receptor
  dysfunction, diagnosis, and whole-lung lavage response.
- PMID:21075760 for CSF2RB-associated hereditary PAP and autosomal recessive
  inheritance.
- PMID:30846703 and PMID:23001804 for PAP pathophysiology,
  surfactant/cholesterol clearance, imaging, diagnosis, and whole-lung lavage.
- PMID:30100408 for model-organism pulmonary macrophage transplantation
  evidence.

## Scope Confirmation

The curation covers the ORPHA:264675/MONDO:0012580 hereditary pulmonary
alveolar proteinosis concept, not autoimmune or secondary pulmonary alveolar
proteinosis. The YAML consumes the structured ORPHA definition, genes, mapping,
inheritance, epidemiology, age-of-onset categories, and all 15 ORPHA HPO
phenotype rows. Literature-backed additions focus on GM-CSF receptor signaling,
CSF2RA/CSF2RB genetics, alveolar macrophage surfactant/cholesterol clearance,
PAS-positive alveolar material, HRCT crazy-paving diagnosis, whole-lung lavage,
supportive respiratory care, and experimental macrophage transplantation.
