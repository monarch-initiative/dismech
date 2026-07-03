

# Slot: disease_term 


_The MONDO disease term for this disease_





URI: [dismech:slot/disease_term](https://w3id.org/monarch-initiative/dismech/slot/disease_term)
Alias: disease_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GroupingMember](../classes/GroupingMember.md) | One member of a grouping, referenced by foreign key, together with the mechan... |  no  |
| [Disease](../classes/Disease.md) |  |  no  |
| [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseDescriptor](../classes/DiseaseDescriptor.md) |
| Domain Of | [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md), [Disease](../classes/Disease.md), [GroupingMember](../classes/GroupingMember.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:disease_term |
| native | dismech:disease_term |




## LinkML Source

<details>
```yaml
name: disease_term
description: The MONDO disease term for this disease
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: disease_term
domain_of:
- DifferentialDiagnosis
- Disease
- GroupingMember
range: DiseaseDescriptor
inlined: true

```
</details>