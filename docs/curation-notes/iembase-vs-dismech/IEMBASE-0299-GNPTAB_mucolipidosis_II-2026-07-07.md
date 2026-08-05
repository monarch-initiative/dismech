# IEMbase 0299: GNPTAB-related UDP-N-acetylglucosamine-1-phosphotransferase subunit alpha/beta deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 299 |
| Nosology | 20.6.01.03 |
| Gene | GNPTAB |
| External IDs | OMIM:252500; ORPHA:576 |
| Generated mapping | MAPPED; `Mucolipidosis_Type_II.yaml` |
| Candidate DisMech targets | `Mucolipidosis_Type_II.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents mucolipidosis II alpha/beta / I-cell disease due to GNPTAB.
Inheritance is autosomal recessive and treatability is unknown.

Clinical rows include coarse facial features, corneal clouding, gingival
hypertrophy, hepatosplenomegaly, hernias, hip dislocation, axial hypotonia,
intellectual disability, speech disturbance, valvular thickening,
cardiomyopathy, foam cells, joint contractures, recurrent otitis media, and
psychomotor retardation. IEMbase also has neuroimaging rows for cortical
atrophy, subcortical atrophy, CNS hypomyelination, and thin corpus callosum.
Biochemical rows show very low fibroblast/RBC enzyme activity, high serum enzyme
activity, normal-to-increased urinary glycosaminoglycans, and markedly
increased urinary oligosaccharides.

## DisMech phenotype coverage

`Mucolipidosis_Type_II.yaml` is the correct local target. The local entry models
GNPTAB loss, GlcNAc-1-phosphotransferase deficiency, failure of mannose-6-
phosphate lysosomal targeting, hydrolase missorting/hypersecretion, multisystem
lysosomal substrate accumulation, skeletal/connective-tissue disease,
cardiorespiratory storage disease, and neuromotor developmental arrest.

Local phenotypes include coarse facial features, gingival overgrowth,
dysostosis multiplex, cardiac valve disease, respiratory insufficiency, growth
failure, joint contractures, kyphosis, thickened skin, developmental delay, and
autosomal recessive inheritance. Local diagnostic coverage includes plasma
lysosomal enzyme activity and GNPTAB sequencing.

## Concordance and completeness

Judgement: correct high-concordance mapping to `Mucolipidosis_Type_II.yaml`.

IEMbase and DisMech agree on GNPTAB identity, recessive inheritance, impaired
GlcNAc-1-phosphotransferase/M6P targeting, extracellular enzyme hypersecretion
with intracellular lysosomal deficiency, coarse facies, gingival overgrowth,
joint contractures, cardiac-valve disease, developmental delay, and severe
multisystem storage. DisMech is stronger for causal mechanism and the
cardiorespiratory/skeletal pathophysiology chain.

IEMbase adds granular review prompts for hepatosplenomegaly, hernias, hip
dislocation, recurrent otitis media, foam cells, speech disturbance, corneal
clouding, MRI cortical/subcortical atrophy, hypomyelination, thin corpus
callosum, urinary oligosaccharides, urinary GAGs, and the compartment-specific
enzyme pattern.

## Curation actions

- Keep this record mapped to `Mucolipidosis_Type_II.yaml`.
- Consider adding the IEMbase compartment-specific enzyme assay pattern and
  urinary oligosaccharide/GAG rows as diagnostic biochemical prompts.
- Review the neuroimaging, hepatosplenic, otitis, hernia, hip, speech, corneal,
  and foam-cell rows before importing.
