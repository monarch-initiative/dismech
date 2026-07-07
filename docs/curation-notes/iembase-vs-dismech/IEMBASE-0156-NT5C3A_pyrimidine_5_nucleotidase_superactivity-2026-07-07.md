# IEMbase 0156: NT5C3A-related pyrimidine 5'-nucleotidase superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 156 |
| Nosology | 16.1.04.01 |
| Gene | NT5C3A |
| External IDs | OMIM:266120; OMIM:197720; ORPHA:35120 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Hereditary_Orotic_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as NT5C3A-related pyrimidine 5'-nucleotidase
superactivity, with the alternate label uridine-5'-monophosphate hydrolase
superactivity. Treatability is marked yes, but the local IEMbase JSON does not
list treatment rows for this disorder.

The biochemical signal differs from the NT5C3A deficiency entry: fibroblast
phosphoribose pyrophosphate is decreased, fibroblast
uridine-5'-monophosphate hydrolase is increased, and urinary uric acid is
decreased. The clinical rows are neurodevelopmental and immune/infectious:
developmental delay, fits/seizures, hyperactivity, and recurrent infections.

## DisMech phenotype coverage

There is no valid local DisMech target for NT5C3A-related pyrimidine
5'-nucleotidase superactivity.

`Hereditary_Orotic_Aciduria.yaml` is not the right target. It covers
UMPS-related pyrimidine synthesis deficiency with orotic acid accumulation and
uridine replacement, not NT5C3A superactivity with low phosphoribose
pyrophosphate, increased UMP hydrolase activity, and low urinary uric acid.

This should also remain distinct from the NT5C3A deficiency phenotype in
IEMbase 154, because the enzymatic direction and clinical signal are different.

## Concordance and completeness

Judgement: true local gap with a scope distinction from NT5C3A deficiency.

The generated hereditary orotic aciduria candidate is a pyrimidine-metabolism
neighbor only. Current DisMech coverage does not capture NT5C3A superactivity,
its fibroblast enzyme pattern, or the associated developmental delay,
seizures, hyperactivity, and recurrent infections.

## Curation actions

- Leave IEMbase 156 unmapped for now.
- Future curation should decide whether NT5C3A superactivity is a standalone
  entry or part of a carefully split NT5C3A spectrum.
- Do not collapse this into hereditary orotic aciduria or into the NT5C3A
  deficiency entry without explicit disease-scope evidence.
