

# Slot: member 


_Foreign key to the grouped entity. For member_type DISEASE this is the Disease entry's `name`; for MODULE it is the module filename stem; for GROUPING it is another grouping's `name`._





URI: [dismech:slot/member](https://w3id.org/monarch-initiative/dismech/slot/member)
Alias: member

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GroupingMember](../classes/GroupingMember.md) | One member of a grouping, referenced by foreign key, together with the mechan... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [GroupingMember](../classes/GroupingMember.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:member |
| native | dismech:member |




## LinkML Source

<details>
```yaml
name: member
description: Foreign key to the grouped entity. For member_type DISEASE this is the
  Disease entry's `name`; for MODULE it is the module filename stem; for GROUPING
  it is another grouping's `name`.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: member
domain_of:
- GroupingMember
range: string
required: true

```
</details>