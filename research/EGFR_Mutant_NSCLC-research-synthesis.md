---
disease: EGFR_Mutant_NSCLC
generated: 2026-05-06T15:56:14Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 14
openscientist_citation_count: 55
shared_citation_count: 0
---

# Research synthesis: EGFR-Mutant Non-Small Cell Lung Cancer

## Source coverage

- Falcon report: `EGFR_Mutant_NSCLC-deep-research-falcon.md`
- OpenScientist report: `EGFR_Mutant_NSCLC-deep-research-openscientist.md`
- Falcon citation identifiers: 14
- OpenScientist citation identifiers: 55
- Shared citation identifiers: 0

## Agreement

Both providers identify EGFR-mutant NSCLC as a kinase-domain driver subtype in
which sensitizing EGFR mutations create dependence on EGFR signaling and
therapeutic sensitivity to EGFR TKIs. They agree that osimertinib is the central
modern EGFR TKI, that CNS disease is clinically important, and that acquired
resistance requires repeat molecular characterization.

## Differences

Falcon emphasized tumor microenvironment and immunology themes in addition to
standard EGFR TKI biology. OpenScientist added newer treatment settings and
resistance updates: C797S after osimertinib, MET bypass, AP-1/EMT resistance
states, high PD-L1 as an adverse subgroup marker, adjuvant and consolidation
osimertinib, and PAPILLON support for amivantamab plus chemotherapy in exon 20
insertion disease.

## YAML integration

Integrated into `kb/disorders/EGFR_Mutant_NSCLC.yaml`:

- Expanded the EGFR TKI resistance node to include C797S, MET bypass, AP-1/EMT,
  oncogenic fusions, and transformation.
- Added an immune-cold microenvironment pathophysiology node anchored by PD-L1
  outcome data.
- Updated osimertinib to cover first-line, adjuvant, CNS, and post-CRT stage III
  use.
- Updated amivantamab and chemotherapy entries with exon 20 insertion and C797S
  post-osimertinib evidence.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Investigational EGFR/MET combinations, detailed perioperative trial ranking,
and broad immunotherapy combination strategies were retained as research leads
until they map cleanly to durable clinical standards or disease mechanisms.
