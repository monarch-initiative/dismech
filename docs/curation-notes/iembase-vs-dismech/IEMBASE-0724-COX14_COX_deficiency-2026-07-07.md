# IEMbase 0724: COX14-related cytochrome c oxidase assembly factor 14 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 724 |
| Nosology | 7.4.15.01 |
| Nosology code | IEM1148 |
| Gene | COX14 |
| External IDs | OMIM:220110; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX14-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COX14-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX14-related cytochrome c oxidase
assembly factor 14 deficiency. The cached rows include increased plasma lactate
in neonatal and infantile windows, neonatal lactic acidosis, neonatal perinatal
death, and neonatal cardiomyopathy.

## DisMech phenotype coverage

DisMech has exact local coverage in `COX14-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 10
(MONDO:0033639) and describes biallelic COX14/C12orf62 loss as failure to
coordinate COX I synthesis with early complex IV assembly.

Local phenotypes include severe congenital lactic acidosis and dysmorphic
facial features, with a fatal neonatal course captured in the description and
mechanistic narrative.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COX14-Related_COX_Deficiency.yaml`.

The records align on COX14, autosomal recessive complex IV assembly failure,
neonatal onset, lactate/lactic acidosis, and fatal severity. IEMbase adds
explicit cardiomyopathy and perinatal-death phenotype rows, while DisMech is
stronger for COX I assembly coupling and dysmorphology.

## Curation actions

- Resolve IEMbase 724 to `COX14-Related_COX_Deficiency.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Consider reviewing local COX14 phenotypes for explicit cardiomyopathy and
  perinatal death.
- Preserve local mechanism detail on COX I synthesis and early complex IV
  assembly.
