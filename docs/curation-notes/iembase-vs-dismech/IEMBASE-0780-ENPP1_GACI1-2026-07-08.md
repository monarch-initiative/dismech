# IEMbase 0780: ENPP1-related ectonucleotide pyrophosphatase-phosphodiesterase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 780 |
| Nosology | 16.3.12.01 |
| Nosology code | IEM0037 |
| Gene | ENPP1 |
| External IDs | OMIM:208000; ORPHA:51608 |
| Generated mapping | AMBIGUOUS; `Arterial_Calcification_of_Infancy` and subtype `ENPP1-related` |
| Candidate DisMech targets | `Arterial_Calcification_of_Infancy.yaml` subtype ENPP1-related |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as ENPP1-related
ectonucleotide pyrophosphatase-phosphodiesterase 1 deficiency, with alternate
name generalized arterial calcification of infancy type 1 and abbreviation
GACI1. The source signal includes neonatal/infantile arterial calcification,
renal artery calcification, calcification of cardiac valve rings and aorta,
hypertension, cardiac failure, coronary artery disease, myocardial infarction,
early death, prenatal signs such as fetal distress, polyhydramnios, or
pericardial effusion, joint calcifications, hearing loss, angioid streaks, and
dental findings including ankylosis, hypercementosis, and infraocclusion.

## DisMech phenotype coverage

`Arterial_Calcification_of_Infancy.yaml` is the correct local target. It has an
explicit ENPP1-related subtype, models ENPP1 loss as defective extracellular
ATP hydrolysis and reduced pyrophosphate generation, and captures arterial
calcification, arterial stenosis, hypertension, congestive heart failure,
FGF23-mediated renal phosphate wasting, hypophosphatemic rickets, and hearing
loss in ENPP1-deficient survivors.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects disease-level
and subtype-level matches.

The gene, OMIM identity, inheritance, GACI1 identity, pyrophosphate mechanism,
arterial calcification/stenosis, hypertension, heart failure, survivor rickets,
and hearing loss are concordant. IEMbase provides useful granularity beyond the
current local phenotype set: prenatal presentation, renal artery and coronary
territory disease, valve/aortic-ring calcification, myocardial infarction,
joint calcification, angioid streaks, and dental ankylosis/hypercementosis/
infraocclusion are not all modeled as discrete DisMech phenotypes.

## Curation actions

- Treat `Arterial_Calcification_of_Infancy.yaml` subtype ENPP1-related as exact
  local coverage for IEMbase 0780.
- Preserve the ENPP1-specific rickets, phosphate/FGF23, and hearing-loss
  survivor phenotype already present locally.
- Consider future phenotype additions for prenatal signs, dental disease,
  angioid streaks, renal/coronary/valve calcification, myocardial infarction,
  and joint/enthesis calcification.
