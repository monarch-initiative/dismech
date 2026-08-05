# IEMbase 0376: LIPC-related hepatic lipase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 376 |
| Nosology | 15.3.19.01 |
| Gene | LIPC |
| External IDs | OMIM:612797; OMIM:614025; ORPHA:140905 |
| Generated mapping | UNMAPPED; low candidate `Hepatic_Veno-occlusive_Disease-Immunodeficiency_Syndrome.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents LIPC-related hepatic lipase deficiency, also listed as HL
deficiency. Inheritance is autosomal recessive.

Clinical rows include coronary artery disease and myocardial ischemia.
Biochemical rows include post-heparin hepatic lipase activity, serum
cholesterol, plasma HDL cholesterol, broad-beta lipoprotein electrophoresis,
and serum triglyceride. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for LIPC-related hepatic lipase
deficiency. The generated low candidate
`Hepatic_Veno-occlusive_Disease-Immunodeficiency_Syndrome.yaml` is a lexical
false positive: that file models SP110-related primary immunodeficiency with
hepatic sinusoidal/terminal venular occlusion and fibrosis. It does not model
hepatic lipase activity, LIPC, lipoprotein remodeling, broad-beta
lipoproteinemia, or hyperalphalipoproteinemia.

Local atherosclerotic disease files may provide downstream cardiovascular
context, but they are not valid disease mappings for the inherited lipase
defect.

## Concordance and completeness

Judgement: true local gap; reject the hepatic veno-occlusive disease candidate.

The IEMbase record is a lipoprotein-metabolism disorder caused by LIPC, whereas
the generated candidate is an immunodeficiency/liver vascular-occlusion
syndrome caused by SP110. The shared word "hepatic" is not sufficient for
mapping.

## Curation actions

- Keep this record unmapped until a LIPC hepatic lipase deficiency target
  exists.
- Do not map to `Hepatic_Veno-occlusive_Disease-Immunodeficiency_Syndrome.yaml`.
- If curated, prioritize hepatic lipase activity after heparin, broad-beta
  lipoprotein electrophoresis, high HDL cholesterol, cholesterol/triglyceride
  abnormalities, and coronary disease risk.
