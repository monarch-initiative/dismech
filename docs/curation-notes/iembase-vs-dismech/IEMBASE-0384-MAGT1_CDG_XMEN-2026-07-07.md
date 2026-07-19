# IEMbase 0384: MAGT1-related Magnesium transporter 1 deficiency (CDG)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 384 |
| Nosology | 18.1.18.01 |
| Gene | MAGT1 |
| External IDs | OMIM:300716; OMIM:300853; ORPHA:317476 |
| Generated mapping | UNMAPPED; low candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents X-linked MAGT1-related magnesium transporter 1 deficiency
(CDG), with alternate names MAGT1-CDG and immunodeficiency, X-linked, with
magnesium defect, Epstein-Barr virus infection and neoplasia.

Clinical rows include T-cell immunodeficiency, magnesium transport defect,
neoplasm, psychomotor delay, and Epstein-Barr virus infection. The biochemical
signal is normal-to-increased serum sialotransferrins. There are no treatment
rows.

## DisMech phenotype coverage

There is no exact local DisMech target for MAGT1 deficiency/XMEN disease. The
generated `Glycogen_Storage_Disease_Type_I.yaml` candidate is a false positive:
the local file models G6PC1/SLC37A4 glucose-6-phosphatase-system disease with
fasting hypoglycemia, hepatomegaly, nephromegaly, lactic acidosis,
hyperlipidemia, hyperuricemia, and in GSD Ib neutropenia/infection risk. That
does not capture MAGT1-related magnesium transport, EBV susceptibility, or
CDG/XMEN biology.

The local `CD27-related_lymphoproliferative_and_immune_disorder.yaml` file
mentions ITK deficiency and MAGT1/XMEN disease as differential
EBV-susceptibility context, but it is not an exact MAGT1 target.

## Concordance and completeness

Judgement: true MAGT1/XMEN-CDG gap; reject the GSD I candidate.

The IEMbase record is an X-linked magnesium-transporter and glycosylation
disorder with EBV susceptibility and neoplasia risk. The generated candidate is
a carbohydrate-storage disorder with a different gene, inheritance, mechanism,
and clinical signature.

## Curation actions

- Keep this record unmapped until a MAGT1 deficiency/XMEN target exists.
- Do not map to `Glycogen_Storage_Disease_Type_I.yaml`.
- Preserve the CD27/EBV-susceptibility mention only as differential context.
- If curated, include X-linked inheritance, T-cell immunodeficiency, EBV
  infection, neoplasia, magnesium transport defect, psychomotor delay, and
  sialotransferrin findings as review prompts.
