

# Slot: mapping_predicate 


_Relationship between this disease and the mapped term (e.g., skos:exactMatch)_





URI: [dismech:slot/mapping_predicate](https://w3id.org/monarch-initiative/dismech/slot/mapping_predicate)
Alias: mapping_predicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ICD11FMapping](../classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [TermMapping](../classes/TermMapping.md) | Mapping from this disease entry to an external term or code |  yes  |
| [ICD10CMMapping](../classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [MondoMapping](../classes/MondoMapping.md) | MONDO disease ontology mapping |  no  |






## Properties

* Range: [Uriorcurie](../types/Uriorcurie.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:mapping_predicate |
| native | dismech:mapping_predicate |




## LinkML Source

<details>
```yaml
name: mapping_predicate
description: Relationship between this disease and the mapped term (e.g., skos:exactMatch)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mapping_predicate
domain_of:
- TermMapping
range: uriorcurie

```
</details>