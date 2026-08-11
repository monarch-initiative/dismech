# IEMbase 0124: H6PD-related Hexose-6-phosphate dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 124 |
| Nosology | 24.2.1.01 |
| Gene | H6PD |
| External IDs | OMIM:604931; ORPHA:168588 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Cortisone_Reductase_Deficiency.yaml#Apparent CRD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as H6PD-related hexose-6-phosphate dehydrogenase
deficiency, with alternate labels cortisone reductase deficiency type 1 and
CRD. Treatability is marked unknown.

The characteristic biochemical rows include increased ACTH, increased adrenal
androgens, increased androstenedione, and a decreased urinary
tetrahydrocortisol/tetrahydrocortisone ratio. Clinical rows include adrenal
hyperplasia, precocious pseudopuberty in 46,XY individuals, and signs of
androgen excess in women such as hirsutism. No treatment rows are listed.

## DisMech phenotype coverage

`Cortisone_Reductase_Deficiency.yaml` includes an `Apparent CRD` subtype for
H6PD variants that reduce endoplasmic-reticulum NADPH supply for 11-beta-HSD1
oxoreductase activity. The local entry describes impaired cortisone-to-cortisol
regeneration, increased HPA drive, adrenal hyperandrogenism, premature
adrenarche, precocious pseudopuberty, menstrual/reproductive dysfunction, and
hirsutism.

The local mechanism and genetics cover H6PD directly. Treatment coverage
includes dexamethasone adrenal androgen suppression.

## Concordance and completeness

Judgement: correct mapping, with subtype resolution to apparent CRD.

DisMech captures the causal H6PD/11-beta-HSD1 cofactor mechanism and the main
androgen-excess phenotype. IEMbase adds useful biochemical specificity for
ACTH, androstenedione, adrenal androgens, and the urinary
tetrahydrocortisol/tetrahydrocortisone ratio. The clinical overlap is strong
for adrenal hyperplasia, precocious pseudopuberty, and hirsutism.

## Curation actions

- Keep `Cortisone_Reductase_Deficiency.yaml#Apparent CRD` as the target.
- Consider adding explicit biochemical rows for ACTH, androstenedione, adrenal
  androgens, and urinary tetrahydrocortisol/tetrahydrocortisone ratio.
- Review whether H6PD-specific rows should be distinguished from HSD11B1 true
  cortisone reductase deficiency rows in downstream subtype exports.
