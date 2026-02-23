

# Slot: context 



URI: [dismech:context](https://w3id.org/monarch-initiative/dismech/context)
Alias: context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |






## Properties

* Range: [String](String.md)





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