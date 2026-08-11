# IEMbase 0603: NUS1-related Nogo-B receptor deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 603 |
| Nosology | 18.4.02.02 |
| Gene | NUS1 |
| External IDs | OMIM:617082; ORPHA:442835 |
| Generated mapping | UNMAPPED; best candidate `Generalized_Epilepsy_with_Febrile_Seizures_Plus.yaml#GABRD` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents NUS1-related Nogo-B receptor deficiency, labelled NUS1-CDG
and NgBR-CDG. The record is autosomal recessive, classified under disorders of
multiple glycosylation pathways, has unknown treatability, and has no treatment
rows.

There are no biochemical rows. Clinical rows include neonatal or infantile axial
hypotonia, cortical atrophy on MRI, developmental delay, epilepsy, failure to
thrive, microcephaly, retinitis pigmentosa, scoliosis, and acral spasticity.

## DisMech phenotype coverage

`Generalized_Epilepsy_with_Febrile_Seizures_Plus.yaml#GABRD` is a weak
false-positive candidate. It models GABRD/GABA-A receptor delta contribution to
GEFS+ and neuronal excitation-inhibition imbalance. It does not represent NUS1,
Nogo-B receptor / cis-prenyltransferase complex biology, autosomal recessive
CDG, retinitis pigmentosa, cortical atrophy, microcephaly, scoliosis, or the
failure-to-thrive phenotype bundle.

The local knowledge base has retinitis-pigmentosa and epilepsy modules/entries,
but no exact NUS1-CDG target was identified.

## Concordance and completeness

Judgement: true local gap; reject the GABRD epilepsy candidate.

The generated weak candidate reflects seizure vocabulary only. IEMbase centers a
NUS1 glycosylation/dolichol-related neuroretinal syndrome with developmental and
growth features, which is not covered by the local GEFS+ entry.

## Curation actions

- Create or identify an exact NUS1 / Nogo-B receptor deficiency / NgBR-CDG target
  before import.
- Reject `Generalized_Epilepsy_with_Febrile_Seizures_Plus.yaml#GABRD` as an
  exact mapping.
- Preserve cortical atrophy, retinitis pigmentosa, epilepsy, microcephaly,
  axial hypotonia, acral spasticity, scoliosis, developmental delay, and
  failure-to-thrive prompts.
