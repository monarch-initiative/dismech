# IEMbase 0483: FBP1-related fructose-1,6-bisphosphatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 483 |
| Nosology | 3.2.02.01 |
| Gene | FBP1 |
| External IDs | OMIM:229700; ORPHA:348 |
| Generated mapping | UNMAPPED; best candidate `Hereditary_Fructose_Intolerance.yaml` |
| Candidate DisMech targets | No exact local target; rejected candidate `Hereditary_Fructose_Intolerance.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive FBP1-related fructose-1,6-bisphosphatase
deficiency. Treatments are dietary fructose/sucrose avoidance and uncooked
cornstarch. Biochemical rows include increased plasma alanine, decreased hepatic
fructose-1,6-bisphosphatase activity, increased plasma and urine ketones,
decreased plasma glucose, increased plasma lactate, low-to-normal phosphate,
normal-to-increased triglycerides and uric acid, and normal-to-increased urinary
glycerol. The only clinical row in this record is tachypnea.

## DisMech phenotype coverage

No exact DisMech disease file was found for FBP1 fructose-1,6-bisphosphatase
deficiency. `Hereditary_Fructose_Intolerance.yaml` models ALDOB-related aldolase
B deficiency with fructose-1-phosphate accumulation after fructose exposure, not
FBP1 loss of hepatic gluconeogenesis. `Type_2_Diabetes_Mellitus.yaml` mentions
FBP1 only as a metformin target in hepatic gluconeogenesis, and
`Glycogen_Storage_Disease_Type_VII.yaml` references the adjacent glycolytic
fructose-6-phosphate to fructose-1,6-bisphosphate step, not FBP1 deficiency.

## Concordance and completeness

Judgement: true local gap; reject hereditary fructose intolerance as an exact
mapping.

FBP1 deficiency and ALDOB/HFI share fructose-related vocabulary and
hypoglycemia, but the causal lesions are different. FBP1 deficiency blocks a
gluconeogenic step and presents with fasting/illness-related hypoglycemia,
lactic acidosis, ketosis, and alanine elevation; HFI is an ALDOB fructose
catabolism defect with fructose-1-phosphate accumulation and toxicity after
fructose/sucrose/sorbitol exposure. The overlap is useful context, not coverage.

## Curation actions

- Create a future DisMech entry for FBP1-related fructose-1,6-bisphosphatase
  deficiency / ORPHA:348 if this disorder is prioritized.
- Do not map this row to `Hereditary_Fructose_Intolerance.yaml`.
- Evidence review should focus on FBP1 loss, impaired gluconeogenesis, fasting
  hypoglycemia, lactic acidosis, ketosis, alanine elevation, cornstarch, and
  fructose/sucrose restriction.
