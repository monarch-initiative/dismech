

# Slot: icimd_category 


_International Classification of Inherited Metabolic Disorders (ICIMD) category/group classification (for inherited metabolic disorders)_





URI: [dismech:slot/icimd_category](https://w3id.org/monarch-initiative/dismech/slot/icimd_category)
Alias: icimd_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseClassifications](../classes/DiseaseClassifications.md) | Container for all classification assignments for a disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ICIMDAssignment](../classes/ICIMDAssignment.md) |
| Domain Of | [DiseaseClassifications](../classes/DiseaseClassifications.md) |

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
| self | dismech:icimd_category |
| native | dismech:icimd_category |




## LinkML Source

<details>
```yaml
name: icimd_category
description: International Classification of Inherited Metabolic Disorders (ICIMD)
  category/group classification (for inherited metabolic disorders)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: icimd_category
domain_of:
- DiseaseClassifications
range: ICIMDAssignment
multivalued: true
inlined: true

```
</details>