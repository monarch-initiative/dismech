# IEMbase 0660: ACOX2-related congenital bile acid synthesis defect

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 660 |
| Nosology | 14.8.06.02 |
| Nosology code | IEM0784 |
| Gene | ACOX2 |
| External IDs | OMIM:617308 |
| Generated mapping | MAPPED to `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` |
| Candidate DisMech targets | Broad bile-acid umbrella only; no exact ACOX2 subtype found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ACOX2-related congenital bile acid
synthesis defect, abbreviated CBAS6.

Biochemical rows include low-to-normal plasma C24 bile acid, increased plasma
and urinary C27 bile acid, normal-to-increased ASAT/ALAT and transaminase, low
serum cholesterol, low plasma 25-hydroxyvitamin D, and normal serum pristanic
acid. Clinical rows include optional childhood ataxia, cognitive dysfunction,
liver fibrosis, and steatorrhea, plus optional adolescent cholestasis.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` is the correct broad disease-family
context. It covers deficient primary bile acid production, toxic C27 bile-acid
intermediate accumulation, cholestasis, progressive liver injury, steatorrhea,
fat-soluble vitamin malabsorption, and neurologic involvement in selected
subtypes.

The local umbrella entry does not currently define an ACOX2/CBAS6 subtype. Its
subtype list focuses on HSD3B7, AKR1D1, CYP7B1, AMACR, CYP27A1, BAAT, and
related disorders. Therefore, the generated mapping is biologically relevant but
not complete at the gene-specific row level.

## Concordance and completeness

Judgement: broad family-level coverage only; exact ACOX2/CBAS6 coverage remains
a local gap.

DisMech captures the general bile-acid synthesis logic and several IEMbase
phenotypes, especially C27 bile-acid accumulation, cholestasis, steatorrhea, and
fat-soluble vitamin deficiency. It does not preserve ACOX2 as the causal gene,
the C24-versus-C27 bile-acid contrast, normal pristanic acid, low cholesterol,
or the childhood/adolescent age-banded neurologic and hepatic prompts.

## Curation actions

- Keep `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` as broad context, not exact
  ACOX2 subtype coverage.
- Consider adding an ACOX2/CBAS6 subtype or separate disease entry after source
  review.
- Preserve C24/C27 bile-acid directionality, transaminases, cholesterol,
  25-hydroxyvitamin D, pristanic acid, ataxia, cognitive dysfunction,
  steatorrhea, cholestasis, and liver-fibrosis prompts.
