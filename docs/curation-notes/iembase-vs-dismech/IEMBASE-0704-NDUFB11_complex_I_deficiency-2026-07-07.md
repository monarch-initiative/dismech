# IEMbase 0704: NDUFB11-related NADH dehydrogenase beta subcomplex subunit 11 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 704 |
| Nosology | 7.1.17.01 |
| Nosology code | IEM0429 |
| Gene | NDUFB11 |
| External IDs | OMIM:300952 for NDUFB11/LSDMCA3 in MONDO; IEMbase source lists OMIM:252010; ORPHA:2556 |
| Generated mapping | CANDIDATE to `COX10-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact NDUFB11/MC1DN30 or NDUFB11/LSDMCA3 target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked NDUFB11-related NADH dehydrogenase beta subcomplex
subunit 11 deficiency. The record is also labeled mitochondrial complex I
deficiency, nuclear type 30, and linear skin defects with multiple congenital
anomalies type 3.

The source lists OMIM:252010, while MONDO resolves the NDUFB11 linear skin
defects term to OMIM:300952. MONDO treats OMIM:252010 as the older complex I
deficiency nuclear type 1 / NDUFS4 identifier, so the source identifier should
be reviewed before downstream use.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate from neonatal through childhood windows. Clinical rows include
sideroblastic anemia, cardiomyopathy, microphthalmia, perinatal death, and
characteristic lactic acidosis.

## DisMech phenotype coverage

No exact NDUFB11, MC1DN30, or linear-skin-defects type 3 local target was
identified.

`Leigh_Syndrome.yaml` provides broad context for complex I-related mitochondrial
energy failure, lactate elevation, and severe early disease, but it does not
model NDUFB11 or the microphthalmia/linear skin defects phenotype.

The generated `COX10-Related_COX_Deficiency.yaml` candidate is a complex IV
heme A biosynthesis disorder and is not exact coverage for an NDUFB11 complex I
subunit disorder.

## Concordance and completeness

Judgement: true local gap with broad complex I / Leigh overlap only.

The IEMbase record combines mitochondrial complex I deficiency with a
syndromic NDUFB11/LSDMCA3 phenotype. The COX10 candidate should be rejected as
an unrelated complex IV target.

## Curation actions

- Add a dedicated NDUFB11/MC1DN30 or NDUFB11/LSDMCA3 target if curated.
- Reject `COX10-Related_COX_Deficiency.yaml` as exact coverage.
- Preserve the source OMIM discrepancy for identifier review.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  sideroblastic anemia, cardiomyopathy, microphthalmia, perinatal death, and
  lactic acidosis.
