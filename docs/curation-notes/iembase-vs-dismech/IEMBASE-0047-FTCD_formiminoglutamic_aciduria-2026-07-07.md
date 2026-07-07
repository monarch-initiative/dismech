# IEMbase 0047: FTCD-related formiminoglutamic aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 47 |
| Nosology | 21.8.06.01 |
| Gene | FTCD |
| External IDs | OMIM:229100 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None; fuzzy neighbor `Hereditary_Orotic_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive FTCD-related
formimidoyltransferase cyclodeaminase deficiency, with alternate labels
formiminoglutamic aciduria, glutamate formimino transferase deficiency, and
FIGLU.

The biochemical signature is increased urinary formiminoglutamic acid (FIGLU)
and increased urinary hydantoin-5-propionic acid. The characteristic clinical
block records no clinical significance, and IEMbase lists no treatments.

## DisMech phenotype coverage

There is no local DisMech entry for FTCD deficiency or FIGLU/formiminoglutamic
aciduria.

The fuzzy neighbor `Hereditary_Orotic_Aciduria.yaml` is a false positive. That
entry is UMPS-related pyrimidine biosynthesis disease. FTCD deficiency instead
sits at the histidine degradation and folate-linked formimino transfer step and
has FIGLU as its key marker.

## Concordance and completeness

Judgement: true unmapped record. The local knowledge base does not currently
have a disease-level target for FTCD deficiency.

This record should not be folded into hereditary orotic aciduria simply because
both names end in aciduria. The differentiators are FTCD versus UMPS, FIGLU
versus orotic acid, and the benign/no-clinical-significance interpretation in
the IEMbase cache.

## Curation actions

- Keep the record unmapped.
- Do not map to hereditary orotic aciduria.
- If curated later, model the FTCD enzymatic block and FIGLU/hydantoin-5-
  propionic acid biochemical readouts before adding clinical claims.
