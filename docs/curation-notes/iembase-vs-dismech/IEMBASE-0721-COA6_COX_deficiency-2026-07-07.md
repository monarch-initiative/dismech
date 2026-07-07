# IEMbase 0721: COA6-related cytochrome c oxidase assembly factor 6 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 721 |
| Nosology | 7.4.01.01 |
| Nosology code | IEM0469 |
| Gene | COA6 |
| External IDs | OMIM:616501; ORPHA:1561 |
| Generated mapping | CANDIDATE to `COX15-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | No exact COA6 disease target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COA6-related cytochrome c oxidase
assembly factor 6 deficiency. The alternate-name field links it to fatal
infantile cardioencephalomyopathy due to cytochrome c oxidase deficiency 4.

The cached rows include increased plasma lactate in neonatal and infantile
windows, perinatal death, and cardiomyopathy.

## DisMech phenotype coverage

No exact standalone COA6 disease file was identified.

Local complex IV assembly context mentions COA6 as part of the copper-center
assembly and metallochaperone network, and `COX16-Related_COX_Deficiency.yaml`
mentions COA6 as a related partner. That is pathway context, not exact COA6
disease coverage.

The generated `COX15-Related_COX_Deficiency.yaml` candidate is a severe COX
deficiency entry but represents COX15 heme A synthase disease, not COA6/type 4
cardioencephalomyopathy.

## Concordance and completeness

Judgement: true local COA6 gap. The COX15 candidate should be rejected as
exact coverage.

IEMbase supplies a compact but coherent neonatal/infantile COA6 phenotype:
lactate elevation, cardiomyopathy, and perinatal death. Existing DisMech module
mentions are useful for future mechanism placement but do not resolve the
standalone disease.

## Curation actions

- Add a dedicated COA6 complex IV/COX assembly deficiency target if curated.
- Reject `COX15-Related_COX_Deficiency.yaml` as exact COA6 coverage.
- Preserve neonatal/infantile lactate elevation, cardiomyopathy, and perinatal
  death.
- Reuse existing complex IV copper-center assembly context only as background.
