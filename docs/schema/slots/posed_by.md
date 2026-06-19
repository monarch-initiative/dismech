

# Slot: posed_by 


_Optional attribution for who posed a Discussion. ORCID is preferred when available (e.g., `ORCID:0000-0002-1825-0097`); a github handle or email is acceptable._





URI: [dismech:slot/posed_by](https://w3id.org/monarch-initiative/dismech/slot/posed_by)
Alias: posed_by

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Discussion](../classes/Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Discussion](../classes/Discussion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:posed_by |
| native | dismech:posed_by |




## LinkML Source

<details>
```yaml
name: posed_by
description: Optional attribution for who posed a Discussion. ORCID is preferred when
  available (e.g., `ORCID:0000-0002-1825-0097`); a github handle or email is acceptable.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: posed_by
domain_of:
- Discussion
range: string

```
</details>