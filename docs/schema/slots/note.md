

# Slot: note 


_Free-text curator note on the link (e.g. which arms overlap)._





URI: [dismech:slot/note](https://w3id.org/monarch-initiative/dismech/slot/note)
Alias: note

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneSetAssociation](../classes/GeneSetAssociation.md) | A curated link between this disease and an external gene set, referenced by i... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [GeneSetAssociation](../classes/GeneSetAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeneSetAssociation](../classes/GeneSetAssociation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:note |
| native | dismech:note |




## LinkML Source

<details>
```yaml
name: note
description: Free-text curator note on the link (e.g. which arms overlap).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: note
owner: GeneSetAssociation
domain_of:
- GeneSetAssociation
range: string

```
</details>