

# Slot: snippet 


_An exact excerpt/quote from the referenced publication that supports or refutes the claim_





URI: [dismech:snippet](https://w3id.org/monarch-initiative/dismech/snippet)
Alias: snippet

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvidenceItem](EvidenceItem.md) |  |  no  |






## Properties

* Range: [String](String.md)





## Examples

| Value |
| --- |
| At the moment there is no healing therapy, so early kidney transplant is a fundamental tool to improve prognosis. |

## Comments

* This is automatically validated by the linkml-reference-validator tool.

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:snippet |
| native | dismech:snippet |




## LinkML Source

<details>
```yaml
name: snippet
implements:
- linkml:excerpt
description: An exact excerpt/quote from the referenced publication that supports
  or refutes the claim
comments:
- This is automatically validated by the linkml-reference-validator tool.
examples:
- value: At the moment there is no healing therapy, so early kidney transplant is
    a fundamental tool to improve prognosis.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: snippet
domain_of:
- EvidenceItem
range: string

```
</details>