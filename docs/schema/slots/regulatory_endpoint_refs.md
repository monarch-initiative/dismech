

# Slot: regulatory_endpoint_refs 


_Stable row identifiers for source-level regulatory surrogate endpoint assertions that use this biomarker readout in a specific context of use. For FDA surrogate endpoints, values should match row_id values in kb/surrogate_endpoints/fda_surrogate_endpoints.yaml._





URI: [dismech:slot/regulatory_endpoint_refs](https://w3id.org/monarch-initiative/dismech/slot/regulatory_endpoint_refs)
Alias: regulatory_endpoint_refs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [BiomarkerReadout](../classes/BiomarkerReadout.md) |

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
| self | dismech:regulatory_endpoint_refs |
| native | dismech:regulatory_endpoint_refs |




## LinkML Source

<details>
```yaml
name: regulatory_endpoint_refs
description: Stable row identifiers for source-level regulatory surrogate endpoint
  assertions that use this biomarker readout in a specific context of use. For FDA
  surrogate endpoints, values should match row_id values in kb/surrogate_endpoints/fda_surrogate_endpoints.yaml.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: regulatory_endpoint_refs
domain_of:
- BiomarkerReadout
range: string
multivalued: true

```
</details>