# IEMbase 0549: ADK-related adenosine kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 549 |
| Nosology | 1.5.05.01 |
| Gene | ADK |
| External IDs | OMIM:614300; ORPHA:289290 |
| Generated mapping | MAPPED; `Adenosine_Kinase_Deficiency.yaml` |
| Candidate DisMech targets | `Adenosine_Kinase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ADK-related adenosine kinase deficiency, also labeled
hypermethioninemia due to adenosine kinase deficiency and ADKD. The record is
autosomal recessive, and treatability is unknown. No treatment rows are listed.

The biochemical rows emphasize increased plasma methionine, increased urinary
adenosine, increased plasma S-adenosylhomocysteine and S-adenosylmethionine,
normal-to-increased total homocysteine, increased ALAT, normal-to-increased
creatine kinase and prothrombin time, neonatal conjugated bilirubin, low-normal
glucose, and normal-to-increased urinary uric acid. Characteristic clinical
rows are developmental delay, frontal bossing, and hypotonia. Additional rows
include cardiac malformations, intrahepatic cholestasis, epilepsy, failure to
thrive, sensorineural hearing loss, hypoglycemia, liver dysfunction, liver
steatosis, macrocephaly, progressive muscle weakness, short stature, slender
hands and feet, and thin corpus callosum.

## DisMech phenotype coverage

`Adenosine_Kinase_Deficiency.yaml` is the correct target. The local entry
models biallelic ADK loss, impaired adenosine phosphorylation to AMP, disrupted
adenosine salvage, methionine-cycle disturbance, hypermethioninemia, hepatic
disease, developmental delay, epilepsy, hypotonia, dysmorphic features,
mitochondrial respiratory-chain abnormalities, cerebrovascular abnormalities,
and cardiac findings.

Local biomarker coverage includes elevated plasma methionine and elevated
S-adenosylhomocysteine as diagnostic signals, with ADK sequencing for
confirmation.

## Concordance and completeness

Judgement: correct high-concordance mapping to
`Adenosine_Kinase_Deficiency.yaml`.

IEMbase and DisMech agree on ADK identity, recessive inheritance,
hypermethioninemia, adenosine/methionine-cycle disruption, liver disease,
developmental delay, epilepsy, hypotonia, dysmorphic features, cardiac
involvement, and diagnostic molecular confirmation. DisMech is stronger for the
causal chain from ADK loss to adenosine salvage and methionine-cycle
perturbation.

IEMbase adds granular review prompts for urinary adenosine, SAM/SAH direction,
ALAT, prothrombin time, creatine kinase, glucose, uric acid, liver steatosis,
frontal bossing, slender hands and feet, thin corpus callosum, hearing loss,
and muscle weakness.

## Curation actions

- Keep this record mapped to `Adenosine_Kinase_Deficiency.yaml`.
- Consider adding IEMbase compartment-specific adenosine, SAM/SAH, liver,
  coagulation, glucose, uric-acid, hearing, and neuroimaging prompts after
  source review.
- Preserve the no-treatment-row status; do not infer a disease-modifying
  therapy from the IEMbase cache.
