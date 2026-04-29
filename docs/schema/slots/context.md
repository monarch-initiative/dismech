

# Slot: context 



URI: [dismech:slot/context](https://w3id.org/monarch-initiative/dismech/slot/context)
Alias: context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)





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