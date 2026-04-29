

# Slot: publication 


_Associated publication (PMID)_





URI: [dismech:slot/publication](https://w3id.org/monarch-initiative/dismech/slot/publication)
Alias: publication

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [ProteinStructure](../classes/ProteinStructure.md) | A 3D protein structure from PDB or AlphaFold relevant to understanding a trea... |  no  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |






## Properties

* Range: [PMID](../types/PMID.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:publication |
| native | dismech:publication |




## LinkML Source

<details>
```yaml
name: publication
description: Associated publication (PMID)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: publication
domain_of:
- Dataset
- ComputationalModel
- ProteinStructure
range: PMID

```
</details>