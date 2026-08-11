# Enum: DiscussionStatusEnum 




_Lifecycle status for a Discussion_



URI: [dismech:enum/DiscussionStatusEnum](https://w3id.org/monarch-initiative/dismech/enum/DiscussionStatusEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| OPEN | None | Posed but not yet under active discussion |
| UNDER_DISCUSSION | None | Actively being discussed in one or more linked venues |
| RESOLVED | None | Closed with a documented resolution; kept for provenance |
| ARCHIVED | None | No longer active and not resolved (deferred, stale, or superseded) |




## Slots

| Name | Description |
| ---  | --- |
| [status](../slots/status.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DiscussionStatusEnum
description: Lifecycle status for a Discussion
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  OPEN:
    text: OPEN
    description: Posed but not yet under active discussion
  UNDER_DISCUSSION:
    text: UNDER_DISCUSSION
    description: Actively being discussed in one or more linked venues
  RESOLVED:
    text: RESOLVED
    description: Closed with a documented resolution; kept for provenance
  ARCHIVED:
    text: ARCHIVED
    description: No longer active and not resolved (deferred, stale, or superseded)

```
</details>