

# Slot: phase 



URI: [dismech:slot/phase](https://w3id.org/monarch-initiative/dismech/slot/phase)
Alias: phase

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhaseTerm](../enums/PhaseTerm.md) |
| Domain Of | [ClinicalTrial](../classes/ClinicalTrial.md), [ProgressionInfo](../classes/ProgressionInfo.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Active TB |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:phase |
| native | dismech:phase |




## LinkML Source

<details>
```yaml
name: phase
examples:
- value: Active TB
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: phase
domain_of:
- ClinicalTrial
- ProgressionInfo
range: PhaseTerm

```
</details>