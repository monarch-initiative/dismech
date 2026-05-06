---
disease: BRAF_V600E_Mutant_Colorectal_Cancer
generated: 2026-05-06T06:10:25Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 20
openscientist_citation_count: 39
shared_citation_count: 0
---

# Research synthesis: BRAF V600E-Mutant Colorectal Cancer

## Source coverage

- Falcon report: `BRAF_V600E_Mutant_Colorectal_Cancer-deep-research-falcon.md`
- OpenScientist report: `BRAF_V600E_Mutant_Colorectal_Cancer-deep-research-openscientist.md`
- Falcon citation identifiers: 20
- OpenScientist citation identifiers: 39
- Shared citation identifiers: 0

## Agreement

Both providers treat BRAF V600E CRC as an aggressive molecular subtype driven by
constitutive RAF-MEK-ERK signaling and poor response to conventional chemotherapy.
They agree that EGFR feedback reactivation explains weak single-agent BRAF inhibitor
activity in CRC and supports combined BRAF plus EGFR targeting with encorafenib and
cetuximab.

## Differences

Falcon emphasized targeted-therapy trial evidence, real-world encorafenib outcomes,
and the existing treatment landscape. OpenScientist added a clearer serrated
neoplasia model, including CIMP-high methylation, MLH1 silencing, the MSI-H versus
MSS split, and acquired resistance mechanisms involving EGFR, KRAS, MAP2K1, MET,
and mutant BRAF amplification.

## YAML integration

Integrated into `kb/disorders/BRAF_V600E_Mutant_Colorectal_Cancer.yaml`:

- Added serrated neoplasia/CIMP-high and MLH1-silencing pathophysiology nodes.
- Added acquired MAPK reactivation as a resistance mechanism.
- Added MLH1, BRAF, PIK3CA, and PTEN gene annotations with HGNC terms.
- Corrected encorafenib/cetuximab combinations to targeted therapy rather than immunotherapy.
- Added MSI-H/dMMR immune checkpoint inhibitor treatment coverage.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Detailed investigational trial strategy, ctDNA monitoring proposals, epigenetic
therapy hypotheses, and model-system limitations were left in research provenance
because they are not yet core curated disease mechanisms or established treatment
entries.
