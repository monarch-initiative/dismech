

# Slot: directness 


_How directly the quoted text bears on the claim. Optional: absent means no one has assessed it, which is the state of most of the knowledge base._





URI: [dismech:slot/directness](https://w3id.org/monarch-initiative/dismech/slot/directness)
Alias: directness

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceItem](../classes/EvidenceItem.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DirectnessEnum](../enums/DirectnessEnum.md) |
| Domain Of | [EvidenceItem](../classes/EvidenceItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| DIRECT |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:directness |
| native | dismech:directness |




## LinkML Source

<details>
```yaml
name: directness
description: 'How directly the quoted text bears on the claim. Optional: absent means
  no one has assessed it, which is the state of most of the knowledge base.'
examples:
- value: DIRECT
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: directness
domain_of:
- EvidenceItem
range: DirectnessEnum

```
</details>