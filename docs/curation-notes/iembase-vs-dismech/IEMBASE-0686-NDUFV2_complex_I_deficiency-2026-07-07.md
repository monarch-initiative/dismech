# IEMbase 0686: NDUFV2-related NADH dehydrogenase flavoprotein 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 686 |
| Nosology | 7.1.02.02 |
| Nosology code | IEM0414 |
| Gene | NDUFV2 |
| External IDs | OMIM:618229; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX6B1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFV2 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFV2-related NADH dehydrogenase
flavoprotein 2 deficiency, also labeled mitochondrial complex I deficiency,
nuclear type 7.

The biochemical row shows decreased fibroblast complex I activity across all
ages. Clinical rows include Leigh syndrome, leukodystrophy, liver dysfunction,
myopathy, optic neuropathy, parkinsonism, and characteristic hypertrophic
cardiomyopathy.

## DisMech phenotype coverage

No exact NDUFV2 or MC1DN7 local target was identified.

`Leigh_Syndrome.yaml` provides broad complex I/Leigh context but does not model
NDUFV2 or the combination of leukodystrophy, liver dysfunction, optic neuropathy,
parkinsonism, myopathy, and hypertrophic cardiomyopathy.

The generated `COX6B1-Related_COX_Deficiency.yaml` candidate is a complex IV
deficiency and should be rejected as exact coverage.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase row has several non-generic prompts that are not guaranteed by a
generic Leigh mapping, especially leukodystrophy, optic neuropathy,
parkinsonism, liver dysfunction, and hypertrophic cardiomyopathy.

## Curation actions

- Add a dedicated NDUFV2/MC1DN7 target if curated.
- Reject COX6B1-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, Leigh syndrome, leukodystrophy, liver
  dysfunction, myopathy, optic neuropathy, parkinsonism, and hypertrophic
  cardiomyopathy.
