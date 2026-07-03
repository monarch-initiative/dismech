

# Slot: subtype_term 


_The ontology term grounding this subtype or cancer facet value. Prefer MONDO when available; use NCIT for oncology-specific subtype refinement when needed._





URI: [dismech:slot/subtype_term](https://w3id.org/monarch-initiative/dismech/slot/subtype_term)
Alias: subtype_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subtype](../classes/Subtype.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SubtypeDescriptor](../classes/SubtypeDescriptor.md) |
| Domain Of | [Subtype](../classes/Subtype.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:subtype_term |
| native | dismech:subtype_term |




## LinkML Source

<details>
```yaml
name: subtype_term
description: The ontology term grounding this subtype or cancer facet value. Prefer
  MONDO when available; use NCIT for oncology-specific subtype refinement when needed.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: subtype_term
domain_of:
- Subtype
range: SubtypeDescriptor
inlined: true

```
</details>