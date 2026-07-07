# IEMbase 0480: SLC2A1-related glucose transporter 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 480 |
| Nosology | 3.6.01.01 |
| Gene | SLC2A1 |
| External IDs | OMIM:606777; OMIM:612126; OMIM:601042; OMIM:614847; ORPHA:98811 |
| Generated mapping | UNMAPPED; best candidate `SLC35A2-CDG.yaml` |
| Candidate DisMech targets | `GLUT1_Deficiency_Syndrome.yaml`; rejected lexical candidate `SLC35A2-CDG.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SLC2A1-related glucose transporter 1 deficiency / GLUT1
deficiency as an autosomal dominant or autosomal recessive disorder. It records
ketogenic diet and triheptanoin as treatments. Biochemical rows include
decreased erythrocyte GLUT1 by western blot, decreased erythrocyte glucose
uptake, decreased CSF glucose, decreased CSF/plasma glucose ratio,
low-to-normal CSF lactate, and decreased galactonic acid, gluconic acid, and
xylose-linked oligosaccharide markers. Clinical rows include neonatal seizures,
ataxia, dystonia, axial muscular hypotonia, and hemolytic anemia.

## DisMech phenotype coverage

`GLUT1_Deficiency_Syndrome.yaml` is the exact local target. The local entry
models SLC2A1 loss of function, reduced GLUT1 transporter function at the
blood-brain barrier and in erythrocytes, cerebral glucose energy deficit,
pharmacoresistant seizures, developmental delay, progressive microcephaly,
ataxia, dystonia, spasticity, hypotonia, paroxysmal exertion-induced dyskinesia,
hypoglycorrhachia, low CSF:blood glucose ratio, erythrocyte glucose uptake /
GLUT1 immunoreactivity testing, and ketogenic diet therapy.

## Concordance and completeness

Judgement: false negative generated mapping; resolve to
`GLUT1_Deficiency_Syndrome.yaml`.

The `SLC35A2-CDG.yaml` candidate is not an exact match. The local GLUT1 entry has
high concordance for the core mechanism, diagnostic CSF glucose signal,
erythrocyte functional assay, movement disorder, seizures, and ketogenic diet.
IEMbase adds prompts that are not fully represented locally, especially
triheptanoin, hemolytic anemia, low/normal CSF lactate, and the additional
specialized carbohydrate/oligosaccharide marker rows.

## Curation actions

- Treat this as covered by `GLUT1_Deficiency_Syndrome.yaml`.
- Reject `SLC35A2-CDG.yaml` as a glycosylation/lexical false positive.
- Consider evidence-backed enrichment for triheptanoin, hemolytic anemia, CSF
  lactate, and the specialized carbohydrate marker rows.
