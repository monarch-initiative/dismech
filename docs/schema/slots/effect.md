

# Slot: effect 



URI: [dismech:slot/effect](https://w3id.org/monarch-initiative/dismech/slot/effect)
Alias: effect

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Transmission](../classes/Transmission.md) |  |  no  |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [Environmental](../classes/Environmental.md), [Transmission](../classes/Transmission.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Potential trigger for flare-ups |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:effect |
| native | dismech:effect |




## LinkML Source

<details>
```yaml
name: effect
examples:
- value: Potential trigger for flare-ups
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: effect
domain_of:
- ExperimentalPerturbation
- Environmental
- Transmission
range: string

```
</details>