

# Slot: consistency 


_Consistency assertions for this mapping against other sources_





URI: [dismech:slot/consistency](https://w3id.org/monarch-initiative/dismech/slot/consistency)
Alias: consistency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ICD11FMapping](../classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [TermMapping](../classes/TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [ICD10CMMapping](../classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [MondoMapping](../classes/MondoMapping.md) | MONDO disease ontology mapping |  no  |






## Properties

* Range: [MappingConsistency](../classes/MappingConsistency.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:consistency |
| native | dismech:consistency |




## LinkML Source

<details>
```yaml
name: consistency
description: Consistency assertions for this mapping against other sources
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: consistency
domain_of:
- TermMapping
range: MappingConsistency
multivalued: true
inlined: true
inlined_as_list: true

```
</details>