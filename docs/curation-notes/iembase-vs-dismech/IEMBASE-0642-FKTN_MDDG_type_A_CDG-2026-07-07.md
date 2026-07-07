# IEMbase 0642: FKTN-related muscular dystrophy-dystroglycanopathy type A

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 642 |
| Nosology | 18.2.08.01 |
| Gene | FKTN |
| External IDs | OMIM:253800; ORPHA:272 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents FKTN-CDG type A / Fukuyama congenital muscular dystrophy as
an autosomal recessive congenital dystroglycanopathy with brain and eye
anomalies.

Biochemical rows include markedly increased plasma creatine kinase, normal
serum sialotransferrins, and abnormal matriglycan-specific antibody readout.
Clinical and characteristic rows include agyria, pachygyria, cobblestone
lissencephaly, Walker-Warburg syndrome, muscle-eye-brain disease, corpus
callosum abnormalities, brainstem hypoplasia, cerebellar abnormalities,
hydrocephalus, polymicrogyria, psychomotor regression, epilepsy, hypotonia,
muscular dystrophy, contractures, calf muscle hypertrophy, dilated
cardiomyopathy, respiratory insufficiency from muscle weakness or diaphragm
paralysis, scoliosis, cataract, chorioretinal degeneration, optic atrophy, and
microphthalmia.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` includes `MDDG4 (FKTN)`, describing fukutin as the
first ribitol-phosphate transferase and noting documented severity types A4,
B4, and C4. The same file has a type A severity subtype and captures the shared
mechanism, defective alpha-dystroglycan glycosylation, abnormal matriglycan /
laminin binding, elevated CK, muscular dystrophy, cobblestone lissencephaly,
retinal dysplasia, intellectual disability, seizures, hydrocephalus, neonatal
hypotonia, and the severe Walker-Warburg / muscle-eye-brain / Fukuyama
continuum.

Local coverage is less complete for the specific FKTN type A phenotype bundle:
contractures, corpus callosum abnormalities, psychomotor regression,
polymicrogyria, scoliosis, respiratory insufficiency, calf hypertrophy, and
dilated cardiomyopathy are not all represented in the dystroglycanopathy entry
as FKTN/type-A-specific phenotype prompts.

## Concordance and completeness

Judgement: broad local coverage, not an unmapped disease-family gap.

The generated weak candidate is biologically appropriate but should be promoted
from weak candidate to primary broad coverage. The incompleteness is row-level:
DisMech models FKTN and type A dystroglycanopathy separately rather than
curating the exact FKTN type A/Fukuyama row as its own cross-product entity.

## Curation actions

- Map broadly to `Dystroglycanopathy.yaml`.
- Add exact FKTN type A / Fukuyama cross-product detail only if the project
  wants row-level MONDO/OMIM coverage.
- Preserve CK, normal sialotransferrins, matriglycan antibody, cortical
  malformation, eye, cardiac, respiratory, contracture, scoliosis, regression,
  hypotonia, and muscular dystrophy prompts.
