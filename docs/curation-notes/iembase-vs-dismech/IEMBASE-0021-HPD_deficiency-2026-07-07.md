# IEMbase 0021: HPD-related 4-hydroxyphenylpyruvate dioxygenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 21 |
| Nosology | 1.4.03.01 |
| Gene | HPD |
| External IDs | OMIM:276710 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Alkaptonuria` at 0.698 |
| Candidate DisMech targets | No current standalone target; `Alkaptonuria.yaml` is a false-positive candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents tyrosinemia type III due to HPD deficiency. The clinical
phenotype signal is sparse, with intellectual disability listed as a variable
feature and no characteristic clinical feature flagged.

The biochemical signal is clearer: elevated plasma tyrosine, plus elevated
urinary 4-hydroxyphenylacetic acid, 4-hydroxyphenyllactic acid, and
4-hydroxyphenylpyruvic acid. No treatment row is listed in the cached IEMbase
record.

## DisMech phenotype coverage

There is no current standalone DisMech entry for HPD-related tyrosinemia type
III. The fuzzy candidate `Alkaptonuria.yaml` is not appropriate: alkaptonuria is
HGD-related, marked by homogentisic-acid accumulation, ochronosis, connective
tissue disease, dark urine, and nitisinone therapy. It does not cover HPD
deficiency or the tyrosinemia type III biochemical profile.

## Concordance and completeness

Judgement: unmapped disease-level gap. Candidate matching is pathway-adjacent
but wrong at the gene, metabolite, and phenotype levels.

The future DisMech target would likely be much narrower than HT1 or
alkaptonuria: biochemical hypertyrosinemia and hydroxyphenyl organic aciduria,
with uncertain/variable neurodevelopmental phenotype.

## Curation actions

- Do not map this record to `Alkaptonuria.yaml`.
- Add a future standalone HPD-deficiency/tyrosinemia type III entry if this
  disorder becomes a curation target.
- Treat intellectual disability cautiously because IEMbase marks no
  characteristic clinical feature and the phenotype may be variably penetrant.
