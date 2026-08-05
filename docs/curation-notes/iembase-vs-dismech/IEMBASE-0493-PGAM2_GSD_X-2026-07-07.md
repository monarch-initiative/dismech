# IEMbase 0493: PGAM2-related muscle phosphoglycerate mutase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 493 |
| Nosology | 3.3.11.01 |
| Gene | PGAM2 |
| External IDs | OMIM:261670; ORPHA:97234 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PGAM2-related muscle phosphoglycerate
mutase deficiency as glycogen storage disease type X / DiMauro disease. No
treatments are listed. Biochemical rows include increased plasma creatine
kinase, decreased muscle phosphoglycerate mutase, normal-to-increased muscle
glycogen, and increased urine myoglobin. No clinical rows are listed in the
local JSON.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. It covers
G6PC1/SLC37A4 glucose-6-phosphatase system deficiency and hepatic/renal
fasting-hypoglycemia biology. It does not model PGAM2, muscle
phosphoglycerate mutase deficiency, GSD X, DiMauro disease, exercise-induced
myoglobinuria, or the skeletal-muscle glycolysis block implied by the IEMbase
record.

## Concordance and completeness

Judgement: false-positive candidate; true PGAM2/GSD X local gap.

The generated candidate shares only broad glycogen-storage vocabulary.
IEMbase's disease is a skeletal-muscle glycolytic enzyme deficiency with CK and
myoglobinuria markers, not a hepatic glucose-6-phosphatase disorder. Local
`Glycogen_Storage_Disease_Type_VII.yaml` provides related glycolytic myopathy
context, but it is PFKM/Tarui disease and should not be treated as exact PGAM2
coverage.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track PGAM2-related GSD X / DiMauro disease as a local curation gap.
- Preserve IEMbase prompts for muscle phosphoglycerate mutase activity,
  creatine kinase, muscle glycogen, and urine myoglobin for a future exact
  entry.
