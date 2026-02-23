

# Slot: review_notes 



URI: [dismech:review_notes](https://w3id.org/monarch-initiative/dismech/review_notes)
Alias: review_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) |  |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [Genetic](Genetic.md) |  |  no  |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |
| [Disease](Disease.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Subtype](Subtype.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |






## Properties

* Range: [String](String.md)





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