# IEMbase 0680: NDUFAF4-related complex I assembly factor 4 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 680 |
| Nosology | 7.1.04.01 |
| Nosology code | IEM0440 |
| Gene | NDUFAF4 |
| External IDs | OMIM:618237; ORPHA:2609 |
| Generated mapping | CANDIDATE to `COX8A-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFAF4 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF4-related complex I assembly factor
4 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 15.

The biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate in neonatal and infantile periods. Clinical rows include Leigh
syndrome, characteristic cardiomyopathy, and characteristic encephalomyopathy.

## DisMech phenotype coverage

No exact NDUFAF4 or MC1DN15 local target was identified.

`Leigh_Syndrome.yaml` provides broad syndrome context for complex I deficiency,
lactic acidosis, basal ganglia vulnerability, and cardiomyopathy-associated
Leigh presentations. It does not identify NDUFAF4 or the MC1DN15 disease entity.

The generated `COX8A-Related_COX_Deficiency.yaml` candidate is a wrong-complex
match. COX8A is a complex IV structural-subunit deficiency and should not be
used for NDUFAF4-related complex I assembly failure.

## Concordance and completeness

Judgement: true local gap with broad Leigh context only.

The core IEMbase package is neonatal/infantile complex I enzyme deficiency with
lactate elevation, Leigh syndrome, encephalomyopathy, and cardiomyopathy.

## Curation actions

- Add a dedicated NDUFAF4/MC1DN15 target if curated.
- Reject COX8A-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased lactate, Leigh
  syndrome, encephalomyopathy, and cardiomyopathy.
- Avoid treating generic Leigh syndrome as gene-specific completeness.
