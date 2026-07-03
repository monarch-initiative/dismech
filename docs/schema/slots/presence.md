

# Slot: presence 



URI: [dismech:slot/presence](https://w3id.org/monarch-initiative/dismech/slot/presence)
Alias: presence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Diagnosis](../classes/Diagnosis.md) |  |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Biochemical](../classes/Biochemical.md), [Genetic](../classes/Genetic.md), [Environmental](../classes/Environmental.md), [Diagnosis](../classes/Diagnosis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Positive |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:presence |
| native | dismech:presence |




## LinkML Source

<details>
```yaml
name: presence
examples:
- value: Positive
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: presence
domain_of:
- Biochemical
- Genetic
- Environmental
- Diagnosis
range: string

```
</details>