# IEMbase 0119: CYP21A2-related 21-hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 119 |
| Nosology | 24.2.01.01 |
| Gene | CYP21A2 |
| External IDs | OMIM:201910; ORPHA:418 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Congenital_Adrenal_Hyperplasia.yaml`; subtype targets include `Classic 21-OHD`, `Salt-Wasting 21-OHD`, `Simple-Virilizing 21-OHD`, and `Nonclassic 21-OHD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP21A2-related 21-hydroxylase deficiency, with
alternate labels congenital adrenal hyperplasia and CAH. Treatability is marked
unknown.

The characteristic biochemical rows are increased ACTH, hyperkalemia, increased
renin, hyponatremia, increased 17-OH-progesterone in plasma and urine,
decreased aldosterone, increased androgens, increased androstenedione,
increased DHEAS, increased urinary progesterone, and increased testosterone.
Clinical rows include accelerated growth, decreased fertility, testicular
adrenal rest tumors, and virilization. Hydrocortisone is listed as treatment.

## DisMech phenotype coverage

`Congenital_Adrenal_Hyperplasia.yaml` is strongly centered on CYP21A2-related
CAH. It includes classic, salt-wasting, simple-virilizing, and nonclassic
21-hydroxylase deficiency subtypes; a CYP21A2 21-hydroxylase deficiency
mechanism; cortisol and aldosterone deficiency; ACTH-driven adrenal hyperplasia
and androgen excess; prenatal/postnatal hyperandrogenism; and biochemical
testing centered on elevated 17-hydroxyprogesterone.

The phenotype section covers adrenal insufficiency, salt-wasting electrolyte
crisis, ambiguous genitalia/46,XX virilization, hirsutism, irregular
menstruation, infertility, hypertension, osteoporosis/osteopenia, short
stature, testicular adrenal rest tumors, and abnormal glucose homeostasis.
Treatments include glucocorticoid replacement, mineralocorticoid replacement,
crinecerfont adjunct therapy, and investigational CYP21A2 gene therapy.

## Concordance and completeness

Judgement: correct mapping with strong local coverage.

DisMech is more complete for subtype structure, mechanism, long-term
phenotypes, and treatment landscape. IEMbase contributes finer biochemical
resolution beyond the local elevated 17-hydroxyprogesterone and reduced
cortisol rows: ACTH, renin, aldosterone, sodium, potassium, and specific
androgen species are all useful future curation targets. The clinical overlap
is good for virilization, fertility impairment, and testicular adrenal rest
tumors; accelerated growth is partly represented indirectly through short
stature/androgen excess but could be made more explicit.

## Curation actions

- Keep `Congenital_Adrenal_Hyperplasia.yaml` as the canonical target, with
  subtype resolution to the appropriate 21-OHD clinical form when needed.
- Consider adding biochemical rows for ACTH, renin, aldosterone, sodium,
  potassium, androstenedione, DHEAS, testosterone, and urinary
  17-OH-progesterone/progesterone.
- Review accelerated growth as a possible explicit childhood phenotype in
  CYP21A2-related CAH.
