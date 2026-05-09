---
disease: BRAF_V600E_Mutant_NSCLC
generated: 2026-05-06T06:10:25Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 14
openscientist_citation_count: 42
shared_citation_count: 0
---

# Research synthesis: BRAF V600E-Mutant Non-Small Cell Lung Cancer

## Source coverage

- Falcon report: `BRAF_V600E_Mutant_NSCLC-deep-research-falcon.md`
- OpenScientist report: `BRAF_V600E_Mutant_NSCLC-deep-research-openscientist.md`
- Falcon citation identifiers: 14
- OpenScientist citation identifiers: 42
- Shared citation identifiers: 0

## Agreement

Both providers identify BRAF V600E NSCLC as a rare actionable NSCLC subtype in
which class I BRAF monomer signaling activates the MAPK pathway independently of
upstream RAS. They agree that broad molecular profiling is required and that combined
BRAF plus MEK inhibition is the central targeted treatment strategy.

## Differences

Falcon focused on the pre-existing dabrafenib plus trametinib treatment landscape
and general BRAF-mutant NSCLC context. OpenScientist added stronger coverage of the
PHAROS encorafenib plus binimetinib data, PD-L1/immunotherapy context, thromboembolism
risk, and resistance mechanisms detected by ctDNA or repeat profiling.

## YAML integration

Integrated into `kb/disorders/BRAF_V600E_Mutant_NSCLC.yaml`:

- Updated the overview and treatment section to include encorafenib plus binimetinib
  as a BRAF/MEK-targeted option supported by PHAROS.
- Expanded the BRAF/MEK inhibitor resistance node to include MAPK reactivation,
  bypass PI3K-AKT-MET signaling, histologic transformation, and acquired BRAF V600E
  after EGFR-TKI therapy.
- Added a BRAF HGNC gene annotation.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Treatment-ranking claims from indirect comparisons, detailed thromboembolism
management, and proposed adjuvant or sequencing trials were retained as research
leads rather than promoted to curated disease mechanisms.
