

# Slot: surrogate_endpoints 


_Curated surrogate endpoint assertions_





URI: [dismech:slot/surrogate_endpoints](https://w3id.org/monarch-initiative/dismech/slot/surrogate_endpoints)
Alias: surrogate_endpoints

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FDASurrogateEndpointCollection](../classes/FDASurrogateEndpointCollection.md) | FDA surrogate endpoint table import preserving row-level source provenance |  no  |
| [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md) | A source-level collection of curated regulatory surrogate endpoint assertions |  yes  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SurrogateEndpoint](../classes/SurrogateEndpoint.md) |
| Domain Of | [SurrogateEndpointCollection](../classes/SurrogateEndpointCollection.md), [Disease](../classes/Disease.md) |

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
| self | dismech:surrogate_endpoints |
| native | dismech:surrogate_endpoints |




## LinkML Source

<details>
```yaml
name: surrogate_endpoints
description: Curated surrogate endpoint assertions
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: surrogate_endpoints
domain_of:
- SurrogateEndpointCollection
- Disease
range: SurrogateEndpoint
multivalued: true
inlined: true
inlined_as_list: true

```
</details>