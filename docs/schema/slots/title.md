

# Slot: title 


_Title of the publication_





URI: [dismech:slot/title](https://w3id.org/monarch-initiative/dismech/slot/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackedIssue](../classes/TrackedIssue.md) | Structured pointer to an external tracker issue (typically a GitHub issue) us... |  yes  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [PublicationReference](../classes/PublicationReference.md) | A reference to a publication with associated findings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Dataset](../classes/Dataset.md), [PublicationReference](../classes/PublicationReference.md), [TrackedIssue](../classes/TrackedIssue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:title |
| native | dismech:title |




## LinkML Source

<details>
```yaml
name: title
implements:
- linkml:title
description: Title of the publication
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: title
domain_of:
- Dataset
- PublicationReference
- TrackedIssue
range: string

```
</details>