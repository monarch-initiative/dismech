

# Slot: consistency 


_Consistency assertions for this mapping against other sources_





URI: [dismech:consistency](https://w3id.org/monarch-initiative/dismech/consistency)
Alias: consistency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |






## Properties

* Range: [MappingConsistency](MappingConsistency.md)

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