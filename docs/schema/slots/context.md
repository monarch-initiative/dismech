

# Slot: context 



URI: [dismech:slot/context](https://w3id.org/monarch-initiative/dismech/slot/context)
Alias: context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Phenotype](../classes/Phenotype.md), [Biochemical](../classes/Biochemical.md), [HistopathologyFinding](../classes/HistopathologyFinding.md), [Stage](../classes/Stage.md), [AgentLifeCycle](../classes/AgentLifeCycle.md), [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md), [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| Pregnancy |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:context |
| native | dismech:context |




## LinkML Source

<details>
```yaml
name: context
examples:
- value: Pregnancy
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: context
domain_of:
- Phenotype
- Biochemical
- HistopathologyFinding
- Stage
- AgentLifeCycle
- AgentLifeCycleStage
- Treatment
range: string

```
</details>