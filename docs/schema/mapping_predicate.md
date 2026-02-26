

# Slot: mapping_predicate 


_Relationship between this disease and the mapped term (e.g., skos:exactMatch)_





URI: [dismech:mapping_predicate](https://w3id.org/monarch-initiative/dismech/mapping_predicate)
Alias: mapping_predicate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  yes  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)




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