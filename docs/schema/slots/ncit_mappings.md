

# Slot: ncit_mappings 


_NCIT disease, subtype, or disease/finding mappings_





URI: [dismech:slot/ncit_mappings](https://w3id.org/monarch-initiative/dismech/slot/ncit_mappings)
Alias: ncit_mappings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseMappings](../classes/DiseaseMappings.md) | Container for external identifier mappings for a disease or subtype |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NCITMapping](../classes/NCITMapping.md) |
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
| self | dismech:ncit_mappings |
| native | dismech:ncit_mappings |




## LinkML Source

<details>
```yaml
name: ncit_mappings
description: NCIT disease, subtype, or disease/finding mappings
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: ncit_mappings
domain_of:
- DiseaseMappings
range: NCITMapping
multivalued: true
inlined: true
inlined_as_list: true

```
</details>