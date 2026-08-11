# IEMbase 0014: ASS1-related argininosuccinate synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 14 |
| Nosology | 1.1.04.01 |
| Gene | ASS1 |
| External IDs | OMIM:215700 |
| Generated mapping | AMBIGUOUS by `alias_exact:argininosuccinate synthetase deficiency` |
| Candidate DisMech targets | `Citrullinemia_Type_I.yaml`; `Urea_Cycle_Disorder.yaml#Argininosuccinate Synthetase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as classical citrullinemia/CTLN1. The characteristic
clinical signal is acute hyperammonemic encephalopathy with coma and
developmental delay, plus stroke-like episodes. Additional features include
neonatal seizures, vomiting, feeding difficulty/protein aversion, failure to
thrive, episodic confusion, ataxia, burst-suppression EEG, acute liver failure,
and neonatal temperature instability.

The biochemical profile distinguishes ASS1 deficiency from other UCDs: very high
plasma and urine citrulline, high ammonia, high plasma/CSF glutamine, low
arginine, normal urinary argininosuccinic acid, variably high orotic acid, and
low/normal urea. Treatments include arginine, protein-defined diet, nitrogen
scavengers, hemodialysis, peritoneal dialysis, and liver transplantation.

## DisMech phenotype coverage

`Citrullinemia_Type_I.yaml` is the correct canonical target. It covers
hyperammonemia, encephalopathy, seizures, lethargy, poor feeding, vomiting,
intellectual disability, global developmental delay, cerebral edema, spasticity,
coma, failure to thrive, and respiratory alkalosis. Biochemical coverage is
strong: citrulline, ammonia, arginine, argininosuccinate, orotic acid, and
glutamine are all explicit. Treatments include diet, nitrogen scavengers,
arginine, acute crisis management, liver transplantation, newborn screening,
genetic counseling, and emerging RNA therapeutics.

The `Urea Cycle Disorder` subtype duplicates the exact disease label and causes
the generated ambiguity.

## Concordance and completeness

Judgement: high concordance. DisMech has the right standalone entry and covers
the major clinical and biochemical axes.

IEMbase adds more age-stratified presentation detail, burst-suppression EEG,
stroke-like episodes, temperature instability, and explicit dialysis modalities.
DisMech adds cerebral edema, respiratory alkalosis, newborn screening, and an
investigational RNA-therapeutic angle not present in IEMbase.

## Curation actions

- Resolve crosswalk ambiguity by mapping to `Citrullinemia_Type_I.yaml`.
- Consider whether burst-suppression EEG and protein aversion should be added as
  evidence-backed phenotype refinements.
- Keep the umbrella subtype as secondary context only.
