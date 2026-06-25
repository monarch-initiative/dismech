

# Slot: allelic_events 


_Event types affecting the allele or locus. Multivalued so events such as deletion plus loss of heterozygosity can be composed without cross-product enum values._





URI: [dismech:slot/allelic_events](https://w3id.org/monarch-initiative/dismech/slot/allelic_events)
Alias: allelic_events

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AllelicEventEnum](../enums/AllelicEventEnum.md) |
| Domain Of | [GeneticContext](../classes/GeneticContext.md) |

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
| self | dismech:allelic_events |
| native | dismech:allelic_events |




## LinkML Source

<details>
```yaml
name: allelic_events
description: Event types affecting the allele or locus. Multivalued so events such
  as deletion plus loss of heterozygosity can be composed without cross-product enum
  values.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: allelic_events
domain_of:
- GeneticContext
range: AllelicEventEnum
multivalued: true

```
</details>