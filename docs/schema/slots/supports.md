

# Slot: supports 


_Which way the cited evidence cuts relative to the claim. Direction only -- use `directness` for how directly the quote bears on it._





URI: [dismech:slot/supports](https://w3id.org/monarch-initiative/dismech/slot/supports)
Alias: supports

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceItem](../classes/EvidenceItem.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EvidenceItemSupportEnum](../enums/EvidenceItemSupportEnum.md) |
| Domain Of | [EvidenceItem](../classes/EvidenceItem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| SUPPORT |

## Comments

* Maps to EvidenceLine.directionOfEvidenceProvided in the draft SEPIO LinkML model. The NO_EVIDENCE value has no SEPIO counterpart; see EvidenceItemSupportEnum.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:supports |
| native | dismech:supports |
| exact | sepio:directionOfEvidenceProvided |




## LinkML Source

<details>
```yaml
name: supports
description: Which way the cited evidence cuts relative to the claim. Direction only
  -- use `directness` for how directly the quote bears on it.
comments:
- Maps to EvidenceLine.directionOfEvidenceProvided in the draft SEPIO LinkML model.
  The NO_EVIDENCE value has no SEPIO counterpart; see EvidenceItemSupportEnum.
examples:
- value: SUPPORT
from_schema: https://w3id.org/monarch-initiative/dismech
exact_mappings:
- sepio:directionOfEvidenceProvided
rank: 1000
alias: supports
domain_of:
- EvidenceItem
range: EvidenceItemSupportEnum

```
</details>