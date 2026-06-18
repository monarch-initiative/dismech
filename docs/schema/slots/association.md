

# Slot: association 


_Free-text descriptor of how the gene is associated with the disease. For a controlled vocabulary, also set `relationship_type`._





URI: [dismech:slot/association](https://w3id.org/monarch-initiative/dismech/slot/association)
Alias: association

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Susceptibility |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:association |
| native | dismech:association |




## LinkML Source

<details>
```yaml
name: association
description: Free-text descriptor of how the gene is associated with the disease.
  For a controlled vocabulary, also set `relationship_type`.
examples:
- value: Susceptibility
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: association
domain_of:
- Genetic
range: string

```
</details>