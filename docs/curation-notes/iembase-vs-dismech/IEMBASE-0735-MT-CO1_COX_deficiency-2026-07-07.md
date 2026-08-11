# IEMbase 0735: MT-CO1-related cytochrome c oxidase subunit 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 735 |
| Nosology | 6.1.01.01 |
| Nosology code | IEM0462 |
| Gene | MT-CO1 |
| External IDs | OMIM:516030; ORPHA:99845 |
| Generated mapping | UNMAPPED; weak candidate `COX4I1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact MT-CO1 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MT-CO1-related cytochrome c oxidase subunit 1 deficiency.
The cached rows include normal-to-high plasma alanine in adulthood,
adult-onset rhabdomyolysis, adolescent/adult stroke-like episodes, epilepsy,
and muscle weakness.

The source inheritance field says autosomal recessive, which is incongruent
with MT-CO1 being an mtDNA-encoded gene and should be reviewed before any
future KB modeling.

## DisMech phenotype coverage

No exact MT-CO1 local target was identified.

The generated `COX4I1-Related_COX_Deficiency.yaml` candidate is a nuclear
COX4I1 structural-subunit disease, not a mitochondrially encoded COX1/MT-CO1
disorder. Local complex IV module and grouping content mention mtDNA-encoded
COX subunits as pathway context, but that is not exact disease coverage.

## Concordance and completeness

Judgement: true local MT-CO1 complex IV gap. The COX4I1 candidate should be
rejected as exact coverage.

The IEMbase row points to an mtDNA-encoded core subunit disease with adult
myopathic and stroke-like features. COX4I1 is a different nuclear-encoded
structural/regulatory subunit with distinct genetics and local phenotype scope.

## Curation actions

- Add a dedicated MT-CO1 cytochrome c oxidase subunit 1 deficiency target if
  curated.
- Reject `COX4I1-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve normal-to-high alanine, rhabdomyolysis, stroke-like episodes,
  epilepsy, and muscle weakness.
- Review the source inheritance field before modeling this mtDNA-encoded
  disease.
