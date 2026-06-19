

# Slot: source_url 


_URL of the source page for a curated assertion or source collection_





URI: [dismech:slot/source_url](https://w3id.org/monarch-initiative/dismech/slot/source_url)
Alias: source_url

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
| Range | [Uri](../types/Uri.md) |
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
| self | dismech:source_url |
| native | dismech:source_url |




## LinkML Source

<details>
```yaml
name: source_url
description: URL of the source page for a curated assertion or source collection
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: source_url
domain_of:
- SurrogateEndpoint
- SurrogateEndpointCollection
range: uri

```
</details>