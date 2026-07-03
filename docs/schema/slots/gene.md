

# Slot: gene 



URI: [dismech:slot/gene](https://w3id.org/monarch-initiative/dismech/slot/gene)
Alias: gene

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](../classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |  no  |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |
| [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md) | A structured perturbation, intervention, or exposure used in an experiment |  no  |
| [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) | A mechanism or feature that distinguishes a grouping member from its siblings... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneDescriptor](../classes/GeneDescriptor.md) |
| Domain Of | [GeneticContext](../classes/GeneticContext.md), [ExperimentalPerturbation](../classes/ExperimentalPerturbation.md), [Pathophysiology](../classes/Pathophysiology.md), [Variant](../classes/Variant.md), [LogicalCriterion](../classes/LogicalCriterion.md), [DifferentiatingMechanism](../classes/DifferentiatingMechanism.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| {preferred_term: MEFV} |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:gene |
| native | dismech:gene |




## LinkML Source

<details>
```yaml
name: gene
examples:
- value: '{preferred_term: MEFV}'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: gene
domain_of:
- GeneticContext
- ExperimentalPerturbation
- Pathophysiology
- Variant
- LogicalCriterion
- DifferentiatingMechanism
range: GeneDescriptor
inlined: true

```
</details>