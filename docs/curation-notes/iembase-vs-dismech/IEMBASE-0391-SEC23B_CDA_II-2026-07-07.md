# IEMbase 0391: SEC23B-related Congenital dyserythropoietic anemia type 2 (CDG)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 391 |
| Nosology | 19.6.08.01 |
| Gene | SEC23B |
| External IDs | OMIM:224100; ORPHA:98873 |
| Generated mapping | CANDIDATE; `Congenital_Dyserythropoietic_Anemia.yaml#CDA II` |
| Candidate DisMech targets | `Congenital_Dyserythropoietic_Anemia.yaml#CDA II` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SEC23B-related congenital
dyserythropoietic anemia type 2, labeled SEC23B-CDG. Characteristic rows include
anemia, dyserythropoietic anemia, increased bilirubin, positive acidified serum
test/HEMPAS test, and bi-nucleated and multinucleated bone-marrow
erythroblasts. Additional rows include jaundice, splenomegaly, adult
cardiomyopathy, insulin-dependent diabetes mellitus, and liver cirrhosis. Serum
sialotransferrins are listed as normal.

The treatment row lists hematopoietic stem cell transplant with blood and
blood-forming-tissue effects.

## DisMech phenotype coverage

The generated candidate is correct and should be accepted as subtype-level
coverage. Local `Congenital_Dyserythropoietic_Anemia.yaml` includes a CDA II
subtype caused by biallelic SEC23B variants, impaired COPII-dependent
ER-to-Golgi vesicular trafficking, mild-to-severe normocytic anemia, hemolysis,
jaundice, splenomegaly, band-3 hypoglycosylation, and bi/multinucleated mature
erythroblasts. It also covers secondary iron overload and hematopoietic stem
cell transplantation in the broader CDA treatment section.

IEMbase is useful for several SEC23B-CDA II lab prompts that are not always
front-and-center in local prose, especially HEMPAS testing, bilirubin, normal
sialotransferrins, and explicit marrow cell wording.

## Concordance and completeness

Judgement: accept candidate as correct subtype mapping to
`Congenital_Dyserythropoietic_Anemia.yaml#CDA II`.

The resources agree on SEC23B, autosomal recessive inheritance, CDA II identity,
dyserythropoietic anemia, jaundice/hemolysis context, splenomegaly, and
bi/multinucleated erythroblast morphology. IEMbase adds useful CDG framing and
normal sialotransferrin contrast.

## Curation actions

- Treat the generated candidate as the correct mapping, with CDA II as the
  canonical subtype target.
- Consider enriching local CDA II with HEMPAS/acidified-serum testing,
  bilirubin directionality, normal sialotransferrins, and IEMbase's diabetes,
  cardiomyopathy, and cirrhosis review prompts after source verification.
- Keep hematopoietic stem cell transplant as a treatment prompt but preserve
  local nuance about indication and disease severity.
