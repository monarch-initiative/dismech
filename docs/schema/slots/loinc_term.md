

# Slot: loinc_term 


_LOINC code for a measured analyte or clinical observation (e.g., LOINC:2823-3 for serum potassium). Binds to the LOINC namespace._





URI: [dismech:slot/loinc_term](https://w3id.org/monarch-initiative/dismech/slot/loinc_term)
Alias: loinc_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceRange](../classes/ReferenceRange.md) | A population reference interval for a clinical laboratory analyte |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Term](../classes/Term.md) |
| Domain Of | [ReferenceRange](../classes/ReferenceRange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:loinc_term |
| native | dismech:loinc_term |




## LinkML Source

<details>
```yaml
name: loinc_term
description: LOINC code for a measured analyte or clinical observation (e.g., LOINC:2823-3
  for serum potassium). Binds to the LOINC namespace.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: loinc_term
domain_of:
- ReferenceRange
range: Term
inlined: true

```
</details>