# IEMbase 0671: CRAT-related carnitine acetyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 671 |
| Nosology | 4.1.08.01 |
| Nosology code | IEM1167 |
| Gene | CRAT |
| External IDs | OMIM:606175 |
| Generated mapping | UNMAPPED; best candidate `Carnitine_Palmitoyltransferase_II_Deficiency.yaml` |
| Candidate DisMech targets | No exact CRAT target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CRAT-related carnitine acetyltransferase deficiency.

The record is clinical-only in this cached extract. Childhood features include
ataxia, consciousness disturbance, hypotonia, intellectual disability, and
oculomotor apraxia.

## DisMech phenotype coverage

No exact CRAT or carnitine acetyltransferase deficiency target was identified.

`Carnitine_Palmitoyltransferase_II_Deficiency.yaml` is a false target despite
the carnitine-related name. It models CPT2 long-chain fatty-acid oxidation and
the carnitine shuttle, including myopathic and severe neonatal/infantile CPT II
phenotypes. CRAT is a carnitine acetyltransferase/acetyl-CoA handling disorder
with a neurodevelopmental signal in IEMbase, not CPT II deficiency.

`Carnitine_Palmitoyltransferase_1A_Deficiency.yaml` contains only broad CPT1
isoform and population-genetics mentions that include CRAT; it is not disease
coverage for CRAT deficiency.

## Concordance and completeness

Judgement: true local gap.

The IEMbase phenotype package is neurologic and childhood-onset, with ataxia,
oculomotor apraxia, consciousness disturbance, hypotonia, and intellectual
disability. Existing CPT1A/CPT2 files should not be stretched to cover this
record.

## Curation actions

- Add a dedicated CRAT/carnitine acetyltransferase deficiency target if curated.
- Reject CPT II deficiency as exact coverage.
- Preserve ataxia and oculomotor apraxia as discriminating neurologic prompts.
- Source-review inheritance and biochemical markers before any KB import, since
  the cached IEMbase row has limited biochemical detail.
