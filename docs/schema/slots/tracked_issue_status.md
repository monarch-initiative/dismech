

# Slot: tracked_issue_status 


_Last known status of the tracked issue (e.g., "OPEN", "CLOSED", "MERGED"). This is a curator-recorded snapshot and may drift from the live tracker state._





URI: [dismech:slot/tracked_issue_status](https://w3id.org/monarch-initiative/dismech/slot/tracked_issue_status)
Alias: tracked_issue_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackedIssue](../classes/TrackedIssue.md) | Structured pointer to an external tracker issue (typically a GitHub issue) us... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [TrackedIssue](../classes/TrackedIssue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| OPEN |
| CLOSED |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:tracked_issue_status |
| native | dismech:tracked_issue_status |




## LinkML Source

<details>
```yaml
name: tracked_issue_status
description: Last known status of the tracked issue (e.g., "OPEN", "CLOSED", "MERGED").
  This is a curator-recorded snapshot and may drift from the live tracker state.
examples:
- value: OPEN
- value: CLOSED
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: tracked_issue_status
domain_of:
- TrackedIssue
range: string

```
</details>