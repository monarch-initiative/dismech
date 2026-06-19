

# Slot: abnormal_flag 


_Categorical abnormal-result flag for a reference-range band, following HL7/LOINC interpretation conventions (normal, low, high, critical)._





URI: [dismech:slot/abnormal_flag](https://w3id.org/monarch-initiative/dismech/slot/abnormal_flag)
Alias: abnormal_flag

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceRangeBand](../classes/ReferenceRangeBand.md) | A single graded interpretation band within a reference range, mapping a value... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AbnormalFlagEnum](../enums/AbnormalFlagEnum.md) |
| Domain Of | [ReferenceRangeBand](../classes/ReferenceRangeBand.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:abnormal_flag |
| native | dismech:abnormal_flag |




## LinkML Source

<details>
```yaml
name: abnormal_flag
description: Categorical abnormal-result flag for a reference-range band, following
  HL7/LOINC interpretation conventions (normal, low, high, critical).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: abnormal_flag
domain_of:
- ReferenceRangeBand
range: AbnormalFlagEnum

```
</details>