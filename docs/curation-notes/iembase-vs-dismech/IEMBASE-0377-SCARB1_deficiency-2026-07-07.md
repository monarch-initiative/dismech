# IEMbase 0377: SCARB1-related scavenger receptor B1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 377 |
| Nosology | 15.4.3.01 |
| Gene | SCARB1 |
| External IDs | OMIM:601040; OMIM:610762 |
| Generated mapping | UNMAPPED; low candidate `Triple_Negative_Breast_Cancer.yaml#Luminal Androgen Receptor (LAR) TNBC` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SCARB1-related scavenger receptor B1 deficiency, also listed
as SRB1 deficiency. Inheritance is listed as autosomal dominant and autosomal
recessive.

The cached record is sparse. It lists abnormal platelet function and
biochemical rows for serum cholesterol, plasma HDL cholesterol, and serum
triglyceride. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for SCARB1 deficiency. The generated low
candidate `Triple_Negative_Breast_Cancer.yaml#Luminal Androgen Receptor (LAR)
TNBC` is a false positive from weak lexical or biology-adjacent matching. The
TNBC file models an oncology subtype defined by absent ER/PR/HER2 expression
and tumor pathway biology, not SCARB1-mediated HDL handling or platelet
function.

General cardiovascular and lipid-metabolism files may provide downstream
context, but no curated SCARB1 deficiency disease entry is present.

## Concordance and completeness

Judgement: true local gap; reject the triple-negative breast cancer candidate.

The IEMbase disease is an inherited lipid/HDL receptor disorder involving
SCARB1, whereas the generated candidate is a breast cancer molecular subtype.
There is no meaningful disease-level concordance.

## Curation actions

- Keep this record unmapped until a SCARB1/SR-BI deficiency target exists.
- Do not map to `Triple_Negative_Breast_Cancer.yaml`.
- If curated, include inheritance heterogeneity, HDL cholesterol, serum
  cholesterol/triglyceride rows, and abnormal platelet function as review
  prompts.
