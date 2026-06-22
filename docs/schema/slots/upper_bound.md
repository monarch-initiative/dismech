

# Slot: upper_bound 


_Upper bound of a reference interval (inclusive). Null indicates no upper limit._





URI: [dismech:slot/upper_bound](https://w3id.org/monarch-initiative/dismech/slot/upper_bound)
Alias: upper_bound

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
| self | dismech:upper_bound |
| native | dismech:upper_bound |




## LinkML Source

<details>
```yaml
name: upper_bound
description: Upper bound of a reference interval (inclusive). Null indicates no upper
  limit.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: upper_bound
domain_of:
- ReferenceRangeBand
- ReferenceRange
range: float

```
</details>