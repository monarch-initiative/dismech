

# Slot: source_workbook_sha256 


_SHA-256 checksum of the downloaded source workbook used for import_





URI: [dismech:slot/source_workbook_sha256](https://w3id.org/monarch-initiative/dismech/slot/source_workbook_sha256)
Alias: source_workbook_sha256

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
| Range | [String](../types/String.md) |
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
| self | dismech:source_workbook_sha256 |
| native | dismech:source_workbook_sha256 |




## LinkML Source

<details>
```yaml
name: source_workbook_sha256
description: SHA-256 checksum of the downloaded source workbook used for import
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: source_workbook_sha256
domain_of:
- SurrogateEndpoint
- SurrogateEndpointCollection
range: string

```
</details>