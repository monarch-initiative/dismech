

# Slot: pdb_id 


_PDB accession code (e.g., 3TCT) or AlphaFold identifier (e.g., AF-P02766-F1). Used to construct viewer URLs and fetch structure data._





URI: [dismech:slot/pdb_id](https://w3id.org/monarch-initiative/dismech/slot/pdb_id)
Alias: pdb_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinStructure](../classes/ProteinStructure.md) | A 3D protein structure from PDB or AlphaFold relevant to understanding a trea... |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:pdb_id |
| native | dismech:pdb_id |




## LinkML Source

<details>
```yaml
name: pdb_id
description: PDB accession code (e.g., 3TCT) or AlphaFold identifier (e.g., AF-P02766-F1).
  Used to construct viewer URLs and fetch structure data.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: pdb_id
owner: ProteinStructure
domain_of:
- ProteinStructure
range: string
required: true

```
</details>