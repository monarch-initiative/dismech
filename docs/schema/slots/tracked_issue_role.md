

# Slot: tracked_issue_role 


_Role this tracked issue plays relative to the dismech content it is attached to. Free-text but common values include "ontology_term_request", "ontology_coverage_gap", "schema_followup", "curation_followup", and "external_tracker_link"._





URI: [dismech:slot/tracked_issue_role](https://w3id.org/monarch-initiative/dismech/slot/tracked_issue_role)
Alias: tracked_issue_role

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
| ontology_term_request |
| schema_followup |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:tracked_issue_role |
| native | dismech:tracked_issue_role |




## LinkML Source

<details>
```yaml
name: tracked_issue_role
description: Role this tracked issue plays relative to the dismech content it is attached
  to. Free-text but common values include "ontology_term_request", "ontology_coverage_gap",
  "schema_followup", "curation_followup", and "external_tracker_link".
examples:
- value: ontology_term_request
- value: schema_followup
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: tracked_issue_role
domain_of:
- TrackedIssue
range: string

```
</details>