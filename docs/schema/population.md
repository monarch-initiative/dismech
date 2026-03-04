

# Slot: population 


_Population or cohort description (e.g., for prevalence or association signals)_





URI: [dismech:population](https://w3id.org/monarch-initiative/dismech/population)
Alias: population

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [Prevalence](Prevalence.md) |  |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| Global |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:population |
| native | dismech:population |




## LinkML Source

<details>
```yaml
name: population
description: Population or cohort description (e.g., for prevalence or association
  signals)
examples:
- value: Global
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: population
domain_of:
- PhenotypeContext
- Prevalence
- AssociationSignal
range: string

```
</details>