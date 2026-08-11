# IEMbase 0756: LIPE-related hormone-sensitive lipase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 756 |
| Nosology | 14.4.09.01 |
| Nosology code | IEM0663 |
| Gene | LIPE |
| External IDs | OMIM:615980; ORPHA:435660 |
| Generated mapping | UNMAPPED; weak candidate `Familial_Partial_Lipodystrophy.yaml` |
| Candidate DisMech targets | `Familial_Partial_Lipodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as LIPE-related
hormone-sensitive lipase deficiency, with alternate name familial partial
lipodystrophy type 6. The source signal includes very high serum cholesterol
and triglycerides, elevated creatine kinase, adult lipodystrophy, low body fat
percentage, low BMI, diabetes, acanthosis nigricans, and hepatic steatosis.

## DisMech phenotype coverage

`Familial_Partial_Lipodystrophy.yaml` includes a LIPE-related familial partial
lipodystrophy type 6 subtype with biallelic LIPE variant context. The generated
mapper status is therefore a false negative or weak partial hit rather than a
true local absence.

The local FPLD entry covers the main disease-family phenotype cluster:
lipodystrophy, insulin resistance or diabetes, hypertriglyceridemia, hepatic
steatosis, and acanthosis nigricans. It is less clear for LIPE-specific
phenotype detail, particularly creatine kinase elevation,
hypercholesterolemia, low BMI, and the adult-predominant onset pattern.

## Concordance and completeness

Judgement: false negative with partial local coverage in a broader FPLD entry.

DisMech has the right broad target and subtype identity, but IEMbase adds useful
LIPE-specific biochemical and age-pattern prompts that may not be fully
represented in the group-level FPLD phenotype set.

## Curation actions

- Treat `Familial_Partial_Lipodystrophy.yaml` as partial local coverage for
  LIPE / FPLD6 rather than as an unrelated weak candidate.
- Consider adding subtype-specific LIPE phenotype and biochemical detail if the
  entry supports subtype-level annotations.
- Preserve CK elevation, hypercholesterolemia, low BMI, and adult-onset pattern
  as source-specific prompts.
