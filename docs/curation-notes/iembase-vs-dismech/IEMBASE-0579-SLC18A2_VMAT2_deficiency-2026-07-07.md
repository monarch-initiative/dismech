# IEMbase 0579: SLC18A2-related vesicular monoamine transporter 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 579 |
| Nosology | 23.1.06.01 |
| Gene | SLC18A2 |
| External IDs | OMIM:193001; ORPHA:352649 |
| Generated mapping | UNMAPPED; best candidate `Primary_Carnitine_Deficiency.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC18A2-related vesicular monoamine transporter 2 deficiency,
also labelled VMAT2 disorder. The record is autosomal recessive, classified
under monoamine neurotransmission, flagged as treatable, and lists pramipexole
as dopamine-agonist therapy.

Biochemical rows include very high urinary 5-HIAA and HVA, decreased urinary
dopamine and norepinephrine, increased CSF 5-HIAA and HVA, decreased blood
serotonin, and increased plasma prolactin. Clinical rows include poor head
control, hypotonia with extremity hypertonia, dystonia, ataxia, dysarthria,
dysdiadochokinesis, hypomimia, hypernasal speech, nasal congestion or profuse
nasal secretion, and sweating.

## DisMech phenotype coverage

`Primary_Carnitine_Deficiency.yaml` is a false-positive generated candidate.
That entry models SLC22A5/OCTN2 carnitine transport failure, fatty-acid
oxidation stress, cardiomyopathy, hypoketotic hypoglycemia, and L-carnitine
therapy. It does not represent SLC18A2, VMAT2, vesicular monoamine packaging,
or the monoamine metabolite pattern in IEMbase.

The local catecholamine-synthesis material is only broad context for monoamine
biology. It does not provide an exact VMAT2 transport subtype.

## Concordance and completeness

Judgement: true local gap; reject the primary carnitine deficiency candidate.

The IEMbase record should not be collapsed into carnitine transport or into
monoamine synthesis. Its core mechanism is defective vesicular loading of
monoamines, with a distinctive biomarker pattern and autonomic/movement-disorder
phenotype.

## Curation actions

- Create or identify an exact SLC18A2/VMAT2 deficiency target before import.
- Reject `Primary_Carnitine_Deficiency.yaml` as an exact mapping.
- Preserve the urinary and CSF HVA/5-HIAA, dopamine, norepinephrine, serotonin,
  prolactin, movement-disorder, and autonomic prompts for later curation.
