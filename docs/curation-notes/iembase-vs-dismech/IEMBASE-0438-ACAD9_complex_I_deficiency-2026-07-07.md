# IEMbase 0438: ACAD9-related Acyl-CoA dehydrogenase 9 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 438 |
| Nosology | 7.1.09.01 |
| Gene | ACAD9 |
| External IDs | OMIM:611126; ORPHA:99901 |
| Generated mapping | UNMAPPED; low candidate `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `ACAD9_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ACAD9 deficiency as a complex I assembly
disorder with hypoglycemia and lactic acidosis. Biochemical rows include
increased plasma and urine lactate, increased lactate/pyruvate ratio, increased
alanine, decreased free carnitine, increased long-chain acylcarnitines, increased
creatine kinase, transaminase elevation, ketosis-related organic acids,
hyperammonemia, and hypoglycemia. Clinical rows include dilated cardiomyopathy,
encephalopathy, exercise intolerance, failure to thrive, hearing loss, axial
hypotonia, liver dysfunction or failure including Reye-like liver failure,
neurologic dysfunction, rhabdomyolysis, and skeletal myopathy. IEMbase records
riboflavin as a treatment row.

## DisMech phenotype coverage

`ACAD9_Deficiency.yaml` is the correct local target. It describes biallelic
ACAD9 disease as a mitochondrial complex I assembly-factor disorder, not as a
primary fatty-acid beta-oxidation defect, and covers complex I deficiency,
oxidative phosphorylation failure, cardiomyopathy, exercise intolerance, lactic
acidosis, muscular weakness, and riboflavin responsiveness.

The generated `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` candidate is a false
positive. Local GCDH deficiency is glutaric acidemia type 1, with lysine,
hydroxylysine, and tryptophan catabolism, glutaric acid and
3-hydroxyglutaric acid biomarkers, and encephalopathic crises. It does not
represent ACAD9 complex I assembly disease.

## Concordance and completeness

Judgement: false negative; resolve IEMbase 438 to `ACAD9_Deficiency.yaml`.

The local target has high mechanism and treatment concordance for the core
complex I/riboflavin-responsive disorder. IEMbase adds useful phenotypic prompts
for long-chain acylcarnitines, hypoglycemia, liver dysfunction, Reye-like liver
failure, rhabdomyolysis, and hearing loss that should be checked against primary
evidence before import.

## Curation actions

- Map IEMbase 438 to `ACAD9_Deficiency.yaml`.
- Do not map to `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml`.
- If importing IEMbase-derived prompts, prioritize ACAD9 complex I assembly,
  lactic acidosis, cardiomyopathy, skeletal myopathy, exercise intolerance,
  riboflavin responsiveness, and verify the liver, hearing, rhabdomyolysis,
  hypoglycemia, and acylcarnitine rows against source evidence.
