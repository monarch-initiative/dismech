

# Slot: rationale 


_Why this Discussion matters / what hangs on its resolution_





URI: [dismech:slot/rationale](https://w3id.org/monarch-initiative/dismech/slot/rationale)
Alias: rationale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalBurden](../classes/ClinicalBurden.md) | Disease-level assessment of the typical clinical burden imposed by a disease |  yes  |
| [Discussion](../classes/Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |
| [AlgorithmValidationStatus](../classes/AlgorithmValidationStatus.md) | Validation maturity of a phenotype algorithm / computable case definition: a ... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ClinicalBurden](../classes/ClinicalBurden.md), [AlgorithmValidationStatus](../classes/AlgorithmValidationStatus.md), [Discussion](../classes/Discussion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:rationale |
| native | dismech:rationale |




## LinkML Source

<details>
```yaml
name: rationale
description: Why this Discussion matters / what hangs on its resolution
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: rationale
domain_of:
- ClinicalBurden
- AlgorithmValidationStatus
- Discussion
range: string

```
</details>