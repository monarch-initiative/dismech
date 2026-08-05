# IEMbase 0597: HAO1-related hydroxyacid oxidase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 597 |
| Nosology | 13.1.03.01 |
| Gene | HAO1 |
| External IDs | OMIM:605023 |
| Generated mapping | UNMAPPED; best candidate `TACO1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `HAO1-Related_Glycolate_Oxidase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents HAO1-related hydroxyacid oxidase 1 deficiency, with alternate
labels glycolate oxidase 1 deficiency, isolated glycolic aciduria, and GOX. The
record is autosomal recessive, classified under disorders of glyoxylate and
oxalate metabolism, has unknown treatability, and has no treatment rows.

Biochemical rows include normal urinary citric acid, normal-to-very-increased
urinary oxalic acid, normal urinary glyceric acid, and very increased urinary
glycolic acid. Clinical rows include achalasia, nephrolithiasis, psychomotor
delay, alacrima, and anisocoria.

## DisMech phenotype coverage

`HAO1-Related_Glycolate_Oxidase_Deficiency.yaml` is the correct local target.
It models autosomal recessive HAO1/glycolate oxidase deficiency, impaired
hepatic glyoxylate precursor metabolism, isolated hyperglycolic aciduria,
normal oxalate/citrate/glycerate in the index family, and a cautious knowledge
gap around whether hyperoxaluria is ever a direct HAO1 consequence.

`TACO1-Related_COX_Deficiency.yaml` is a false-positive generated candidate
from mitochondrial/organic-acid neighborhood signals. It models TACO1-related
Complex IV deficiency and Leigh syndrome, not HAO1/glyoxylate metabolism.

## Concordance and completeness

Judgement: generated false negative; resolve to
`HAO1-Related_Glycolate_Oxidase_Deficiency.yaml`.

IEMbase and DisMech agree on HAO1 identity, autosomal recessive inheritance,
glycolate oxidase deficiency, isolated glycolic aciduria, very high urinary
glycolic acid, and normal glycerate/citrate. IEMbase adds urinary oxalate and
nephrolithiasis prompts that overlap with the local knowledge gap, but the
local entry is more cautious: it treats hyperoxaluria as observed in one case
and not yet proven as a general downstream consequence.

The IEMbase achalasia, alacrima, anisocoria, and psychomotor-delay rows are not
obvious consequences of the local HAO1 mechanism and should be source-reviewed
before import.

## Curation actions

- Promote this record to `HAO1-Related_Glycolate_Oxidase_Deficiency.yaml`.
- Reject `TACO1-Related_COX_Deficiency.yaml` as an exact mapping.
- Preserve urinary oxalate and nephrolithiasis as source-review prompts tied to
  the existing HAO1 hyperoxaluria knowledge gap.
- Source-review achalasia, alacrima, anisocoria, and psychomotor-delay rows
  before adding them to DisMech.
