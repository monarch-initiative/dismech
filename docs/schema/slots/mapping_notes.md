

# Slot: mapping_notes 


_Notes on code-to-concept mapping decisions for this signal_





URI: [dismech:slot/mapping_notes](https://w3id.org/monarch-initiative/dismech/slot/mapping_notes)
Alias: mapping_notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [SurrogateEndpoint](../classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [SurrogateEndpoint](../classes/SurrogateEndpoint.md), [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:mapping_notes |
| native | dismech:mapping_notes |




## LinkML Source

<details>
```yaml
name: mapping_notes
description: Notes on code-to-concept mapping decisions for this signal
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mapping_notes
domain_of:
- SurrogateEndpoint
- AssociationSignal
range: string

```
</details>