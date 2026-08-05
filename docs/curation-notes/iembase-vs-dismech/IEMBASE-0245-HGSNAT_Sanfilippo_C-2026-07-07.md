# IEMbase 0245: HGSNAT-related Heparan-alpha-glucosaminide N-acetyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 245 |
| Nosology | 20.2.05.01 |
| Gene | HGSNAT |
| External IDs | OMIM:252930; ORPHA:79271 |
| Generated mapping | MAPPED; `Sanfilippo_syndrome.yaml#MPS IIIC` |
| Candidate DisMech targets | `Sanfilippo_syndrome.yaml#MPS IIIC` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HGSNAT-related heparan-alpha-glucosaminide
N-acetyltransferase deficiency, with alternate labels Sanfilippo syndrome type C
severe, retinitis pigmentosa type 73 milder, mucopolysaccharidosis type 3C, and
MPS IIIC. The record is autosomal recessive and treatability is marked yes, with
no treatment rows in the cached JSON.

Biochemical rows include decreased acetyl-CoA:alpha-N-glucosaminide-
N-acetyltransferase activity in white blood cells and increased urinary heparan
sulfate and total glycosaminoglycans. Clinical rows include Alder-Reilly
anomaly, diarrhea, dysostosis multiplex, hearing loss, and sleep disturbances.
Characteristic rows include aggressive behavior, coarse facial features,
hyperactivity, intellectual disability, liver dysfunction, neurologic
regression, pigmentary retinopathy, seizures, and swallowing difficulties.

## DisMech phenotype coverage

`Sanfilippo_syndrome.yaml#MPS IIIC` is the correct local target. The local file
has subtype coverage for HGSNAT-related Sanfilippo syndrome type C/heparan-
alpha-glucosaminide N-acetyltransferase deficiency, and the shared Sanfilippo
entry covers autosomal recessive inheritance, heparan sulfate catabolic failure,
heparan sulfate storage, progressive neurodegeneration, developmental
regression, intellectual disability, behavioral problems, hyperactivity, sleep
disturbance, seizures, swallowing and feeding difficulty, hearing and visual
impairment, and mild systemic MPS features.

## Concordance and completeness

Judgement: correct subtype-level mapping with high concordance.

IEMbase and DisMech agree on HGSNAT/MPS IIIC identity, heparan sulfate storage,
total GAG elevation, neurobehavioral disease, seizures, sleep disturbance,
swallowing difficulty, hearing involvement, and systemic MPS features. IEMbase
adds useful specificity for the enzyme assay, pigmentary retinopathy, and the
retinitis pigmentosa type 73/attenuated retina-focused label. The current local
Sanfilippo file does not split that milder RP73 context into a separate disease
target.

## Curation actions

- Keep this record mapped to `Sanfilippo_syndrome.yaml#MPS IIIC`.
- Preserve the note that IEMbase spans severe Sanfilippo C and milder RP73
  labeling.
- Consider retinal phenotype detail if HGSNAT/MPS IIIC subtype coverage is
  refreshed.
