# IEMbase 0710: MT-ND5-related NADH dehydrogenase core subunit 5 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 710 |
| Nosology | 6.1.23.01 |
| Nosology code | IEM0435 |
| Gene | MT-ND5 |
| External IDs | OMIM:252010; ORPHA:255210 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Partial MT-ND5 context in `Leigh_Syndrome.yaml` and `MELAS_Syndrome.yaml`; no exact MT-ND5 complex I deficiency target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents maternally inherited MT-ND5-related NADH dehydrogenase core
subunit 5 deficiency.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate across all age windows. Clinical rows include childhood-to-adult
Leber hereditary optic neuropathy, infantile-to-adult Leigh syndrome,
MELAS-like features, source-spelled "MERFF-like syndrome", and renal failure.
The characteristic clinical row adds infantile-to-adult myopathy.

## DisMech phenotype coverage

There is meaningful but incomplete local context for MT-ND5.

`Leigh_Syndrome.yaml` lists MT-ND5 in its complex I deficiency section and
models broad complex I-related Leigh syndrome. `MELAS_Syndrome.yaml` has an
`MT-ND5 and other genes` subtype and a genetic entry for MT-ND5 and other
mitochondrial-gene variants. Those entries support MT-ND5 as a contributor to
Leigh/MELAS-spectrum disease.

However, no exact MT-ND5 complex I deficiency target was identified, and no
local entry fully covers the IEMbase package of LHON, Leigh, MELAS-like,
MERRF/MERFF-like, renal failure, myopathy, lactate, and decreased complex I
activity.

## Concordance and completeness

Judgement: partial syndrome/gene context only; exact MT-ND5 disease target is
missing.

This is stronger than the other MT-ND rows because MT-ND5 is explicitly present
in local Leigh and MELAS entries, but those entries are not a complete
standalone MT-ND5 complex I deficiency mapping.

## Curation actions

- Keep `Leigh_Syndrome.yaml` and `MELAS_Syndrome.yaml` as partial MT-ND5
  context.
- Add a dedicated MT-ND5 complex I deficiency target or subtype if curated.
- Preserve decreased complex I activity, increased lactate, LHON, Leigh
  syndrome, MELAS-like features, the source "MERFF-like" spelling for review,
  renal failure, and myopathy.
