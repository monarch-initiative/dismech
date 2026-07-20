# IEMbase 0128: CYP19A1-related Aromatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 128 |
| Nosology | 24.2.15.01 |
| Gene | CYP19A1 |
| External IDs | OMIM:107910; ORPHA:91 |
| Generated mapping | MAPPED, high confidence |
| Candidate DisMech targets | `Aromatase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP19A1-related aromatase deficiency, with alternate
label Aro deficiency. Treatability is marked unknown.

The characteristic biochemical rows are increased FSH, increased LH, and
increased gonadotropins. Clinical rows include varying degrees of genital
ambiguity in 46,XX individuals and virilization. No treatment rows are listed.

## DisMech phenotype coverage

`Aromatase_Deficiency.yaml` is the correct local target. It describes
autosomal recessive CYP19A1 loss of function with impaired androgen-to-estrogen
conversion, congenital estrogen deficiency, and androgen excess. The local
entry captures sex- and age-dependent presentation across 46,XX and 46,XY
individuals.

DisMech phenotype coverage includes maternal antenatal virilization, ambiguous
genitalia, clitoromegaly, delayed puberty, hypergonadotropic hypogonadism,
primary amenorrhea, polycystic ovaries, infertility, delayed skeletal
maturation, tall stature, osteoporosis/osteopenia, and insulin resistance.
Biochemical rows include serum estradiol and serum testosterone, and treatment
coverage includes estrogen replacement therapy.

## Concordance and completeness

Judgement: correct mapping, with DisMech substantially richer for clinical
scope.

The IEMbase record confirms the expected hypergonadotropic pattern and
virilization/genital ambiguity signal, but it is much narrower than the local
entry. DisMech better captures estrogen deficiency, androgen excess, skeletal
and metabolic consequences, and treatment. IEMbase adds explicit FSH, LH, and
gonadotropin rows that would strengthen endocrine-feedback coverage.

## Curation actions

- Keep `Aromatase_Deficiency.yaml` as the canonical target.
- Consider adding FSH, LH, and gonadotropin elevation to the biochemical or
  endocrine feedback representation.
- No mapping correction is needed.
