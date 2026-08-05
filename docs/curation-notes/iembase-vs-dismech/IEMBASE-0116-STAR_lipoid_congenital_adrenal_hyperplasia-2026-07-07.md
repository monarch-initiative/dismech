# IEMbase 0116: STAR-related steroidogenic acute regulatory protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 116 |
| Nosology | 24.2.06.01 |
| Gene | STAR |
| External IDs | OMIM:201710; ORPHA:314376 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Congenital_Adrenal_Hyperplasia.yaml#Lipoid CAH` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as STAR-related steroidogenic acute regulatory protein
deficiency, with alternate labels lipoid adrenal hyperplasia and StAR
deficiency. Treatability is marked unknown.

The characteristic biochemical rows show primary steroidogenic failure:
increased plasma ACTH, hyperkalemia, hyponatremia, and decreased steroids in
plasma and urine. Clinical rows include alkalosis, ambiguous genitalia or
female external genitalia in 46,XY individuals, and delayed puberty. Treatments
listed are glucocorticoids and mineralocorticoids.

## DisMech phenotype coverage

The generated unmapped status is a false negative. `Congenital_Adrenal_Hyperplasia.yaml`
has a `Lipoid CAH` subtype described as severe STAR-related steroidogenesis
disorder impairing cholesterol delivery for adrenal and gonadal steroid hormone
synthesis. The entry includes STAR pathogenic variants and places lipoid CAH in
the broader CAH phenotype frame of adrenal insufficiency, salt-wasting
electrolyte crisis, ambiguous genitalia/virilization, and glucocorticoid plus
mineralocorticoid replacement.

DisMech currently has only broad CAH biochemical rows, mainly reduced cortisol
and elevated 17-hydroxyprogesterone for 21-hydroxylase deficiency. It does not
yet expose STAR-specific low steroid profiles or ACTH/potassium/sodium patterns
as discrete biochemical markers.

## Concordance and completeness

Judgement: false negative to existing subtype-level local coverage.

The local CAH entry is concordant for STAR/lipoid CAH and for adrenal
insufficiency with replacement therapy. IEMbase is more granular for the
STAR-specific biochemical signature and for 46,XY undervirilization/female
external genitalia and delayed puberty. DisMech's broad ambiguous-genitalia row
is not a perfect match because STAR deficiency is a sex-steroid-deficiency
phenotype rather than the androgen-excess virilization branch that dominates
21-hydroxylase CAH.

## Curation actions

- Resolve to `Congenital_Adrenal_Hyperplasia.yaml#Lipoid CAH`.
- Add or review subtype-specific STAR biochemical markers: ACTH, sodium,
  potassium, and global steroid deficiency.
- Consider more precise sex-development phenotypes for 46,XY undervirilization
  in lipoid CAH rather than reusing the 46,XX virilization framing.
