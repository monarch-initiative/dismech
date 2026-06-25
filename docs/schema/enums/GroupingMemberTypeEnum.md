# Enum: GroupingMemberTypeEnum 




_The kind of entity referenced by a GroupingMember._



URI: [dismech:enum/GroupingMemberTypeEnum](https://w3id.org/monarch-initiative/dismech/enum/GroupingMemberTypeEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| DISEASE | None | A Disease entry in kb/disorders/ |
| SUBTYPE | None | A named subtype within a Disease entry |
| MODULE | None | A mechanism module in kb/modules/ |
| GROUPING | None | Another Grouping (nested grouping) |




## Slots

| Name | Description |
| ---  | --- |
| [member_type](../slots/member_type.md) | The kind of entity referenced by this member |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: GroupingMemberTypeEnum
description: The kind of entity referenced by a GroupingMember.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  DISEASE:
    text: DISEASE
    description: A Disease entry in kb/disorders/.
  SUBTYPE:
    text: SUBTYPE
    description: A named subtype within a Disease entry.
  MODULE:
    text: MODULE
    description: A mechanism module in kb/modules/.
  GROUPING:
    text: GROUPING
    description: Another Grouping (nested grouping).

```
</details>