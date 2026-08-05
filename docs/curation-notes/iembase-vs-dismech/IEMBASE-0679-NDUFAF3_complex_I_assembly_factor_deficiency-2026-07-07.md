# IEMbase 0679: NDUFAF3-related complex I assembly factor 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 679 |
| Nosology | 7.1.03.01 |
| Nosology code | IEM0439 |
| Gene | NDUFAF3 |
| External IDs | OMIM:618240; ORPHA:70474 |
| Generated mapping | CANDIDATE to `COX6A2-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFAF3 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF3-related complex I assembly factor
3 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 18.

The cached phenotype signal is severe neonatal/infantile mitochondrial disease:
decreased fibroblast complex I activity, characteristic increased plasma
lactate, hypotonia, diffuse leukomalacia, respiratory failure, perinatal death,
and characteristic optic atrophy.

## DisMech phenotype coverage

No exact NDUFAF3 or MC1DN18 local target was identified.

`Leigh_Syndrome.yaml` and other broad mitochondrial entries provide generic
complex I/oxidative phosphorylation context but do not model the NDUFAF3 disease
entity or its severe neonatal leukomalacia/perinatal-death phenotype.

The generated `COX6A2-Related_COX_Deficiency.yaml` candidate is a complex IV
structural-subunit disorder and should be rejected as exact coverage.

## Concordance and completeness

Judgement: true local gap.

The IEMbase row is compact but specific: early lethal complex I assembly-factor
disease with lactate elevation, respiratory failure, optic atrophy, and diffuse
leukomalacia. A complex IV myopathy/COX candidate does not cover this record.

## Curation actions

- Add a dedicated NDUFAF3/MC1DN18 target if curated.
- Reject COX6A2-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased lactate, diffuse
  leukomalacia, respiratory failure, perinatal death, hypotonia, and optic
  atrophy.
- Use broad Leigh/complex I context only as background.
