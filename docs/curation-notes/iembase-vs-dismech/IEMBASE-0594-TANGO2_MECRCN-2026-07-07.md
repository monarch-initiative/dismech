# IEMbase 0594: TANGO2-related recurrent metabolic encephalomyopathic crises

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 594 |
| Nosology | 19.6.09.02 |
| Gene | TANGO2 |
| External IDs | OMIM:616878; ORPHA:480864 |
| Generated mapping | UNMAPPED; best candidate `Pantothenate_Kinase-Associated_Neurodegeneration.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TANGO2-related recurrent metabolic encephalomyopathic crises
associated with rhabdomyolysis, cardiac arrhythmias, and neurodegeneration
(MECRCN). The record is autosomal recessive, classified under disorders of
vesicular trafficking, has unknown treatability, and has no treatment rows.

Biochemical rows include increased acylcarnitine, increased plasma creatine
kinase, increased urinary C6-C10 dicarboxylic acids, normal-to-increased blood
ammonia, decreased plasma glucose, and increased plasma lactate. Clinical rows
include ataxia, dystonia, optic atrophy, spasticity, brain atrophy on MRI,
cardiac arrhythmia, hypoglycemia, intellectual disability, neurodegenerative
disease, rhabdomyolysis, and seizures.

## DisMech phenotype coverage

`Pantothenate_Kinase-Associated_Neurodegeneration.yaml` is a false-positive
generated candidate. PKAN models biallelic PANK2 disease, coenzyme A
biosynthesis disruption, brain iron accumulation, progressive dystonia,
spasticity, and retinal/neurodegenerative features. It does not represent
TANGO2, vesicular-trafficking disease, recurrent metabolic crises,
rhabdomyolysis, hypoglycemia, acylcarnitine/dicarboxylic-acid abnormalities, or
cardiac arrhythmia crises.

No exact TANGO2/MECRCN target was identified locally.

## Concordance and completeness

Judgement: true local gap; reject PKAN as an exact target.

The generated match is driven by dystonia, spasticity, optic involvement, and
neurodegeneration. The IEMbase record's defining pattern is metabolic crisis
with rhabdomyolysis and cardiac arrhythmia in TANGO2 disease, which is
mechanistically separate from PANK2-related NBIA.

## Curation actions

- Create or identify an exact TANGO2 / MECRCN target before import.
- Reject `Pantothenate_Kinase-Associated_Neurodegeneration.yaml` as an exact
  mapping.
- Preserve acylcarnitine, C6-C10 dicarboxylic-acid, CK, glucose, lactate,
  ammonia, rhabdomyolysis, arrhythmia, hypoglycemia, seizure, neurodegeneration,
  optic-atrophy, and MRI prompts.
