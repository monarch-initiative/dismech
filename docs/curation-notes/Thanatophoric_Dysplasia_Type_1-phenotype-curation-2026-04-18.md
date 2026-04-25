## Scope

Focused phenotype curation for `kb/disorders/Thanatophoric_Dysplasia_Type_1.yaml`
for issue `#1457`.

Goals:
- strengthen phenotype assertions with exact PMID-backed abstract evidence
- add clinically important TD1 phenotypes missing from the phenotype block
- remove unsupported frequency claims
- remove or soften phenotype claims that were not directly supportable from abstracts

## PMIDs Used

- `PMID:11241532`
  TD1 prenatal cases with polyhydramnios, macrocephaly, narrow thoracic cage,
  and curved short femora; also supports redundant skin folds on 3D ultrasound.
- `PMID:11270184`
  TD1 summary stating respiratory failure is due to narrow thorax with pulmonary
  hypoplasia.
- `PMID:17048442`
  Molecularly confirmed TD1 case with severe limb shortening, redundant skin
  folds, frontal bossing, depressed nasal bridge, narrow thoracic cage,
  respiratory insufficiency, short ribs, platyspondyly, and bowed femora.
- `PMID:18504386`
  Prenatal ultrasound case showing short limbs at 12 weeks and short bowed long
  bones by 16 weeks.
- `PMID:23408600`
  Larger prenatal TD cohort supporting short fingers as a recurring sonographic
  feature.
- `PMID:23551494`
  Molecularly confirmed TD1 neuropathology with enlarged hyperconvoluted
  temporal lobe and cortical disorganization.
- `PMID:25328339`
  TD1 fetal autopsy report listing short neck and protuberant abdomen.
- `PMID:26043509`
  TD1-specific case report supporting cloverleaf skull as a rare variant rather
  than a typical TD1 finding.
- `PMID:9481650`
  TD1 postmortem series describing H-, U-, and reversed U-shaped vertebrae.

## Phenotype Decisions

Added or materially strengthened:
- `Micromelia`
- `Curved femurs`
- `Short ribs`
- `Narrow thorax`
- `Platyspondyly`
- `Macrocephaly`
- `Frontal bossing`
- `Depressed nasal bridge`
- `Short neck`
- `Protuberant abdomen`
- `Pulmonary hypoplasia`
- `Respiratory insufficiency`
- `Redundant skin folds`
- `Polyhydramnios`
- `Cloverleaf skull` retained only as a rare TD1 variant
- `Abnormal temporal lobe morphology`

Kept but sourced cautiously:
- `Brachydactyly`
  Supported by `short fingers` language from a larger prenatal thanatophoric
  dysplasia cohort, but the abstract does not break down frequency by subtype.

Removed or softened:
- all phenotype `frequency:` assignments
  The available abstracts support association but generally do not justify a TD1
  subtype-specific frequency band.
- `Midface retrusion`
  Removed because I did not find a clean abstract-backed TD1-specific statement
  supporting this exact phenotype.
- `Hypotonia`
  Removed because the available abstract support was tertiary/general TD wording
  rather than direct TD1 abstract evidence.

## Curation Notes

- I favored TD1-specific case reports and prenatal series over generalized
  review language whenever possible.
- When only mixed TD evidence was available, I kept the phenotype only if the
  abstract statement was still clinically useful and I made the limitation
  explicit in the explanation.
