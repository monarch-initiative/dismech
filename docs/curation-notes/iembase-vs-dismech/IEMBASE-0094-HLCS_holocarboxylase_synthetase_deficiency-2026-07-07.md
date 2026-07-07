# IEMbase 0094: HLCS-related holocarboxylase synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 94 |
| Nosology | 21.7.02.01 |
| Gene | HLCS |
| External IDs | OMIM:253270 |
| Generated mapping | MAPPED to `Holocarboxylase_Synthetase_Deficiency.yaml` |
| Candidate DisMech targets | `Holocarboxylase_Synthetase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive HLCS-related holocarboxylase
synthetase deficiency, with alternate labels infantile-onset multiple
carboxylase deficiency and HCSD. Treatability is marked yes.

The characteristic biochemical rows are urinary 3-methylcrotonylglycine, C5-OH
acylcarnitine in dried blood spot or plasma, urinary 3-hydroxypropionic acid,
and plasma lactate. Urinary methylcitric acid is also present in the wider
panel.

The characteristic clinical rows are alopecia, ataxia, skin rash, and mitral
valvulitis.

Treatment is biotin.

## DisMech phenotype coverage

The generated mapping is correct. `Holocarboxylase_Synthetase_Deficiency.yaml`
directly models HLCS deficiency as impaired protein biotinylation and
functional deficiency of the biotin-dependent carboxylases.

DisMech covers the major biochemical and clinical signals: C5-OH, lactate,
3-hydroxyisovaleric acid, 3-methylcrotonylglycine, 3-hydroxypropionate,
methylcitric acid, skin rash, alopecia, seizures, hypotonia, developmental
delay, feeding/growth problems, metabolic acidosis, hyperammonemia, and
biotin supplementation. It also models neonatal and late-onset presentations,
biotin responsiveness, newborn-screening issues, and genotype-response detail.

## Concordance and completeness

Judgement: high concordance.

IEMbase adds ataxia and mitral valvulitis as characteristic clinical rows.
DisMech is stronger for mechanism, multi-carboxylase branch logic, acute
decompensation detail, and biotin treatment response.

## Curation actions

- Keep the generated mapping to `Holocarboxylase_Synthetase_Deficiency.yaml`.
- Consider reviewing ataxia and mitral valvulitis for possible phenotype
  additions if source evidence supports them.
- Preserve dried-blood-spot versus plasma C5-OH distinctions if lab
  compartment granularity is added later.
