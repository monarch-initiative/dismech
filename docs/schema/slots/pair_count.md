

# Slot: pair_count 


_Number of records/patients with co-occurrence of disorder A and disorder B in the source dataset_





URI: [dismech:slot/pair_count](https://w3id.org/monarch-initiative/dismech/slot/pair_count)
Alias: pair_count

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](../types/Integer.md) |
| Domain Of | [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:pair_count |
| native | dismech:pair_count |




## LinkML Source

<details>
```yaml
name: pair_count
description: Number of records/patients with co-occurrence of disorder A and disorder
  B in the source dataset
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: pair_count
domain_of:
- AssociationSignal
range: integer

```
</details>