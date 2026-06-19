

# Slot: phenotype_term 


_The HP term for this phenotype_





URI: [dismech:slot/phenotype_term](https://w3id.org/monarch-initiative/dismech/slot/phenotype_term)
Alias: phenotype_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReferenceRangeBand](../classes/ReferenceRangeBand.md) | A single graded interpretation band within a reference range, mapping a value... |  yes  |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |
| [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) | A mechanism or feature that distinguishes a grouping member from its siblings... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) |
| Domain Of | [ExperimentalReadout](../classes/ExperimentalReadout.md), [ReferenceRangeBand](../classes/ReferenceRangeBand.md), [Phenotype](../classes/Phenotype.md), [LogicalCriterion](../classes/LogicalCriterion.md), [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:phenotype_term |
| native | dismech:phenotype_term |




## LinkML Source

<details>
```yaml
name: phenotype_term
description: The HP term for this phenotype
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: phenotype_term
domain_of:
- ExperimentalReadout
- ReferenceRangeBand
- Phenotype
- LogicalCriterion
- DifferentiatingMechanism
range: PhenotypeDescriptor
inlined: true

```
</details>