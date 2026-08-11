# IEMbase 0191: MVK-related mild mevalonate kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 191 |
| Nosology | 14.7.01.01 |
| Gene | MVK |
| External IDs | OMIM:260920; ORPHA:343 |
| Generated mapping | MAPPED; `Mevalonate_Kinase_Deficiency.yaml#HIDS` |
| Candidate DisMech targets | `Mevalonate_Kinase_Deficiency.yaml#HIDS` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as MVK-related mevalonate kinase deficiency (mild), with
alternate labels hyper Ig D syndrome, mevalonic aciduria, and HIDS.
Treatability is marked yes.

The biochemical rows include increased urinary mevalonic acid, normal serum
cholesterol, normal-to-increased erythrocyte sedimentation rate, low-to-normal
plasma coenzyme Q10, and normal-to-increased immunoglobulin D. Characteristic
clinical rows are anemia and thrombocytopenia. Additional rows include diarrhea,
hepatosplenomegaly, variable axial hypotonia, leukocytosis, and malabsorption.
No treatment rows are listed in this IEMbase record.

## DisMech phenotype coverage

`Mevalonate_Kinase_Deficiency.yaml#HIDS` is the correct target. The local entry
models the HIDS/mild MKD end of the MVK spectrum, reduced mevalonate kinase
activity, isoprenoid shortage, defective protein prenylation, RhoA/pyrin
inflammasome activation, IL-1 beta driven recurrent inflammatory attacks,
urinary mevalonic acid, elevated IgD/IgA, recurrent fever, cervical
lymphadenopathy, abdominal symptoms, rash, arthralgia, aphthous ulcers, and
multiple treatment options including canakinumab, anakinra, etanercept,
NSAIDs/corticosteroids, and hematopoietic stem cell transplantation in severe
contexts.

## Concordance and completeness

Judgement: correct mapped subtype with high concordance, but local coverage is
substantially richer.

IEMbase and DisMech agree on MVK/HIDS identity, mevalonic acid elevation,
inflammatory laboratory findings, GI involvement, hepatosplenomegaly, cytopenia
rows, and the mild end of the MKD spectrum. DisMech adds the central
prenylation-pyrin inflammasome mechanism, recurrent fever attack phenotype,
lymphadenopathy, rash, arthralgia, oral ulcers, IgA context, and the main
IL-1-targeted treatment model. IEMbase adds explicit low-to-normal coenzyme Q10
and a compact cytopenia/malabsorption summary.

## Curation actions

- Keep this record mapped to `Mevalonate_Kinase_Deficiency.yaml#HIDS`.
- Consider coenzyme Q10 and malabsorption as possible review targets if the
  HIDS subtype is enriched.
- Do not infer absent treatment from IEMbase; local treatment coverage is
  stronger than this JSON record.
