---
disease: Arterial_Dissection_Lentiginosis_Syndrome
generated: 2026-05-06T22:36:00Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 4
openscientist_citation_count: 34
shared_citation_count: 0
---

# Research synthesis: Arterial Dissection-Lentiginosis Syndrome

## Source coverage

- Falcon report: `Arterial_Dissection_Lentiginosis_Syndrome-deep-research-falcon.md`
- OpenScientist report: `Arterial_Dissection_Lentiginosis_Syndrome-deep-research-openscientist.md`
- Falcon citation identifiers: 4
- OpenScientist citation identifiers: 34
- Shared citation identifiers: 0

## Agreement

Both providers treat ADL as an ultra-rare familial arteriopathy defined by early
arterial dissection with lentiginosis and cystic medial degeneration or necrosis.
They agree that the causal gene is unresolved and that the available curation must
remain conservative because the primary PubMed cache contains only title-level
text for the original report.

## Differences

Falcon emphasized uncertainty: autosomal recessive inheritance was suggested from
the original kindreds, but autosomal dominant inheritance with variable penetrance
was not excluded. OpenScientist asserted autosomal recessive status from
OMIM/Orphanet and proposed a neural-crest/endothelin lineage-balance model using
supporting literature from related pigmentation and vascular-development systems.

## YAML integration

Integrated into `kb/disorders/Arterial_Dissection_Lentiginosis_Syndrome.yaml`:

- Backfilled Falcon and OpenScientist top-level reference provenance.
- Replaced the prior autosomal-dominant inheritance assertion with an unresolved
  inheritance entry that captures the provider disagreement and cache limitation.
- Preserved the conservative neural-crest/mesenchymal developmental mechanism and
  unknown-causal-gene curation.
- Updated review notes to record OpenScientist's ORPHA:1682/AR claim without
  citing it as cache-backed evidence.

## Not integrated

The endothelin-pathway lineage-balance hypothesis, detailed differential
diagnosis against other lentiginosis syndromes, and broad arterial-dissection
management literature were retained as research leads because they are not
ADL-specific enough for curated mechanism assertions.
