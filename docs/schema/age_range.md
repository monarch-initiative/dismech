

# Slot: age_range 


_Age range or stratification, if applicable_





URI: [dismech:age_range](https://w3id.org/monarch-initiative/dismech/age_range)
Alias: age_range

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |
| [Demographics](Demographics.md) | Demographic stratification for an association signal |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Childhood-Adolescence |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:age_range |
| native | dismech:age_range |




## LinkML Source

<details>
```yaml
name: age_range
description: Age range or stratification, if applicable
examples:
- value: Childhood-Adolescence
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: age_range
domain_of:
- PhenotypeContext
- ProgressionInfo
- Demographics
range: string

```
</details>