# IEMbase 0762: DDHD2-related phosphatidic acid-preferring phospholipase 2 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 762 |
| Nosology | 14.5.01.11 |
| Nosology code | IEM0671 |
| Gene | DDHD2 |
| External IDs | OMIM:609340; ORPHA:320380 |
| Generated mapping | UNMAPPED; weak candidate `ALDH18A1_De_Barsy_Spectrum.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as DDHD2-related phosphatidic
acid-preferring phospholipase 2 deficiency, with alternate name autosomal
recessive spastic paraplegia type 54. The phenotype rows describe a childhood
through adult neurodevelopmental and motor syndrome: developmental delay,
behavioral disorder, microcephaly, spastic paraparesis, pyramidal signs, bulbar
dysfunction, abnormal eye movements, brainstem atrophy, cerebellar atrophy,
cerebellar white matter abnormalities, corpus callosum hypoplasia, and syrinx.

## DisMech phenotype coverage

No exact DDHD2 / SPG54 entry is present locally. The generated
`ALDH18A1_De_Barsy_Spectrum.yaml` candidate is a false positive. That entry
models ALDH18A1 / P5CS deficiency with SPG9A/SPG9B and neurocutaneous disease,
not DDHD2 phospholipase deficiency or SPG54.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record should be curated as a distinct DDHD2 hereditary spastic
paraplegia entity. The local ALDH18A1 entry shares broad spastic-paraplegia
vocabulary but has different gene, biochemical mechanism, subtype identity,
and expected amino-acid metabolism context.

## Curation actions

- Add a distinct DDHD2 / autosomal recessive spastic paraplegia type 54 target
  before treating this record as covered.
- Reject `ALDH18A1_De_Barsy_Spectrum.yaml` as exact coverage.
- Review the duplicated OMIM value in the local IEMbase cache before modeling
  identifiers, because the source record repeats the DDHD1 OMIM value.
