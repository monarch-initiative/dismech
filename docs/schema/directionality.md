

# Slot: directionality 


_Direction of a comorbidity/trajectory association_





URI: [dismech:directionality](https://w3id.org/monarch-initiative/dismech/directionality)
Alias: directionality

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |






## Properties

* Range: [ComorbidityDirectionEnum](ComorbidityDirectionEnum.md)




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