

# Slot: action_category 


_Optional high-level category for a clinical action in the treatments section. Use THERAPEUTIC for actions that treat, prevent, mitigate, or manage disease mechanisms or symptoms; use non-therapeutic categories for screening, diagnosis, monitoring, and counseling or informational interventions._





URI: [dismech:slot/action_category](https://w3id.org/monarch-initiative/dismech/slot/action_category)
Alias: action_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MedicalActionCategoryEnum](../enums/MedicalActionCategoryEnum.md) |
| Domain Of | [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:action_category |
| native | dismech:action_category |




## LinkML Source

<details>
```yaml
name: action_category
description: Optional high-level category for a clinical action in the treatments
  section. Use THERAPEUTIC for actions that treat, prevent, mitigate, or manage disease
  mechanisms or symptoms; use non-therapeutic categories for screening, diagnosis,
  monitoring, and counseling or informational interventions.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: action_category
domain_of:
- Treatment
range: MedicalActionCategoryEnum

```
</details>