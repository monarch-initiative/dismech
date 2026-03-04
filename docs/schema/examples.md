

# Slot: examples 



URI: [dismech:examples](https://w3id.org/monarch-initiative/dismech/examples)
Alias: examples

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Genetic](Genetic.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |






## Properties

* Range: [String](String.md)

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