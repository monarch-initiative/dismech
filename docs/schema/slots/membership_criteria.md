

# Slot: membership_criteria 


_The shared criteria a Disease must satisfy to belong to this grouping, expressed as human-readable prose plus an optional structured boolean expression. Multivalued so a grouping can carry several independent NECESSARY criteria blocks alongside an optional defining (NECESSARY_AND_SUFFICIENT) block, mirroring OWL subclass/equivalence axioms._





URI: [dismech:slot/membership_criteria](https://w3id.org/monarch-initiative/dismech/slot/membership_criteria)
Alias: membership_criteria

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupingCriteria](../classes/GroupingCriteria.md) |
| Domain Of | [Grouping](../classes/Grouping.md) |

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
| self | dismech:membership_criteria |
| native | dismech:membership_criteria |




## LinkML Source

<details>
```yaml
name: membership_criteria
description: The shared criteria a Disease must satisfy to belong to this grouping,
  expressed as human-readable prose plus an optional structured boolean expression.
  Multivalued so a grouping can carry several independent NECESSARY criteria blocks
  alongside an optional defining (NECESSARY_AND_SUFFICIENT) block, mirroring OWL subclass/equivalence
  axioms.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: membership_criteria
domain_of:
- Grouping
range: GroupingCriteria
multivalued: true
inlined: true
inlined_as_list: true

```
</details>