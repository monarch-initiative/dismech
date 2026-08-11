# IEMbase 0551: MTHFD1-related methylene tetrahydrofolate dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 551 |
| Nosology | 21.8.04.01 |
| Gene | MTHFD1 |
| External IDs | OMIM:172460; ORPHA:268377 |
| Generated mapping | UNMAPPED; low candidate `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MTHFD1-related 5,10-methylene-tetrahydrofolate
dehydrogenase deficiency, also labeled trifunctional
dehydrogenase/cyclohydrolase/synthetase deficiency. The record is autosomal
recessive, and treatability is unknown. Treatment rows list betaine, folinic
acid, hydroxycobalamin, and IVIG.

The biochemical rows include increased plasma total homocysteine, decreased
methylcobalamin synthesis in fibroblasts, increased plasma methylmalonic acid,
decreased CSF 5-MTHF, normal plasma folate, and normal plasma vitamin B12.
Characteristic clinical rows are megaloblastic anemia, atypical hemolytic
uremic syndrome, severe combined immunodeficiency, and thrombocytopenia.

## DisMech phenotype coverage

No exact local MTHFD1 disease target was found. The generated low candidate,
`Congenital_Adrenal_Hyperplasia.yaml#3B-HSD`, is a lexical false positive from
"dehydrogenase deficiency." That local subtype is HSD3B2 adrenal
steroidogenesis disease, not folate one-carbon metabolism, methylcobalamin
synthesis, immunodeficiency, atypical HUS, or megaloblastic anemia.

Other local folate and cobalamin entries provide contextual overlap for folate
handling, homocysteine, methylmalonic acid, and folinic acid, but they do not
model MTHFD1 or this combined immunohematologic phenotype.

## Concordance and completeness

Judgement: true local disease gap; reject the CAH 3B-HSD candidate.

The IEMbase record is a folate one-carbon metabolism disorder with
homocysteine, methylmalonic acid, low CSF 5-MTHF, megaloblastic anemia, SCID,
thrombocytopenia, and atypical HUS. It should not be mapped to adrenal
steroidogenesis CAH.

## Curation actions

- Keep this record unmapped until an MTHFD1 / methylene tetrahydrofolate
  dehydrogenase deficiency target exists.
- Do not map to `Congenital_Adrenal_Hyperplasia.yaml#3B-HSD`.
- Preserve homocysteine, methylmalonic acid, CSF 5-MTHF, normal folate/B12,
  megaloblastic anemia, atypical HUS, SCID, thrombocytopenia, and
  betaine/folinic acid/hydroxycobalamin/IVIG prompts.
