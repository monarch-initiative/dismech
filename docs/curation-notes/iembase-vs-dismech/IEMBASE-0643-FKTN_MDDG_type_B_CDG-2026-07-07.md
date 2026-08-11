# IEMbase 0643: FKTN-related muscular dystrophy-dystroglycanopathy type B

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 643 |
| Nosology | 18.2.08.02 |
| Gene | FKTN |
| External IDs | OMIM:613152; ORPHA:272 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this row as autosomal recessive FKTN-CDG type B:
congenital muscular dystrophy-dystroglycanopathy without mental retardation.

The IEMbase phenotype signal is intentionally narrow. Biochemical rows include
markedly increased plasma creatine kinase in the neonatal, infancy, and
childhood periods and normal serum sialotransferrins in the same periods. The
only characteristic clinical rows are hypotonia and muscular dystrophy, both
present from neonatal life through childhood.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` includes `MDDG4 (FKTN)` and the type B severity
subtype. It captures the core alpha-dystroglycan glycosylation mechanism,
muscular dystrophy, elevated CK, and neonatal hypotonia.

However, the local type B description currently frames type B as congenital
muscular dystrophy with variable intellectual disability. That is appropriate
for the broader type B class but does not explicitly represent this IEMbase
row's "without mental retardation" phenotype emphasis.

## Concordance and completeness

Judgement: broad local coverage with a subtype nuance gap.

This is not a new disease-family gap: FKTN and type B dystroglycanopathy are
already represented. The gap is that DisMech does not distinguish the FKTN type
B row from other type B dystroglycanopathies and does not explicitly preserve
the IEMbase assertion that this congenital muscular dystrophy form lacks
intellectual disability.

## Curation actions

- Map broadly to `Dystroglycanopathy.yaml`.
- If row-level coverage is needed, add FKTN type B / MDDG B4 detail or a note
  under the FKTN subtype.
- Preserve the narrow phenotype signal: CK elevation, normal
  sialotransferrins, neonatal-childhood hypotonia, muscular dystrophy, and the
  "without intellectual disability" distinction.
