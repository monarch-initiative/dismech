

# Slot: review_notes 



URI: [dismech:slot/review_notes](https://w3id.org/monarch-initiative/dismech/slot/review_notes)
Alias: review_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [Disease](../classes/Disease.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |






## Properties

* Range: [String](../types/String.md)





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