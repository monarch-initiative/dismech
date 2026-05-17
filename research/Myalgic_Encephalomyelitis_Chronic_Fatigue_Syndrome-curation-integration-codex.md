---
provider: codex-curation-review
model: GPT-5
cached: false
start_time: '2026-05-17T00:00:00Z'
template_file: manual_curation_integration
template_variables:
  disease_name: Myalgic Encephalomyelitis/Chronic Fatigue Syndrome
  source_reports:
  - Myalgic_Encephalomyelitis_Chronic_Fatigue_Syndrome-deep-research-falcon.md
  - Myalgic_Encephalomyelitis_Chronic_Fatigue_Syndrome-deep-research-perplexity.md
  - Myalgic_Encephalomyelitis_Chronic_Fatigue_Syndrome-deep-research-cyberian-codex.md
citation_count: 3
---

# ME/CFS Curation Integration

Manual review of the deep-research reports identified updates that should be
represented in assertions rather than only in top-level provenance:

- The NK-cell dysfunction mechanism and biochemical marker now cite the 2024
  meta-analysis that quantified reduced cytotoxicity.
- The endothelial/coagulation pathophysiology now cites the 2024 plasma
  proteomics study.
- Orthostatic intolerance now includes the 2024 NASA lean-test/POTS subset
  evidence from the endothelial-inflammation biomarker study.
