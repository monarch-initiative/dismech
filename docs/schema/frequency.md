

# Slot: frequency 



URI: [dismech:frequency](https://w3id.org/monarch-initiative/dismech/frequency)
Alias: frequency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [Genetic](Genetic.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |






## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[FrequencyEnum](FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](FrequencyQuantity.md)





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