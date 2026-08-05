# IEMbase 0736: MT-CO2-related cytochrome c oxidase subunit 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 736 |
| Nosology | 6.1.02.01 |
| Nosology code | IEM0463 |
| Gene | MT-CO2 |
| External IDs | OMIM:516040; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX4I1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact MT-CO2 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents mitochondrial MT-CO2-related cytochrome c oxidase subunit 2
deficiency, under the mtDNA-encoded oxidative phosphorylation protein subgroup.
The cached phenotype rows include plasma lactate elevation from neonatal life
through adulthood, childhood cardiomyopathy and developmental delay as possible
features, persistent myopathy from infancy through adulthood, possible childhood
retinopathy, and muscle weakness across all age bands.

## DisMech phenotype coverage

No exact MT-CO2 disease target was identified locally.

The generated `COX4I1-Related_COX_Deficiency.yaml` candidate is a different
complex IV structural-subunit disease: it models a nuclear COX4I1 defect rather
than a mitochondrially encoded COX2/MT-CO2 disorder. Local complex IV module and
grouping content mention mtDNA-encoded COX subunits as pathway context, and
`COX18-Related_COX_Deficiency.yaml` is mechanistically adjacent through COX2
membrane insertion, but neither is exact disease coverage.

## Concordance and completeness

Judgement: true local MT-CO2 complex IV gap. Reject the COX4I1 candidate as
exact coverage.

IEMbase supplies a compact phenotype seed for a future MT-CO2 entry: chronic
lactate elevation, myopathy and weakness, plus possible cardiomyopathy,
developmental delay, and retinopathy. DisMech has the reusable complex IV
mechanism context, but not the mtDNA-encoded COX2 disease identity.

## Curation actions

- Add a dedicated MT-CO2 cytochrome c oxidase subunit 2 deficiency target if
  curated.
- Reject `COX4I1-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve age-banded lactate, myopathy, muscle weakness, cardiomyopathy,
  developmental-delay, and retinopathy prompts.
