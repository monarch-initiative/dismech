# IEMbase 0257: APTX-related Aprataxin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 257 |
| Nosology | 8.1.13.01 |
| Gene | APTX |
| External IDs | OMIM:606350; ORPHA:1168 |
| Generated mapping | MAPPED; `Ataxia_Telangiectasia.yaml#AOA1` |
| Candidate DisMech targets | `Ataxia_Telangiectasia.yaml#AOA1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as APTX-related aprataxin deficiency, with alternate
labels secondary coenzyme Q10 deficiency, ataxia oculomotor apraxia 1, and
AOA1. The record is autosomal recessive and treatability is marked unknown,
with no treatment rows in the cached JSON.

The cached phenotype signal is sparse. Biochemical rows include serum albumin,
coded as increased in childhood, adolescence, and adulthood. The clinical row
contains cognitive dysfunction. No characteristic rows are present in the cached
JSON.

## DisMech phenotype coverage

`Ataxia_Telangiectasia.yaml#AOA1` is the correct local target. The local subtype
defines AOA1 as APTX-related autosomal recessive cerebellar ataxia with
oculomotor apraxia, axonal sensorimotor neuropathy, and hypoalbuminemia with
hypercholesterolemia. It places AOA1 within a broader DNA-repair ataxia
differential where telangiectasia, immunodeficiency, and cancer predisposition
are absent.

## Concordance and completeness

Judgement: correct subtype-level mapping, but IEMbase is much less complete
than DisMech and has a lab-direction issue to review.

IEMbase and DisMech agree on the APTX/AOA1 identity and autosomal recessive
inheritance. DisMech is much richer for the defining phenotype and mechanism:
aprataxin/DNA single-strand break repair, cerebellar ataxia, oculomotor
apraxia, axonal neuropathy, hypoalbuminemia, and hypercholesterolemia. IEMbase's
serum albumin row is coded increased, which conflicts with the local subtype
description and AOA1 label emphasizing hypoalbuminemia.

## Curation actions

- Keep this record mapped to `Ataxia_Telangiectasia.yaml#AOA1`.
- Review the IEMbase serum albumin direction before using it as a curation lead.
- Treat the secondary CoQ10 deficiency synonym as a context cue only; the cached
  JSON does not include CoQ10 biochemical or treatment rows.
