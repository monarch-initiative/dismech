

# Slot: directionality 


_Direction of a comorbidity/trajectory association_





URI: [dismech:slot/directionality](https://w3id.org/monarch-initiative/dismech/slot/directionality)
Alias: directionality

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ComorbidityDirectionEnum](../enums/ComorbidityDirectionEnum.md) |
| Domain Of | [ComorbidityAssociation](../classes/ComorbidityAssociation.md), [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:directionality |
| native | dismech:directionality |




## LinkML Source

<details>
```yaml
name: directionality
description: Direction of a comorbidity/trajectory association
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: directionality
domain_of:
- ComorbidityAssociation
- AssociationSignal
range: ComorbidityDirectionEnum

```
</details>