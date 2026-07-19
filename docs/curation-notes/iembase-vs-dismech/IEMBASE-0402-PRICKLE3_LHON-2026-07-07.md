# IEMbase 0402: PRICKLE3-related Leber Hereditary Optic Neuropathy, LHON

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 402 |
| Nosology | 11.4.09.01 |
| Gene | PRICKLE3 |
| External IDs | OMIM:535000 |
| Generated mapping | UNMAPPED; low candidate `Congenital_Insensitivity_to_Pain.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PRICKLE3-related Leber hereditary optic neuropathy (LHON),
with X-linked dominant inheritance. Characteristic clinical rows include loss
of central vision, optic atrophy, and cardiac conduction deficits. Additional
rows include ataxia and subacute demyelinating mixed motor-sensory neuropathy.
The record has no biochemical or treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for PRICKLE3-related LHON. The generated
`Congenital_Insensitivity_to_Pain.yaml` candidate is a false positive: the local
CIP file is a phenotype-grouping/navigation entry for congenital absence of
protective pain perception, not an optic neuropathy or mitochondrial disease
entry.

The local corpus contains many Leber congenital amaurosis and optic-atrophy
entries, plus a differential-diagnosis mention of LHON in
`Multiple_Mitochondrial_Dysfunctions_Syndrome_9B.yaml`, but those are not
disease-level PRICKLE3-LHON coverage.

## Concordance and completeness

Judgement: true PRICKLE3-LHON local gap; reject the congenital-insensitivity-to-
pain candidate.

The IEMbase disease is an inherited optic neuropathy with PRICKLE3 and
conduction/neuropathy context. The generated candidate has a different disease
axis, phenotype definition, and gene set.

## Curation actions

- Keep this record unmapped until a PRICKLE3-related LHON target exists.
- Do not map to `Congenital_Insensitivity_to_Pain.yaml`.
- Do not substitute Leber congenital amaurosis files; LHON and LCA are distinct
  optic/retinal disease classes.
- If curated, include X-linked dominant inheritance, central vision loss, optic
  atrophy, conduction deficits, ataxia, and mixed motor-sensory neuropathy as
  review prompts.
