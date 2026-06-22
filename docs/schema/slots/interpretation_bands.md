

# Slot: interpretation_bands 


_Ordered graded interpretation bands that partition a measurement scale into categorical tiers (e.g., normal / mild / moderate / severe). Each band maps a value interval to a clinical category, so a numeric result can be classified. Complements the normal interval given by lower_bound/upper_bound on the parent reference range._





URI: [dismech:slot/interpretation_bands](https://w3id.org/monarch-initiative/dismech/slot/interpretation_bands)
Alias: interpretation_bands

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceRange](../classes/ReferenceRange.md) | A population reference interval for a clinical laboratory analyte |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceRangeBand](../classes/ReferenceRangeBand.md) |
| Domain Of | [ReferenceRange](../classes/ReferenceRange.md) |

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
| self | dismech:interpretation_bands |
| native | dismech:interpretation_bands |




## LinkML Source

<details>
```yaml
name: interpretation_bands
description: Ordered graded interpretation bands that partition a measurement scale
  into categorical tiers (e.g., normal / mild / moderate / severe). Each band maps
  a value interval to a clinical category, so a numeric result can be classified.
  Complements the normal interval given by lower_bound/upper_bound on the parent reference
  range.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: interpretation_bands
domain_of:
- ReferenceRange
range: ReferenceRangeBand
multivalued: true
inlined: true
inlined_as_list: true

```
</details>