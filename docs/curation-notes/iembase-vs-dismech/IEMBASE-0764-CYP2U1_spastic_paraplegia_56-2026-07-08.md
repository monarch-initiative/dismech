# IEMbase 0764: CYP2U1-related spastic paraplegia 56

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 764 |
| Nosology | 14.5.01.14 |
| Nosology code | IEM0673 |
| Gene | CYP2U1 |
| External IDs | OMIM:615030; ORPHA:320411 |
| Generated mapping | CANDIDATE; `Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as CYP2U1-related spastic
paraplegia 56. The source signal includes characteristic spastic paraparesis,
psychomotor retardation or regression, intellectual disability, dystonia,
peripheral neuropathy, pigmentary maculopathy, thin corpus callosum,
cerebellar white matter abnormalities, basal ganglia calcifications, and
low-to-normal CSF 5-methyltetrahydrofolic acid in infancy and childhood.

## DisMech phenotype coverage

No exact CYP2U1 / SPG56 entry is present locally. The generated
`Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity.yaml`
candidate is a false positive for disease identity. That local entry is a
GBA2-related SPG46 / cerebellar ataxia with late-onset spasticity disorder
based on nonlysosomal glucosylceramidase deficiency, not CYP2U1-related SPG56.

## Concordance and completeness

Judgement: true local gap.

The GBA2 candidate shares spasticity, ataxia, neuropathy, and corpus-callosum
vocabulary, but it has the wrong causal gene and lipid mechanism. The IEMbase
CYP2U1 record should remain unmapped until a SPG56-specific entry exists.

## Curation actions

- Add a distinct CYP2U1 / spastic paraplegia 56 target before treating this
  record as covered.
- Reject `Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity.yaml`
  as exact coverage.
- Preserve the CSF 5-MTHF, basal-ganglia calcification, pigmentary maculopathy,
  thin corpus callosum, dystonia, neuropathy, and psychomotor regression prompts.
