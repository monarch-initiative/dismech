# IEMbase 0026: AHCY-related S-adenosylhomocysteine hydrolase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 26 |
| Nosology | 1.5.04.01 |
| Gene | AHCY |
| External IDs | OMIM:613752 |
| Generated mapping | UNMAPPED; best fuzzy candidate `Cholesteryl_Ester_Storage_Disease.yaml` |
| Candidate DisMech targets | none currently valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents inherited S-adenosylhomocysteine hydrolase deficiency. The
characteristic clinical signals are coagulopathy, developmental delay, muscle
weakness, and myopathy. Additional findings include absent or weak tendon
reflexes, attention disorder, hyperactivity, aggressive behavior, fetal hydrops,
cerebellar hypoplasia, pontine hypoplasia, corpus callosum hypoplasia, delayed
myelination, liver dysfunction, hepatocellular carcinoma/hepatoblastoma signal,
reduced protein synthesis, respiratory insufficiency from muscle weakness or
diaphragm paralysis, and strabismus.

The biochemical signal is distinctive: markedly elevated
S-adenosylhomocysteine and S-adenosylmethionine, elevated creatine kinase,
variable hypermethioninemia and homocysteine, transaminase elevation, prolonged
prothrombin time, and low-to-normal albumin. Treatments listed by IEMbase include
a creatinine-labeled nutritional treatment, methionine restriction,
phosphatidylcholine, and liver transplantation.

## DisMech phenotype coverage

There is no current DisMech entry or subtype for AHCY deficiency. The generated
fuzzy candidate `Cholesteryl_Ester_Storage_Disease.yaml` is a false positive.
CESD is a lysosomal acid lipase/LIPA disorder with cholesteryl ester and
triglyceride storage, hepatosplenomegaly, dyslipidemia, hepatic steatosis and
fibrosis, and sebelipase alfa therapy. It does not model the methylation-cycle,
myopathic, neurologic, and SAH/SAM biochemical pattern of AHCY deficiency.

`Adenosine_Kinase_Deficiency.yaml` mentions AHCY-related metabolic disturbance
in differential context, but it is also not AHCY deficiency and should not be
used as the disease target.

## Concordance and completeness

Judgement: generated status is correctly unmapped; the CESD fuzzy candidate is
not biologically defensible.

IEMbase indicates a future AHCY curation target would need to combine
methylation-cycle biochemistry, liver/coagulation disease, myopathy, early
neurodevelopmental/imaging features, and possible liver-directed therapies.

## Curation actions

- Do not map this record to `Cholesteryl_Ester_Storage_Disease.yaml`.
- Consider a future AHCY deficiency entry or subtype in the inherited
  methylation/methionine-cycle area.
- If curated, resolve the IEMbase treatment label carefully; the JSON says
  `Creatinine`, but this may need source-level review before reuse.
