

# Slot: frequency 



URI: [dismech:slot/frequency](https://w3id.org/monarch-initiative/dismech/slot/frequency)
Alias: frequency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

* Range: [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[FrequencyEnum](../enums/FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](../types/FrequencyQuantity.md)





## Examples

| Value |
| --- |
| Occasional |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:frequency |
| native | dismech:frequency |




## LinkML Source

<details>
```yaml
name: frequency
examples:
- value: Occasional
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: frequency
domain_of:
- PhenotypeContext
- Pathophysiology
- Phenotype
- Biochemical
- HistopathologyFinding
- Genetic
range: Any
any_of:
- range: FrequencyEnum
- range: FrequencyQuantity

```
</details>