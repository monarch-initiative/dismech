# IEMbase 0687: NDUFS1-related NADH dehydrogenase iron-sulfur protein 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 687 |
| Nosology | 7.1.03.02 |
| Nosology code | IEM0415 |
| Gene | NDUFS1 |
| External IDs | OMIM:618226 for NDUFS1/MC1DN5; IEMbase source lists OMIM:618229; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX8A-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFS1 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS1-related NADH dehydrogenase
iron-sulfur protein 1 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 5.

The cached IEMbase record lists OMIM:618229, which appears to correspond to
NDUFV2/MC1DN7 rather than NDUFS1/MC1DN5. The scope table records the expected
NDUFS1/MC1DN5 identifier while preserving the source anomaly.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across all ages. Clinical rows include hypertrophic
cardiomyopathy, encephalopathy, hypotonia, liver dysfunction, myopathy, and
characteristic leukodystrophy and optic neuropathy.

## DisMech phenotype coverage

No exact NDUFS1 or MC1DN5 local target was identified.

`Leigh_Syndrome.yaml` provides broad complex I/Leigh context, and local complex
IV files model other respiratory-chain defects. There is no NDUFS1-specific
entry or subtype.

The generated `COX8A-Related_COX_Deficiency.yaml` candidate is a wrong-complex
match. COX8A is complex IV, while NDUFS1 is a complex I iron-sulfur subunit.

## Concordance and completeness

Judgement: true local gap.

The phenotype package combines complex I biochemical deficiency, lactate,
cardiac/myopathic disease, liver dysfunction, encephalopathy/hypotonia,
leukodystrophy, and optic neuropathy. Generic Leigh coverage is insufficient for
NDUFS1 completeness.

## Curation actions

- Add a dedicated NDUFS1/MC1DN5 target if curated.
- Reject COX8A-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, hypertrophic
  cardiomyopathy, myopathy, liver dysfunction, encephalopathy, hypotonia,
  leukodystrophy, and optic neuropathy.
