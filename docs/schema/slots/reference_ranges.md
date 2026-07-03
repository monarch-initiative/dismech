

# Slot: reference_ranges 


_Clinical laboratory reference intervals for this biomarker, keyed by LOINC code with population qualifier and UCUM units._





URI: [dismech:slot/reference_ranges](https://w3id.org/monarch-initiative/dismech/slot/reference_ranges)
Alias: reference_ranges

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceRange](../classes/ReferenceRange.md) |
| Domain Of | [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:reference_ranges |
| native | dismech:reference_ranges |




## LinkML Source

<details>
```yaml
name: reference_ranges
description: Clinical laboratory reference intervals for this biomarker, keyed by
  LOINC code with population qualifier and UCUM units.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: reference_ranges
domain_of:
- Biochemical
range: ReferenceRange
multivalued: true
inlined: true
inlined_as_list: true

```
</details>