# Hypochondroplasia phenotype curation notes

Date: 2026-04-19
Target file: `kb/disorders/Hypochondroplasia.yaml`
Issue: `#1450`

## Scope

Focused phenotype-only curation pass for hypochondroplasia. The goal was to make
the phenotype section more complete while tightening every retained statement to
exact PMID-backed evidence.

## Core sources used

- PMID:20301650. GeneReviews summary with the broadest clinically relevant
  phenotype overview and radiographic pattern.
- PMID:41762373. 2026 diagnostic pathway review with age-specific phenotype
  recognition clues.
- PMID:36442838. Korean FGFR3 N540K cohort with directly quotable frequencies for
  genu varum, macrocephaly, and developmental delay.
- PMID:23165795. Finnish FGFR3 N540K cohort defining seizure burden and MRI
  abnormalities.
- PMID:41040055. 2026 cohort analysis quantifying head-height disproportion.
- PMID:26867606. Neonatal radiology study supporting specific skeletal findings.
- PMID:14755409. Prenatal/neonatal case confirming early rhizomelic limb
  shortening.
- PMID:11475794. Radiology-focused review confirming classic vertebral and
  metaphyseal findings.

## Added or strengthened

- Short stature
- Rhizomelic limb shortening
- Relative macrocephaly
- Mild joint laxity
- Neurodevelopmental delay
- Hydrocephalus
- Spinal canal stenosis
- Narrow vertebral interpedicular distance
- Posterior scalloping of vertebral bodies
- Metaphyseal widening
- Short iliac bones
- Short femur

## Kept but softened

- Seizure: kept as an association, but frequency removed because the strongest
  quantitative evidence comes from a neurologically selected cohort.
- Temporal lobe dysplasia: retained with ascertainment caveat and without a
  whole-disease frequency claim.
- Ventriculomegaly: retained without frequency because available counts come from
  MRI-selected patients.

## Removed as unsupported or overclaimed

- Lumbar hyperlordosis
- Brachydactyly
- Frontal bossing
- The old combined entry `Spinal stenosis with reduced interpedicular distance`
  was replaced by separate clinical and radiographic findings.

## Frequency decisions

- Kept `HP_0040282` for relative macrocephaly based on 9/20 (45%) in PMID:36442838.
- Kept `HP_0040282` for genu varum based on 11/20 (55%) in PMID:36442838.
- Kept `HP_0040283` for neurodevelopmental delay based on 5/20 (25%) in
  PMID:36442838.
- Removed unsupported frequencies from short stature, seizures, temporal lobe
  dysplasia, ventriculomegaly, and radiographic findings.
