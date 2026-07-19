# IEMbase 0732: COX6B1-related cytochrome c oxidase subunit 6B1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 732 |
| Nosology | 7.4.06.02 |
| Nosology code | IEM0467 |
| Gene | COX6B1 |
| External IDs | OMIM:220110; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX6B1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COX6B1-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX6B1-related cytochrome c oxidase
subunit 6B1 deficiency. The cached rows include increased plasma lactate across
age windows, possible neonatal/infantile/childhood cardiomyopathy and
encephalopathy, childhood leukodystrophy, childhood/adolescent myopathy, and
possible childhood epilepsy.

## DisMech phenotype coverage

DisMech has exact local coverage in `COX6B1-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 7
(MONDO:0033637) and describes biallelic COX6B1 variants as loss of a
nuclear-encoded structural subunit of complex IV.

Local phenotype coverage includes severe infantile encephalomyopathy,
hydrocephalus, and hypertrophic cardiomyopathy, with the structural-subunit
mechanism and reduced COX activity captured in detail.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COX6B1-Related_COX_Deficiency.yaml`.

The IEMbase and local records align on COX6B1, autosomal recessive complex IV
structural-subunit disease, encephalopathy, and cardiomyopathy. IEMbase adds
age-banded lactate, leukodystrophy, myopathy, and epilepsy prompts, while
DisMech adds hydrocephalus and stronger mechanism/evidence context.

## Curation actions

- Resolve IEMbase 732 to `COX6B1-Related_COX_Deficiency.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Consider reviewing local COX6B1 phenotypes for lactate elevation,
  leukodystrophy, myopathy, and epilepsy.
- Preserve local hydrocephalus and structural-subunit mechanism detail.
