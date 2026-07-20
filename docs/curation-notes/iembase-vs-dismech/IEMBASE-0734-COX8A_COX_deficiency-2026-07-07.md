# IEMbase 0734: COX8A-related cytochrome c oxidase subunit 8A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 734 |
| Nosology | 7.4.08.01 |
| Nosology code | IEM1145 |
| Gene | COX8A |
| External IDs | OMIM:619059; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX8A-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COX8A-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX8A-related cytochrome c oxidase
subunit 8A deficiency. The cached phenotype rows include childhood/adolescent
epilepsy, microcephaly across neonatal through adolescent windows,
developmental delay across all age windows, and neonatal/infantile pulmonary
hypertension.

## DisMech phenotype coverage

DisMech has exact local coverage in `COX8A-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 15
(MONDO:0033650) and describes biallelic COX8A splice disruption as loss of the
smallest nuclear-encoded structural subunit of complex IV, destabilizing the
holoenzyme.

Local phenotype coverage includes severe drug-resistant epilepsy and
leukodystrophy in a Leigh-like syndrome.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COX8A-Related_COX_Deficiency.yaml`.

The IEMbase and local records align on COX8A, autosomal recessive complex IV
structural-subunit disease, and epilepsy. IEMbase adds microcephaly,
developmental delay, and pulmonary hypertension prompts, while DisMech captures
leukodystrophy, Leigh-like framing, and the structural-subunit destabilization
mechanism.

## Curation actions

- Resolve IEMbase 734 to `COX8A-Related_COX_Deficiency.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Consider reviewing local COX8A phenotypes for microcephaly, developmental
  delay, and pulmonary hypertension.
- Preserve local leukodystrophy and Leigh-like syndrome context.
