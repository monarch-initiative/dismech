

# Slot: mapped_diseases 


_Names of dismech disease entries mapped or candidate-mapped to this FDA row_





URI: [dismech:slot/mapped_diseases](https://w3id.org/monarch-initiative/dismech/slot/mapped_diseases)
Alias: mapped_diseases

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SurrogateEndpoint](../classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [SurrogateEndpoint](../classes/SurrogateEndpoint.md) |

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
| self | dismech:mapped_diseases |
| native | dismech:mapped_diseases |




## LinkML Source

<details>
```yaml
name: mapped_diseases
description: Names of dismech disease entries mapped or candidate-mapped to this FDA
  row
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mapped_diseases
domain_of:
- SurrogateEndpoint
range: string
multivalued: true

```
</details>