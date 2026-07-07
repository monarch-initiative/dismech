# IEMbase 0723: COX10-related cytochrome c oxidase assembly factor 10 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 723 |
| Nosology | 7.4.02.01 |
| Nosology code | IEM0470 |
| Gene | COX10 |
| External IDs | OMIM:220110; OMIM:256000; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COX10-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COX10-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COX10-related cytochrome c oxidase
assembly factor 10 deficiency. The alternate-name field includes Leigh
syndrome due to mitochondrial COX4 deficiency, which should be preserved as
source wording but treated cautiously because the gene in this record is
COX10.

The cached rows include neonatal and infantile low-to-normal plasma glucose,
low neonatal hemoglobin, increased plasma lactate, possible anemia and
cardiomyopathy, Leigh syndrome, perinatal death, proximal renal tubulopathy,
developmental delay, and hypotonia.

## DisMech phenotype coverage

DisMech has exact local coverage in `COX10-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 3
(MONDO:0033635) and describes biallelic COX10 loss as a heme O synthase defect
that impairs heme A biosynthesis and complex IV assembly.

Local phenotypes include Leigh syndrome or encephalopathy, muscle weakness, and
lactic acidosis. The local mechanism is strong for the COX10 heme A
biosynthesis step.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COX10-Related_COX_Deficiency.yaml`.

Gene, inheritance, complex IV biology, and Leigh/lactate identity align. The
IEMbase record adds useful phenotype prompts not prominent in the local file,
including glucose, hemoglobin/anemia, cardiomyopathy, perinatal death, proximal
renal tubulopathy, developmental delay, and hypotonia.

## Curation actions

- Resolve IEMbase 723 to `COX10-Related_COX_Deficiency.yaml`.
- Preserve the source alternate-name anomaly without letting it override the
  COX10 disease identity.
- Consider reviewing local COX10 phenotypes for anemia/hemoglobin, glucose,
  cardiomyopathy, renal tubulopathy, developmental delay, and hypotonia.
- Keep COX10 heme O synthase disease distinct from other COX assembly factors.
