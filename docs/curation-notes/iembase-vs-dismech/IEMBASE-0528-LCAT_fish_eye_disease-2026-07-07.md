# IEMbase 0528: LCAT-related fish-eye disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 528 |
| Nosology | 15.4.22.02 |
| Gene | LCAT |
| External IDs | OMIM:136120; OMIM:606967; ORPHA:79292 |
| Generated mapping | UNMAPPED; low candidate `Carnitine_Palmitoyltransferase_II_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents partial familial lecithin cholesterol acyl transferase
deficiency, with fish-eye disease and FED as alternate labels. The record is
autosomal recessive, subtype is marked idiopathic, and no treatments are listed.

Characteristic rows include decreased fibroblast LCAT activity, very low HDL
cholesterol, very low apolipoprotein A-I, normal unesterified plasma
cholesterol, normal cholesterol esterification rate, normal urinary protein,
normal creatinine, and normal to increased serum triglycerides. Clinical
characteristic rows include arcus cornealis, corneal clouding, and corneal
deposits.

## DisMech phenotype coverage

There is no exact local DisMech target for LCAT-related fish-eye disease. The
generated candidate `Carnitine_Palmitoyltransferase_II_Deficiency.yaml` is a
fatty-acid oxidation disorder and does not model LCAT, cholesterol
esterification, ApoA-I/HDL depletion, or corneal lipid deposition.

This record is related to the earlier IEMbase LCAT deficiency gap, but it is the
partial/fish-eye phenotype rather than the classic renal LCAT deficiency
phenotype.

## Concordance and completeness

Judgement: true local gap; reject the carnitine palmitoyltransferase II
candidate.

The IEMbase record should not be collapsed into a generic lipid disorder or a
fatty-acid oxidation disease. A future local LCAT entry should decide whether to
model classic LCAT deficiency and fish-eye disease as subtypes or closely
related spectrum records.

## Curation actions

- Keep this record unmapped until an LCAT fish-eye disease or LCAT deficiency
  spectrum target exists.
- Do not map to `Carnitine_Palmitoyltransferase_II_Deficiency.yaml`.
- Preserve the partial-LCAT pattern: low LCAT activity, very low HDL/ApoA-I,
  relatively normal renal/unesterified-cholesterol rows, and corneal
  clouding/deposit/arcus prompts.
