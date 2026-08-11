

# Slot: member_type 


_The kind of entity referenced by this member._





URI: [dismech:slot/member_type](https://w3id.org/monarch-initiative/dismech/slot/member_type)
Alias: member_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GroupingMember](../classes/GroupingMember.md) | One member of a grouping, referenced by foreign key, together with the mechan... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GroupingMemberTypeEnum](../enums/GroupingMemberTypeEnum.md) |
| Domain Of | [GroupingMember](../classes/GroupingMember.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:member_type |
| native | dismech:member_type |




## LinkML Source

<details>
```yaml
name: member_type
description: The kind of entity referenced by this member.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: member_type
domain_of:
- GroupingMember
range: GroupingMemberTypeEnum

```
</details>