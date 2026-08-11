# IEMbase 0695: NDUFA2-related NADH dehydrogenase alpha subcomplex subunit 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 695 |
| Nosology | 7.1.11.01 |
| Nosology code | IEM0423 |
| Gene | NDUFA2 |
| External IDs | OMIM:618235 for NDUFA2/MC1DN13; IEMbase source lists OMIM:256000; ORPHA:85136 |
| Generated mapping | CANDIDATE to `COX10-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA2 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA2-related NADH dehydrogenase alpha
subcomplex subunit 2 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 13.

The source lists OMIM:256000, which is a broad Leigh/mitochondrial respiratory
chain identifier rather than the expected NDUFA2/MC1DN13 identifier
OMIM:618235. The scope table records both so the source anomaly is not lost.

Biochemical rows show decreased fibroblast complex I activity in neonatal and
infantile windows and increased plasma lactate through childhood. Clinical rows
include lactic acidosis, Leigh syndrome, and leukoencephalopathy.

## DisMech phenotype coverage

No exact NDUFA2 or MC1DN13 local target was identified.

`Leigh_Syndrome.yaml` covers shared Leigh-spectrum context, including complex I
deficiency as a cause of Leigh syndrome, lactate elevation, and white-matter or
brainstem/basal-ganglia neurologic involvement. It does not provide a
gene-specific NDUFA2 model.

The generated `COX10-Related_COX_Deficiency.yaml` candidate is a complex IV heme
A biosynthesis disorder and should not be accepted as exact coverage for an
NDUFA2 complex I subunit defect.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase record is sparse but specific: NDUFA2 loss, decreased complex I
activity, lactate elevation, lactic acidosis, Leigh syndrome, and
leukoencephalopathy. DisMech currently has only the syndrome-level context, not
the gene-specific disease entity.

## Curation actions

- Add a dedicated NDUFA2/MC1DN13 target if curated.
- Reject COX10-related complex IV deficiency as exact coverage.
- Preserve the source OMIM discrepancy for review before downstream identifier
  use.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  lactic acidosis, Leigh syndrome, and leukoencephalopathy.
