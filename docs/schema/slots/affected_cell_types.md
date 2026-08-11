

# Slot: affected_cell_types 


_Cell types in which gene expression is specifically gained or lost. Particularly relevant for mLOE variants (modular loss in specific cell types) and GOE variants (ectopic gain in new cell types)._





URI: [dismech:slot/affected_cell_types](https://w3id.org/monarch-initiative/dismech/slot/affected_cell_types)
Alias: affected_cell_types

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FunctionalEffect](../classes/FunctionalEffect.md) | Describes the functional consequence of a genetic variant, including regulato... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CellTypeDescriptor](../classes/CellTypeDescriptor.md) |
| Domain Of | [FunctionalEffect](../classes/FunctionalEffect.md) |

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
| self | dismech:affected_cell_types |
| native | dismech:affected_cell_types |




## LinkML Source

<details>
```yaml
name: affected_cell_types
description: Cell types in which gene expression is specifically gained or lost. Particularly
  relevant for mLOE variants (modular loss in specific cell types) and GOE variants
  (ectopic gain in new cell types).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: affected_cell_types
domain_of:
- FunctionalEffect
range: CellTypeDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>