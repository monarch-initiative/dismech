# IEMbase 0702: NDUFB3-related NADH dehydrogenase beta subcomplex subunit 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 702 |
| Nosology | 7.1.15.01 |
| Nosology code | IEM0427 |
| Gene | NDUFB3 |
| External IDs | OMIM:618246 for NDUFB3/MC1DN25; IEMbase source lists OMIM:252010; ORPHA:2609 |
| Generated mapping | CANDIDATE to `COX18-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFB3 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFB3-related NADH dehydrogenase beta
subcomplex subunit 3 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 25.

The source lists OMIM:252010, while MONDO resolves mitochondrial complex I
deficiency nuclear type 25 to OMIM:618246 and NDUFB3. The source identifier
appears broad or cross-listed and should be reviewed before downstream use.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate through childhood. Clinical rows include developmental delay,
encephalopathy, hypotonia, myopathy, and characteristic lactic acidosis.

## DisMech phenotype coverage

No exact NDUFB3 or MC1DN25 local target was identified.

`Leigh_Syndrome.yaml` supplies broad overlap for complex I-related neurologic
disease, lactate elevation, hypotonia, developmental impairment, and
encephalopathy. It does not model NDUFB3.

The generated `COX18-Related_COX_Deficiency.yaml` candidate is a complex IV
COX2-maturation disorder. It shares the nuclear-type number 25 but belongs to
MC4DN25 rather than MC1DN25.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase row is a complex I beta-subcomplex disease with neuromuscular and
encephalopathic features. COX18 is a wrong-complex number-collision candidate,
and the source OMIM field should not be treated as a gene-specific NDUFB3
identifier without review.

## Curation actions

- Add a dedicated NDUFB3/MC1DN25 target if curated.
- Reject COX18-related complex IV deficiency as exact coverage.
- Preserve the source OMIM discrepancy for review before downstream identifier
  use.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  developmental delay, encephalopathy, hypotonia, myopathy, and lactic acidosis.
