# IEMbase 0776: IFIH1-related MDA5 superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 776 |
| Nosology | 16.3.08.01 |
| Nosology code | IEM0033 |
| Gene | IFIH1 |
| External IDs | OMIM:615846; ORPHA:85191 |
| Generated mapping | AMBIGUOUS; `Aicardi_Goutieres_Syndrome` and subtype `Aicardi-Goutieres syndrome 7` |
| Candidate DisMech targets | `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 7 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal dominant record as IFIH1-related MDA5
superactivity, with alternate name Aicardi-Goutieres syndrome type 7. The source
signal includes cognitive dysfunction, dystonia, seizures, hepatosplenomegaly,
sterile pyrexia, sleep disturbance, chilblains, feeding difficulty,
intracerebral calcifications, cerebral atrophy, leukodystrophy, microcephaly,
spasticity, exaggerated startle, irritability, and an optional isolated spastic
paraparesis row. Laboratory rows include transaminases, CSF neopterin, CSF
lymphocytes, CSF interferon-alpha, interferon-stimulated gene signature,
autoantibodies, platelets, and neonatal C26:0 fatty acid.

## DisMech phenotype coverage

`Aicardi_Goutieres_Syndrome.yaml` has an explicit Aicardi-Goutieres syndrome 7
subtype with IFIH1 and MONDO:0014367. The local AGS entry captures
heterozygous IFIH1 gain-of-function, abnormal MDA5 sensing, type I interferon
signaling, and the broad shared AGS phenotype set: neurodevelopmental
impairment, regression, spasticity, dystonia, seizures, microcephaly,
leukodystrophy, cerebral calcification, brain atrophy, chilblains, fevers,
hepatosplenomegaly, CSF lymphocytosis, increased CSF interferon-alpha, and
autoimmunity.

## Concordance and completeness

Judgement: exact subtype coverage; generated ambiguity reflects local
disease-level and subtype-level matches.

The gene, dominant inheritance, OMIM identity, subtype identity, and core
interferonopathy phenotype are concordant. IEMbase adds several explicit
phenotype prompts that are not independently represented in the local
phenotype list, especially isolated spastic paraparesis, feeding difficulty,
sleep disturbance, startle response, and CSF neopterin.

## Curation actions

- Treat `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 7
  as exact local coverage for IEMbase 0776.
- Preserve IFIH1 gain-of-function and autosomal dominant inheritance as
  subtype-specific distinguishing features.
- Review isolated spastic paraparesis and CSF neopterin as possible
  completeness additions before changing the KB.
