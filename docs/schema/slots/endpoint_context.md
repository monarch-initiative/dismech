

# Slot: endpoint_context 


_Endpoint or use context for a biomarker readout link_





URI: [dismech:slot/endpoint_context](https://w3id.org/monarch-initiative/dismech/slot/endpoint_context)
Alias: endpoint_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomarkerEndpointContextEnum](../enums/BiomarkerEndpointContextEnum.md) |
| Domain Of | [BiomarkerReadout](../classes/BiomarkerReadout.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:endpoint_context |
| native | dismech:endpoint_context |




## LinkML Source

<details>
```yaml
name: endpoint_context
description: Endpoint or use context for a biomarker readout link
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: endpoint_context
domain_of:
- BiomarkerReadout
range: BiomarkerEndpointContextEnum

```
</details>