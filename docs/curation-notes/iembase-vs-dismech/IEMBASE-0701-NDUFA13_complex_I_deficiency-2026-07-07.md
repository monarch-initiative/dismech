# IEMbase 0701: NDUFA13-related NADH dehydrogenase alpha subcomplex subunit 13 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 701 |
| Nosology | 7.1.27.01 |
| Nosology code | IEM1141 |
| Gene | NDUFA13 |
| External IDs | OMIM:618249; ORPHA:255241 |
| Generated mapping | CANDIDATE to `TACO1-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA13 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA13-related NADH dehydrogenase alpha
subcomplex subunit 13 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 28.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate through childhood. Clinical rows include cerebellar atrophy,
developmental delay, encephalopathy, feeding difficulties, lactic acidosis, and
characteristic hypotonia.

## DisMech phenotype coverage

No exact NDUFA13 or MC1DN28 local target was identified.

`Leigh_Syndrome.yaml` provides broad overlap for complex I-related
mitochondrial encephalopathy, lactate elevation, hypotonia, feeding/bulbar
difficulties, and developmental impairment. It does not model NDUFA13-specific
disease.

The generated `TACO1-Related_COX_Deficiency.yaml` candidate is a complex IV
mitochondrial translation disorder, not a complex I subunit disease.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase phenotype package includes complex I enzyme deficiency, lactate,
cerebellar atrophy, feeding difficulty, encephalopathy, developmental delay,
and hypotonia. These should not be attributed to TACO1-related complex IV
deficiency.

## Curation actions

- Add a dedicated NDUFA13/MC1DN28 target if curated.
- Reject TACO1-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  cerebellar atrophy, developmental delay, encephalopathy, feeding difficulties,
  lactic acidosis, and hypotonia.
