

# Slot: ligand 


_Name of bound drug/ligand if this is a co-crystal structure_





URI: [dismech:slot/ligand](https://w3id.org/monarch-initiative/dismech/slot/ligand)
Alias: ligand

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinStructure](../classes/ProteinStructure.md) | A 3D protein structure from PDB or AlphaFold relevant to understanding a trea... |  no  |






## Properties

* Range: [String](../types/String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ligand |
| native | dismech:ligand |




## LinkML Source

<details>
```yaml
name: ligand
description: Name of bound drug/ligand if this is a co-crystal structure
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: ligand
owner: ProteinStructure
domain_of:
- ProteinStructure
range: string

```
</details>