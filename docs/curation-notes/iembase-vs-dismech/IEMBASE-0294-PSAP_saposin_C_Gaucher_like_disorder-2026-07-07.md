# IEMbase 0294: PSAP-related Gaucher disease-like disorder due to saposin C deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 294 |
| Nosology | 20.1.02.01 |
| Gene | PSAP |
| External IDs | OMIM:610539; ORPHA:309263 |
| Generated mapping | MAPPED; `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml` |
| Candidate DisMech targets | `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents isolated saposin C deficiency, a PSAP cofactor disorder with
a Gaucher-like presentation. Inheritance is autosomal recessive and
treatability is unknown.

Clinical rows include anemia, abnormal eye movements, foam cells,
hepatosplenomegaly, pathological fractures, myoclonic seizures,
thrombocytopenia, bone pain, and developmental delay. Biochemical rows are
particularly useful: markedly increased plasma chitotriosidase, normal
beta-D-glucosidase activity, and increased serum glucosylsphingosine.

## DisMech phenotype coverage

`Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml` is the correct local target.
The local entry explicitly models PSAP variants abolishing saposin C, impaired
glucocerebrosidase access to glucosylceramide despite normal GBA1 enzyme
activity, lysosomal glucosylceramide accumulation, Gaucher-like macrophage
storage, hepatosplenomegaly, and thrombocytopenia.

Local diagnosis also captures the main differentiator from classic Gaucher
disease: a Gaucher-like phenotype with normal glucocerebrosidase activity and
confirmatory PSAP sequencing.

## Concordance and completeness

Judgement: correct high-concordance mapping to
`Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml`.

IEMbase and DisMech agree on PSAP/saposin C identity, recessive inheritance,
Gaucher-like macrophage storage, hepatosplenomegaly, thrombocytopenia, normal
glucocerebrosidase activity, and increased glucosylsphingosine. DisMech is
stronger for the cofactor-defect mechanism and for distinguishing saposin C
deficiency from GBA1 Gaucher disease.

IEMbase adds phenotype prompts that are not all explicit locally: anemia,
abnormal eye movements, foam cells, pathological fractures, myoclonic seizures,
bone pain, developmental delay, and chitotriosidase. These should be reviewed
carefully because the local entry is intentionally conservative and the
published case base is small.

## Curation actions

- Keep this record mapped to `Gaucher_Disease_Due_To_Saposin_C_Deficiency.yaml`.
- Consider adding normal beta-D-glucosidase plus elevated glucosylsphingosine and
  chitotriosidase as biochemical prompts if supported by the local evidence base.
- Review IEMbase-only neurologic, ocular-motor, skeletal, hematologic, and foam
  cell rows before importing.
