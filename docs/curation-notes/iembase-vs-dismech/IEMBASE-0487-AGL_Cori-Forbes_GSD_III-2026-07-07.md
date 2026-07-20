# IEMbase 0487: AGL-related amylo-1,6-glucosidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 487 |
| Nosology | 3.4.06.01 |
| Gene | AGL |
| External IDs | OMIM:232400; ORPHA:366 |
| Generated mapping | UNMAPPED; best candidate `Cori_Forbes_Disease.yaml` |
| Candidate DisMech targets | `Cori_Forbes_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive AGL-related amylo-1,6-glucosidase
debrancher deficiency as glycogen storage disease type III / Cori-Forbes
disease / limit dextrinosis. Treatments are high-protein diet and uncooked
cornstarch. Biochemical rows include increased ASAT/ALAT, decreased hepatic and
white-blood-cell amylo-1,6-glucosidase activity, increased biotinidase,
normal-to-increased creatine kinase, increased fasted plasma and urine ketones,
increased liver glycogen, increased cholesterol, decreased fasting plasma
glucose, normal lactate, increased triglycerides, and normal uric acid. Clinical
rows include doll-like adiposity, biliary cirrhosis, cardiomyopathy, delayed
tooth eruption, exercise intolerance, liver adenoma/carcinoma/fibrosis, muscle
weakness, osteopenia, short stature, and taurodontism.

## DisMech phenotype coverage

`Cori_Forbes_Disease.yaml` is the exact local target. The entry models AGL
glycogen debranching enzyme deficiency, the dual transferase and glucosidase
activities, limit-dextrin/glycogen accumulation in liver, skeletal muscle, and
cardiac muscle, GSD IIIa and IIIb subtypes, hepatomegaly, fasting ketotic
hypoglycemia, hyperlipidemia, transaminase elevation, elevated cholesterol and
triglycerides, elevated glucose tetrasaccharide, myopathy, hypertrophic
cardiomyopathy, creatine kinase, hepatic fibrosis/cirrhosis/HCC, high-protein
and uncooked cornstarch dietary management, liver transplantation, and genetic
counseling.

## Concordance and completeness

Judgement: false negative generated mapping; resolve to
`Cori_Forbes_Disease.yaml`.

The best candidate is the correct disease despite the generated UNMAPPED status.
IEMbase and DisMech agree on AGL/GSD III identity, recessive inheritance,
debranching enzyme deficiency, ketotic fasting hypoglycemia with normal lactate,
hepatic glycogen storage, transaminase and lipid abnormalities, muscle/cardiac
involvement, liver fibrosis/tumor complications, and high-protein/cornstarch
management. IEMbase adds granular prompts such as WBC amylo-1,6-glucosidase,
biotinidase, delayed tooth eruption, taurodontism, osteopenia, and doll-like
adiposity.

## Curation actions

- Treat this as covered by `Cori_Forbes_Disease.yaml`.
- If importing IEMbase-derived prompts, verify WBC enzyme testing, biotinidase,
  delayed tooth eruption, taurodontism, osteopenia, and doll-like adiposity.
- Consider adding explicit synonym / mapping hints so future automated matching
  treats GSD III, Cori-Forbes disease, limit dextrinosis, and AGL debrancher
  deficiency as exact aliases.
