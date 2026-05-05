# Achondroplasia phenotype curation notes

Date: 2026-04-18
Curator: Codex
Issue: monarch-initiative/dismech#1449

## Scope

Focused only on strengthening `kb/disorders/Achondroplasia.yaml` phenotype coverage.
Priority was given to cohort, natural-history, and complication-specific PubMed
abstracts that could support exact quoted snippets for phenotype assertions.

## Key sources used

- PMID:32803853
  Supports disproportionate short stature as a defining phenotype.
- PMID:29972438
  Natural-history cohort supporting macrocephaly, high/prominent forehead,
  trident hands, genu varum, rhizomelic long-bone shortening, motor delay,
  speech delay, obesity, sleep apnea, middle-ear dysfunction, and occasional
  hydrocephalus.
- PMID:37072824
  Supports prominent forehead and midface/maxillary retrusion in a dedicated
  craniofacial cohort.
- PMID:37493935
  Supports childhood thoracolumbar kyphosis with frequent spontaneous
  resolution by age 10.
- PMID:27927547
  Supports scoliosis and thoracolumbar kyphosis prevalence in a large
  orthopedic cohort.
- PMID:32883660
  Supports infant foramen magnum stenosis severity spectrum on MRI.
- PMID:38554024
  Confirms frequent foramen magnum stenosis in a young-child cohort.
- PMID:32864841
  Supports lifespan complications including cervical/lumbar stenosis,
  childhood elbow contractures and radial head dislocations, and central/obstructive
  sleep apnea.
- PMID:32170149
  Refines adult lumbar spinal stenosis phenotype.
- PMID:40675782
  Supports pediatric obstructive and central sleep apnea by polysomnography.
- PMID:39660705
  Supports otitis media with effusion and predominantly conductive hearing loss.
- PMID:34736503
  Confirms persistent conductive/mixed hearing loss burden in adults.
- PMID:3228140
  Supports obesity beginning in early childhood and remaining prevalent at all ages.
- PMID:22409389
  Supports delayed gross motor and later communication development.
- PMID:33579320
  Supports cautious retention of hydrocephalus as an occasional pediatric complication.

## Curation decisions

- Removed unsupported phenotype frequency qualifiers instead of preserving
  broad `VERY_FREQUENT`/`FREQUENT` claims without explicit evidence.
- Removed unsupported or weakly grounded phenotype entries rather than keeping
  them on general clinical familiarity alone.
- Replaced imprecise mappings with more grounded HPO terms, including:
  - `HP:0008905` Rhizomelia
  - `HP:0011220` Prominent forehead
  - `HP:0031353` Otitis media with effusion
  - `HP:0000405` Conductive hearing impairment
  - `HP:0002194` Delayed gross motor development
  - `HP:0000750` Delayed speech and language development

## Open caution

Lumbar hyperlordosis and brachydactyly were not retained as standalone
phenotypes because the current source set did not provide sufficiently direct
abstract-level support for a clean, evidence-backed entry.
