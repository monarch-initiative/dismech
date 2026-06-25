

# Slot: row_id 


_Stable row identifier assigned during source-table curation_





URI: [dismech:slot/row_id](https://w3id.org/monarch-initiative/dismech/slot/row_id)
Alias: row_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SurrogateEndpoint](../classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [SurrogateEndpoint](../classes/SurrogateEndpoint.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:row_id |
| native | dismech:row_id |




## LinkML Source

<details>
```yaml
name: row_id
description: Stable row identifier assigned during source-table curation
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
identifier: true
alias: row_id
domain_of:
- SurrogateEndpoint
range: string
required: true

```
</details>