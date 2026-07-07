# IEMbase 0504: HOGA1-related primary hyperoxaluria type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 504 |
| Nosology | 1.7.02.02 |
| Gene | HOGA1 |
| External IDs | OMIM:613616; ORPHA:93600 |
| Generated mapping | UNMAPPED; best scored candidate `erythromelalgia.yaml` (0.588) |
| Candidate DisMech targets | `Primary_Hyperoxaluria_Type_3.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive HOGA1-related mitochondrial
4-hydroxy-2-oxoglutarate aldolase deficiency as primary hyperoxaluria type 3.
No treatments are listed. Biochemical rows include variable plasma oxalic acid,
markedly increased urinary oxalic acid, normal-to-increased urinary calcium,
normal-to-increased plasma creatinine and urea, and increased urinary
4-hydroxy-2-oxoglutaric acid. Clinical rows include nephrolithiasis, renal
colic, nephrocalcinosis, chronic renal failure, hematuria, urinary infections,
bone pain, growth retardation, failure to thrive, calcinosis cutis, cardiac
oxalate deposition, cardiomyopathy, trabecular-structure derangement,
pathological fractures, radiolucent metaphyseal bands, optic atrophy,
pigmentary retinopathy, pancytopenia, and livedo reticularis.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Primary_Hyperoxaluria_Type_3.yaml` is the exact disease target. It models
autosomal recessive HOGA1 loss of mitochondrial
4-hydroxy-2-oxoglutarate aldolase activity, hydroxyproline-pathway metabolite
accumulation, cytosolic glyoxylate-to-oxalate overproduction, urinary calcium
oxalate supersaturation, recurrent calcium oxalate nephrolithiasis, occasional
nephrocalcinosis, hyperoxaluria, urinary HOG-related metabolite elevation,
HOGA1 genetics, and supportive high-fluid/citrate-style management.

## Concordance and completeness

Judgement: false negative; resolve to `Primary_Hyperoxaluria_Type_3.yaml`.

The two resources agree on HOGA1/PH3 identity, recessive inheritance, oxalate
overproduction, urinary oxalate, 4-hydroxy-2-oxoglutarate/HOG metabolite
elevation, nephrolithiasis, renal colic/stone presentation, and
nephrocalcinosis. IEMbase is broader on possible systemic oxalosis or renal
complication prompts, including skin, cardiac, skeletal, hematologic, ocular,
and vascular-pattern findings. DisMech intentionally emphasizes PH3's generally
milder kidney-stone phenotype, so those severe systemic rows need careful
source review before import.

## Curation actions

- Map this record to `Primary_Hyperoxaluria_Type_3.yaml`.
- Treat the erythromelalgia candidate as unrelated noise.
- Consider IEMbase's creatinine/urea, urinary calcium, hematuria, urinary
  infections, and systemic oxalosis prompts only after verifying that they are
  appropriate for PH3 rather than primary hyperoxaluria in general or more
  severe PH1/PH2 presentations.
