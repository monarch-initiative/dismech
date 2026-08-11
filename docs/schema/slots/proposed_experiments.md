

# Slot: proposed_experiments 


_Experiments proposed as ways to resolve this Discussion. The Experiment object is intentionally neutral: whether it is proposed, planned, in progress, or reported is determined by its containing context. Here, nesting under a Discussion means the experiment is proposed as a response to an open item or knowledge gap._





URI: [dismech:slot/proposed_experiments](https://w3id.org/monarch-initiative/dismech/slot/proposed_experiments)
Alias: proposed_experiments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Discussion](../classes/Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Experiment](../classes/Experiment.md) |
| Domain Of | [Discussion](../classes/Discussion.md) |

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
| self | dismech:proposed_experiments |
| native | dismech:proposed_experiments |




## LinkML Source

<details>
```yaml
name: proposed_experiments
description: 'Experiments proposed as ways to resolve this Discussion. The Experiment
  object is intentionally neutral: whether it is proposed, planned, in progress, or
  reported is determined by its containing context. Here, nesting under a Discussion
  means the experiment is proposed as a response to an open item or knowledge gap.'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: proposed_experiments
domain_of:
- Discussion
range: Experiment
multivalued: true
inlined: true
inlined_as_list: true

```
</details>