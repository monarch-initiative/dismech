

# Slot: cohort_size 


_Number of probands/cases in the cohort the case fraction was computed in, when reported. Helps weight competing per-gene estimates._





URI: [dismech:slot/cohort_size](https://w3id.org/monarch-initiative/dismech/slot/cohort_size)
Alias: cohort_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneCaseFraction](../classes/GeneCaseFraction.md) | A structured estimate of the fraction of cases of a genetically heterogeneous... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [GeneCaseFraction](../classes/GeneCaseFraction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 61 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:cohort_size |
| native | dismech:cohort_size |




## LinkML Source

<details>
```yaml
name: cohort_size
description: Number of probands/cases in the cohort the case fraction was computed
  in, when reported. Helps weight competing per-gene estimates.
examples:
- value: '61'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: cohort_size
domain_of:
- GeneCaseFraction
range: integer

```
</details>