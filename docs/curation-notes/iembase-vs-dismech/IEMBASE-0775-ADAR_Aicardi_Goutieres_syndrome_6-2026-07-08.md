# IEMbase 0775: ADAR-related RNA-specific adenosine deaminase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 775 |
| Nosology | 16.3.07.01 |
| Nosology code | IEM0032 |
| Gene | ADAR |
| External IDs | OMIM:615010; ORPHA:41 |
| Generated mapping | AMBIGUOUS; `Aicardi_Goutieres_Syndrome` and subtype `Aicardi-Goutieres syndrome 6` |
| Candidate DisMech targets | `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 6 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as ADAR-related AGS6. The source
signal includes cognitive dysfunction, seizures, feeding difficulty,
hepatosplenomegaly, sterile pyrexia, chilblains, cerebral atrophy,
intracerebral calcifications, leukodystrophy, microcephaly, dystonia,
exaggerated startle, irritability, sleep disturbance, spasticity, and an
ADAR-relevant bilateral striatal degeneration row. Laboratory rows include
transaminases, CSF neopterin, CSF lymphocytes, autoantibodies, CSF
interferon-alpha, and interferon-stimulated gene signature.

## DisMech phenotype coverage

`Aicardi_Goutieres_Syndrome.yaml` includes an explicit Aicardi-Goutieres
syndrome 6 subtype with ADAR and MONDO:0014007. The shared local AGS phenotype
set covers the major neurologic, inflammatory, cutaneous, and imaging signal:
spasticity, developmental delay/regression, seizures, dystonia, microcephaly,
leukodystrophy, cerebral calcification, brain atrophy, chilblains, fevers,
hepatosplenomegaly, CSF lymphocytosis, increased CSF interferon-alpha, and
autoimmunity. The local mechanistic hypotheses specifically include ADAR1
RNA-editing and MDA5-dependent immune activation, and the dystonia phenotype
description notes ADAR-associated striatal necrosis.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects disease-level
and subtype-level matches.

The disease identity, gene, OMIM, inheritance, and canonical AGS phenotype are
concordant. IEMbase is useful for making the ADAR-specific striatal signal more
visible: bilateral striatal degeneration is not a standalone local phenotype
row even though ADAR-associated striatal necrosis is mentioned in the dystonia
description and mechanism discussion.

## Curation actions

- Treat `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 6
  as exact local coverage for IEMbase 0775.
- Consider promoting ADAR-associated bilateral striatal degeneration/striatal
  necrosis to a discrete phenotype row if local evidence supports it.
- Preserve CSF neopterin, feeding difficulty, sleep disturbance, startle
  response, and optional cardiopulmonary/ocular rows as future prompts.
