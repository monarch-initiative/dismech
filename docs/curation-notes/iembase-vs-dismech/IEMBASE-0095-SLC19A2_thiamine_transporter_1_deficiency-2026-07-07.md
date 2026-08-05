# IEMbase 0095: SLC19A2-related thiamine transporter 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 95 |
| Nosology | 21.2.01.01 |
| Gene | SLC19A2 |
| External IDs | OMIM:603941 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive SLC19A2-related thiamine
transporter 1 deficiency, with alternate labels thiamine-responsive
megaloblastic anemia syndrome, Rogers syndrome, and THTR1.

Treatability is marked unknown, but thiamine is listed as a treatment row.

The characteristic biochemical rows are plasma glucose, plasma lactate, and
plasma vitamin B1/thiamine.

The characteristic clinical rows are sideroblastic anemia, deafness,
insulin-dependent diabetes mellitus, and thrombocytopenia.

## DisMech phenotype coverage

There is no exact DisMech disease entry for thiamine-responsive megaloblastic
anemia/Rogers syndrome.

`Diabetes_Mellitus.yaml` mentions SLC19A2 as a monogenic diabetes gene and notes
its relationship to thiamine-responsive megaloblastic anemia syndrome, but that
is not a disease-level TRMA entry and does not cover the hematologic and
hearing-loss syndrome as a mechanistic disease model.

`Biotin_Thiamine_Responsive_Basal_Ganglia_Disease.yaml` is not a valid target:
it is SLC19A3/thiamine transporter 2 disease, not SLC19A2/THTR1 disease.

## Concordance and completeness

Judgement: no valid local target, with narrow secondary context in the broad
diabetes entry.

The missing local disease would likely be a high-value treatable inborn error
entry because IEMbase records thiamine treatment and the classic triad of
diabetes, deafness, and megaloblastic/sideroblastic anemia.

## Curation actions

- Do not map this record to SLC19A3-related
  `Biotin_Thiamine_Responsive_Basal_Ganglia_Disease.yaml`.
- Consider a standalone SLC19A2/TRMA/Rogers syndrome entry.
- Resolve the IEMbase treatability inconsistency during curation: treatment is
  listed as thiamine even though treatability is marked unknown.
