

# Slot: source_content_current_as_of 


_Date shown by the source as the content-current-as-of date_





URI: [dismech:slot/source_content_current_as_of](https://w3id.org/monarch-initiative/dismech/slot/source_content_current_as_of)
Alias: source_content_current_as_of

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
| self | dismech:source_content_current_as_of |
| native | dismech:source_content_current_as_of |




## LinkML Source

<details>
```yaml
name: source_content_current_as_of
description: Date shown by the source as the content-current-as-of date
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: source_content_current_as_of
domain_of:
- SurrogateEndpoint
- SurrogateEndpointCollection
range: date

```
</details>