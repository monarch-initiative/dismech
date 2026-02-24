

# Slot: mapping_source 


_Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)_





URI: [dismech:mapping_source](https://w3id.org/monarch-initiative/dismech/mapping_source)
Alias: mapping_source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:mapping_source |
| native | dismech:mapping_source |




## LinkML Source

<details>
```yaml
name: mapping_source
description: Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mapping_source
domain_of:
- TermMapping
range: string

```
</details>