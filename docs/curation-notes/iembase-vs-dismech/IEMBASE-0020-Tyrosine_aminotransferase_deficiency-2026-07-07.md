# IEMbase 0020: TAT-related tyrosine aminotransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 20 |
| Nosology | 1.4.02.01 |
| Gene | TAT |
| External IDs | OMIM:276600 |
| Generated mapping | CANDIDATE by fuzzy alias to `Tyrosinemia_Type_I.yaml` |
| Candidate DisMech targets | No current standalone target; `Tyrosinemia_Type_I.yaml` is a false-positive candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents tyrosinemia type II/Richner-Hanhart syndrome. Characteristic
clinical features are corneal erosion and palmoplantar hyperkeratosis. Additional
features include photophobia, lacrimation, blisters and erosions on palms and
soles, and occasional intellectual disability.

The biochemical profile is severe hypertyrosinemia with elevated urinary
4-hydroxyphenylacetic acid, 4-hydroxyphenyllactic acid, and
4-hydroxyphenylpyruvic acid. The listed treatment is phenylalanine and tyrosine
restriction.

## DisMech phenotype coverage

There is no current standalone DisMech entry for TAT-related tyrosinemia type
II. The generated fuzzy candidate, `Tyrosinemia_Type_I.yaml`, is not appropriate:
HT1 is FAH-related, dominated by liver failure, renal tubular dysfunction,
succinylacetone, delta-ALA, and hepatocellular carcinoma risk. Those features do
not represent the corneal and palmoplantar phenotype of TAT deficiency.

## Concordance and completeness

Judgement: unmapped disease-level gap. The candidate is a tyrosinemia-family
string match, not a biological or phenotypic match.

IEMbase contributes a clear compact phenotype set for a future entry: corneal
erosions/photophobia/lacrimation, palmoplantar hyperkeratosis with blistering or
erosions, intellectual disability as a variable feature, high plasma tyrosine,
elevated urinary p-hydroxyphenyl organic acids, and dietary phenylalanine and
tyrosine restriction.

## Curation actions

- Do not map this record to `Tyrosinemia_Type_I.yaml`.
- Add a future standalone `Tyrosinemia_Type_II` or TAT-deficiency disease entry
  if this disease is in scope for curation.
- Use this note as a phenotype checklist for that future entry.
