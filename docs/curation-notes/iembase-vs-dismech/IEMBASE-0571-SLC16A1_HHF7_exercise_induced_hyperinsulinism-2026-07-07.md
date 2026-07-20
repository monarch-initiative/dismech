# IEMbase 0571: SLC16A1-related exercise-induced hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 571 |
| Nosology | 4.3.05.01 |
| Gene | SLC16A1 |
| External IDs | OMIM:610021; ORPHA:438075 |
| Generated mapping | UNMAPPED; best candidate `PRPS1_Superactivity.yaml` |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml` as broad context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC16A1-related monocarboxylate transporter 1 superactivity,
with alternate label familial hyperinsulinemic hypoglycemia type 7 and
abbreviation HHF7. The record is autosomal dominant, idiopathic subtype, of
unknown treatability, and has no treatment rows.

Biochemical rows include decreased serum free fatty acids, low-to-normal urinary
ketones, decreased ketones during hypoglycemia, normal plasma ammonia, and low
blood and plasma glucose. Characteristic rows include hyperinsulinism,
exercise-induced hypoglycemia, pyruvate- and exercise-stimulated insulin
secretion, and syncope.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` lists SLC16A1 among established CHI
genes in evidence text, but it does not appear to define an SLC16A1/HHF7 subtype
or the inappropriate beta-cell monocarboxylate transporter expression mechanism.
The generated `PRPS1_Superactivity.yaml` candidate is a false positive based on
"superactivity" wording and does not cover SLC16A1, exercise-induced insulin
secretion, or monocarboxylate transport.

## Concordance and completeness

Judgement: broad congenital-hyperinsulinism context only; exact SLC16A1/HHF7
coverage remains a local gap.

IEMbase overlaps with local CHI context on hyperinsulinism, hypoketotic
hypoglycemia, low glucose, and suppressed free fatty acids/ketones. The missing
local content is the SLC16A1/MCT1-specific exercise/pyruvate-triggered
insulin-secretion mechanism.

## Curation actions

- Reject `PRPS1_Superactivity.yaml` as an exact mapping.
- Add SLC16A1/HHF7 exercise-induced hyperinsulinism to the congenital
  hyperinsulinism curation backlog.
- Preserve IEMbase exercise-induced hypoglycemia, pyruvate-stimulated insulin
  secretion, syncope, ammonia-normal, and ketone/free-fatty-acid prompts.
