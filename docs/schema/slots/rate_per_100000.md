

# Slot: rate_per_100000 


_Normalized point estimate of occurrence expressed as cases per 100,000, for machine comparison across records. Convert from any source notation (% -> x1000; "per million" -> /10; "1 in N" -> 100000/N). Leave absent for band-only or qualitative records; use rate_low/rate_high for ranges._





URI: [dismech:slot/rate_per_100000](https://w3id.org/monarch-initiative/dismech/slot/rate_per_100000)
Alias: rate_per_100000

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [Prevalence](../classes/Prevalence.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| 0.82 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:rate_per_100000 |
| native | dismech:rate_per_100000 |




## LinkML Source

<details>
```yaml
name: rate_per_100000
description: Normalized point estimate of occurrence expressed as cases per 100,000,
  for machine comparison across records. Convert from any source notation (% -> x1000;
  "per million" -> /10; "1 in N" -> 100000/N). Leave absent for band-only or qualitative
  records; use rate_low/rate_high for ranges.
examples:
- value: '0.82'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: rate_per_100000
domain_of:
- Prevalence
range: float

```
</details>