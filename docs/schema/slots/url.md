

# Slot: url 


_URL for the external assertion or registry record_





URI: [dismech:slot/url](https://w3id.org/monarch-initiative/dismech/slot/url)
Alias: url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TrackedIssue](../classes/TrackedIssue.md) | Structured pointer to an external tracker issue (typically a GitHub issue) us... |  yes  |
| [ExternalAssertion](../classes/ExternalAssertion.md) | An externally curated assertion or registry record relevant to a disease or v... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uri](../types/Uri.md) |
| Domain Of | [ExternalAssertion](../classes/ExternalAssertion.md), [TrackedIssue](../classes/TrackedIssue.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:url |
| native | dismech:url |




## LinkML Source

<details>
```yaml
name: url
description: URL for the external assertion or registry record
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: url
domain_of:
- ExternalAssertion
- TrackedIssue
range: uri

```
</details>