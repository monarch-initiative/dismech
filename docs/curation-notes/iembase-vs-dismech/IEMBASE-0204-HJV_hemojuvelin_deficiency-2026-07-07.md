# IEMbase 0204: HJV-related hemojuvelin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 204 |
| Nosology | 22.2.02.01 |
| Gene | HJV |
| External IDs | OMIM:602390; ORPHA:79230 |
| Generated mapping | CANDIDATE; `Hemochromatosis.yaml` |
| Candidate DisMech targets | `Hemochromatosis.yaml#Type 2A` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as HJV-related hemojuvelin deficiency, with alternate
labels hereditary hemochromatosis type 2A and HFE2A. Treatability is marked
yes.

The biochemical rows include increased ferritin, variable glucose, increased
liver iron, and increased transferrin saturation. Characteristic clinical rows
include arthralgia, cardiomyopathy, fatigue, hepatopathy, hypogonadism, and
liver cirrhosis. Treatment rows list iron chelation and phlebotomy, both
decreasing serum iron.

## DisMech phenotype coverage

`Hemochromatosis.yaml#Type 2A` is the correct target. The local entry explicitly
defines Type 2A as HJV-related juvenile hemochromatosis caused by biallelic HJV
pathogenic variants. It covers the non-HFE hepcidin-deficiency mechanism,
early/severe systemic iron overload, high transferrin saturation, elevated
ferritin, liver disease, cirrhosis, cardiomyopathy, diabetes/hyperglycemia,
hypogonadotropic hypogonadism, arthropathy, fatigue, abdominal pain, and iron
removal by phlebotomy or chelation.

## Concordance and completeness

Judgement: accept generated candidate as correct, with subtype resolution to
`Hemochromatosis.yaml#Type 2A`.

IEMbase and DisMech agree on HJV/type 2A juvenile hemochromatosis identity,
iron-overload biomarkers, hepatic disease, cardiomyopathy, endocrine disease,
arthralgia, phlebotomy, and chelation. IEMbase adds concise HJV-specific liver
iron and hepatopathy rows. DisMech is richer for the shared hepcidin pathway,
subtype differentiation, evidence, penetrance and modifier framing, and
treatment rationale.

## Curation actions

- Treat this as covered by `Hemochromatosis.yaml#Type 2A`, not only the file
  level.
- Consider adding liver iron as a structured readout if the hemochromatosis
  biochemical section is expanded.
- No standalone HJV entry is required unless future curation chooses to split
  juvenile hemochromatosis subtypes into separate disease files.
