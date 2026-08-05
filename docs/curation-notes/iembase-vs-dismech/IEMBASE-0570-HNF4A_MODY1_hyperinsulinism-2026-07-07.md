# IEMbase 0570: HNF4A-related MODY1 with hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 570 |
| Nosology | 24.1.05.01 |
| Gene | HNF4A |
| External IDs | OMIM:600281; ORPHA:93111 |
| Generated mapping | UNMAPPED; best candidate `Fanconi_Renotubular_Syndrome.yaml#FRTS4` |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#HNF4A/HNF1A-HI`; `Diabetes_Mellitus.yaml#HNF4A`; `Fanconi_Renotubular_Syndrome.yaml#FRTS4` as variant-specific context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents HNF4A-related hepatocyte nuclear factor 4-alpha deficiency /
MODY1. The record is autosomal dominant, idiopathic subtype, of unknown
treatability, and has no treatment rows.

Biochemical rows include decreased free fatty acids during hypoglycemia,
decreased ketones during hypoglycemia, low plasma glucose, and increased
insulin during hypoglycemia. Clinical and characteristic rows include
hypoglycemia, MODY1 diabetes, hyperinsulinism, hypoketotic hypoglycemia, and
macrosomia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` has a transcription-factor
hyperinsulinism subtype for HNF4A/HNF1A variants, describing neonatal
hyperinsulinism followed by maturity-onset diabetes later in life, often with
macrosomia. `Diabetes_Mellitus.yaml` includes HNF4A as a causative monogenic
diabetes gene. The generated `Fanconi_Renotubular_Syndrome.yaml#FRTS4`
candidate is variant-specific for HNF4A R76W/R85W renal Fanconi syndrome plus
beta-cell phenotype, and should not be used as the primary target for a generic
MODY1/hyperinsulinism IEMbase record.

## Concordance and completeness

Judgement: generated false negative to the congenital hyperinsulinism and
monogenic-diabetes neighborhood; reject `Fanconi_Renotubular_Syndrome.yaml#FRTS4`
as an exact mapping.

IEMbase and the local congenital hyperinsulinism entry agree on HNF4A,
dominant inheritance, neonatal or early hyperinsulinism, hypoketotic
hypoglycemia, macrosomia, and later MODY-type diabetes. `Diabetes_Mellitus.yaml`
supports the HNF4A/MODY aspect but is broader than the IEMbase insulin-
metabolism record.

## Curation actions

- Resolve the hyperinsulinism portion to
  `Congenital_Isolated_Hyperinsulinism.yaml#HNF4A/HNF1A-HI`.
- Use `Diabetes_Mellitus.yaml#HNF4A` as monogenic-diabetes context, not as a
  complete gene-specific MODY1 entry.
- Do not map this generic MODY1 record to FRTS4 unless the variant-specific
  Fanconi renal phenotype is present.
