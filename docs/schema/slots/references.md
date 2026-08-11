

# Slot: references 


_Top-level list of references with their key findings for this disease_





URI: [dismech:slot/references](https://w3id.org/monarch-initiative/dismech/slot/references)
Alias: references

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |
| [Grouping](../classes/Grouping.md) | An explicit, curated union of distinct Disease entries assembled below the le... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PublicationReference](../classes/PublicationReference.md) |
| Domain Of | [Disease](../classes/Disease.md), [Grouping](../classes/Grouping.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:references |
| native | dismech:references |




## LinkML Source

<details>
```yaml
name: references
description: Top-level list of references with their key findings for this disease
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: references
domain_of:
- Disease
- Grouping
range: PublicationReference
multivalued: true
inlined: true
inlined_as_list: true

```
</details>