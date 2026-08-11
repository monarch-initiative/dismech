# IEMbase 0774: SAMHD1-related SAMS association and AGS5

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 774 |
| Nosology | 9.1.06.02 |
| Nosology code | IEM0031 |
| Gene | SAMHD1 |
| External IDs | OMIM:612952; ORPHA:481662 |
| Generated mapping | AMBIGUOUS; `Aicardi_Goutieres_Syndrome` and subtype `Aicardi-Goutieres syndrome 5` |
| Candidate DisMech targets | `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 5 |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as SAMHD1-related stenosis,
aneurysm, moyamoya, and stroke association, with alternate name
Aicardi-Goutieres syndrome type 5. The phenotype signal includes the standard
AGS neurologic and inflammatory pattern plus an explicit cerebrovascular row:
cognitive dysfunction, seizures, feeding difficulty, hepatosplenomegaly,
sterile pyrexia, chilblains, cerebral atrophy, intracerebral calcifications,
leukodystrophy, microcephaly, dystonia, exaggerated startle, irritability,
sleep disturbance, spasticity, and cerebrovascular disease including stenosis,
aneurysm, moyamoya-like disease, and stroke. Laboratory rows include CSF
neopterin, CSF lymphocytes, CSF interferon-alpha, interferon-stimulated gene
signature, autoantibodies, transaminases, platelets, and neonatal C26:0 fatty
acid.

## DisMech phenotype coverage

`Aicardi_Goutieres_Syndrome.yaml` has an explicit Aicardi-Goutieres syndrome 5
subtype with SAMHD1 and MONDO:0013059. The local AGS disease-level phenotype
set covers the shared brain, movement, neurodevelopmental, inflammatory,
cutaneous, and laboratory findings. It also has a pathophysiology node for
systemic interferon-mediated inflammation and vasculopathy whose description
specifically mentions SAMHD1-associated intracranial vasculopathy.

## Concordance and completeness

Judgement: exact subtype coverage with an important cerebrovascular
completeness prompt.

The gene, OMIM identity, inheritance, AGS5 subtype, and type I interferonopathy
model are concordant. IEMbase is more explicit than the current phenotype list
for SAMHD1-related SAMS: stenosis, aneurysm, moyamoya-like disease, and stroke
are visible as source phenotypes, while DisMech currently captures this mainly
in prose/pathophysiology plus more general hemiplegia/hemiparesis and
vasculopathy context.

## Curation actions

- Treat `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 5
  as exact local coverage for IEMbase 0774.
- Consider adding explicit SAMHD1-associated intracranial stenosis, aneurysm,
  moyamoya, or stroke phenotype rows if supported by existing local evidence.
- Preserve CSF neopterin, startle response, feeding difficulty, sleep
  disturbance, and platelet rows as broader AGS completeness prompts.
