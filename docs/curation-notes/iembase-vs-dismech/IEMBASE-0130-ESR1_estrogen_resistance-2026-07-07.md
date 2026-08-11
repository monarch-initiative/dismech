# IEMbase 0130: ESR1-related Estrogen receptor deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 130 |
| Nosology | 24.2.17.01 |
| Gene | ESR1 |
| External IDs | OMIM:133430; ORPHA:785 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No valid standalone estrogen resistance/ESR1 target found; `Aromatase_Deficiency.yaml` is related context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ESR1-related estrogen receptor deficiency, with
alternate labels estrogen resistance and ESR1. Treatability is marked unknown.

The characteristic biochemical rows are increased FSH, increased LH, estradiol
normal-to-high or high, and increased gonadotropins. No clinical or treatment
rows are listed in the extract.

## DisMech phenotype coverage

No local standalone estrogen resistance, estrogen receptor deficiency, or ESR1
disease target was found. ESR1 appears in other contexts in the repository,
including cancer, osteoporosis risk, and reproductive/endocrine context, but
those entries do not represent the IEMbase monogenic estrogen-resistance
disease.

`Aromatase_Deficiency.yaml` mentions estrogen resistance as literature context,
but aromatase deficiency is a CYP19A1 estrogen-biosynthesis disorder with low
estrogen production. It should not be used as the disease target for ESR1
estrogen receptor deficiency.

## Concordance and completeness

Judgement: true unmapped local disease gap.

The IEMbase biochemical signal is consistent with estrogen resistance: high
gonadotropins despite normal-to-high or high estradiol. That mechanism is
distinct from aromatase deficiency and from ESR1 alterations represented in
cancer or risk-context entries. The generated unmapped result is appropriate.

## Curation actions

- Keep this record unmapped until a standalone ESR1 estrogen resistance entry
  exists.
- Do not map to `Aromatase_Deficiency.yaml`, ESR1 cancer entries, PMDD, or
  osteoporosis-risk content.
- Future curation should add an ESR1/estrogen resistance target with
  gonadotropin elevation, normal-to-high/high estradiol, estrogen-receptor
  resistance mechanism, and any disease-specific reproductive/skeletal
  phenotype evidence found in primary sources.
