

# Slot: conforms_to 


_Reference to a mechanism module that this pathophysiology node is an organ-specific instance of. Value is a path relative to kb/modules/ (e.g., "fibrotic_response") plus an optional node name after a hash (e.g., "fibrotic_response#Mesenchymal Cell Activation"). Used for cross-disorder consistency checking: if a node declares conformance, it should include the expected cell types, biological processes, and causal edges defined in the referenced module node._





URI: [dismech:slot/conforms_to](https://w3id.org/monarch-initiative/dismech/slot/conforms_to)
Alias: conforms_to

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:conforms_to |
| native | dismech:conforms_to |




## LinkML Source

<details>
```yaml
name: conforms_to
description: 'Reference to a mechanism module that this pathophysiology node is an
  organ-specific instance of. Value is a path relative to kb/modules/ (e.g., "fibrotic_response")
  plus an optional node name after a hash (e.g., "fibrotic_response#Mesenchymal Cell
  Activation"). Used for cross-disorder consistency checking: if a node declares conformance,
  it should include the expected cell types, biological processes, and causal edges
  defined in the referenced module node.'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: conforms_to
domain_of:
- Pathophysiology
range: string

```
</details>