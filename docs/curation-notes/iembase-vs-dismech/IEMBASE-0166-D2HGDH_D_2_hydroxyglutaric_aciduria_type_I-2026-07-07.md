# IEMbase 0166: D2HGDH-related D-2-hydroxyglutaric aciduria type I

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 166 |
| Nosology | 12.1.01.01 |
| Gene | D2HGDH |
| External IDs | OMIM:600721; ORPHA:79315 |
| Generated mapping | MAPPED to `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Candidate DisMech targets | `D-2-Hydroxyglutaric_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as D2HGDH-related D-2-hydroxyglutarate
dehydrogenase deficiency, with alternate labels D-2-hydroxyglutaric aciduria
type I and D2HGA type I. Treatability is marked unknown, and the local
IEMbase JSON does not list treatment rows.

The biochemical signal is focused: D-2-hydroxyglutaric acid is increased in
CSF, plasma, and urine across age bands. Clinical rows include developmental
delay, hypotonia, and variable epilepsy. Cardiomyopathy is represented as
normal across age bands, which distinguishes this D2HGDH subtype from the
IDH2-related type II profile in the adjacent IEMbase record.

## DisMech phenotype coverage

`D-2-Hydroxyglutaric_Aciduria.yaml` is the correct target. The local entry
explicitly covers both genetically distinct subtypes: type I due to autosomal
recessive D2HGDH loss of mitochondrial D-2-hydroxyglutarate dehydrogenase
activity, and type II due to IDH2 gain of neomorphic D-2-HG production. For
type I, DisMech models impaired D-2-HG clearance, increased D-2-HG in urine,
plasma, and CSF, developmental delay, hypotonia, seizures/epilepsy, white
matter abnormalities, psychomotor impairment, supportive care, genetic
counseling, and organic acid monitoring.

## Concordance and completeness

Judgement: correct mapping with high concordance.

The IEMbase and DisMech profiles agree on D2HGDH-related type I disease and on
increased D-2-HG in urine, plasma, and CSF. They also agree on developmental
delay, hypotonia, and seizures/epilepsy as the principal clinical signal.
DisMech is richer for molecular mechanism, neuroimaging, subtype separation,
supportive management, and monitoring. IEMbase is useful here mainly as a
subtype-specific reminder that cardiomyopathy is not expected in the D2HGDH
type I record.

## Curation actions

- Keep the mapping to `D-2-Hydroxyglutaric_Aciduria.yaml`.
- Preserve the type I versus type II subtype distinction inside the shared
  DisMech entry.
- If future mapping output supports subtype anchors, map this record to the
  local type I branch rather than only the file-level disease.
