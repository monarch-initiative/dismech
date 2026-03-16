

# Slot: mappings_list 


_Ontology term mappings for a model variable (LOINC, CHEBI, HP, etc.)_





URI: [dismech:slot/mappings_list](https://w3id.org/monarch-initiative/dismech/slot/mappings_list)
Alias: mappings_list

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelVariable](../classes/ModelVariable.md) | A variable in a computational model, identified by a human-readable name, wit... |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

* Range: [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:mappings_list |
| native | dismech:mappings_list |




## LinkML Source

<details>
```yaml
name: mappings_list
description: Ontology term mappings for a model variable (LOINC, CHEBI, HP, etc.)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mappings_list
domain_of:
- ModelVariable
- Biochemical
range: ModelVariableDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>