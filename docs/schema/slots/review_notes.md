

# Slot: review_notes 



URI: [dismech:slot/review_notes](https://w3id.org/monarch-initiative/dismech/slot/review_notes)
Alias: review_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ClinicalTrial](../classes/ClinicalTrial.md), [Subtype](../classes/Subtype.md), [ProgressionInfo](../classes/ProgressionInfo.md), [Phenotype](../classes/Phenotype.md), [Genetic](../classes/Genetic.md), [Environmental](../classes/Environmental.md), [Disease](../classes/Disease.md), [Stage](../classes/Stage.md), [AgentLifeCycle](../classes/AgentLifeCycle.md), [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md), [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Added an additional clinically relevant subtype. |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:review_notes |
| native | dismech:review_notes |




## LinkML Source

<details>
```yaml
name: review_notes
examples:
- value: Added an additional clinically relevant subtype.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: review_notes
domain_of:
- ClinicalTrial
- Subtype
- ProgressionInfo
- Phenotype
- Genetic
- Environmental
- Disease
- Stage
- AgentLifeCycle
- AgentLifeCycleStage
- Treatment
range: string

```
</details>