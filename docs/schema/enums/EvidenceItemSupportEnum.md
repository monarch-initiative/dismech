# Enum: EvidenceItemSupportEnum 




_The level of support for an evidence item_



URI: [dismech:enum/EvidenceItemSupportEnum](https://w3id.org/monarch-initiative/dismech/enum/EvidenceItemSupportEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| WRONG_STATEMENT | None | The annotated claim contains a demonstrable factual error (e | Title: Wrong statement<br>|
| SUPPORT | None | The cited evidence directly supports the claim | Title: Supports<br>|
| REFUTE | None | The cited evidence directly contradicts the claim | Title: Refutes<br>|
| NO_EVIDENCE | None | The cited reference does not contain evidence relevant to the claim | Title: No evidence<br>|
| PARTIAL | None | The cited evidence partially or indirectly supports the claim | Title: Partially supports<br>|




## Slots

| Name | Description |
| ---  | --- |
| [supports](../slots/supports.md) |  |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: EvidenceItemSupportEnum
description: The level of support for an evidence item
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  WRONG_STATEMENT:
    text: WRONG_STATEMENT
    description: The annotated claim contains a demonstrable factual error (e.g.,
      an incorrect statistic or assertion); the cited evidence documents the correct
      information. Use this when the claim is outright wrong, not merely contested.
      If the cited reference simply does not mention the claim, use NO_EVIDENCE instead.
      If the reference contradicts the claim but does not prove it factually wrong,
      use REFUTE.
    title: Wrong statement
  SUPPORT:
    text: SUPPORT
    description: The cited evidence directly supports the claim
    title: Supports
  REFUTE:
    text: REFUTE
    description: The cited evidence directly contradicts the claim
    title: Refutes
  NO_EVIDENCE:
    text: NO_EVIDENCE
    description: The cited reference does not contain evidence relevant to the claim
    title: No evidence
  PARTIAL:
    text: PARTIAL
    description: The cited evidence partially or indirectly supports the claim
    title: Partially supports

```
</details>