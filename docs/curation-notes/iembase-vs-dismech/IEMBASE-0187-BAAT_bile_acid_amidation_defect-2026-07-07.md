# IEMbase 0187: BAAT-related bile acid amidation defect

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 187 |
| Nosology | 14.8.07.01 |
| Gene | BAAT |
| External IDs | OMIM:602938; ORPHA:238475 |
| Generated mapping | UNMAPPED; best candidate `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1` |
| Candidate DisMech targets | `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as BAAT-related bile acid-CoA:aminoacid
N-acyltransferase deficiency, with alternate labels bile acid amidation defect
and BAAT. Treatability is marked unknown.

The biochemical rows include increased unamidated bile acids by negative-mode
ESI-MS, including ions at m/z 391, 407, 471, 487, 567, and 583, positive BAAT
sequencing, normal-to-increased alkaline phosphatase, normal gamma-GT,
normal-to-increased transaminases, normal-to-increased prothrombin ratio,
normal-to-increased bilirubin, and low-to-normal 25-OH vitamin D, vitamin A,
and vitamin E. Clinical rows include hepatomegaly, hepatosplenomegaly, liver
cirrhosis, bridging fibrosis, cholestasis, failure to thrive, itching,
jaundice, rickets, and steatorrhea. The treatment row lists glycocholic acid.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1` is
the correct target even though the generated crosswalk left this record
unmapped. The local subtype explicitly covers BAAT, final amidation with
glycine or taurine, unamidated bile acids, neonatal cholestasis,
fat-soluble vitamin malabsorption, glycocholic acid replacement, and vitamin
supplementation.

## Concordance and completeness

Judgement: false negative; accept the BAAT bile acid conjugation defect subtype.

IEMbase and DisMech agree on BAAT identity, impaired bile acid amidation,
unamidated bile acid accumulation, cholestasis, fat-soluble vitamin deficiency,
steatorrhea, failure to thrive, progressive liver injury, and glycocholic acid
treatment. IEMbase adds granular ESI-MS ions, bilirubin/prothrombin/liver
enzyme rows, rickets, itching, bridging fibrosis, hepatomegaly, and cirrhosis
as potential enrichment details.

## Curation actions

- Resolve this record to
  `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1`.
- Consider adding the specific unamidated bile acid ESI-MS ion pattern and
  rickets/itching/bridging fibrosis detail if the subtype is enriched.
- Preserve separation from SLC27A5-related bile acid-CoA ligase deficiency.
