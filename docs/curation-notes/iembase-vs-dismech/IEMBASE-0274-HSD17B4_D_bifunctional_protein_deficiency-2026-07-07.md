# IEMbase 0274: HSD17B4-related D-bifunctional protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 274 |
| Nosology | 14.2.03.01 |
| Gene | HSD17B4 |
| External IDs | OMIM:261515; ORPHA:300 |
| Generated mapping | MAPPED to `D-Bifunctional_Protein_Deficiency.yaml` |
| Candidate DisMech targets | `D-Bifunctional_Protein_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive HSD17B4-related D-bifunctional protein
deficiency, with alternate labels pseudo-Zellweger syndrome and Perrault
syndrome type 1. Prevalence is listed as 1:100,000. Treatability is marked
unknown and the cached JSON has no treatment rows.

Characteristic clinical rows include sensorineural deafness, defective visual
acuity, developmental delay, and osteopenia. Additional rows include ataxia,
diminished brain auditory evoked potentials, diminished ERG response, cataract,
retinitis pigmentosa, cerebral neocortical dysplasia, cerebral white-matter
involvement, hypotonia, intellectual disability, seizures, spastic paresis,
peripheral neuropathy, dysmorphic features, clubfoot, low nasal bridge,
upslanting palpebral fissures, epiphyseal and periarticular calcific
stippling, hepatomegaly, jaundice, portal hypertension, renal cysts, failure
to thrive, diarrhea, and glaucoma.

The biochemical panel includes increased VLCFA, pristanic acid, bile-acid
intermediates, pipecolic acid, AST/ALT, and fat-soluble vitamin abnormalities,
with low or low-normal coagulation factors, DHA, and plasmalogens.

## DisMech phenotype coverage

`D-Bifunctional_Protein_Deficiency.yaml` is the correct local target. It covers
biallelic HSD17B4 disease, impaired peroxisomal hydratase/dehydrogenase steps,
VLCFA, pristanic-acid, and bile-acid intermediate accumulation, neonatal
hypotonia, seizures, leukodystrophy, psychomotor delay, sensorineural hearing
loss, optic atrophy, craniofacial dysmorphism, HSD17B4 allelic Perrault
context, DBP subtypes, supportive care, and DHA/fat-soluble vitamin
supplementation.

## Concordance and completeness

Judgement: correct mapping with high concordance.

IEMbase and DisMech agree on HSD17B4/DBP identity, autosomal recessive
inheritance, Zellweger-like severe phenotype framing, sensory loss,
neurodevelopmental disease, leukodystrophy/white-matter involvement, and the
major peroxisomal beta-oxidation biochemical abnormalities. DisMech is richer
for mechanism, subtype structure, Perrault distinction, and management.

IEMbase adds useful prompts for osteopenia, cataract/ERG/glaucoma,
portal hypertension, renal cysts, skeletal/dysmorphic detail, and age-stratified
lab rows. As with ACOX1, the plasmalogen and phytanic-acid directionality should
be reviewed against DBP-specific sources before import, because the local entry
emphasizes DBP as an isolated beta-oxidation enzyme defect rather than a
generalized biogenesis disorder.

## Curation actions

- Keep the mapping to `D-Bifunctional_Protein_Deficiency.yaml`.
- Use IEMbase's ocular, skeletal, renal, and portal-hypertension rows as
  enrichment prompts.
- Review plasmalogen and phytanic/pristanic directionality before adding those
  lab statements to the local entry.
