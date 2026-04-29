

# Slot: subtype 



URI: [dismech:slot/subtype](https://w3id.org/monarch-initiative/dismech/slot/subtype)
Alias: subtype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Prevalence](../classes/Prevalence.md) |  |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| Eyelid Myoclonia with Absences |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:subtype |
| native | dismech:subtype |




## LinkML Source

<details>
```yaml
name: subtype
examples:
- value: Eyelid Myoclonia with Absences
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: subtype
domain_of:
- PhenotypeContext
- Prevalence
- ProgressionInfo
- Phenotype
- Biochemical
- HistopathologyFinding
- Genetic
range: string

```
</details>