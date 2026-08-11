

# Slot: association_signals 


_Association signals from EHR, registry, or computational sources_





URI: [dismech:slot/association_signals](https://w3id.org/monarch-initiative/dismech/slot/association_signals)
Alias: association_signals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AssociationSignal](../classes/AssociationSignal.md) |
| Domain Of | [ComorbidityAssociation](../classes/ComorbidityAssociation.md) |

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
| self | dismech:association_signals |
| native | dismech:association_signals |




## LinkML Source

<details>
```yaml
name: association_signals
description: Association signals from EHR, registry, or computational sources
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: association_signals
domain_of:
- ComorbidityAssociation
range: AssociationSignal
multivalued: true
inlined: true
inlined_as_list: true

```
</details>