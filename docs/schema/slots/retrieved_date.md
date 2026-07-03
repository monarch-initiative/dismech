

# Slot: retrieved_date 


_Date on which the source was retrieved for curation_





URI: [dismech:slot/retrieved_date](https://w3id.org/monarch-initiative/dismech/slot/retrieved_date)
Alias: retrieved_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FDASurrogateEndpointCollection](../classes/FDASurrogateEndpointCollection.md) | FDA surrogate endpoint table import preserving row-level source provenance |  no  |
| [SurrogateEndpoint](../classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |  no  |
| [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md) | A source-level collection of curated regulatory surrogate endpoint assertions |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](../types/Date.md) |
| Domain Of | [SurrogateEndpoint](../classes/SurrogateEndpoint.md), [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:retrieved_date |
| native | dismech:retrieved_date |




## LinkML Source

<details>
```yaml
name: retrieved_date
description: Date on which the source was retrieved for curation
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: retrieved_date
domain_of:
- SurrogateEndpoint
- SurrogateEndpointCollection
range: date

```
</details>