# IEMbase 0093: BTD-related biotinidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 93 |
| Nosology | 21.7.01.01 |
| Gene | BTD |
| External IDs | OMIM:253260 |
| Generated mapping | MAPPED to `Biotinidase_Deficiency.yaml` |
| Candidate DisMech targets | `Biotinidase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive BTD-related biotinidase
deficiency, with alternate labels late-onset multiple carboxylase deficiency
and BTD deficiency. Treatability is marked yes, and prevalence is listed near
1:61,000.

The characteristic biochemical rows are 3-methylcrotonylglycine, C5-OH
acylcarnitine in dried blood spot or plasma, plasma biotinidase, urinary
3-hydroxyisovaleric acid, and urinary 3-hydroxypropionic acid. The wider panel
also includes urinary methylcitric acid and plasma lactate.

The characteristic clinical rows are glossitis, stomatitis, and mitral
valvulitis.

Treatment is biotin.

## DisMech phenotype coverage

The generated mapping is correct. `Biotinidase_Deficiency.yaml` directly models
BTD deficiency as impaired biotin recycling causing secondary multiple
carboxylase deficiency.

DisMech covers the core biochemical pattern: reduced biotinidase enzyme
activity, C5-OH acylcarnitine, 3-hydroxyisovaleric acid, C3-related
propionylcarnitine context, organic aciduria, lactate, and metabolic acidosis.
It also covers the major clinical consequences of untreated or late-treated
disease, including seizures, developmental delay, hypotonia, rash, alopecia,
hearing loss, optic neuropathy, respiratory features, and lifelong biotin
treatment with newborn-screening context.

## Concordance and completeness

Judgement: high concordance.

IEMbase adds several compact clinical rows that are not prominent in the local
entry: glossitis, stomatitis, and mitral valvulitis. DisMech is substantially
richer for mechanism, severity classes, genotype-phenotype notes, treatment
rationale, newborn screening, and long-term neurologic/auditory/visual risks.

## Curation actions

- Keep the generated mapping to `Biotinidase_Deficiency.yaml`.
- Consider adding glossitis, stomatitis, and mitral valvulitis as review
  targets if supported by source evidence.
- Keep IEMbase biochemical compartments in mind if future structured lab
  curation distinguishes dried blood spot, plasma, and urine assays.
