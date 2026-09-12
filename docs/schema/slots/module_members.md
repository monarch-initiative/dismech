

# Slot: module_members 


_The mechanism modules explicitly included in this collection. Module filename stems are used as foreign keys._





URI: [dismech:slot/module_members](https://w3id.org/monarch-initiative/dismech/slot/module_members)
Alias: module_members

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModuleCollection](../classes/ModuleCollection.md) | A curated navigation or framework record that organizes mechanism modules |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ModuleCollectionMember](../classes/ModuleCollectionMember.md) |
| Domain Of | [ModuleCollection](../classes/ModuleCollection.md) |

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
| self | dismech:module_members |
| native | dismech:module_members |




## LinkML Source

<details>
```yaml
name: module_members
description: The mechanism modules explicitly included in this collection. Module
  filename stems are used as foreign keys.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: module_members
domain_of:
- ModuleCollection
range: ModuleCollectionMember
multivalued: true
inlined: true
inlined_as_list: true

```
</details>