# Osteoglophonic Dysplasia Deep Research Notes

Date: 2026-04-18
Curator: Codex manual synthesis

## Scope

Disease: Osteoglophonic dysplasia

Focus for issue #1506:
- phenotype section only
- add clinically important manifestations backed by exact PMID text
- include frequency or onset only when directly supported
- remove unsupported obligate-style assertions

## Core Phenotype Sources Used

- PMID:15625620
  - Mutation-confirmed FGFR1 paper with direct abstract support for craniosynostosis, prominent supraorbital ridges, depressed nasal bridge, rhizomelic dwarfism, and nonossifying bone lesions.
- PMID:16918680
  - Dental follow-up case with direct abstract support for multiple unerupted teeth, several impacted teeth, and lucent jaw/long-bone lesions.
- PMID:29147600
  - Mutation-confirmed Indian case with direct abstract support for disproportionate short stature, delayed tooth eruption, hypodontia, long-bone nonossifying lesions, and hypophosphatemia.
- PMID:35148738
  - Four-year follow-up dental case with direct abstract support for frontal bossing and anteverted nares.
- PMID:38648328
  - 2024 GeneReviews synthesis with PMID-backed abstract text supporting multisuture craniosynostosis, multiple craniofacial features, delayed/failed tooth eruption, gingival overgrowth, osteopenia, and fracture risk.
- PMID:8958322
  - Review/case report supporting delayed tooth eruption, rib expansion, speech/developmental issues, and rare spontaneous fractures with pseudoarthroses.
- PMID:8995175
  - Radiology report supporting platyspondyly and epiphyseal dysplasia in addition to nonossifying fibromata.
- PMID:40260920
  - 2025 phenotype update supporting hypophosphatemia as part of the spectrum and adding overlapping toes as a newly reported feature.

## Included in YAML

Phenotypes added or materially strengthened:
- multisuture craniosynostosis
- disproportionate short-limb short stature
- rhizomelia
- nonossifying fibromas of the long bones
- platyspondyly
- epiphyseal dysplasia
- osteopenia
- pathologic fracture
- frontal bossing
- prominent supraorbital ridges
- depressed nasal bridge
- proptosis
- hypertelorism
- midface retrusion
- short nose
- anteverted nares
- low-set ears
- high palate
- delayed eruption of teeth
- impacted teeth
- hypodontia
- gingival overgrowth
- hypophosphatemia
- overlapping toe

## Deliberate Omissions / Softening

- No phenotype `frequency:` values were retained or added.
  - The available abstracts reliably support disease-phenotype association, but they do not provide direct quantitative frequency bands for these manifestations.
- Bone age was not modeled.
  - PMID:29147600 reports advanced bone age, while PMID:35148738 reports delayed skeletal maturation, so the current literature is conflicting.
- Developmental delay / speech delay were not promoted to core phenotypes.
  - PMID:8958322 describes them, but older reports such as PMID:7422392 and PMID:20339250 emphasize normal intelligence or later normal cognition, suggesting variable expression rather than a stable core manifestation.
- Elevated frontal temperature from PMID:40260920 was not modeled.
  - It appears to be a newly reported observation in two individuals, but HPO grounding is less clear and clinical importance is currently less established than overlapping toes.
- Short, broad hands and feet from PMID:38648328 were not separately encoded.
  - The review clearly notes distal extremity involvement, but the closest exact HPO fits were less clean than the other added manifestations, so I kept the YAML focused on stronger mappings first.
