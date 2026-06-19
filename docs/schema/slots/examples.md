

# Slot: examples 



URI: [dismech:slot/examples](https://w3id.org/monarch-initiative/dismech/slot/examples)
Alias: examples

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md), [Genetic](../classes/Genetic.md), [Environmental](../classes/Environmental.md), [Stage](../classes/Stage.md), [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| ['Kaposi Sarcoma'] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:examples |
| native | dismech:examples |




## LinkML Source

<details>
```yaml
name: examples
examples:
- value: '[''Kaposi Sarcoma'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: examples
domain_of:
- Pathophysiology
- Genetic
- Environmental
- Stage
- Treatment
range: string
multivalued: true

```
</details>