# IEMbase 0616: PLPBP-related pyridoxal 5-prime-phosphate binding protein deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 616 |
| Nosology | 21.6.02.01 |
| Gene | PLPBP |
| External IDs | OMIM:617290; ORPHA:3006 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None exact; `Pyruvate_Dehydrogenase_Deficiency.yaml` is a lexical false candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PLPBP / PROSC-deficient vitamin B6-dependent epilepsy as an
autosomal recessive treatable disorder. Biochemical rows include low CSF
pyridoxal 5-prime-phosphate, low CSF homovanillic acid, increased CSF
5-hydroxytryptophan, normal-to-increased plasma 3-methoxytyrosine,
normal-to-increased urinary vanillactic acid, and normal-to-increased plasma
lactate.

Clinical rows include neonatal/infantile seizures, burst-suppression EEG,
irritability, motor regression, delayed or absent speech, optional microcephaly,
optional hypertonia or hypotonia, optional respiratory distress, and optional
dysmorphic features including prominent forehead, upslanting palpebral
fissures, and syndactyly. IEMbase includes a vitamin B6 treatment row.

## DisMech phenotype coverage

No exact PLPBP target was identified locally. The best lexical candidate,
`Pyruvate_Dehydrogenase_Deficiency.yaml`, is an E3-binding / lactate-related
false positive and should not receive PLPBP phenotype rows.

The vitamin B6 treatment row should be source-reviewed before import because
the cited treatment reference appears to be a broader pyridoxine-dependent
epilepsy treatment source rather than necessarily PLPBP-specific evidence.

## Concordance and completeness

Judgement: true local gap.

This is a high-priority treatable epilepsy gap because the IEMbase record has a
clear therapeutic signal and a distinctive CSF PLP / biogenic-amine profile.

## Curation actions

- Create or identify an exact PLPBP / EPVB6D target before import.
- Reject `Pyruvate_Dehydrogenase_Deficiency.yaml` as an exact mapping.
- Preserve vitamin B6/PLP treatment, CSF PLP and biogenic-amine markers,
  burst-suppression EEG, seizure, regression, speech, tone, respiratory, and
  dysmorphic prompts.
