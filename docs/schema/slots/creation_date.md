

# Slot: creation_date 


_ISO 8601/RFC 3339 timestamp string for when this disease entry was first created (e.g., 2025-06-12T20:16:27Z)_





URI: [dismech:slot/creation_date](https://w3id.org/monarch-initiative/dismech/slot/creation_date)
Alias: creation_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  yes  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  yes  |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Disease](../classes/Disease.md), [ComorbidityAssociation](../classes/ComorbidityAssociation.md), [Grouping](../classes/Grouping.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Recommended | Yes |
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
| self | dismech:creation_date |
| native | dismech:creation_date |




## LinkML Source

<details>
```yaml
name: creation_date
description: ISO 8601/RFC 3339 timestamp string for when this disease entry was first
  created (e.g., 2025-06-12T20:16:27Z)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: creation_date
domain_of:
- Disease
- ComorbidityAssociation
- Grouping
range: string
recommended: true
pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})$

```
</details>