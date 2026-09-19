

# Slot: biological_scale 


_Biological scale of the substrate this pathophysiology node primarily describes — molecular, cellular, tissue/organ, or organism. Optional tag; each value covers both ongoing processes and persistent states at that scale. See BiologicalScaleEnum for scope of each value and projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the design rationale._





URI: [dismech:slot/biological_scale](https://w3id.org/monarch-initiative/dismech/slot/biological_scale)
Alias: biological_scale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalScaleEnum](../enums/BiologicalScaleEnum.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| MOLECULAR |
| TISSUE |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:biological_scale |
| native | dismech:biological_scale |




## LinkML Source

<details>
```yaml
name: biological_scale
description: Biological scale of the substrate this pathophysiology node primarily
  describes — molecular, cellular, tissue/organ, or organism. Optional tag; each value
  covers both ongoing processes and persistent states at that scale. See BiologicalScaleEnum
  for scope of each value and projects/PATHOPHYSIOLOGY_SCALE_FEASIBILITY.md for the
  design rationale.
examples:
- value: MOLECULAR
- value: TISSUE
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: biological_scale
domain_of:
- Pathophysiology
range: BiologicalScaleEnum

```
</details>