

# Slot: lower_bound 


_Lower bound of a reference interval (inclusive). Null indicates no lower limit._





URI: [dismech:slot/lower_bound](https://w3id.org/monarch-initiative/dismech/slot/lower_bound)
Alias: lower_bound

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceRangeBand](../classes/ReferenceRangeBand.md) | A single graded interpretation band within a reference range, mapping a value... |  yes  |
| [ReferenceRange](../classes/ReferenceRange.md) | A population reference interval for a clinical laboratory analyte |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](../types/Float.md) |
| Domain Of | [ReferenceRangeBand](../classes/ReferenceRangeBand.md), [ReferenceRange](../classes/ReferenceRange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:lower_bound |
| native | dismech:lower_bound |




## LinkML Source

<details>
```yaml
name: lower_bound
description: Lower bound of a reference interval (inclusive). Null indicates no lower
  limit.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: lower_bound
domain_of:
- ReferenceRangeBand
- ReferenceRange
range: float

```
</details>