# IEMbase 0184: SLC27A5-related bile acid-CoA ligase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 184 |
| Nosology | 14.8.09.01 |
| Gene | SLC27A5 |
| External IDs | OMIM:603314; ORPHA:276066 |
| Generated mapping | UNMAPPED; best candidate `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1` |
| Candidate DisMech targets | Partial umbrella only; no valid SLC27A5 subtype |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SLC27A5-related bile acid-CoA ligase deficiency,
with BA CoA LD as the alternate label. Treatability is marked unknown.

The biochemical rows include increased unamidated bile acids by negative-mode
ESI-MS, including ions at m/z 391, 407, 471, 487, 567, and 583, positive
SLC27A5 sequencing, normal neonatal gamma-GT, normal-to-increased
transaminases, and normal-to-increased conjugated bilirubin. Clinical rows
include variable neonatal cholestasis, bridging fibrosis, and jaundice. The
treatment row lists ursodeoxycholic acid with low evidence.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` has relevant group-level context:
its description and enzyme-block coverage mention final bile acid
amidation/conjugation steps involving BAAT and SLC27A5. However, the explicit
`Bile acid conjugation defect 1` subtype is BAAT-related and should not be used
as a direct SLC27A5 subtype mapping.

## Concordance and completeness

Judgement: partial umbrella coverage, but no valid local SLC27A5 subtype.

The local bile acid synthesis/conjugation file is mechanistically close enough
to preserve as context, but the generated best candidate is not equivalent to
SLC27A5-related bile acid-CoA ligase deficiency. IEMbase provides a concise
SLC27A5 disease profile: unamidated bile acids, normal gamma-GT cholestasis,
bridging fibrosis, jaundice, and possible ursodeoxycholic acid use.

## Curation actions

- Do not resolve this record directly to the BAAT-specific conjugation defect 1
  subtype.
- Add a future SLC27A5-related bile acid-CoA ligase deficiency subtype under
  the bile acid synthesis/conjugation disease group if subtype anchors are
  supported.
- Seed that future subtype with unamidated bile acid ESI-MS markers, neonatal
  cholestasis, bridging fibrosis, jaundice, and ursodeoxycholic acid context.
