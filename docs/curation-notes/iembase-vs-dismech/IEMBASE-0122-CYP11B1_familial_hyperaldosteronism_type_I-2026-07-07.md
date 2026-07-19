# IEMbase 0122: CYP11B1-related 11-beta-Hydroxylase superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 122 |
| Nosology | 24.2.03.01 |
| Gene | CYP11B1 |
| External IDs | OMIM:103900; ORPHA:90795 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Familial_Hyperaldosteronism_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP11B1-related 11-beta-hydroxylase superactivity,
with alternate labels glucocorticoid suppressible hyperaldosteronism 1 and
HALD1. Treatability is marked unknown, but dexamethasone is listed as a
pharmacological treatment row.

The characteristic biochemical rows are low potassium, increased urinary
18-oxocortisol, and increased aldosterone. No clinical rows are listed in the
IEMbase extract.

## DisMech phenotype coverage

`Familial_Hyperaldosteronism_Type_I.yaml` is the correct local disease target.
It describes autosomal dominant primary aldosteronism caused by unequal
crossover between CYP11B1 and CYP11B2, producing a chimeric CYP11B1/CYP11B2
gene in which aldosterone synthase is under ACTH-responsive CYP11B1 regulatory
control.

The local phenotype and biochemical coverage includes early-onset hypertension,
dexamethasone-suppressible primary hyperaldosteronism, low plasma renin
activity, hypokalemia, adrenal hyperplasia, aldosterone excess, 18-oxocortisol,
and 18-hydroxycortisol. Treatments include glucocorticoid suppression and
mineralocorticoid receptor antagonist therapy.

## Concordance and completeness

Judgement: correct standalone mapping with strong concordance.

IEMbase and DisMech agree on the key biochemical signature: aldosterone excess,
hypokalemia, and elevated 18-oxocortisol. DisMech is richer for the genetic
mechanism, hypertension/low-renin clinical context, hybrid steroid profile, and
treatment options. IEMbase provides a compact confirmation that dexamethasone
is the relevant suppressive therapy.

## Curation actions

- Keep `Familial_Hyperaldosteronism_Type_I.yaml` as the canonical target.
- No mapping change is needed.
- Consider cross-checking whether urinary 18-oxocortisol should be represented
  separately from the existing hybrid-steroid biochemical rows.
