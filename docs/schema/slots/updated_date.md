

# Slot: updated_date  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_ISO 8601/RFC 3339 timestamp string for when this disease entry was last updated (e.g., 2025-06-12T20:16:27Z). Deprecated: use git history for authoritative change timestamps. Existing entries may retain this field; new entries should omit it._





URI: [dismech:slot/updated_date](https://w3id.org/monarch-initiative/dismech/slot/updated_date)
Alias: updated_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  yes  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Disease](../classes/Disease.md), [ComorbidityAssociation](../classes/ComorbidityAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:updated_date |
| native | dismech:updated_date |




## LinkML Source

<details>
```yaml
name: updated_date
description: 'ISO 8601/RFC 3339 timestamp string for when this disease entry was last
  updated (e.g., 2025-06-12T20:16:27Z). Deprecated: use git history for authoritative
  change timestamps. Existing entries may retain this field; new entries should omit
  it.'
deprecated: 'True'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: updated_date
domain_of:
- Disease
- ComorbidityAssociation
range: string
recommended: false
pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$

```
</details>