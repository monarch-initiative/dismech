# IEMbase 0477: ALDOB-related aldolase B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 477 |
| Nosology | 3.1.02.03 |
| Gene | ALDOB |
| External IDs | OMIM:229600; ORPHA:469 |
| Generated mapping | MAPPED; high candidate `Hereditary_Fructose_Intolerance.yaml` |
| Candidate DisMech targets | `Hereditary_Fructose_Intolerance.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ALDOB-related aldolase B deficiency,
also called hereditary fructose intolerance and fructose-1-phosphate aldolase
deficiency. Biochemical rows include decreased hepatic fructose-1-phosphate
aldolase activity, increased transaminases, type I sialotransferrin pattern,
conjugated bilirubin elevation, decreased coagulation factors, low-to-normal
plasma glucose, low-to-normal magnesium and phosphate, variably increased
triglycerides and uric acid, and increased urinary glycerol. Clinical rows
include abdominal pain, steatorrhea, failure to thrive, abnormal feeding habits,
hepatomegaly, liver cirrhosis, liver failure, renal tubulopathy, and vomiting.
IEMbase records fructose-, sucrose-, and sorbitol-free diet as a nutritional
treatment.

## DisMech phenotype coverage

`Hereditary_Fructose_Intolerance.yaml` is the correct local target. The local
entry explicitly models biallelic ALDOB disease, autosomal recessive
inheritance, aldolase B deficiency in liver/kidney/intestine, fructose
catabolism failure, fructose-1-phosphate accumulation with ATP depletion,
hypoglycemia, vomiting, abdominal pain, diarrhea, hepatomegaly, renal tubular
dysfunction, liver failure, steatosis/metabolic complications, and lifelong
avoidance of fructose, sucrose, and sorbitol.

## Concordance and completeness

Judgement: correct ALDOB/hereditary fructose intolerance mapping with high
concordance.

The resources agree on gene, inheritance, disease identity, proximal
biochemical lesion, fructose-triggered metabolic toxicity, liver/kidney
phenotype, gastrointestinal symptoms, and diet treatment. IEMbase adds granular
prompts not fully represented locally, including type I sialotransferrin
pattern, conjugated bilirubin, coagulation factors, magnesium/phosphate,
triglycerides, uric acid, urinary glycerol, steatorrhea, and abnormal feeding
habits.

## Curation actions

- Keep the mapping to `Hereditary_Fructose_Intolerance.yaml`.
- If importing IEMbase-derived prompts, verify type I sialotransferrin pattern,
  conjugated bilirubin, coagulation-factor abnormalities, magnesium/phosphate,
  triglyceride and uric-acid rows, urinary glycerol, steatorrhea, and abnormal
  feeding habits against source evidence.
