# IEMbase 0501: ENO3-related beta-enolase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 501 |
| Nosology | 3.3.12.01 |
| Gene | ENO3 |
| External IDs | OMIM:612932; ORPHA:99849 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ENO3-related beta-enolase deficiency as
glycogen storage disease type 13. No treatments are listed. Biochemical rows
include elevated plasma creatine kinase, decreased muscle beta-enolase
activity, and increased muscle glycogen in adulthood. Characteristic clinical
rows include adult exercise intolerance, muscle cramps, muscle pain, and muscle
weakness.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. The local GSD
I entry models G6PC1/SLC37A4 glucose-6-phosphatase system deficiency and does
not model ENO3, beta-enolase deficiency, adult myopathic exercise intolerance,
or the muscle beta-enolase assay.

The local GSD VII entry is a closer myopathic glycolysis neighbor, but it is
PFKM/Tarui disease and should not be treated as exact coverage for ENO3/GSD
XIII.

## Concordance and completeness

Judgement: false-positive candidate; true ENO3/GSD XIII local gap.

The mapping is again a broad GSD alias collision. IEMbase's record is a
skeletal-muscle glycolytic enzyme defect with adult exercise intolerance and
increased muscle glycogen. The candidate DisMech target is a hepatic/renal
glucose-6-phosphatase disorder with a different gene, tissue focus, and
phenotype profile.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track ENO3-related beta-enolase deficiency / GSD XIII as a local curation
  gap.
- Preserve IEMbase prompts for muscle beta-enolase activity, adult CK
  elevation, increased muscle glycogen, exercise intolerance, cramps, pain, and
  weakness for a future exact entry.
