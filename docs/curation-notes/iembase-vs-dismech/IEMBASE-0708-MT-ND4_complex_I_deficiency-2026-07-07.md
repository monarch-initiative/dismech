# IEMbase 0708: MT-ND4-related NADH dehydrogenase core subunit 4 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 708 |
| Nosology | 6.1.21.01 |
| Nosology code | IEM0433 |
| Gene | MT-ND4 |
| External IDs | OMIM:252010; ORPHA:99718 |
| Generated mapping | UNMAPPED; weak generated candidate to `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact MT-ND4 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents maternally inherited MT-ND4-related NADH dehydrogenase core
subunit 4 deficiency. The cached source label lacks a space between
"related" and "NADH"; preserve this as a source-label cleanup issue rather than
as a biological distinction.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across all age windows. Clinical rows include childhood-to-adult
dystonia, adolescent/adult Leber hereditary optic neuropathy, and adult
MELAS-like features. The characteristic clinical row lists Leigh syndrome
across all age windows.

## DisMech phenotype coverage

No exact MT-ND4 local target was identified.

`Leigh_Syndrome.yaml` provides broad context for mtDNA complex I-related Leigh
syndrome, and `MELAS_Syndrome.yaml` provides mitochondrial-gene MELAS context
focused most explicitly on MT-ND5. Neither entry models MT-ND4 as a specific
complex I deficiency target. No exact local LHON target was identified.

The weak generated `Pyruvate_Dehydrogenase_Deficiency.yaml` candidate is not
exact coverage.

## Concordance and completeness

Judgement: true local gap with broad mitochondrial syndrome overlap only.

The IEMbase row combines complex I biochemical deficiency with Leigh, LHON,
dystonia, and adult MELAS-like features. Local syndrome entries provide useful
context but not MT-ND4 disease-level completeness.

## Curation actions

- Add a dedicated MT-ND4 complex I deficiency target if curated.
- Reject pyruvate dehydrogenase deficiency as exact coverage.
- Preserve the source-label spacing anomaly for cleanup.
- Preserve decreased complex I activity, increased lactate, dystonia, LHON,
  adult MELAS-like features, and Leigh syndrome.
