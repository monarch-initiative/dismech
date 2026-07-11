# IEMbase 0102: MAOA-related monoamine oxidase A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 102 |
| Nosology | 23.1.04.01 |
| Gene | MAOA |
| External IDs | OMIM:309850 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None; fuzzy candidate `Chronic_Granulomatous_Disease.yaml` is not valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as MAOA-related monoamine oxidase A deficiency, with
alternate labels Brunner syndrome and MAO-A. Treatability is marked yes, but the
cached JSON has no treatment rows and no clinical phenotype rows.

The biochemical rows are increased urinary 3-methoxytyramine, decreased CSF
5-HIAA, decreased CSF and urinary homovanillic acid, increased urinary
normetanephrine, decreased urinary VMA, and decreased fibroblast MAO-A activity.

## DisMech phenotype coverage

There is no valid local MAOA deficiency or Brunner syndrome target. The
generated fuzzy candidate `Chronic_Granulomatous_Disease.yaml` is unrelated.

MAOA deficiency is also not just another subtype of the existing catecholamine
synthesis umbrella. It is primarily a monoamine degradation/catabolism disorder,
whereas the current `Disorder_of_Catecholamine_Synthesis.yaml` entry models
defective synthesis or related cofactor/chaperone biology.

## Concordance and completeness

Judgement: true local gap with sparse IEMbase clinical content.

IEMbase captures a useful monoamine-metabolite signature and the reduced MAO-A
activity row, but it does not provide the behavioral/developmental phenotype
surface in this cached record. DisMech currently has no disease or umbrella
entry that should absorb this record without a new monoamine catabolism scope
decision.

## Curation actions

- Leave unmapped until a MAOA deficiency / Brunner syndrome entry or a
  monoamine catabolism grouping is curated.
- Do not map to chronic granulomatous disease or to the catecholamine-synthesis
  umbrella without an explicit scope expansion.
- If curated, start with the biochemical readouts plus independently sourced
  neurobehavioral phenotype evidence, because IEMbase clinical rows are empty.
