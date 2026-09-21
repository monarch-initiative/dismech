# Enum: EvidenceItemSupportEnum 




_Which way the cited evidence cuts relative to the claim. This is direction only. How *directly* the quote bears on the claim is a separate axis -- see DirectnessEnum and the `directness` slot -- and how strong the evidence is has no slot at all (see design decisions section 12)._



URI: [dismech:enum/EvidenceItemSupportEnum](https://w3id.org/monarch-initiative/dismech/enum/EvidenceItemSupportEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SUPPORT | None | The cited evidence supports the claim | Title: Supports<br>|
| REFUTE | None | The cited evidence contradicts the claim | Title: Refutes<br>|
| NO_EVIDENCE | None | The cited reference does not contain evidence relevant to the claim | Title: No evidence<br>|




## Slots

| Name | Description |
| ---  | --- |
| [supports](../slots/supports.md) | Which way the cited evidence cuts relative to the claim |








## Comments

* SUPPORT and REFUTE map onto the SEPIO `directionOfEvidenceProvided` values `supports` and `disputes`. NO_EVIDENCE is a dismech extension: SEPIO's third value, `neutral`, means the evidence bears on the claim without favouring either side, whereas NO_EVIDENCE means it does not bear on the claim at all. The exporter must not silently equate them.
* PARTIAL and WRONG_STATEMENT were removed in the issue #7439 narrowing. PARTIAL conflated four distinct things -- indirect support, an inverted model system, an item that supported one claim while contradicting another, and simple irrelevance -- and became SUPPORT (with `directness` left unset), a split pair of items, or NO_EVIDENCE. WRONG_STATEMENT had a single use recording that an earlier entry text was inaccurate, which is provenance for a history/ record rather than evidence direction.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: EvidenceItemSupportEnum
description: Which way the cited evidence cuts relative to the claim. This is direction
  only. How *directly* the quote bears on the claim is a separate axis -- see DirectnessEnum
  and the `directness` slot -- and how strong the evidence is has no slot at all (see
  design decisions section 12).
comments:
- 'SUPPORT and REFUTE map onto the SEPIO `directionOfEvidenceProvided` values `supports`
  and `disputes`. NO_EVIDENCE is a dismech extension: SEPIO''s third value, `neutral`,
  means the evidence bears on the claim without favouring either side, whereas NO_EVIDENCE
  means it does not bear on the claim at all. The exporter must not silently equate
  them.'
- 'PARTIAL and WRONG_STATEMENT were removed in the issue #7439 narrowing. PARTIAL
  conflated four distinct things -- indirect support, an inverted model system, an
  item that supported one claim while contradicting another, and simple irrelevance
  -- and became SUPPORT (with `directness` left unset), a split pair of items, or
  NO_EVIDENCE. WRONG_STATEMENT had a single use recording that an earlier entry text
  was inaccurate, which is provenance for a history/ record rather than evidence direction.'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  SUPPORT:
    text: SUPPORT
    description: The cited evidence supports the claim
    title: Supports
    exact_mappings:
    - sepio:supports
  REFUTE:
    text: REFUTE
    description: The cited evidence contradicts the claim
    title: Refutes
    exact_mappings:
    - sepio:disputes
  NO_EVIDENCE:
    text: NO_EVIDENCE
    description: The cited reference does not contain evidence relevant to the claim
    title: No evidence

```
</details>