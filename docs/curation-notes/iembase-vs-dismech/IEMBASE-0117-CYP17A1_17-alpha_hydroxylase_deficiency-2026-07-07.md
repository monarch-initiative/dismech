# IEMbase 0117: CYP17A1-related 17-alpha-hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 117 |
| Nosology | 24.2.05.01 |
| Gene | CYP17A1 |
| External IDs | OMIM:202110; ORPHA:418 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Congenital_Adrenal_Hyperplasia.yaml#17A-OHD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP17A1-related 17-alpha-hydroxylase deficiency, with
alternate labels congenital adrenal hyperplasia and P450c17 deficiency.
Treatability is marked unknown.

The characteristic biochemical rows show mineralocorticoid precursor excess and
sex-steroid/cortisol deficiency: low potassium, high sodium, high
corticosterone, low cortisol, high deoxycorticosterone, high progesterone, and
low sex hormones. Clinical rows include adrenal hyperplasia, alkalosis, and
hypertension. Glucocorticoids are listed as treatment.

## DisMech phenotype coverage

`Congenital_Adrenal_Hyperplasia.yaml` includes a `17A-OHD` subtype and a
CYP17A1 17-hydroxylase/17,20-lyase deficiency mechanism. The local entry
explicitly frames CYP17A1 deficiency as cortisol deficiency, sex-steroid
deficiency, and mineralocorticoid excess. It also links this mechanism to
hypertension in the phenotype section.

The local CAH treatment section includes glucocorticoid replacement, but the
entry is primarily optimized around 21-hydroxylase deficiency and broader CAH
management rather than detailed CYP17A1-specific steroid profiling.

## Concordance and completeness

Judgement: correct subtype-level mapping, with IEMbase richer for biochemical
resolution.

The mapping is concordant for CYP17A1/17A-OHD and for the hypertension/mineralocorticoid
excess phenotype. DisMech captures the essential mechanism and subtype identity.
IEMbase adds important diagnostic granularity: low potassium, high sodium,
corticosterone, deoxycorticosterone, progesterone, cortisol, and sex hormone
profiles across age bins. These are not present as discrete local biochemical
rows.

## Curation actions

- Keep `Congenital_Adrenal_Hyperplasia.yaml#17A-OHD` as the current target.
- Consider adding subtype-specific biochemical rows for deoxycorticosterone,
  corticosterone, potassium, sodium, cortisol, and sex hormone deficiency.
- Review whether delayed/absent puberty or undervirilization phenotypes should
  be made explicit for CYP17A1 deficiency in addition to hypertension.
