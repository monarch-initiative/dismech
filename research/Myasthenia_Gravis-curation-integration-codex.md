---
provider: codex-curation-review
model: GPT-5
cached: false
start_time: '2026-05-17T00:00:00Z'
template_file: manual_curation_integration
template_variables:
  disease_name: Myasthenia Gravis
  source_reports:
  - Myasthenia_Gravis-deep-research-falcon.md
  - Myasthenia_Gravis-deep-research-cyberian-codex.md
citation_count: 3
---

# Myasthenia Gravis Curation Integration

Manual review of the deep-research reports identified missing assertion-level
integration beyond `found_in` provenance:

- Antibody-defined subtypes now cite the 2024 clinical review that places AChR,
  MuSK, and LRP4 antibodies together.
- Genetics now includes the 2024 genome-wide meta-analysis and polygenic
  susceptibility framing.
- FcRn antagonist treatment now includes mechanism-level evidence for IgG
  recycling blockade, not only approval status.
