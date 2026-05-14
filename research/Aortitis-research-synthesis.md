---
disease: Aortitis
generated: 2026-05-06T22:52:00Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 13
openscientist_citation_count: 53
shared_citation_count: 0
---

# Research synthesis: Aortitis

## Source coverage

- Falcon report: `Aortitis-deep-research-falcon.md`
- OpenScientist report: `Aortitis-deep-research-openscientist.md`
- Falcon citation identifiers: 13
- OpenScientist citation identifiers: 53
- Shared citation identifiers: 0

## Agreement

Both providers frame aortitis as a heterogeneous syndrome rather than a single
etiology, spanning large-vessel vasculitis, clinically isolated surgical
aortitis, infectious aortitis, IgG4-related aortitis/periaortitis, and
G-CSF-associated drug-induced disease. They agree that the main curated risk is
ongoing aortic remodeling with aneurysm, dissection, stenosis, occlusion, and
the need for imaging-based surveillance.

## Differences

Falcon emphasized the existing surgical-pathology, imaging, and G-CSF case-review
literature already represented in the YAML. OpenScientist added newer treatment
and surveillance details, including upadacitinib phase III evidence in giant cell
arteritis, HLA-B52/rechallenge signal in G-CSF-associated aortitis, isolated
aortitis follow-up recommendations, and broader biomarker/imaging prognosis
leads.

## YAML integration

Integrated into `kb/disorders/Aortitis.yaml`:

- Backfilled Falcon and OpenScientist top-level reference provenance.
- Added G-CSF recurrence and HLA-B52 susceptibility signal as partial
  case-report evidence.
- Added repeated clinical and imaging surveillance support for isolated
  aortitis.
- Added upadacitinib as a GCA-context JAK inhibitor therapy while noting that
  aortitis-specific remodeling endpoints remain uncertain.

## Not integrated

Checkpoint-inhibitor aortitis, detailed PET-CT performance statistics, VZV
trigger hypotheses, and broad cytokine/NET/tertiary-lymphoid-organ mechanisms
were retained as research leads because the current YAML already covers the
major syndrome-level mechanisms and subtype structure.
