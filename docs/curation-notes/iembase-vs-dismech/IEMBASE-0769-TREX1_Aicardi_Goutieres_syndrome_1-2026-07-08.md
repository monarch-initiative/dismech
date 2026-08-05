# IEMbase 0769: TREX1-related 3-prime repair exonuclease 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 769 |
| Nosology | 16.3.01.01 |
| Nosology code | IEM0026 |
| Gene | TREX1 |
| External IDs | OMIM:225750; ORPHA:481662 |
| Generated mapping | AMBIGUOUS; `Aicardi_Goutieres_Syndrome` and subtype `Aicardi-Goutieres syndrome 1` |
| Candidate DisMech targets | `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 1 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as TREX1-related AGS1, with
alternate name Aicardi-Goutieres syndrome type 1 and abbreviation AGS1. The
source signal is the classical AGS interferonopathy pattern: cognitive
impairment, dystonia, seizures, feeding difficulty, hepatosplenomegaly,
sterile pyrexia, sleep disturbance, spasticity, microcephaly, leukodystrophy,
cerebral atrophy, intracerebral calcification, chilblain lesions, exaggerated
startle, and irritability. Laboratory rows include raised CSF neopterin, CSF
lymphocytes, CSF interferon-alpha, interferon-stimulated gene signature,
autoantibodies, variably elevated transaminases, low-to-normal neonatal
platelets, and a neonatal normal-to-high C26:0 fatty acid row.

## DisMech phenotype coverage

`Aicardi_Goutieres_Syndrome.yaml` is the correct local target. It has an
explicit Aicardi-Goutieres syndrome 1 subtype with TREX1 and MONDO:0009165,
and the disease-level AGS entry covers the shared clinical phenotype: spasticity,
developmental delay or regression, profound intellectual disability, seizures,
dystonia, hepatosplenomegaly, unexplained fevers, microcephaly, leukodystrophy,
cerebral calcification, brain atrophy, CSF lymphocytosis, increased CSF
interferon-alpha, chilblains, autoimmunity, elevated transaminases, and the
type I interferon mechanism.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects disease-level
and subtype-level matches.

The gene, OMIM identity, inheritance, AGS subtype, and major neurologic,
cutaneous, inflammatory, and biomarker signal are concordant. DisMech is more
mechanistically explicit for TREX1 loss, endogenous nucleic-acid sensing, and
type I interferon signaling. IEMbase adds several useful completeness prompts:
CSF neopterin, feeding difficulty, sleep disturbance, startle response, and
low-to-normal neonatal platelets are not represented as separate local phenotype
or biomarker rows. IEMbase also lists optional glaucoma, hypertrophic
cardiomyopathy, and pulmonary hypertension; those should not be promoted
without source review because they are low-confidence/optional in the IEMbase
age table.

## Curation actions

- Treat `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 1
  as exact local coverage for IEMbase 0769.
- Do not create a standalone TREX1 disease file unless DisMech later decides to
  split AGS subtypes out of the current subtype model.
- Preserve CSF neopterin, feeding difficulty, sleep disturbance, startle
  response, platelet, and optional cardiopulmonary/ocular rows as future
  phenotype-completeness prompts.
