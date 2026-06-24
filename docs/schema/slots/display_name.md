

# Slot: display_name 


_Human-readable display name for a subtype, used when the name (which serves as the FK target) is too terse for comfortable display. Optional; when absent, renderers should fall back to name._





URI: [dismech:slot/display_name](https://w3id.org/monarch-initiative/dismech/slot/display_name)
Alias: display_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [GroupingMember](../classes/GroupingMember.md) | One member of a grouping, referenced by foreign key, together with the mechan... |  no  |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Subtype](../classes/Subtype.md), [Grouping](../classes/Grouping.md), [GroupingMember](../classes/GroupingMember.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:display_name |
| native | dismech:display_name |




## LinkML Source

<details>
```yaml
name: display_name
description: Human-readable display name for a subtype, used when the name (which
  serves as the FK target) is too terse for comfortable display. Optional; when absent,
  renderers should fall back to name.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: display_name
domain_of:
- Subtype
- Grouping
- GroupingMember
range: string

```
</details>