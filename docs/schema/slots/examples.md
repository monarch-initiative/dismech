

# Slot: examples 



URI: [dismech:slot/examples](https://w3id.org/monarch-initiative/dismech/slot/examples)
Alias: examples

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Multivalued: True





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