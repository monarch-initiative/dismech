# NAMO Rare-Disease Experimental Models

## Goal
Bridge dismech's disease-centric curation model to Monarch NAMO without importing
the full NAMO schema into dismech.

The immediate target is a small set of disease-level `experimental_models` entries
that are:
- first-class inside dismech disorder files
- explicitly mapped to NAMO classes with `namo_type`
- focused on high-signal rare-disease examples

## Initial Scope
- Cystic Fibrosis
- Stargardt Disease
- Noonan Syndrome
- Crohn Disease as an IBD-adjacent host-microbiome/barrier test case

## Current Bridge Pattern
Use a narrow disease-level `experimental_models` slot in dismech rather than a
full study-centric import of NAMO.

Each model should capture:
- `experimental_model_type` for local coarse typing
- `namo_type` for crosswalk to NAMO classes
- `cell_source` and `culture_system` for translational interpretation
- disease-relevant `findings` and `evidence`

## NAMO Classes In Scope
- `namo:Organoid`
- `namo:OrganOnChip`
- `namo:CellLineModel`
- `namo:TwoDCellCulture`

These class CURIEs were verified against the current NAMO schema snapshot used
for this bridge spike.

These cover the current bridge cases better than a direct wholesale import because
dismech remains disease-centric while NAMO is model-centric.

## Disease Anchors

### Cystic Fibrosis
- Patient-derived airway organoid theratyping
- CF airway-on-chip microphysiological model
- NuLi/CuFi airway epithelial cell-line model

### Stargardt Disease
- Patient-derived retinal organoid model
- STGD1 iPSC-derived RPE disease-in-a-dish model

### Noonan Syndrome
- Noonan cortical organoid model
- Noonan iPSC-cardiomyocyte model

### Crohn / IBD Bridge
- Primary human small-intestinal monolayer barrier model from UNC

## Aadra Bhatt / UNC Note
The user's requested UNC lead appears to be Aadra P. Bhatt.

Current curation stance:
- UNC public profile language points to primary human cells plus representative
  human intestinal bacteria as a lab direction.
- The strongest immediately curatable Bhatt anchor is PMID:29094594, a primary
  human small-intestinal monolayer platform paper.
- That paper is not Crohn-specific, so it should be modeled as `PARTIAL` support
  for Crohn/IBD translational relevance, not as direct Crohn evidence.

This is the right level of confidence for now. Stronger Crohn-specific curation
should wait for a directly attributable host-microbe coculture, organoid, or
microbiome paper tied to Crohn disease or broader IBD.

## Next Expansion Targets
- Add Ulcerative Colitis alongside Crohn if a stronger microbiome coculture model
  is identified.
- Add CF intestinal organoid-monolayer as a separate bridge case if we want
  explicit coverage of organoid-derived 2D systems.
- Consider a follow-on schema refinement for `functional_assays` and `concordance`
  if we decide to track more of NAMO's richer comparison model.
