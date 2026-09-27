

# Slot: validation_status 


_Structured validation maturity of a phenotype algorithm / computable case definition (a graded status plus a free-text rationale and optional citing evidence)._





URI: [dismech:slot/validation_status](https://w3id.org/monarch-initiative/dismech/slot/validation_status)
Alias: validation_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Definition](../classes/Definition.md) | A diagnostic or phenotype definition for the disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AlgorithmValidationStatus](../classes/AlgorithmValidationStatus.md) |
| Domain Of | [Definition](../classes/Definition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:validation_status |
| native | dismech:validation_status |




## LinkML Source

<details>
```yaml
name: validation_status
description: Structured validation maturity of a phenotype algorithm / computable
  case definition (a graded status plus a free-text rationale and optional citing
  evidence).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: validation_status
domain_of:
- Definition
range: AlgorithmValidationStatus
inlined: true

```
</details>