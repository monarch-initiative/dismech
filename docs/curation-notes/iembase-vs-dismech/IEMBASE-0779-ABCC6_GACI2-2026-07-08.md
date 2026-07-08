# IEMbase 0779: ABCC6-related generalized arterial calcification of infancy type 2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 779 |
| Nosology | 16.3.11.01 |
| Nosology code | IEM0036 |
| Gene | ABCC6 |
| External IDs | OMIM:614473; ORPHA:51608 |
| Generated mapping | AMBIGUOUS; `Arterial_Calcification_of_Infancy` and subtype `ABCC6-related` |
| Candidate DisMech targets | `Arterial_Calcification_of_Infancy.yaml` subtype ABCC6-related |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as ABCC6-related generalized
arterial calcification of infancy type 2, abbreviation GACI2. The source signal
includes arterial calcification, renal artery calcification, calcification of
cardiac valve rings and aorta, hypertension, cardiac failure, coronary artery
disease, myocardial infarction, early death, joint calcifications, and optional
childhood/adolescent rickets and nephrocalcinosis.

## DisMech phenotype coverage

`Arterial_Calcification_of_Infancy.yaml` is the correct local target. It has an
explicit ABCC6-related subtype, describes biallelic ABCC6 variants as a smaller
fraction of GACI, and models ENPP1/ABCC6 disruption of extracellular
pyrophosphate anti-mineralization, arterial calcification and stenosis,
hypertension, and congestive heart failure. The local genetic section includes
ABCC6 as the causal gene for the ABCC6-related subtype.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects disease-level
and subtype-level matches.

The gene, OMIM identity, recessive inheritance, GACI disease identity, and core
arterial calcification/stenosis/cardiac-compromise phenotype are concordant.
IEMbase is more granular for vascular territories and downstream consequences:
renal artery calcification, cardiac valve/aortic ring calcification, coronary
artery disease, myocardial infarction, and joint calcifications are not all
separate local phenotype rows. IEMbase also lists rickets and nephrocalcinosis
as optional ABCC6 rows; DisMech currently localizes the strong
hypophosphatemic-rickets phenotype to the ENPP1-related subtype, with ABCC6
only a low-frequency context in cited natural-history evidence.

## Curation actions

- Treat `Arterial_Calcification_of_Infancy.yaml` subtype ABCC6-related as exact
  local coverage for IEMbase 0779.
- Preserve the ABCC6-vs-ENPP1 subtype distinction; do not transfer the
  ENPP1-dominant rickets model to ABCC6 without evidence.
- Consider future phenotype granularity for renal artery, coronary, myocardial
  infarction, valve/aortic-ring, joint calcification, nephrocalcinosis, and
  low-frequency ABCC6 rickets.
