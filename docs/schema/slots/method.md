

# Slot: method 


_Method or pipeline name_





URI: [dismech:slot/method](https://w3id.org/monarch-initiative/dismech/slot/method)
Alias: method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  yes  |
| [ProteinStructure](../classes/ProteinStructure.md) | A 3D protein structure from PDB or AlphaFold relevant to understanding a trea... |  no  |
| [GOEnrichment](../classes/GOEnrichment.md) | GO enrichment results for an association signal |  no  |






## Properties

* Range: [String](../types/String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:method |
| native | dismech:method |




## LinkML Source

<details>
```yaml
name: method
description: Method or pipeline name
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: method
domain_of:
- ProteinStructure
- AssociationSignal
- GOEnrichment
range: string

```
</details>