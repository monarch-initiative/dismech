# IEMbase 0531: COQ6-related primary CoQ10 deficiency type 6

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 531 |
| Nosology | 8.1.05.01 |
| Gene | COQ6 |
| External IDs | OMIM:614650; ORPHA:93921 |
| Generated mapping | UNMAPPED; best candidate `Primary_Coenzyme_Q10_Deficiency.yaml` |
| Candidate DisMech targets | `Primary_Coenzyme_Q10_Deficiency.yaml#COQ6` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents COQ6-related coenzyme Q6 monooxygenase deficiency, with
primary coenzyme Q10 deficiency type 6, early-onset steroid-resistant nephrosis
with sensorineural deafness, and COQ6 deficiency as alternate labels. The record
is autosomal recessive and treatment rows list CoQ10.

The compact phenotype signal is an oto-renal CoQ10 biosynthesis disorder:
characteristic rows include sensorineural deafness and nephrotic syndrome, with
additional ataxia and epilepsy rows. Biochemical rows include low or normal
fibroblast CoQ10 and normal plasma lactate.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. `Primary_Coenzyme_Q10_Deficiency.yaml`
has a specific COQ6 subtype for steroid-resistant nephrotic syndrome with
sensorineural deafness. The local file covers COQ6 as a CoQ10 biosynthesis gene,
defective CoQ10 synthesis, renal podocyte/nephrotic disease, inner-ear
involvement, sensorineural deafness, and high-dose oral CoQ10 treatment.

## Concordance and completeness

Judgement: false negative; resolve to the COQ6 subtype in the local primary
coenzyme Q10 deficiency file.

IEMbase and DisMech agree on COQ6 identity, autosomal recessive inheritance,
primary CoQ10 deficiency, steroid-resistant nephrotic syndrome, sensorineural
deafness, and CoQ10 treatment. IEMbase adds a concise fibroblast CoQ10/lactate
biomarker checklist and flags occasional ataxia/epilepsy.

## Curation actions

- Map this record to `Primary_Coenzyme_Q10_Deficiency.yaml#COQ6`.
- Add COQ6 deficiency and primary CoQ10 deficiency type 6 aliases to future
  mapping support if needed.
- Preserve IEMbase's nephrotic syndrome, sensorineural deafness, fibroblast
  CoQ10, lactate, ataxia, epilepsy, and CoQ10-treatment prompts.
