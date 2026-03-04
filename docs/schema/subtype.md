

# Slot: subtype 



URI: [dismech:subtype](https://w3id.org/monarch-initiative/dismech/subtype)
Alias: subtype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [Prevalence](Prevalence.md) |  |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [Genetic](Genetic.md) |  |  no  |






## Properties

* Range: [String](String.md)





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