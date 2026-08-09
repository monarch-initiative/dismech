

# Slot: measure_type 


_Which epidemiological measure this Prevalence record reports (point prevalence, birth prevalence, annual incidence, literature case-count, etc.). Makes explicit a dimension that was previously leaking into population/notes._





URI: [dismech:slot/measure_type](https://w3id.org/monarch-initiative/dismech/slot/measure_type)
Alias: measure_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrevalenceMeasureEnum](../enums/PrevalenceMeasureEnum.md) |
| Domain Of | [Prevalence](../classes/Prevalence.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| POINT_PREVALENCE |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:measure_type |
| native | dismech:measure_type |




## LinkML Source

<details>
```yaml
name: measure_type
description: Which epidemiological measure this Prevalence record reports (point prevalence,
  birth prevalence, annual incidence, literature case-count, etc.). Makes explicit
  a dimension that was previously leaking into population/notes.
examples:
- value: POINT_PREVALENCE
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: measure_type
domain_of:
- Prevalence
range: PrevalenceMeasureEnum

```
</details>