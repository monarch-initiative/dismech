---
disease: Arterial_Calcification_of_Infancy
generated: 2026-05-06T22:36:00Z
providers:
  - falcon
  - openscientist
falcon_citation_count: 14
openscientist_citation_count: 47
shared_citation_count: 0
---

# Research synthesis: Arterial Calcification of Infancy

## Source coverage

- Falcon report: `Arterial_Calcification_of_Infancy-deep-research-falcon.md`
- OpenScientist report: `Arterial_Calcification_of_Infancy-deep-research-openscientist.md`
- Falcon citation identifiers: 14
- OpenScientist citation identifiers: 47
- Shared citation identifiers: 0

## Agreement

Both providers identify GACI as an ENPP1/ABCC6 pyrophosphate-deficiency disorder
with infantile arterial calcification, stenosis, hypertension, heart failure, and
high early mortality. They also agree that ENPP1 survivors often transition into
a later ENPP1-deficiency spectrum with hypophosphatemic rickets, elevated FGF23,
hearing loss, and enthesopathy.

## Differences

Falcon emphasized clinical-trial provenance for INZ-701, including ENERGY 2,
ADAPT, ENERGY, and ENERGY 3 records. OpenScientist supplied a broader mechanistic
review of ENPP1-Fc/INZ-701 preclinical data, the AMP/adenosine branch of ENPP1
biology, and natural-history statistics for bisphosphonate uncertainty and
ENPP1-versus-ABCC6 outcome differences.

## YAML integration

Integrated into `kb/disorders/Arterial_Calcification_of_Infancy.yaml`:

- Backfilled Falcon and OpenScientist top-level reference provenance.
- Kept the existing ENPP1/ABCC6, PPi, FGF23, hearing-loss, and INZ-701 trial
  structure.
- Updated bisphosphonate therapy wording with the large natural-history cohort's
  no-survival-benefit finding.
- Added preclinical INZ-701/ENPP1-Fc support as model-organism evidence while
  retaining human efficacy as trial-stage.

## Not integrated

Detailed prenatal ultrasound findings, speculative TNAP inhibition, nanoparticle
chelation strategies, and expanded genotype-specific variant lists were retained
as research leads rather than promoted to curated disease mechanisms.
