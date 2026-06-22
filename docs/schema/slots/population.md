

# Slot: population 


_Population or cohort description (e.g., for prevalence or association signals)_





URI: [dismech:slot/population](https://w3id.org/monarch-initiative/dismech/slot/population)
Alias: population

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [ReferenceRange](../classes/ReferenceRange.md) | A population reference interval for a clinical laboratory analyte |  yes  |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [PhenotypeContext](../classes/PhenotypeContext.md), [ReferenceRange](../classes/ReferenceRange.md), [Prevalence](../classes/Prevalence.md), [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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
- ReferenceRange
- Prevalence
- AssociationSignal
range: string

```
</details>