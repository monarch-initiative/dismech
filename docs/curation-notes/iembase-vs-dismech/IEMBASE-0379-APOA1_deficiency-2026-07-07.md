# IEMbase 0379: APOA1-related Apolipoprotein A-I deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 379 |
| Nosology | 15.4.24.01 |
| Gene | APOA1 |
| External IDs | OMIM:107680; ORPHA:93560 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents APOA1-related apolipoprotein A-I deficiency, also listed as
hypoalphalipoproteinemia. Inheritance is listed as autosomal dominant.

Clinical rows are sparse and adult-focused, including coronary artery disease
and xanthelasma. Biochemical rows emphasize normal serum cholesterol, very low
plasma HDL cholesterol, normal-to-increased serum triglyceride in adolescence
and adulthood, and very low apolipoprotein A-I level. There are no treatment
rows.

## DisMech phenotype coverage

There is no exact local DisMech target for APOA1-related apolipoprotein A-I
deficiency. `Tangier_Disease.yaml` overlaps on the low HDL cholesterol, low
apolipoprotein A-I, and hypoalphalipoproteinemia vocabulary, but it models
biallelic ABCA1-related Tangier disease with ABCA1-mediated HDL biogenesis
failure, orange tonsils, tissue cholesteryl ester storage, hepatosplenomegaly,
and peripheral neuropathy. That is not the same disease mechanism as primary
APOA1 deficiency.

The separate APOA1 amyloidosis record in IEMbase maps to amyloidosis context,
but that does not provide a lipid-deficiency target for this record.

## Concordance and completeness

Judgement: true local gap; keep unmapped.

The IEMbase disease is a primary APOA1 apolipoprotein deficiency with very low
HDL/ApoA-I and adult coronary/xanthelasma findings. The closest local lipid
entries are mechanistically different and should not absorb this record just
because they share hypoalphalipoproteinemia or low ApoA-I terms.

## Curation actions

- Keep this record unmapped until an APOA1/apolipoprotein A-I deficiency target
  exists.
- Do not map to `Tangier_Disease.yaml`; use Tangier only as differential lipid
  context.
- If curated, include autosomal dominant inheritance, HDL cholesterol,
  apolipoprotein A-I level, triglyceride directionality, coronary artery
  disease, and xanthelasma as review prompts.
