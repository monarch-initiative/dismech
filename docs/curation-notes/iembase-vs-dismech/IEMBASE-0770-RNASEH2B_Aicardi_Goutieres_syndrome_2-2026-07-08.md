# IEMbase 0770: RNASEH2B-related ribonuclease H2 subunit B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 770 |
| Nosology | 16.3.02.01 |
| Nosology code | IEM0027 |
| Gene | RNASEH2B |
| External IDs | OMIM:610181; ORPHA:51 |
| Generated mapping | AMBIGUOUS; `Aicardi_Goutieres_Syndrome` and subtype `Aicardi-Goutieres syndrome 2` |
| Candidate DisMech targets | `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 2 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as RNASEH2B-related AGS2. Its
clinical signal closely mirrors classical AGS: cognitive impairment, seizures,
feeding difficulty, hepatosplenomegaly, sterile pyrexia, dystonia, sleep
disturbance, exaggerated startle, irritability, spasticity, microcephaly,
leukodystrophy, cerebral atrophy, intracerebral calcification, and chilblain
lesions. Laboratory rows include raised CSF neopterin, CSF lymphocytes, CSF
interferon-alpha, interferon-stimulated gene signature, autoantibodies,
transaminases, platelets, and a neonatal C26:0 fatty acid row.

## DisMech phenotype coverage

`Aicardi_Goutieres_Syndrome.yaml` includes an explicit Aicardi-Goutieres
syndrome 2 subtype with RNASEH2B and MONDO:0012429. The disease-level AGS
phenotype set covers the major IEMbase neurologic, inflammatory, cutaneous, and
imaging features, including spasticity, developmental delay/regression,
seizures, dystonia, hepatosplenomegaly, unexplained fevers, microcephaly,
leukodystrophy, cerebral calcification, brain atrophy, CSF lymphocytosis,
increased CSF interferon-alpha, chilblains, and autoimmunity. The local entry
also records RNASEH2B-specific mechanistic nuance: some RNASEH2B patients are
interferon-negative and RNASEH2B-associated neurodegeneration may include
non-canonical p53/cGAS distinctions.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects duplicate
disease-level and subtype-level match keys.

The subtype identity, gene, inheritance, and main phenotype pattern are
concordant. The main caveat is biomarker interpretation. IEMbase records
interferon signature and CSF interferon-alpha as abnormal across the age bands,
while DisMech already preserves evidence that a subset of RNASEH2B cases may be
IFN-negative. IEMbase should therefore be used as a phenotype prompt, not as a
universal RNASEH2B biomarker assertion.

## Curation actions

- Treat `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 2
  as exact local coverage for IEMbase 0770.
- Keep the local RNASEH2B-specific IFN-negative caveat; do not flatten the
  subtype into an always-IFN-positive phenotype.
- Preserve CSF neopterin, feeding difficulty, sleep disturbance, startle
  response, platelet, and optional cardiopulmonary/ocular rows as completeness
  prompts.
