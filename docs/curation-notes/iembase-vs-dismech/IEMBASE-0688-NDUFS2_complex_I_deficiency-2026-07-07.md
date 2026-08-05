# IEMbase 0688: NDUFS2-related NADH dehydrogenase iron-sulfur protein 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 688 |
| Nosology | 7.1.04.02 |
| Nosology code | IEM0416 |
| Gene | NDUFS2 |
| External IDs | OMIM:618228; ORPHA:70474 |
| Generated mapping | CANDIDATE to `COX4I1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFS2 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS2-related NADH dehydrogenase
iron-sulfur protein 2 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 6.

Biochemical rows include decreased fibroblast complex I activity and increased
plasma lactate across all ages. Clinical rows include encephalopathy, hypotonia,
Leigh syndrome, liver dysfunction, parkinsonism, and characteristic hypertrophic
cardiomyopathy and myopathy.

## DisMech phenotype coverage

No exact NDUFS2 or MC1DN6 local target was identified.

`Leigh_Syndrome.yaml` overlaps at the syndrome level but does not capture this
gene-specific complex I subunit disease. The generated `COX4I1-Related_COX_Deficiency.yaml`
candidate is a complex IV regulatory-subunit disorder, not NDUFS2-related
complex I disease.

## Concordance and completeness

Judgement: true local gap.

The IEMbase row should be kept distinct from complex IV deficiency and from
generic Leigh syndrome, especially because it includes liver dysfunction,
parkinsonism, myopathy, and hypertrophic cardiomyopathy.

## Curation actions

- Add a dedicated NDUFS2/MC1DN6 target if curated.
- Reject COX4I1-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, encephalopathy,
  hypotonia, Leigh syndrome, liver dysfunction, parkinsonism, hypertrophic
  cardiomyopathy, and myopathy.
