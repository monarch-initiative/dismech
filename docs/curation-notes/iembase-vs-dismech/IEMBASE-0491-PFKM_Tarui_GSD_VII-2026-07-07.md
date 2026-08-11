# IEMbase 0491: PFKM-related muscle phosphofructokinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 491 |
| Nosology | 3.3.07.01 |
| Gene | PFKM |
| External IDs | OMIM:232800; ORPHA:371 |
| Generated mapping | MAPPED; HIGH; `Glycogen_Storage_Disease_Type_VII.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_VII.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PFKM-related muscle phosphofructokinase
deficiency as glycogen storage disease type VII / Tarui disease. No treatments
are listed. Biochemical rows include increased plasma creatine kinase,
decreased phosphofructokinase activity in unspecified, fibroblast, and muscle
contexts, decreased lactate rise in forearm exercise testing, increased muscle
glycogen, normal ammonia rise in the forearm exercise test, increased bilirubin,
increased reticulocytes, increased uric acid, decreased RBC
2,3-diphosphoglycerate, and possible urine myoglobin. Clinical rows include
gallstones, jaundice, and the second-wind phenomenon.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_VII.yaml` is the correct local target. The entry
models autosomal recessive PFKM/Tarui disease, reduced muscle
6-phosphofructokinase activity, impaired skeletal-muscle glycolysis, increased
muscle glycogen, exercise intolerance, myalgia, cramps, myoglobinuria,
hyperuricemia, hemolytic anemia, reduced erythrocyte 2,3-diphosphoglycerate,
low exercise lactate with delayed post-exercise rise, high exercise ammonia,
muscle biopsy, and ketogenic diet as a documented symptomatic approach.

## Concordance and completeness

Judgement: correct generated mapping with high concordance.

IEMbase and DisMech agree on PFKM/GSD VII identity, recessive inheritance,
muscle PFK deficiency, exercise lactate abnormality, increased muscle glycogen,
hyperuricemia, myoglobinuria/rhabdomyolysis context, hemolysis-related RBC
findings, bilirubin/reticulocyte abnormalities, and reduced RBC
2,3-diphosphoglycerate. IEMbase adds explicit gallstones, jaundice, second-wind
wording, and a "normal ammonia rise" exercise-test row that should be reviewed
against the DisMech evidence for high ammonia during and after exercise.

## Curation actions

- Treat this as covered by `Glycogen_Storage_Disease_Type_VII.yaml`.
- If importing IEMbase prompts, verify gallstones, jaundice, second wind, and
  the apparent ammonia-profile discrepancy before adding them.
- Consider adding IEMbase's fibroblast/unspecified phosphofructokinase activity
  compartments only if independently supported.
