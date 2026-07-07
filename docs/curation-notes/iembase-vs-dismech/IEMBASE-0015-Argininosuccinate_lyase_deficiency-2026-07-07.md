# IEMbase 0015: ASL-related argininosuccinate lyase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 15 |
| Nosology | 1.1.05.01 |
| Gene | ASL |
| External IDs | OMIM:207900 |
| Generated mapping | AMBIGUOUS by `alias_exact:argininosuccinate lyase deficiency` |
| Candidate DisMech targets | `Argininosuccinic_Aciduria.yaml`; `Urea_Cycle_Disorder.yaml#Argininosuccinate Lyase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase highlights acute UCD-type decompensation with coma, encephalopathy,
developmental delay, and stroke-like episodes. Additional signs include
seizures, vomiting, feeding difficulty/protein aversion, failure to thrive,
episodic confusion, ataxia, hepatopathy, brittle hair/trichorrhexis nodosa, and
neonatal temperature instability.

The laboratory pattern is very strong for ASL deficiency: markedly increased
urinary argininosuccinic acid, increased plasma argininosuccinic acid, mildly
increased citrulline, high ammonia, high plasma/CSF glutamine, low arginine,
variably high orotic acid, and low/normal urea. Treatments mirror UCD care:
arginine or citrulline, protein-defined diet, nitrogen scavengers, hemodialysis,
peritoneal dialysis, and liver transplantation.

## DisMech phenotype coverage

`Argininosuccinic_Aciduria.yaml` is the correct standalone target. It covers
hyperammonemia, encephalopathy, intellectual disability, seizures, movement
abnormality, global developmental delay, hepatomegaly, elevated hepatic
transaminase, hepatic fibrosis, hypertension, hypotonia, abnormal behavior, and
trichorrhexis nodosa. Biochemical coverage goes beyond the generic UCD pattern:
argininosuccinic acid, ammonia, arginine, glutathione, nitric oxide, and alanine
aminotransferase. Treatments include diet with arginine, nitrogen scavengers,
liver transplantation, acute decompensation care, nitric oxide supplementation,
genetic counseling, newborn screening, and investigational mRNA therapy.

The umbrella `Urea Cycle Disorder` subtype explains the mapping ambiguity.

## Concordance and completeness

Judgement: high disease-level concordance, with DisMech richer for the
ammonia-independent ASL biology.

IEMbase is stronger for age-specific acute decompensation, explicit plasma and
urine argininosuccinic acid, protein aversion, stroke-like episodes, ataxia, and
dialysis modality detail. DisMech is stronger for nitric-oxide deficiency,
glutathione/oxidative stress, hepatic fibrosis, hypertension, and advanced
therapeutic hypotheses.

## Curation actions

- Resolve crosswalk ambiguity by mapping to `Argininosuccinic_Aciduria.yaml`.
- Consider adding stroke-like episodes and protein aversion if supported.
- Consider whether peritoneal dialysis and hemodialysis should be modeled
  separately or left under acute decompensation management.
