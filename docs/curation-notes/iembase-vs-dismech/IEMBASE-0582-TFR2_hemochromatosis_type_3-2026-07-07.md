# IEMbase 0582: TFR2-related transferrin receptor 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 582 |
| Nosology | 22.2.04.01 |
| Gene | TFR2 |
| External IDs | OMIM:604250; ORPHA:225123 |
| Generated mapping | MAPPED; `Hemochromatosis.yaml` |
| Candidate DisMech targets | `Hemochromatosis.yaml#Type 3` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TFR2-related transferrin receptor 2 deficiency, corresponding
to hereditary hemochromatosis type 3 / HFE3. The record is autosomal recessive,
classified under disorders of iron metabolism, marked as a juvenile subtype,
has unknown treatability, and lists iron chelation and phlebotomy.

Biochemical rows include normal-to-increased ferritin, normal-to-increased
transferrin saturation, normal-to-increased glucose, and normal-to-increased
liver iron. Clinical rows include abdominal pain and hyperpigmentation.

## DisMech phenotype coverage

`Hemochromatosis.yaml` is the correct local target, specifically the Type 3
subtype. It models biallelic TFR2-related hemochromatosis, increased intestinal
iron absorption, liver/heart/pancreas/endocrine organ iron accumulation,
transferrin saturation and ferritin elevation, abdominal pain, bronze
hyperpigmentation, diabetes or hyperglycemia, and phlebotomy with chelation as
a selected alternative.

## Concordance and completeness

Judgement: correct subtype-level mapping.

IEMbase and DisMech agree on TFR2, autosomal recessive type 3 hemochromatosis,
iron-index abnormalities, liver iron loading, glucose involvement,
hyperpigmentation, abdominal pain, and iron-depletion therapy. The
normal-to-increased IEMbase rows are useful because they preserve variable stage
or penetrance at individual biomarker level.

## Curation actions

- Resolve this record to `Hemochromatosis.yaml#Type 3`.
- Preserve IEMbase normal-to-high ferritin, transferrin-saturation, glucose,
  and liver-iron staging prompts for future subtype review.
