

# Slot: pathways 



URI: [dismech:slot/pathways](https://w3id.org/monarch-initiative/dismech/slot/pathways)
Alias: pathways

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

* Range: [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: Wnt Pathway}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:pathways |
| native | dismech:pathways |




## LinkML Source

<details>
```yaml
name: pathways
examples:
- value: '[{preferred_term: Wnt Pathway}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: pathways
domain_of:
- Pathophysiology
range: BiologicalProcessDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>