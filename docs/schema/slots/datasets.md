

# Slot: datasets 


_Publicly available datasets relevant to disease research_





URI: [dismech:slot/datasets](https://w3id.org/monarch-initiative/dismech/slot/datasets)
Alias: datasets

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Experiment](../classes/Experiment.md) | A structured experiment or protocol-level study design that can be proposed t... |  no  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Dataset](../classes/Dataset.md) |
| Domain Of | [Experiment](../classes/Experiment.md), [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:datasets |
| native | dismech:datasets |




## LinkML Source

<details>
```yaml
name: datasets
description: Publicly available datasets relevant to disease research
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: datasets
domain_of:
- Experiment
- Disease
range: Dataset
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>