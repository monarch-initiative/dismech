# IEMbase 0700: NDUFA12-related NADH dehydrogenase alpha subcomplex subunit 12 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 700 |
| Nosology | 7.1.14.01 |
| Nosology code | IEM0426 |
| Gene | NDUFA12 |
| External IDs | OMIM:618244; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX11-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA12 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA12-related NADH dehydrogenase alpha
subcomplex subunit 12 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 23.

The biochemical row shows decreased fibroblast complex I activity through
childhood. Clinical rows include growth retardation, Leigh syndrome,
psychomotor retardation, dystonia, and hypotonia.

## DisMech phenotype coverage

No exact NDUFA12 or MC1DN23 local target was identified.

`Leigh_Syndrome.yaml` covers the broad syndrome-level features: Leigh syndrome,
complex I deficiency context, dystonia/movement disorder, hypotonia, and
developmental impairment. It does not include NDUFA12 as a modeled causal gene.

The generated `COX11-Related_COX_Deficiency.yaml` candidate is a complex IV
copper-delivery disorder. It shares the nuclear-type number 23 but belongs to
MC4DN23 rather than MC1DN23.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase record is a sparse but specific NDUFA12 complex I disease. Generic
Leigh syndrome can provide context, but the COX11 candidate is a wrong-complex
number collision and should not be accepted as disease-level coverage.

## Curation actions

- Add a dedicated NDUFA12/MC1DN23 target if curated.
- Reject COX11-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, growth retardation, Leigh
  syndrome, psychomotor retardation, dystonia, and hypotonia.
