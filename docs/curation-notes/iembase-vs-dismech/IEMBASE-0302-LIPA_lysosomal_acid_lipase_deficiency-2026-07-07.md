# IEMbase 0302: LIPA-related Lysosomal acid lipase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 302 |
| Nosology | 20.6.03.01 |
| Gene | LIPA |
| External IDs | OMIM:278000; ORPHA:275761 |
| Generated mapping | MAPPED; `Cholesteryl_Ester_Storage_Disease.yaml` |
| Candidate DisMech targets | `Wolman_Disease.yaml`; `Cholesteryl_Ester_Storage_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents the lysosomal acid lipase deficiency spectrum and names both
Wolman disease and cholesteryl ester storage disease. Inheritance is autosomal
recessive and treatability is unknown in the cached record.

Clinical rows combine infantile and later-onset spectrum features: adrenal
calcification, anemia, severe atherosclerosis, hepatosplenomegaly,
thrombocytopenia, abdominal distension, developmental delay, failure to thrive,
hemophagocytosis, hepatocellular carcinoma/hepatoblastoma, pulmonary
hypertension, spiculated red cells, steatorrhea, and vomiting. Biochemical rows
show markedly decreased acid lipase activity in neonatal/infantile rows and
decreased activity later, plus normal-to-increased serum cholesterol and
triglyceride.

## DisMech phenotype coverage

The generated CESD mapping is valid for the later-onset portion of the IEMbase
record but incomplete for the full label. Local DisMech has separate entries for
the main LIPA spectrum ends: `Wolman_Disease.yaml` and
`Cholesteryl_Ester_Storage_Disease.yaml`.

`Wolman_Disease.yaml` models rapidly progressive infantile LAL deficiency with
severe loss of LIPA activity, cholesteryl ester and triglyceride storage,
hepatic/reticuloendothelial lipid storage, intestinal lipid storage,
malabsorption, adrenal cortical lipid storage, failure to thrive,
hepatosplenomegaly, hepatic failure, diarrhea, vomiting, malabsorption, adrenal
calcification, anemia, reduced LAL activity, storage burden, elevated hepatic
transaminases, sebelipase alfa, and nutritional management. `Cholesteryl_Ester_Storage_Disease.yaml`
models the milder later-onset LAL deficiency phenotype with residual activity,
hepatomegaly, splenomegaly, elevated transaminases, dyslipidemia, hepatic
steatosis, hepatic fibrosis/cirrhosis, atherogenic dyslipidemia, LIPA variants,
and sebelipase alfa.

## Concordance and completeness

Judgement: split the IEMbase spectrum record across `Wolman_Disease.yaml` and
`Cholesteryl_Ester_Storage_Disease.yaml`; do not treat the generated CESD
mapping as complete.

IEMbase and DisMech agree on LIPA identity, recessive inheritance, low acid
lipase activity, neutral-lipid storage, hepatosplenomegaly, infantile failure
to thrive/vomiting/adrenal calcification/anemia, and later-onset dyslipidemia
with serum cholesterol/triglyceride abnormalities. DisMech is richer for
mechanism, the Wolman-versus-CESD split, hepatic failure and malabsorption,
enzyme replacement, and dietary management.

IEMbase adds review prompts for thrombocytopenia, abdominal distension,
developmental delay, hemophagocytosis, hepatocellular carcinoma or
hepatoblastoma, pulmonary hypertension, spiculated red cells, steatorrhea, and
severe atherosclerosis. These should be placed carefully by phenotype end of the
LIPA spectrum if imported.

## Curation actions

- Treat IEMbase 302 as a spectrum record spanning `Wolman_Disease.yaml` and
  `Cholesteryl_Ester_Storage_Disease.yaml`.
- Add subtype-specific placement notes if future mapping infrastructure can
  represent both LIPA spectrum endpoints.
- Review IEMbase-only hematologic, cancer, pulmonary-hypertension, red-cell,
  steatorrhea, abdominal-distension, and atherosclerosis rows before import.
