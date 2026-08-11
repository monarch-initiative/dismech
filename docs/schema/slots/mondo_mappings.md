

# Slot: mondo_mappings 


_MONDO disease ontology mappings for this disease_





URI: [dismech:slot/mondo_mappings](https://w3id.org/monarch-initiative/dismech/slot/mondo_mappings)
Alias: mondo_mappings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseMappings](../classes/DiseaseMappings.md) | Container for external identifier mappings for a disease or subtype |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MondoMapping](../classes/MondoMapping.md) |
| Domain Of | [DiseaseMappings](../classes/DiseaseMappings.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:mondo_mappings |
| native | dismech:mondo_mappings |




## LinkML Source

<details>
```yaml
name: mondo_mappings
description: MONDO disease ontology mappings for this disease
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mondo_mappings
domain_of:
- DiseaseMappings
range: MondoMapping
multivalued: true
inlined: true
inlined_as_list: true

```
</details>