

# Slot: dietary_modifications 


_Structured dietary additions, restrictions, avoidances, or substitutions associated with a treatment descriptor._





URI: [dismech:slot/dietary_modifications](https://w3id.org/monarch-initiative/dismech/slot/dietary_modifications)
Alias: dietary_modifications

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinica... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DietaryModification](../classes/DietaryModification.md) |
| Domain Of | [TreatmentDescriptor](../classes/TreatmentDescriptor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Use only for intentional prescribed dietary manipulations within a treatment entry
* Do not mirror environmental risk factors here unless the treatment explicitly prescribes avoidance, restriction, or addition



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:dietary_modifications |
| native | dismech:dietary_modifications |




## LinkML Source

<details>
```yaml
name: dietary_modifications
description: Structured dietary additions, restrictions, avoidances, or substitutions
  associated with a treatment descriptor.
comments:
- Use only for intentional prescribed dietary manipulations within a treatment entry
- Do not mirror environmental risk factors here unless the treatment explicitly prescribes
  avoidance, restriction, or addition
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: dietary_modifications
domain_of:
- TreatmentDescriptor
range: DietaryModification
multivalued: true
inlined: true
inlined_as_list: true

```
</details>