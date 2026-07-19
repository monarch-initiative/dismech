# IEMbase 0118: HSD3B2-related 3-beta-hydroxysteroid dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 118 |
| Nosology | 24.2.04.01 |
| Gene | HSD3B2 |
| External IDs | OMIM:201810; ORPHA:418 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HSD3B2-related 3-beta-hydroxysteroid dehydrogenase
deficiency, with alternate labels 3beta-HSD deficiency and congenital adrenal
hyperplasia. Treatability is marked unknown.

The characteristic biochemical rows are hyperkalemia, hyponatremia, increased
17-OH-pregnenolone, decreased aldosterone, decreased cortisol, increased DHEAS,
and decreased sex hormones. The cached JSON has no clinical rows for this
record. Treatments listed are glucocorticoids and mineralocorticoids.

## DisMech phenotype coverage

`Congenital_Adrenal_Hyperplasia.yaml` includes a `3B-HSD` subtype described as
HSD3B2-related disruption of glucocorticoid, mineralocorticoid, and sex-steroid
synthesis. HSD3B2 pathogenic variants are represented in the genetic section.
The broad CAH phenotype coverage includes adrenal insufficiency, salt-wasting
electrolyte crisis, ambiguous genitalia/virilization, and hormone replacement
therapy with glucocorticoids and mineralocorticoids.

The local entry does not currently have a dedicated HSD3B2 pathophysiology node
or HSD3B2-specific biochemical profile comparable to the CYP21A2, CYP11B1, and
CYP17A1 nodes.

## Concordance and completeness

Judgement: correct subtype-level mapping, but local coverage is thin for this
specific subtype.

The target is correct for HSD3B2/3B-HSD deficiency and treatment overlap is
good. IEMbase is substantially more granular for biochemical completeness:
17-OH-pregnenolone, DHEAS, aldosterone, cortisol, sodium, potassium, and sex
hormones are all subtype-specific signals that are not individually represented
in DisMech. DisMech has the right umbrella/subtype structure but less mechanistic
depth for this subtype than for 21-OHD or 17A-OHD.

## Curation actions

- Keep `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD` as the current target.
- Add a future HSD3B2 pathophysiology node if the CAH entry is expanded.
- Consider adding subtype-specific biochemical rows for 17-OH-pregnenolone,
  DHEAS, aldosterone, cortisol, sodium, potassium, and sex hormone deficiency.
