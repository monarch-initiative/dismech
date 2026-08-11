# IEMbase 0489: PYGM-related muscle glycogen phosphorylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 489 |
| Nosology | 3.4.08.01 |
| Gene | PYGM |
| External IDs | OMIM:232600; ORPHA:368 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PYGM-related muscle glycogen
phosphorylase deficiency as glycogen storage disease type V / McArdle disease.
Treatments are creatine and sucrose. Biochemical rows include elevated plasma
creatine kinase, decreased muscle phosphorylase, decreased lactate rise in the
forearm exercise test, increased muscle glycogen, normal ammonia rise in the
forearm exercise test, increased plasma uric acid, and normal-to-increased
urine myoglobin. Clinical rows include the second-wind phenomenon and
taurodontism.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. The local GSD
I entry models glucose-6-phosphatase system deficiency due to G6PC1 or SLC37A4,
with hepatic/renal glucose-6-phosphate hydrolysis failure, fasting
hypoglycemia, lactic acidosis, hyperlipidemia, hyperuricemia, hepatomegaly, and
GSD Ia/GSD Ib subtypes. It does not model PYGM, muscle glycogen phosphorylase
deficiency, McArdle disease, exercise-test lactate failure, myoglobinuria, or
second wind.

## Concordance and completeness

Judgement: false-positive candidate; true PYGM/McArdle disease local gap.

The generated candidate appears driven by shared "glycogen storage disease"
vocabulary rather than disease identity. IEMbase's source disease is a skeletal
muscle glycogenolysis disorder caused by PYGM deficiency, whereas the candidate
DisMech file is a hepatic/renal glucose-release disorder caused by G6PC1 or
SLC37A4. `Glycogen_Storage_Disease_Type_VII.yaml` is a closer myopathic
exercise-intolerance neighbor, but it is PFKM/Tarui disease and should not be
used as exact coverage either.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track PYGM-related McArdle disease / GSD V as a local curation gap.
- Preserve IEMbase prompts for muscle phosphorylase activity, exercise-test
  lactate/ammonia pattern, second wind, myoglobinuria, creatine, sucrose, and
  taurodontism for a future exact entry.
