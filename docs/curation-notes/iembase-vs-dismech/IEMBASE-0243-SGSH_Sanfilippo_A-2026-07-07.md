# IEMbase 0243: SGSH-related Heparan N-sulfatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 243 |
| Nosology | 20.2.03.01 |
| Gene | SGSH |
| External IDs | OMIM:252900; ORPHA:79269 |
| Generated mapping | MAPPED; `Sanfilippo_syndrome.yaml#MPS IIIA` |
| Candidate DisMech targets | `Sanfilippo_syndrome.yaml#MPS IIIA` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SGSH-related heparan N-sulfatase deficiency, with
alternate labels Sanfilippo A disease, mucopolysaccharidosis type 3A, and MPS
IIIA. The record is autosomal recessive and treatability is marked yes, with no
treatment rows in the cached JSON.

Biochemical rows include decreased heparan-N-sulfatase activity in white blood
cells and increased urinary heparan sulfate and total glycosaminoglycans.
Clinical rows include Alder-Reilly anomaly, diarrhea, dysostosis multiplex,
hearing loss, liver dysfunction, macular involvement, and retinopathy.
Characteristic rows include aggressive behavior, coarse facial features,
hyperactivity, intellectual disability, neurologic regression, seizures, sleep
disturbances, and swallowing difficulties.

## DisMech phenotype coverage

`Sanfilippo_syndrome.yaml#MPS IIIA` is the correct local target. The local file
has subtype coverage for SGSH-related Sanfilippo syndrome type A/sulfamidase
deficiency, and the shared Sanfilippo entry covers autosomal recessive MPS III,
failed lysosomal heparan sulfate catabolism, heparan sulfate accumulation,
progressive neurodegeneration, intellectual disability, developmental
regression, behavioral problems, hyperactivity, sleep disturbance, seizures,
swallowing and feeding difficulty, hearing and visual impairment, mild systemic
skeletal involvement, respiratory complications, and supportive/investigational
therapy context.

## Concordance and completeness

Judgement: correct subtype-level mapping with high concordance.

IEMbase and DisMech agree on SGSH/MPS IIIA identity, enzyme deficiency, heparan
sulfate storage, total GAG elevation, neurobehavioral disease, seizures,
sleep disturbance, swallowing difficulty, and systemic MPS features. IEMbase is
more explicit for subtype-specific enzyme testing, Alder-Reilly anomaly,
diarrhea, macular involvement, and retinopathy.

## Curation actions

- Keep this record mapped to `Sanfilippo_syndrome.yaml#MPS IIIA`.
- No mapping correction is needed.
- Use IEMbase's subtype-specific clinical rows as enrichment prompts if
  Sanfilippo phenotype detail is refreshed.
