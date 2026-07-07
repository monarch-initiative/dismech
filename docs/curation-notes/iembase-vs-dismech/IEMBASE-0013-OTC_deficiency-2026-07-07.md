# IEMbase 0013: OTC-related ornithine transcarbamylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 13 |
| Nosology | 1.1.03.01 |
| Gene | OTC |
| External IDs | OMIM:311250; ORPHA:664 |
| Generated mapping | AMBIGUOUS by `alias_exact:ornithine carbamoyltransferase deficiency` |
| Candidate DisMech targets | `Ornithine_Carbamoyltransferase_Deficiency.yaml`; `Urea_Cycle_Disorder.yaml#Ornithine Carbamoyltransferase Deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

The IEMbase record emphasizes the classic hyperammonemic UCD presentation:
coma, encephalopathy, developmental delay, neonatal/infantile severity, and
stroke-like episodes. Additional clinical features include seizures, vomiting,
feeding difficulty/protein aversion, episodic confusion, ataxia, asterixis,
coagulopathy, acute liver failure, rare adult liver adenoma/carcinoma signals,
temperature instability, and impaired vision.

The biochemical profile is specific for OTC deficiency: very high ammonia,
high plasma and CSF glutamine, very low plasma citrulline, low arginine,
low/normal urea, normal urinary argininosuccinic acid, and variably high urinary
orotic acid. Treatments include protein-defined diet, arginine or citrulline,
nitrogen scavengers, hemodialysis, peritoneal dialysis, and liver
transplantation.

## DisMech phenotype coverage

The standalone DisMech entry is the correct disease-level target. It covers
hyperammonemia, encephalopathy, vomiting, lethargy, seizures, coma, cerebral
edema, global developmental delay, hepatic failure, hyperglutaminemia,
oroticaciduria, low plasma citrulline, and behavioral abnormalities. It also
models the distinguishing biochemical markers: ammonia, glutamine, citrulline,
uracil, and orotic acid. Treatments cover protein restriction, nitrogen
scavengers, arginine supplementation, acute hyperammonemia management, liver
transplantation, and genetic counseling.

The `Urea Cycle Disorder` umbrella subtype is useful context but should not be
the canonical crosswalk target.

## Concordance and completeness

Judgement: high phenotype and biochemical concordance, with the generated
ambiguity caused by duplicate exact matching between the standalone disease and
the umbrella subtype.

IEMbase adds a more granular age-by-age severity profile, protein aversion,
stroke-like episodes, asterixis/ataxia, temperature instability, visual
impairment, liver tumor signals, and dialysis modality detail. DisMech is richer
mechanistically, especially for carbamoyl phosphate diversion and ammonia-driven
cerebral injury, and includes cerebral edema and lethargy explicitly.

## Curation actions

- Resolve crosswalk ambiguity by treating
  `Ornithine_Carbamoyltransferase_Deficiency.yaml` as the canonical target.
- Consider evidence-backed additions for protein aversion, stroke-like episodes,
  and late-onset movement/confusion features.
- Decide whether peritoneal dialysis needs separate treatment representation or
  remains covered by acute hyperammonemia management.
