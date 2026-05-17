---
disease: ROS1_Rearranged_NSCLC
generated: 2026-05-06T15:56:14Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 8
openscientist_citation_count: 34
shared_citation_count: 0
---

# Research synthesis: ROS1-Rearranged Non-Small Cell Lung Cancer

## Source coverage

- Falcon report: `ROS1_Rearranged_NSCLC-deep-research-falcon.md`
- OpenScientist report: `ROS1_Rearranged_NSCLC-deep-research-openscientist.md`
- Falcon citation identifiers: 8
- OpenScientist citation identifiers: 34
- Shared citation identifiers: 0

## Agreement

Both providers identify ROS1-rearranged NSCLC as a rare fusion-driven lung
adenocarcinoma subtype with constitutive ROS1 kinase signaling, enrichment in
younger never/light smokers, frequent CNS considerations, and strong dependence
on ROS1-directed therapy.

## Differences

Falcon emphasized late-breaking ROS1 therapeutic comparisons, especially
repotrectinib, taletrectinib, entrectinib, and real-world treatment patterns.
OpenScientist added broader resistance biology, including L2086F type-switching,
MET amplification after sequential ROS1 inhibitors, and HGF-MET bypass
resistance to entrectinib.

## YAML integration

Integrated into `kb/disorders/ROS1_Rearranged_NSCLC.yaml`:

- Expanded the ROS1 inhibitor resistance node to include L2086F, MET
  amplification, HGF-MET bypass, and serial profiling.
- Updated repotrectinib to emphasize macrocyclic design, CNS distribution, and
  TRIDENT-1 activity.
- Updated taletrectinib to emphasize TKI-naive, TKI-pretreated, intracranial, and
  G2032R contexts.
- Backfilled top-level reference provenance for Falcon and OpenScientist citation trails.

## Not integrated

Zidesamtinib, other emerging ROS1 agents, detailed adverse-event profiles, and
case-level sequencing recommendations were retained as research leads rather
than promoted to curated treatment entries.
