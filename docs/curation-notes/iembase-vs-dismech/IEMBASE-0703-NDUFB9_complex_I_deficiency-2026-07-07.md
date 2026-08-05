# IEMbase 0703: NDUFB9-related NADH dehydrogenase beta subcomplex subunit 9 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 703 |
| Nosology | 7.1.26.01 |
| Nosology code | IEM1142 |
| Gene | NDUFB9 |
| External IDs | OMIM:618245 for NDUFB9/MC1DN24; IEMbase source lists OMIM:252010; ORPHA:2609 |
| Generated mapping | CANDIDATE to `FASTKD5-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFB9 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFB9-related NADH dehydrogenase beta
subcomplex subunit 9 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 24.

The source lists OMIM:252010, while MONDO resolves mitochondrial complex I
deficiency nuclear type 24 to OMIM:618245 and NDUFB9. The source identifier
should be reviewed before downstream use.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate in neonatal and infantile windows. Clinical rows include
perinatal death, hypotonia, and characteristic lactic acidosis.

## DisMech phenotype coverage

No exact NDUFB9 or MC1DN24 local target was identified.

`Leigh_Syndrome.yaml` gives broad context for complex I-related mitochondrial
encephalopathy, lactate elevation, hypotonia, and severe early-onset disease,
but it does not model NDUFB9.

The generated `FASTKD5-Related_COX_Deficiency.yaml` candidate is a complex IV
mRNA-processing disorder. It shares the nuclear-type number 24 but belongs to
MC4DN24 rather than MC1DN24.

## Concordance and completeness

Judgement: true local gap with broad mitochondrial/Leigh overlap only.

The IEMbase record is a severe early NDUFB9 complex I deficiency with
perinatal death and lactic acidosis. FASTKD5 is a wrong-complex number-collision
candidate, not exact coverage.

## Curation actions

- Add a dedicated NDUFB9/MC1DN24 target if curated.
- Reject FASTKD5-related complex IV deficiency as exact coverage.
- Preserve the source OMIM discrepancy for review before downstream identifier
  use.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  perinatal death, hypotonia, and lactic acidosis.
