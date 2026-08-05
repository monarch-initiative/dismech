# IEMbase 0513: MVK-related Mevalonate kinase deficiency, severe

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 513 |
| Nosology | 14.7.01.02 |
| Gene | MVK |
| External IDs | OMIM:610377; ORPHA:309025 |
| Generated mapping | MAPPED; `Mevalonate_Kinase_Deficiency.yaml#Mevalonic Aciduria` |
| Candidate DisMech targets | `Mevalonate_Kinase_Deficiency.yaml#Mevalonic Aciduria` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as severe MVK-related mevalonate kinase deficiency, with
alternate labels mevalonic aciduria and MKD. No treatments are listed.

The biochemical rows include very markedly increased urinary mevalonic acid,
increased plasma leukotriene E4, normal-to-high creatine kinase and
transaminases, low-to-normal cholesterol, low-to-normal coenzyme Q10, and
normal-to-high immunoglobulin D. Clinical rows include ataxia, cataract,
dolichocephaly, down-slanting eyelids, dysplastic ears, hypotonia, axial
hypotonia, leukocytosis, maculopapular rash, triangular face, anemia,
cerebellar hypoplasia, dysmorphic features, hepatosplenomegaly, psychomotor
delay, respiratory failure, and thrombocytopenia.

## DisMech phenotype coverage

`Mevalonate_Kinase_Deficiency.yaml#Mevalonic Aciduria` is the correct target.
The local entry explicitly models the MVK spectrum, with the severe end named
mevalonic aciduria. It includes reduced mevalonate kinase activity, deficient
mevalonate/isoprenoid/cholesterol pathway output, defective protein
prenylation, pyrin inflammasome activation, IL-1 beta inflammatory biology, and
severe mevalonic-aciduria features such as developmental delay, cerebellar
ataxia, dysmorphism, cataracts, and high early-childhood severity.

## Concordance and completeness

Judgement: correct mapped subtype with high concordance.

IEMbase and DisMech agree on MVK/mevalonic aciduria identity, urinary mevalonic
acid, the severe neurologic/dysmorphic end of the spectrum, cataracts, ataxia,
hypotonia, hepatosplenomegaly, inflammatory features, and cytopenia prompts.
DisMech is richer for mechanism and treatment framing, while IEMbase adds
compact prompts for leukotriene E4, low-to-normal coenzyme Q10, CK/transaminase
ranges, respiratory failure, and specific dysmorphic descriptors.

## Curation actions

- Keep this record mapped to `Mevalonate_Kinase_Deficiency.yaml#Mevalonic Aciduria`.
- Consider leukotriene E4, CK/transaminases, coenzyme Q10, respiratory failure,
  and IEMbase's specific dysmorphic-feature list as future enrichment prompts.
- Do not infer absent treatment from this JSON record; local MKD treatment
  coverage is stronger than the IEMbase row set.
