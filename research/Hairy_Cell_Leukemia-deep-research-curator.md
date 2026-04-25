# Hairy Cell Leukemia Curator Notes

## Modeling Choices

- The dismech unit here is the disease-level mechanism graph for classic BRAF-driven HCL, anchored to MONDO:0018935.
- HCL-v is not represented under `has_subtypes` because the literature consistently separates it from classic HCL by immunophenotype, BRAF status, and therapy response.
- A flat response-state subtype is used for refractory HCL because that is a contextual disease-state facet, not a separate causal program.

## MONDO And NCIT Roles

- MONDO is used for the primary disease anchor, the refractory response-state subtype, and the differential diagnoses.
- NCIT is used where the current schema supports oncology-specific grounding most naturally: histopathology (`Bone Marrow Fibrosis`), molecular diagnosis (`BRAF V600E Mutation Analysis`), and the antineoplastic agent `Moxetumomab Pasudotox`.
- The current schema does not yet expose a disease-level NCIT mapping slot, and the current `RegimenTerm` dynamic enum did not accept the chosen HCL regimen codes during validation, so regimen specificity is carried by the treatment block plus ontology-grounded agents rather than forced into a failing pattern.

## Graph Shape

- The graph is kept atomic: driver mutation, MAPK activation, apoptosis resistance, TGF-beta1 overproduction, marrow fibrosis, and multilineage cytopenia are separate nodes.
- Differential diagnosis carries HCL-v, SMZL, and SDRPL instead of creating placeholder pages for adjacent ontology classes.
