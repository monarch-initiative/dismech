# IEMbase 0537: SUGCT-related glutaric aciduria type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 537 |
| Nosology | 1.2.06.01 |
| Gene | SUGCT |
| External IDs | OMIM:231690; ORPHA:35706 |
| Generated mapping | CANDIDATE; fuzzy alias match to `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SUGCT-related succinate-hydroxymethylglutarate-CoA
transferase deficiency, with glutaric aciduria type 3 and GA3 as alternate
labels. The record is autosomal recessive, subtype is marked benign form, and
no treatments are listed.

The biochemical signal is increased glutaric acid in plasma and urine with
normal urinary 3-hydroxyglutaric acid. The clinical row is no clinical
significance.

## DisMech phenotype coverage

The generated `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` candidate is a false
positive caused by glutaric-aciduria vocabulary overlap. The local file is
GCDH-related glutaric aciduria type 1, a lysine/tryptophan catabolism disorder
with neurotoxic glutaric and 3-hydroxyglutaric acid accumulation, striatal
injury risk, dystonia, newborn-screening context, and metabolic treatment.

No local file was found for SUGCT, glutaric aciduria type 3, or
succinate-hydroxymethylglutarate-CoA transferase deficiency.

## Concordance and completeness

Judgement: true local gap; reject the glutaric aciduria type 1 candidate.

This IEMbase record is specifically SUGCT/GA3 and is marked benign with normal
3-hydroxyglutaric acid and no clinical significance. That is mechanistically and
clinically distinct from GCDH/GA1.

## Curation actions

- Keep this record unmapped until a SUGCT / glutaric aciduria type 3 target
  exists.
- Do not map to `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml`.
- Preserve the benign-form scope, increased plasma/urine glutaric acid, normal
  urinary 3-hydroxyglutaric acid, and no-clinical-significance row.
