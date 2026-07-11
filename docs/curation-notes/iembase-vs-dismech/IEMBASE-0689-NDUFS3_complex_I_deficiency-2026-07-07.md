# IEMbase 0689: NDUFS3-related NADH dehydrogenase iron-sulfur protein 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 689 |
| Nosology | 7.1.05.02 |
| Nosology code | IEM0417 |
| Gene | NDUFS3 |
| External IDs | OMIM:256000; OMIM:252010; ORPHA:255241 |
| Generated mapping | CANDIDATE to `TACO1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFS3 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFS3-related NADH dehydrogenase
iron-sulfur protein 3 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 8.

The cached IEMbase record lists OMIM:256000 and OMIM:252010. The latter appears
to correspond to NDUFS4/MC1DN1 rather than NDUFS3/MC1DN8, so it should be
source-reviewed before downstream use as an NDUFS3-specific identifier.

The biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate from the neonatal period through childhood. Clinical rows include
developmental delay, encephalopathy, Leigh syndrome, and characteristic myopathy
through adolescence.

## DisMech phenotype coverage

No exact NDUFS3 or MC1DN8 local target was identified.

`Leigh_Syndrome.yaml` provides broad syndrome-level context. The generated
`TACO1-Related_COX_Deficiency.yaml` candidate is a complex IV translation/COX
deficiency and should not be accepted as coverage for an NDUFS3 complex I
subunit disorder.

## Concordance and completeness

Judgement: true local gap.

The row is compact but still needs gene-specific treatment as an NDUFS3 complex
I disease with lactate elevation, developmental delay, encephalopathy, Leigh
syndrome, and myopathy.

## Curation actions

- Add a dedicated NDUFS3/MC1DN8 target if curated.
- Reject TACO1-related complex IV deficiency as exact coverage.
- Preserve decreased complex I activity, increased lactate, developmental delay,
  encephalopathy, Leigh syndrome, and myopathy.
