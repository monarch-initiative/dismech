# IEMbase 0375: CETP-related cholesteryl ester transfer protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 375 |
| Nosology | 15.4.26.01 |
| Gene | CETP |
| External IDs | OMIM:607322; OMIM:143470; ORPHA:79506 |
| Generated mapping | UNMAPPED; low candidate `Cholesteryl_Ester_Storage_Disease.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CETP-related cholesteryl ester transfer protein deficiency,
also listed as familial hyperalphalipoproteinemia type 1 and CETP deficiency.
Inheritance is autosomal dominant.

The cached record has no clinical rows or treatment rows. Biochemical rows
include serum cholesterol, plasma HDL cholesterol, and serum triglyceride.

## DisMech phenotype coverage

There is no exact local DisMech target for CETP deficiency. The generated low
candidate `Cholesteryl_Ester_Storage_Disease.yaml` is a lexical false positive:
that file models LIPA-related lysosomal acid lipase deficiency with lysosomal
storage of cholesteryl esters and triglycerides in hepatocytes and macrophages.
It does not model CETP-mediated transfer of cholesteryl esters between
lipoprotein classes or familial hyperalphalipoproteinemia.

General hyperlipidemia content may provide lipid-metabolism context, but it
does not replace a gene-specific CETP deficiency entry.

## Concordance and completeness

Judgement: true local gap; reject the cholesteryl ester storage disease
candidate.

The IEMbase disease is a circulating lipoprotein-transfer disorder, whereas
CESD is an autosomal recessive lysosomal hydrolase deficiency caused by LIPA.
The shared "cholesteryl ester" words are insufficient for disease mapping.

## Curation actions

- Keep this record unmapped until a CETP deficiency or familial
  hyperalphalipoproteinemia target exists.
- Do not map to `Cholesteryl_Ester_Storage_Disease.yaml`.
- If curated, include CETP, high-HDL/familial hyperalphalipoproteinemia scope,
  and the serum cholesterol/HDL/triglyceride biochemical pattern.
