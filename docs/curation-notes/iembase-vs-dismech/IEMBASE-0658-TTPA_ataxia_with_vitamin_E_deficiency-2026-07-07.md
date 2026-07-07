# IEMbase 0658: TTPA-related alpha-tocopherol transfer protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 658 |
| Nosology | 21.11.01.02 |
| Nosology code | IEM0270 |
| Gene | TTPA |
| External IDs | OMIM:277460; ORPHA:96 |
| Generated mapping | MAPPED to `Familial_Isolated_Vitamin_E_Deficiency.yaml` |
| Candidate DisMech targets | `Familial_Isolated_Vitamin_E_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive TTPA-related alpha-tocopherol transfer
protein deficiency, also labeled ataxia with isolated vitamin E deficiency
(AVED). Treatability is marked yes.

Biochemical rows include decreased plasma vitamin E from childhood onward,
adolescent/adult increases in cholesterol and triglyceride, and broad beta
lipoprotein electrophoresis. Clinical rows include adolescent/adult ataxia,
brain MRI abnormality, dystonia, optional areflexia, optional dysarthria, and
adult xanthomas.

## DisMech phenotype coverage

`Familial_Isolated_Vitamin_E_Deficiency.yaml` is the correct local target. It
models TTPA/alpha-TTP loss, impaired hepatic alpha-tocopherol transfer into
lipoproteins, systemic vitamin E deficiency, oxidative neuronal injury,
progressive ataxia, proprioceptive/sensory involvement, areflexia, dysarthria,
dystonia, retinal disease, occasional cardiomyopathy, and vitamin E
supplementation.

The DisMech entry is stronger than IEMbase for mechanistic detail and treatment
rationale. IEMbase adds compact age-banded prompts for brain MRI abnormality,
adult xanthomas, hypercholesterolemia, hypertriglyceridemia, and broad beta
lipoprotein electrophoresis that are not prominent in the local entry.

## Concordance and completeness

Judgement: correct exact mapping with high concordance.

The gene, disease name, inheritance, key biochemical readout, and neurologic
phenotype are aligned. Remaining differences are mostly granularity: IEMbase
tracks some lipid/lipoprotein and imaging rows that could be reviewed if the
DisMech AVED entry is expanded.

## Curation actions

- Accept `Familial_Isolated_Vitamin_E_Deficiency.yaml` as the disease-level
  target.
- Preserve IEMbase prompts for low vitamin E, ataxia, dystonia, areflexia,
  dysarthria, brain MRI abnormality, xanthomas, cholesterol, triglyceride, and
  broad beta lipoprotein electrophoresis.
- If updating the local entry later, review whether lipid/xanthoma findings are
  disease-core, modifier, or source-specific.
