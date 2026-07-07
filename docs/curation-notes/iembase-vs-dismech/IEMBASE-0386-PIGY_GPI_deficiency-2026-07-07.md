# IEMbase 0386: PIGY-related Phosphatidylinositolglycan, class V, deficiency (CDG)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 386 |
| Nosology | 18.3.00.25 |
| Gene | PIGY |
| External IDs | OMIM:239300; ORPHA:247262 |
| Generated mapping | UNMAPPED; low candidate `CHIME_syndrome.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PIGY-related
phosphatidylinositolglycan, class V, deficiency, also listed as PIGY-CDG and
hyperphosphatasia-mental retardation syndrome 1.

Clinical rows include brachytelephalangy, epilepsy, intellectual disability,
and large fleshy earlobes. The biochemical signal is increased plasma alkaline
phosphatase. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for PIGY-related GPI-anchor deficiency.
The generated candidate `CHIME_syndrome.yaml` is a pathway-neighbor false
positive: local CHIME syndrome is PIGL-related and models colobomas, heart
defects, ichthyosiform dermatosis, intellectual disability, and ear anomalies
from a different GPI-anchor biosynthesis gene.

CHIME syndrome may provide general GPI-anchor deficiency context, but it should
not be used as a disease-level mapping for PIGY-CDG or the
hyperphosphatasia/intellectual-disability phenotype represented here.

## Concordance and completeness

Judgement: true PIGY local gap; reject the CHIME/PIGL candidate.

The IEMbase and candidate files share broad GPI-anchor biology and partial
neurodevelopmental overlap, but the causal gene, named syndrome, and core
clinical/biochemical signals differ.

## Curation actions

- Keep this record unmapped until a PIGY-CDG/GPI-anchor deficiency target
  exists.
- Do not map to `CHIME_syndrome.yaml`.
- If curated, include intellectual disability, epilepsy, brachytelephalangy,
  large fleshy earlobes, and elevated alkaline phosphatase as review prompts.
