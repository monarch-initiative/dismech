---
disease: ALK_Rearranged_NSCLC
generated: 2026-05-06T15:56:14Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 4
openscientist_citation_count: 69
shared_citation_count: 0
---

# Research synthesis: ALK-Rearranged Non-Small Cell Lung Cancer

## Source coverage

- Falcon report: `ALK_Rearranged_NSCLC-deep-research-falcon.md`
- OpenScientist report: `ALK_Rearranged_NSCLC-deep-research-openscientist.md`
- Falcon citation identifiers: 4
- OpenScientist citation identifiers: 69
- Shared citation identifiers: 0

## Agreement

Both providers frame ALK-rearranged NSCLC as a fusion-driven lung adenocarcinoma
subtype enriched in younger never/light smokers. They agree that oncogene
addiction to ALK signaling, modern ALK TKI sequencing, CNS involvement, and
acquired resistance are the major curated concepts.

## Differences

Falcon emphasized the existing ALK inhibitor landscape and broad diagnostic and
immunotherapy context. OpenScientist added more recent clinical and mechanistic
detail: variant 3 prognosis, ALINA adjuvant alectinib, five-year CROWN
lorlatinib data, and resistance mechanisms involving EMT, CAF-driven HGF-MET and
integrin signaling, and SRC bypass signaling.

## YAML integration

Integrated into `kb/disorders/ALK_Rearranged_NSCLC.yaml`:

- Updated the overview and EML4-ALK subtype to capture ongoing CNS and resistance
  challenges and the adverse PFS association of EML4-ALK variant 3.
- Expanded the ALK TKI resistance node to include EMT, CAF/HGF-MET/integrin, SRC,
  and broader bypass biology.
- Updated brain metastases evidence with modern CNS-active ALK inhibitor data.
- Added ALINA support to alectinib and CROWN five-year support to lorlatinib.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Investigational ALK combinations, detailed adverse-event management, and broad
immunotherapy sequencing claims were retained as research leads rather than
promoted to curated disease mechanisms.
