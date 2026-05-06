---
disease: BRAF_V600_Mutant_Melanoma
generated: 2026-05-06T06:10:25Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 25
openscientist_citation_count: 60
shared_citation_count: 0
---

# Research synthesis: BRAF V600 Mutant Melanoma

## Source coverage

- Falcon report: `BRAF_V600_Mutant_Melanoma-deep-research-falcon.md`
- OpenScientist report: `BRAF_V600_Mutant_Melanoma-deep-research-openscientist.md`
- Falcon citation identifiers: 25
- OpenScientist citation identifiers: 60
- Shared citation identifiers: 0

## Agreement

Both providers describe BRAF V600 melanoma as a MAPK-driven cutaneous melanoma
subtype centered on constitutive BRAF kinase activation, melanocyte proliferation,
and high responsiveness to combined BRAF plus MEK inhibition. They also agree that
immune checkpoint blockade remains central because melanoma has high UV-associated
neoantigen burden.

## Differences

Falcon emphasized established targeted and immune therapy patterns. OpenScientist
added variant distribution across V600E, V600K, V600R, and V600M; demographic
differences for V600K; acquired resistance through NRAS and MEK/MAP2K1 mutations,
BRAF amplification or splice variants, PI3K-AKT bypass, and oxidative phosphorylation
adaptation; and brain metastasis treatment evidence.

## YAML integration

Integrated into `kb/disorders/BRAF_V600_Mutant_Melanoma.yaml`:

- Added BRAF V600 subtype entries for V600E, V600K, and other V600 substitutions.
- Added an acquired MAPK reactivation and bypass resistance pathophysiology node.
- Added BRAF HGNC annotations for V600E, V600K, V600R, and V600M genetic entries.
- Kept immune checkpoint blockade linked to the existing immune-checkpoint module.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Detailed brain-metastasis regimen comparisons, investigational triplet strategies,
and biomarker prioritization proposals were retained in research provenance because
they need focused curator review before becoming first-class YAML assertions.
