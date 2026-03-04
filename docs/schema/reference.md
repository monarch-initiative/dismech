

# Slot: reference 


_The authoritative reference (publication) for this evidence item_





URI: [dismech:reference](https://w3id.org/monarch-initiative/dismech/reference)
Alias: reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MappingConsistency](MappingConsistency.md) | Consistency assertion for a mapping relative to another source |  yes  |
| [EvidenceItem](EvidenceItem.md) |  |  no  |
| [PublicationReference](PublicationReference.md) | A reference to a publication with associated findings |  yes  |






## Properties

* Range: [PMID](PMID.md)





## Examples

| Value |
| --- |
| PMID:35533128 |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:reference |
| native | dismech:reference |




## LinkML Source

<details>
```yaml
name: reference
implements:
- linkml:authoritative_reference
description: The authoritative reference (publication) for this evidence item
examples:
- value: PMID:35533128
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: reference
domain_of:
- EvidenceItem
- PublicationReference
- MappingConsistency
range: PMID

```
</details>