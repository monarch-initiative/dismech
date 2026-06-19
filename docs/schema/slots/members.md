

# Slot: members 


_The explicit members of this grouping (the union it groups; points down to individual entries)._





URI: [dismech:slot/members](https://w3id.org/monarch-initiative/dismech/slot/members)
Alias: members

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupingMember](../classes/GroupingMember.md) |
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
| self | dismech:members |
| native | dismech:members |




## LinkML Source

<details>
```yaml
name: members
description: The explicit members of this grouping (the union it groups; points down
  to individual entries).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: members
domain_of:
- Grouping
range: GroupingMember
multivalued: true
inlined: true
inlined_as_list: true

```
</details>