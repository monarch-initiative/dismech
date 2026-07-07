# IEMbase 0179: HSD3B7-related bile acid synthesis defect type 1

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 179 |
| Nosology | 14.8.01.01 |
| Gene | HSD3B7 |
| External IDs | OMIM:607764; ORPHA:79301 |
| Generated mapping | UNMAPPED; best candidate `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 1` |
| Candidate DisMech targets | `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HSD3B7-related
3beta-hydroxy-Delta5-C27-steroid dehydrogenase-isomerase deficiency, with
alternate labels 3beta-dehydrogenase deficiency and C27-3beta-HSD.
Treatability is marked yes.

The biochemical rows include decreased plasma chenodeoxycholic acid, increased
ESI-MS signals for sulfate/glycine conjugated dihydroxy and trihydroxy
5-cholenoic acids, increased sulfated 3beta,7alpha,12alpha-trihydroxy-
5-cholenoic acids in plasma and urine, increased sulfated
3beta,7alpha-dihydroxy-5-cholenoic acids in plasma and urine, increased
fibroblast 7-alpha-hydroxycholesterol dehydrogenase, increased ASAT/ALAT and
alkaline phosphatase, normal gamma-GT, normal to increased prothrombin ratio,
normal or low-to-normal albumin, increased or normal-to-increased conjugated
bilirubin, and decreased or low-to-normal calcium, cholesterol,
25-OH vitamin D, vitamin A, and vitamin E. Clinical rows include bridging
fibrosis, hepatomegaly, liver cirrhosis, periportal inflammation, cholestasis,
giant-cell hepatitis, itching, jaundice, rickets, hypocalcemic seizures or
tetany, steatorrhea, and vitamin K responsive bleeding. The treatment row
lists cholic acid analogs.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 1` is the correct
target even though the generated crosswalk left the record unmapped. The local
entry explicitly lists BASD type 1 as HSD3B7-related
3beta-hydroxy-Delta5-C27-steroid oxidoreductase deficiency. It models impaired
primary bile acid synthesis, accumulation of toxic C27 bile acid
intermediates, neonatal or infantile cholestasis with normal GGT, fat and
fat-soluble vitamin malabsorption, failure to thrive, jaundice, steatorrhea,
bleeding tendency, cirrhosis or liver failure risk, cholic acid replacement,
chenodeoxycholic acid context, fat-soluble vitamin supplementation, liver
transplantation for advanced disease, and bile-acid profiling by mass
spectrometry.

## Concordance and completeness

Judgement: false negative at file level; accept the local BASD type 1 subtype
target.

IEMbase and DisMech agree on HSD3B7/BASD type 1, impaired primary bile acid
synthesis, atypical C27 bile acid intermediates, normal GGT cholestasis,
fat-soluble vitamin deficiency, jaundice, steatorrhea, bleeding, progressive
liver injury, and cholic acid based treatment. IEMbase adds highly granular
mass-spectrometry analytes, low chenodeoxycholic acid, alkaline phosphatase,
albumin/prothrombin/calcium/cholesterol rows, rickets, hypocalcemic
seizures/tetany, bridging fibrosis, periportal inflammation, and giant-cell
hepatitis as possible enrichment targets.

## Curation actions

- Resolve this record to
  `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 1`.
- Consider adding HSD3B7-specific diagnostic analytes if the current group
  entry is later split or enriched.
- Keep cholic acid analog treatment aligned with the existing cholic acid
  replacement mechanism.
