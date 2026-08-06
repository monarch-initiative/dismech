

# Slot: isds_skeletal_category 


_ISDS Nosology and Classification of Genetic Skeletal Disorders group assignment (for genetic skeletal disorders). Assign only to entries the Nosology itself lists (or an unambiguous subtype/synonym of one); a single listed disorder carries exactly one group._





URI: [dismech:slot/isds_skeletal_category](https://w3id.org/monarch-initiative/dismech/slot/isds_skeletal_category)
Alias: isds_skeletal_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseClassifications](../classes/DiseaseClassifications.md) | Container for all classification assignments for a disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ISDSNosologyAssignment](../classes/ISDSNosologyAssignment.md) |
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
| self | dismech:isds_skeletal_category |
| native | dismech:isds_skeletal_category |




## LinkML Source

<details>
```yaml
name: isds_skeletal_category
description: ISDS Nosology and Classification of Genetic Skeletal Disorders group
  assignment (for genetic skeletal disorders). Assign only to entries the Nosology
  itself lists (or an unambiguous subtype/synonym of one); a single listed disorder
  carries exactly one group.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: isds_skeletal_category
domain_of:
- DiseaseClassifications
range: ISDSNosologyAssignment
multivalued: true
inlined: true

```
</details>