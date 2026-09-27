

# Slot: interpretation 


_Curator-facing explanation of how to interpret the biomarker relative to the linked pathograph node_





URI: [dismech:slot/interpretation](https://w3id.org/monarch-initiative/dismech/slot/interpretation)
Alias: interpretation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  yes  |
| [PhenotypeReadout](../classes/PhenotypeReadout.md) | Links an investigation-readout phenotype (an abnormal electrophysiology, func... |  yes  |
| [ReferenceRangeBand](../classes/ReferenceRangeBand.md) | A single graded interpretation band within a reference range, mapping a value... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExperimentalReadout](../classes/ExperimentalReadout.md), [BiomarkerReadout](../classes/BiomarkerReadout.md), [PhenotypeReadout](../classes/PhenotypeReadout.md), [ReferenceRangeBand](../classes/ReferenceRangeBand.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:interpretation |
| native | dismech:interpretation |




## LinkML Source

<details>
```yaml
name: interpretation
description: Curator-facing explanation of how to interpret the biomarker relative
  to the linked pathograph node
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: interpretation
domain_of:
- ExperimentalReadout
- BiomarkerReadout
- PhenotypeReadout
- ReferenceRangeBand
range: string

```
</details>