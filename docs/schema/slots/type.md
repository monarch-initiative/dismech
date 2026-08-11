

# Slot: type 



URI: [dismech:slot/type](https://w3id.org/monarch-initiative/dismech/slot/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](../classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |  no  |
| [FunctionalEffect](../classes/FunctionalEffect.md) | Describes the functional consequence of a genetic variant, including regulato... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Variant](../classes/Variant.md), [FunctionalEffect](../classes/FunctionalEffect.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:type |
| native | dismech:type |




## LinkML Source

<details>
```yaml
name: type
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: type
domain_of:
- Variant
- FunctionalEffect
range: string

```
</details>