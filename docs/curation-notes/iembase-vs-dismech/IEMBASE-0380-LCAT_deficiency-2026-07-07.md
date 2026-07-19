# IEMbase 0380: LCAT-related Familial lecithin cholesterol acyl transferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 380 |
| Nosology | 15.4.22.01 |
| Gene | LCAT |
| External IDs | OMIM:606967; OMIM:245900; ORPHA:79292 |
| Generated mapping | UNMAPPED; low candidate `Lipoyl_Transferase_1_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive familial lecithin cholesterol acyl
transferase deficiency, with alternate names lecithin cholesterol acyl
transferase deficiency and LCAT deficiency.

Clinical rows include arcus cornealis, corneal clouding/deposits, and adult
kidney failure. Biochemical rows include very low fibroblast LCAT activity,
very low cholesterol esterification rate, increased unesterified plasma
cholesterol, low HDL cholesterol, low apolipoprotein A-I, increased adult
creatinine and urinary total protein, renal biopsy findings, and serum
triglyceride elevation. Treatment rows list corticosteroids, lipid-lowering
drugs, kidney transplantation, and renin-angiotensin-aldosterone system
blockers.

## DisMech phenotype coverage

There is no exact local DisMech target for LCAT deficiency. The generated
candidate `Lipoyl_Transferase_1_Deficiency.yaml` is a lexical false positive:
it models LIPT1-related mitochondrial lipoylation failure with dehydrogenase
complex dysfunction, lactic acidosis, and Leigh-like encephalopathy, not LCAT
cholesterol esterification.

No current lipid disorder file captures the LCAT enzyme defect, corneal
deposition, renal disease, and unesterified-cholesterol biochemical pattern as
a disease-level entry.

## Concordance and completeness

Judgement: true local gap; reject the lipoyl transferase candidate.

The IEMbase record is an LCAT cholesterol-esterification disorder. The local
candidate is a mitochondrial protein-lipoylation disease with a different gene,
pathway, clinical phenotype, and diagnostic biomarker set.

## Curation actions

- Keep this record unmapped until a familial LCAT deficiency target exists.
- Do not map to `Lipoyl_Transferase_1_Deficiency.yaml`.
- Future curation should preserve LCAT activity, cholesterol esterification
  rate, unesterified cholesterol, HDL/ApoA-I, renal, corneal, and treatment
  rows. A later IEMbase fish-eye/partial LCAT record should be reviewed for
  spectrum splitting rather than collapsed silently into this note.
