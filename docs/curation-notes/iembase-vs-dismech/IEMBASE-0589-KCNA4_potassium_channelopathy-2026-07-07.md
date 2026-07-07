# IEMbase 0589: KCNA4-related potassium channelopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 589 |
| Nosology | 25.1.05.01 |
| Gene | KCNA4 |
| External IDs | OMIM:176266 |
| Generated mapping | UNMAPPED; best candidate `CACNA1A_Related_Disorder.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents KCNA4-related potassium channelopathy, with alternate label
KCNA4 deficiency. The record is autosomal recessive, classified as
unclassified, has unknown treatability, and has no treatment rows.

The record has no biochemical rows. Characteristic clinical rows include
attention disorder, bilateral striatal necrosis, cataract, dystonia, growth
retardation, and microcephaly.

## DisMech phenotype coverage

`CACNA1A_Related_Disorder.yaml` is a false-positive generated candidate. It
models autosomal dominant CACNA1A P/Q-type calcium-channel disease, including
episodic ataxia type 2, familial hemiplegic migraine type 1, spinocerebellar
ataxia type 6, and developmental and epileptic encephalopathy type 42. It does
not represent KCNA4, Kv1.4 voltage-gated potassium-channel deficiency,
autosomal recessive inheritance, or bilateral striatal necrosis.

The local knowledge base has broad potassium-channel and striatal-necrosis
context in other diseases, but no exact KCNA4 deficiency target was identified.

## Concordance and completeness

Judgement: true local gap; reject the CACNA1A candidate.

The generated candidate shares a channelopathy/neurodevelopmental neighborhood,
but gene, channel class, inheritance, and phenotype anchor differ. The IEMbase
record should remain a separate KCNA4 potassium-channelopathy work item.

## Curation actions

- Create or identify an exact KCNA4 deficiency target before import.
- Reject `CACNA1A_Related_Disorder.yaml` as an exact mapping.
- Preserve attention disorder, bilateral striatal necrosis, cataract, dystonia,
  growth retardation, and microcephaly as clinical prompts for source review.
