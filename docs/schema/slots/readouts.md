

# Slot: readouts 


_Links this biomarker to disease pathograph nodes that it measures, reflects, predicts, or pharmacodynamically reports on. The target should be a named pathograph node, typically a pathophysiology mechanism._





URI: [dismech:slot/readouts](https://w3id.org/monarch-initiative/dismech/slot/readouts)
Alias: readouts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomarkerReadout](../classes/BiomarkerReadout.md) |
| Domain Of | [Experiment](../classes/Experiment.md), [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Target names should match pathophysiology or phenotype entry names in the same disease file
* Readout links are observational/associative, not causal disease-progression edges
* Use evidence on the readout link when the biomarker-to-mechanism mapping is distinct from the biomarker's own evidence



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:readouts |
| native | dismech:readouts |




## LinkML Source

<details>
```yaml
name: readouts
description: Links this biomarker to disease pathograph nodes that it measures, reflects,
  predicts, or pharmacodynamically reports on. The target should be a named pathograph
  node, typically a pathophysiology mechanism.
comments:
- Target names should match pathophysiology or phenotype entry names in the same disease
  file
- Readout links are observational/associative, not causal disease-progression edges
- Use evidence on the readout link when the biomarker-to-mechanism mapping is distinct
  from the biomarker's own evidence
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: readouts
domain_of:
- Experiment
- Biochemical
range: BiomarkerReadout
multivalued: true
inlined: true
inlined_as_list: true

```
</details>