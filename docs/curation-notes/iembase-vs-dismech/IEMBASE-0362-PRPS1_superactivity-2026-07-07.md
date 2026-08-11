# IEMbase 0362: PRPS1 superactivity

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 362 |
| Nosology | 16.2.01.01 |
| Gene | PRPS1 |
| External IDs | OMIM:300661; ORPHA:99014 |
| Generated mapping | CANDIDATE/MEDIUM to `PRPS1_Superactivity.yaml` |
| Candidate DisMech targets | `PRPS1_Superactivity.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PRPS1-related phosphoribosyl pyrophosphate synthetase 1
superactivity, an X-linked recessive purine-metabolism disorder.
Characteristic rows include sensorineural deafness, facial dysmorphism, gout,
urine hypoxanthine, plasma uric acid, and urine uric acid.

Additional clinical rows include ataxia, developmental delay, intellectual
disability, and urolithiasis. Biochemical rows include urine hypoxanthine,
PRPP synthase activity in fibroblasts, PRPP synthase activity in red blood
cells, phosphoribose pyrophosphate in red blood cells, plasma uric acid, and
urine uric acid. The IEMbase source row spells phosphoribose as "Phosporibose".
No treatment rows are present.

## DisMech phenotype coverage

The generated candidate is the correct target despite being marked medium
confidence. DisMech has a PRPS1 Superactivity file describing X-linked PRPS1
gain-of-function or transcriptional overactivity, increased PRPP, increased de
novo purine nucleotide synthesis, and uric acid overproduction.

Local coverage includes mild and severe disease, hyperuricemia,
hyperuricosuria, uric acid crystalluria/nephrolithiasis, gout, developmental
delay, intellectual disability, sensorineural hearing loss, hypotonia, and
ataxia. Local mechanism is stronger for allosteric PRS-I dysregulation and
purine overproduction.

## Concordance and completeness

Judgement: accept the candidate as the correct DisMech mapping.

The resources agree on PRPS1 identity, X-linked inheritance, PRPP synthetase
superactivity, uric acid overproduction, gout, urolithiasis/nephrolithiasis,
sensorineural deafness, ataxia, developmental delay, and intellectual
disability. IEMbase is more granular for assay material and specimen-specific
hypoxanthine/uric-acid rows.

## Curation actions

- Map this record to `PRPS1_Superactivity.yaml`.
- Consider future enrichment with urine hypoxanthine, PRPP synthase activity in
  fibroblasts and red blood cells, red-cell PRPP, and specimen-specific plasma
  versus urine uric-acid rows after source verification.
- Treat absent IEMbase treatment rows as incomplete IEMbase coverage rather than
  a contradiction of any local urate-lowering management context.
