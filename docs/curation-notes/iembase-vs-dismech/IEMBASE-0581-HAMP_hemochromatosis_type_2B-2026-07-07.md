# IEMbase 0581: HAMP-related hepcidin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 581 |
| Nosology | 22.2.03.01 |
| Gene | HAMP |
| External IDs | OMIM:602390; ORPHA:79230 |
| Generated mapping | MAPPED; `Hemochromatosis.yaml` |
| Candidate DisMech targets | `Hemochromatosis.yaml#Type 2B` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents HAMP-related hepcidin deficiency, corresponding to hereditary
hemochromatosis type 2B / HFE2B. The record is autosomal recessive, classified
under disorders of iron metabolism, marked as a juvenile subtype, flagged as
treatable, and lists iron chelation and phlebotomy.

Biochemical rows include increased serum ferritin, increased plasma glucose,
increased transferrin saturation, and increased liver iron.

## DisMech phenotype coverage

`Hemochromatosis.yaml` is the correct local target, specifically the Type 2B
subtype. It models juvenile-onset autosomal recessive HAMP-related
hemochromatosis, hepcidin insufficiency, increased intestinal iron absorption,
elevated transferrin saturation and ferritin, progressive iron accumulation in
liver and other organs, diabetes/hyperglycemia, and iron-depletion therapy by
phlebotomy or chelation when appropriate.

## Concordance and completeness

Judgement: correct subtype-level mapping.

IEMbase and DisMech agree on HAMP, autosomal recessive juvenile
hemochromatosis, hepcidin-pathway failure, transferrin saturation, ferritin,
liver iron, glucose/diabetes risk, phlebotomy, and chelation. DisMech is
stronger for systemic iron-distribution mechanism and downstream organ damage.

IEMbase provides a compact biomarker checklist for type 2B: ferritin, plasma
glucose, transferrin saturation, and liver iron.

## Curation actions

- Resolve this record to `Hemochromatosis.yaml#Type 2B`.
- Preserve the IEMbase subtype-specific iron-index and glucose rows as review
  prompts for any future HAMP branch enrichment.
