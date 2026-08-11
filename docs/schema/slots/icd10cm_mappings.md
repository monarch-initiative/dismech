

# Slot: icd10cm_mappings 


_ICD-10-CM code mappings for this disease_





URI: [dismech:slot/icd10cm_mappings](https://w3id.org/monarch-initiative/dismech/slot/icd10cm_mappings)
Alias: icd10cm_mappings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseMappings](../classes/DiseaseMappings.md) | Container for external identifier mappings for a disease or subtype |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ICD10CMMapping](../classes/ICD10CMMapping.md) |
| Domain Of | [DiseaseMappings](../classes/DiseaseMappings.md) |

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
| self | dismech:icd10cm_mappings |
| native | dismech:icd10cm_mappings |




## LinkML Source

<details>
```yaml
name: icd10cm_mappings
description: ICD-10-CM code mappings for this disease
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: icd10cm_mappings
domain_of:
- DiseaseMappings
range: ICD10CMMapping
multivalued: true
inlined: true
inlined_as_list: true

```
</details>