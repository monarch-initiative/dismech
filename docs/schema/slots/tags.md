

# Slot: tags 


_Authoritative-source tags for a reference (e.g. GeneReviews). Populated programmatically by scripts/tag_references.py; use `just tag-references` to refresh._





URI: [dismech:slot/tags](https://w3id.org/monarch-initiative/dismech/slot/tags)
Alias: tags

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PublicationReference](../classes/PublicationReference.md) | A reference to a publication with associated findings |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceTagEnum](../enums/ReferenceTagEnum.md) |
| Domain Of | [PublicationReference](../classes/PublicationReference.md) |

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
| self | dismech:tags |
| native | dismech:tags |




## LinkML Source

<details>
```yaml
name: tags
description: Authoritative-source tags for a reference (e.g. GeneReviews). Populated
  programmatically by scripts/tag_references.py; use `just tag-references` to refresh.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: tags
domain_of:
- PublicationReference
range: ReferenceTagEnum
multivalued: true

```
</details>