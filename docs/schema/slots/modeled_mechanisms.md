

# Slot: modeled_mechanisms 


_Pathophysiology mechanism nodes/assertions that this experimental model is intended to recapitulate, perturb, or measure within the disease pathograph._





URI: [dismech:slot/modeled_mechanisms](https://w3id.org/monarch-initiative/dismech/slot/modeled_mechanisms)
Alias: modeled_mechanisms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalModel](../classes/ExperimentalModel.md) | A disease-relevant non-animal experimental model system |  no  |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ModelMechanismLink](../classes/ModelMechanismLink.md) |
| Domain Of | [ExperimentalModel](../classes/ExperimentalModel.md), [ComputationalModel](../classes/ComputationalModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Target names should match pathophysiology entry names in the same disease file
* Use description to capture the specific assayable or modeled assertion, not just the node label
* Kept intentionally lightweight so it can later align more explicitly with NAMO relations



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:modeled_mechanisms |
| native | dismech:modeled_mechanisms |




## LinkML Source

<details>
```yaml
name: modeled_mechanisms
description: Pathophysiology mechanism nodes/assertions that this experimental model
  is intended to recapitulate, perturb, or measure within the disease pathograph.
comments:
- Target names should match pathophysiology entry names in the same disease file
- Use description to capture the specific assayable or modeled assertion, not just
  the node label
- Kept intentionally lightweight so it can later align more explicitly with NAMO relations
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: modeled_mechanisms
domain_of:
- ExperimentalModel
- ComputationalModel
range: ModelMechanismLink
multivalued: true
inlined: true
inlined_as_list: true

```
</details>