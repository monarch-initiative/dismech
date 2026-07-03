

# Slot: subtype 



URI: [dismech:slot/subtype](https://w3id.org/monarch-initiative/dismech/slot/subtype)
Alias: subtype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [PhenotypeContext](../classes/PhenotypeContext.md), [Prevalence](../classes/Prevalence.md), [ProgressionInfo](../classes/ProgressionInfo.md), [Phenotype](../classes/Phenotype.md), [Biochemical](../classes/Biochemical.md), [HistopathologyFinding](../classes/HistopathologyFinding.md), [Genetic](../classes/Genetic.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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