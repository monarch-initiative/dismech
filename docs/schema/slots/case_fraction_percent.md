

# Slot: case_fraction_percent 


_Point estimate of the percentage of cases attributable to this gene in the stated cohort (0-100). The structured, queryable counterpart of the free-text genetic `frequency` band. Use case_fraction_low/high for ranges._





URI: [dismech:slot/case_fraction_percent](https://w3id.org/monarch-initiative/dismech/slot/case_fraction_percent)
Alias: case_fraction_percent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneCaseFraction](../classes/GeneCaseFraction.md) | A structured estimate of the fraction of cases of a genetically heterogeneous... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [GeneCaseFraction](../classes/GeneCaseFraction.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 24.6 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:case_fraction_percent |
| native | dismech:case_fraction_percent |




## LinkML Source

<details>
```yaml
name: case_fraction_percent
description: Point estimate of the percentage of cases attributable to this gene in
  the stated cohort (0-100). The structured, queryable counterpart of the free-text
  genetic `frequency` band. Use case_fraction_low/high for ranges.
examples:
- value: '24.6'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: case_fraction_percent
domain_of:
- GeneCaseFraction
range: float

```
</details>