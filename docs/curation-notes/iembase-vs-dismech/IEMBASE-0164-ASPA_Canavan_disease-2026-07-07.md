# IEMbase 0164: ASPA-related Canavan disease

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 164 |
| Nosology | 1.9.01.03 |
| Gene | ASPA |
| External IDs | OMIM:271900; ORPHA:314911 |
| Generated mapping | MAPPED to `Canavan_Disease.yaml` |
| Candidate DisMech targets | `Canavan_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ASPA-related aspartoacylase deficiency, with
alternate labels Canavan disease, N-acetylaspartic aciduria, and CD.
Treatability is marked unknown.

The biochemical rows report increased N-acetylaspartic acid in CSF, plasma,
and urine. The clinical rows include bilateral subcortical leukodystrophy,
globus pallidus MRI abnormalities, macrocephaly, axial muscular hypotonia,
spasticity, psychomotor retardation, intellectual disability, loss of very
early milestones, blindness, optic atrophy, nystagmus, epilepsy, dysarthria,
deafness, extrapyramidal movement disorder, decerebrate posture, and
opisthotonus.

## DisMech phenotype coverage

`Canavan_Disease.yaml` is the correct target. It models biallelic ASPA
pathogenic variants, aspartoacylase deficiency, impaired hydrolysis of
N-acetyl-L-aspartate, NAA accumulation in the central nervous system and body
fluids, reduced NAA-derived acetate and myelin lipid synthesis, oligodendrocyte
and myelination defects, spongiform white-matter vacuolation, macrocephaly,
hypotonia, global developmental delay, visual impairment/blindness, optic
atrophy, nystagmus, seizures, hypertonia/spasticity, developmental regression,
feeding difficulty, supportive care, and investigational ASPA gene replacement
or NAA-lowering strategies.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The IEMbase and DisMech profiles agree on ASPA/aspartoacylase deficiency,
N-acetylaspartate accumulation, leukodystrophy, macrocephaly, hypotonia,
developmental impairment/regression, optic/visual involvement, nystagmus,
seizures, and spasticity. IEMbase adds compartment-specific CSF and plasma NAA
rows, globus pallidus MRI abnormalities, bilateral subcortical leukodystrophy
wording, decerebrate posture, opisthotonus, deafness, and extrapyramidal
movement disorder as possible refinement targets.

The IEMbase ORPHA identifier differs from the local Canavan structured record
used in DisMech; the disease identity is still correct through ASPA, OMIM
271900, and the Canavan/N-acetylaspartic aciduria labels.

## Curation actions

- Keep the mapping to `Canavan_Disease.yaml`.
- Consider future biomarker refinement for CSF and plasma NAA in addition to
  urine and brain MRS.
- Review whether IEMbase globus pallidus, decerebrate posture, opisthotonus,
  and extrapyramidal rows should be represented locally.
- Check the ORPHA cross-reference difference during any future Canavan metadata
  cleanup.
