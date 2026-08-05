# IEMbase 0180: AKR1D1-related BASD type 2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 180 |
| Nosology | 14.8.02.01 |
| Gene | AKR1D1 |
| External IDs | OMIM:604741; ORPHA:79303 |
| Generated mapping | CANDIDATE; `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 2` |
| Candidate DisMech targets | `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 2` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as AKR1D1-related
Delta4-3-oxosteroid-5beta-reductase deficiency, with alternate labels
5beta-reductase deficiency and SRD5B1. Treatability is marked yes.

The biochemical rows emphasize increased urinary 7-alpha-hydroxy-3-oxo-
cholenoic acids and 7alpha,12alpha-dihydroxy-3-oxo-4-cholenoic acids,
increased plasma allochenodeoxycholic acid and allocholic acid, positive
AKR1D1 sequencing, increased ASAT/ALAT, normal-to-increased alkaline
phosphatase and gamma-GT, increased or normal-to-increased prothrombin ratio,
low-to-normal albumin, increased or normal-to-increased conjugated bilirubin,
and low-to-normal cholesterol. Clinical rows include neonatal or infantile
cholestasis, giant-cell hepatitis, lobular and periportal inflammation,
pseudoacinar transformation, abnormal canaliculi and microvilli, ascites,
edema, hepatosplenomegaly, and jaundice. Treatment rows list
chenodeoxycholic acid and ursodeoxycholic acid.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 2` is the correct
target. The local subtype covers AKR1D1/SRD5B1, defective
Delta4-3-oxosteroid 5beta-reductase activity, accumulation of
3-oxo-Delta4 bile acids and allocholic bile acids, severe neonatal cholestasis,
fat-soluble vitamin deficiency, bleeding risk, progressive liver injury, and
bile acid replacement therapy.

## Concordance and completeness

Judgement: accept the generated candidate as the correct subtype mapping.

IEMbase and DisMech agree on the gene, enzyme defect, toxic atypical bile acid
intermediates, normal or low gamma-GT cholestasis pattern, neonatal or infantile
liver disease, bleeding risk, and bile acid treatment. IEMbase adds more
granular analytes, particularly specific 3-oxo-Delta4 and allocholic bile acid
species, and separates chenodeoxycholic acid from ursodeoxycholic acid
treatment rows. DisMech is stronger for mechanism and group-level treatment
rationale.

## Curation actions

- Resolve this record to
  `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 2`.
- Consider adding the specific urinary and plasma allocholic/3-oxo bile acid species
  if the BASD type 2 subtype is enriched.
- Review whether ursodeoxycholic acid should be represented separately from
  primary bile acid replacement in the local treatment model.
