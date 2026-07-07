# IEMbase 0474: GALK1-related galactokinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 474 |
| Nosology | 3.1.03.01 |
| Gene | GALK1 |
| External IDs | OMIM:230200; ORPHA:79237 |
| Generated mapping | UNMAPPED; low candidate `Galactosemia.yaml` |
| Candidate DisMech targets | `Galactosemia.yaml#Galactokinase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GALK1-related galactokinase deficiency,
also called galactosemia type 2. Biochemical rows include decreased
galactokinase activity in fibroblasts and red blood cells, normal erythrocyte
GALT activity, increased plasma and urine galactose, increased urine
galactitol, urine reducing substances, normal erythrocyte galactose-1-phosphate,
and neonatal or infantile plasma glucose that is low-to-normal. Clinical rows
include cataract and pseudotumor cerebri. IEMbase records
galactose-restricted and lactose-free diet as a nutritional treatment.

## DisMech phenotype coverage

`Galactosemia.yaml#Galactokinase Deficiency` is the correct local target. The
local Galactosemia entry explicitly includes a galactokinase deficiency subtype
caused by GALK1 deficiency, with decreased galactokinase activity, disrupted
galactose catabolism, excess galactose conversion to galactitol, lens toxicity,
and cataract.

## Concordance and completeness

Judgement: false negative; resolve IEMbase 474 to
`Galactosemia.yaml#Galactokinase Deficiency`.

The local target captures the entity, gene, Leloir-pathway step, galactitol-lens
mechanism, and cataract endpoint. IEMbase adds useful biochemical and clinical
prompts not yet fully represented locally, including normal GALT activity,
normal galactose-1-phosphate, explicit urine/plasma galactose rows,
galactose-restricted diet, and pseudotumor cerebri.

## Curation actions

- Map IEMbase 474 to `Galactosemia.yaml#Galactokinase Deficiency`.
- If importing IEMbase-derived prompts, verify diet response, normal
  erythrocyte GALT activity, normal erythrocyte galactose-1-phosphate, urinary
  reducing substances, and pseudotumor cerebri against source evidence.
