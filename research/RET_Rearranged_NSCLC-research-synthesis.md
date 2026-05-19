---
disease: RET_Rearranged_NSCLC
generated: 2026-05-06T15:56:14Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 17
openscientist_citation_count: 51
shared_citation_count: 4
---

# Research synthesis: RET-Rearranged Non-Small Cell Lung Cancer

## Source coverage

- Falcon report: `RET_Rearranged_NSCLC-deep-research-falcon.md`
- OpenScientist report: `RET_Rearranged_NSCLC-deep-research-openscientist.md`
- Falcon citation identifiers: 17
- OpenScientist citation identifiers: 51
- Shared citation identifiers: 4

## Agreement

Both providers identify RET-rearranged NSCLC as a rare fusion-driven lung
adenocarcinoma subtype with constitutive RET signaling and strong clinical
benefit from selective RET inhibition. They agree that selpercatinib and
pralsetinib are the main curated targeted therapies and that resistance emerges
through both on-target RET mutations and bypass signaling.

## Differences

Falcon focused on the selective RET inhibitor treatment landscape, diagnostics,
and first-line selpercatinib evidence. OpenScientist added more resistance
detail, including RET G810 solvent-front mutations, MET/KRAS bypass
amplification, SRC biology, intracranial efficacy, and the limited benefit of
immunotherapy in retrospective RET-positive cohorts.

## YAML integration

Integrated into `kb/disorders/RET_Rearranged_NSCLC.yaml`:

- Expanded the RET inhibitor resistance node to include G810R/S/C, MET and KRAS
  amplification, SRC bypass biology, and post-progression profiling.
- Updated selpercatinib with LIBRETTO-431 first-line and LIBRETTO-001 CNS
  evidence.
- Updated pralsetinib with ARROW systemic and intracranial response evidence.
- Updated immunotherapy to reflect the weaker retrospective signal compared with
  selective RET inhibitors.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Next-generation investigational RET inhibitors, experimental RET/SRC
combinations as treatment entries, and fine-grained adverse-event management
were retained as research leads pending stronger clinical integration.
