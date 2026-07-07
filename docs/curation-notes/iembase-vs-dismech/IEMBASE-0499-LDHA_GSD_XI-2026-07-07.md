# IEMbase 0499: LDHA-related lactate dehydrogenase A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 499 |
| Nosology | 3.3.14.01 |
| Gene | LDHA |
| External IDs | OMIM:612933; ORPHA:2088 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive LDHA-related lactate dehydrogenase A
deficiency as glycogen storage disease type 11. No treatments are listed.
Biochemical rows include elevated plasma creatine kinase, decreased muscle and
RBC lactate dehydrogenase activity, increased lactate rise in the forearm
exercise test, normal-to-increased muscle glycogen, normal ammonia rise in the
forearm exercise test, increased plasma lactate, and increased urine myoglobin.
Clinical rows include exercise intolerance, muscle cramps, muscle pain, muscle
weakness, skin rash, and uterine muscle stiffness in pregnancy.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. The local GSD
I entry models glucose-6-phosphatase system deficiency caused by G6PC1 or
SLC37A4, with hepatic/renal fasting hypoglycemia, lactic acidosis,
hyperlipidemia, hyperuricemia, hepatomegaly, and GSD Ia/GSD Ib subtypes. It
does not model LDHA, lactate dehydrogenase A deficiency, myopathic
exercise intolerance, RBC/muscle LDH activity, myoglobinuria, or the pregnancy
uterine-stiffness feature.

## Concordance and completeness

Judgement: false-positive candidate; true LDHA/GSD XI local gap.

The generated candidate is driven by broad glycogen-storage terminology rather
than disease identity. IEMbase's source disease is a glycolysis/lactate
interconversion defect with muscle and erythrocyte enzyme deficiency, whereas
the candidate DisMech entry is a glucose-6-phosphate hydrolysis disorder. The
nearby local myopathic GSD entry, `Glycogen_Storage_Disease_Type_VII.yaml`,
captures some shared exercise-intolerance vocabulary but is PFKM/Tarui disease
and is not exact coverage.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track LDHA-related lactate dehydrogenase A deficiency / GSD XI as a local
  curation gap.
- Preserve IEMbase prompts for RBC and muscle LDH activity, exercise-test
  lactate/ammonia pattern, myoglobinuria, skin rash, and uterine stiffness in
  pregnancy for a future exact entry.
