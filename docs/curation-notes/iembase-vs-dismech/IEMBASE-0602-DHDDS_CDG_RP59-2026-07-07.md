# IEMbase 0602: DHDDS-related dehydrodolichyl diphosphate synthase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 602 |
| Nosology | 18.4.01.04 |
| Gene | DHDDS |
| External IDs | OMIM:613861; OMIM:608172; ORPHA:442835 |
| Generated mapping | CANDIDATE; `EYS_Related_Retinitis_Pigmentosa.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DHDDS-related dehydrodolichyl diphosphate synthase
deficiency, labelled DHDDS-CDG and retinitis pigmentosa 59. The record is
autosomal recessive, classified under disorders of dolichol biosynthesis and
activation, has unknown treatability, and has no treatment rows.

The record has normal serum sialotransferrins as its only biochemical row.
Clinical rows include retinitis pigmentosa, epilepsy, intellectual disability,
ataxia, dystonia, hypotonia, micropenis, and acute renal failure.

## DisMech phenotype coverage

`EYS_Related_Retinitis_Pigmentosa.yaml` is a false-positive generated candidate.
It models EYS/RP25, a photoreceptor structural/ciliary retinitis pigmentosa
caused by the EYS gene. It does not represent DHDDS, dolichol-pathway
dehydrodolichyl diphosphate synthase deficiency, CDG biology, or the
extra-ocular epilepsy, intellectual-disability, movement, endocrine, and renal
features in IEMbase.

Other local retinitis-pigmentosa entries provide final-common photoreceptor
degeneration context only. No exact DHDDS-CDG / RP59 target was identified.

## Concordance and completeness

Judgement: true local gap; reject EYS-related retinitis pigmentosa as exact
coverage.

The candidate captures a shared retinitis-pigmentosa phenotype but fails the
gene, pathway, and multisystem checks. IEMbase 0602 is a dolichol-biosynthesis
CDG/retinal-neurologic disease, not an EYS photoreceptor structural disorder.

## Curation actions

- Create or identify an exact DHDDS-CDG / retinitis pigmentosa 59 target before
  import.
- Reject `EYS_Related_Retinitis_Pigmentosa.yaml` as an exact mapping.
- Preserve normal sialotransferrins, retinitis pigmentosa, epilepsy,
  intellectual disability, ataxia, dystonia, hypotonia, micropenis, and acute
  renal-failure prompts.
