# IEMbase 0667: SLC45A1-related neuronal glucose transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 667 |
| Nosology | 3.6.02.02 |
| Nosology code | IEM0315 |
| Gene | SLC45A1 |
| External IDs | OMIM:617532; ORPHA:88616 |
| Generated mapping | UNMAPPED; best candidate `SLC35A2-CDG.yaml` |
| Candidate DisMech targets | `SLC45A1-Related_Neuronal_Glucose_Transporter_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC45A1-related neuronal glucose
transporter deficiency, also labeled intellectual developmental disorder with
neuropsychiatric features.

Clinical rows include intellectual disability, behavioral disorder, anxiety,
autism, seizures, dysmorphic features, stereotyped hand movements, broad nasal
bridge, maxillary prognathism, open mouth, thick eyebrows, and thick lips.
Biochemical rows report normal CSF glucose and normal plasma glucose.

## DisMech phenotype coverage

`SLC45A1-Related_Neuronal_Glucose_Transporter_Deficiency.yaml` is an exact local
target. It models biallelic SLC45A1 deficiency as a neuronal glucose transporter
disorder with intellectual disability, epilepsy/focal seizures,
neuropsychiatric features including anxiety and autistic behaviors, mild facial
dysmorphism, and developmental delay.

The local entry also explicitly distinguishes SLC45A1 disease from GLUT1/SLC2A1
deficiency by noting that reduced CSF glucose has not been reported in published
SLC45A1 cases. That aligns with the IEMbase normal CSF and plasma glucose rows.

The generated `SLC35A2-CDG.yaml` candidate is a glycosylation false positive.

## Concordance and completeness

Judgement: false negative from stale generated mapping; current DisMech has an
exact high-concordance SLC45A1 target.

IEMbase provides useful dysmorphology granularity and a normal-glucose caveat
that strengthens the local distinction from SLC2A1/GLUT1 deficiency. DisMech is
stronger for mechanism and differential framing.

## Curation actions

- Resolve this record to
  `SLC45A1-Related_Neuronal_Glucose_Transporter_Deficiency.yaml`.
- Reject `SLC35A2-CDG.yaml` as exact coverage.
- Preserve normal CSF glucose and normal plasma glucose as distinguishing rows.
- Review whether broad nasal bridge, maxillary prognathism, open mouth, thick
  eyebrows/lips, and stereotyped hand movements should be added explicitly.
