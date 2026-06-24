

# Slot: direction 


_Direction of association between the biomarker value/presence and the linked pathograph node_





URI: [dismech:slot/direction](https://w3id.org/monarch-initiative/dismech/slot/direction)
Alias: direction

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  no  |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomarkerReadoutDirectionEnum](../enums/BiomarkerReadoutDirectionEnum.md) |
| Domain Of | [ExperimentalReadout](../classes/ExperimentalReadout.md), [BiomarkerReadout](../classes/BiomarkerReadout.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:direction |
| native | dismech:direction |




## LinkML Source

<details>
```yaml
name: direction
description: Direction of association between the biomarker value/presence and the
  linked pathograph node
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: direction
domain_of:
- ExperimentalReadout
- BiomarkerReadout
range: BiomarkerReadoutDirectionEnum

```
</details>