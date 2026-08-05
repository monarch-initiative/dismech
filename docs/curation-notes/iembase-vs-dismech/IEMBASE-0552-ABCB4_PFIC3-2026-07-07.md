# IEMbase 0552: ABCB4-related progressive familial intrahepatic cholestasis type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 552 |
| Nosology | 14.8.06.01 |
| Gene | ABCB4 |
| External IDs | OMIM:602347; ORPHA:79305 |
| Generated mapping | UNMAPPED; best candidate `Progressive_Familial_Heart_Block.yaml#Type 1A` |
| Candidate DisMech targets | None valid; heart-block candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCB4-related progressive familial intrahepatic cholestasis
type 3. The record is autosomal recessive, and treatability is unknown.
Treatment rows list ursodeoxycholic acid and liver transplantation.

The biochemical rows include increased serum bile acids, positive ABCB4
sequencing, increased plasma bile acids by enzyme assay, and increased
gamma-glutamyl transpeptidase. Clinical rows include cholestatic jaundice,
liver dysfunction, gallstones, biliary cirrhosis, liver fibrosis, portal
inflammation with ductular proliferation, splenomegaly, and adolescent
cholangiocarcinoma risk.

## DisMech phenotype coverage

No valid local ABCB4/PFIC3 target was found. The generated
`Progressive_Familial_Heart_Block.yaml#Type 1A` candidate is a lexical false
positive from "progressive familial" and "type"; it models cardiac conduction
disease, not ABCB4/MDR3-related hepatobiliary phospholipid transport disease.

This is consistent with prior PFIC1 and PFIC2 review notes, where ATP8B1 and
ABCB11 PFIC records were also local gaps rather than heart-block mappings.

## Concordance and completeness

Judgement: true local disease gap; generated heart-block candidate is false.

IEMbase provides a coherent PFIC3 profile with ABCB4 identity, high-GGT
cholestasis, bile acid elevation, ductular proliferation, fibrosis/cirrhosis,
gallstones, splenomegaly, cholangiocarcinoma risk, ursodeoxycholic acid, and
liver transplantation. None of this should be collapsed into progressive
familial heart block.

## Curation actions

- Do not map this record to progressive familial heart block.
- Add a future ABCB4/PFIC3 or MDR3 deficiency entry if PFIC disorders are in
  scope.
- Seed the future entry with high-GGT cholestasis, serum/plasma bile acids,
  ductular proliferation, fibrosis/cirrhosis, gallstones, splenomegaly,
  cholangiocarcinoma risk, ursodeoxycholic acid, and liver transplantation.
