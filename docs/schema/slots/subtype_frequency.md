

# Slot: subtype_frequency 


_Frequency of this subtype among all cases of the parent disease (e.g., '60-70%', '~15%'). Distinct from phenotype frequency._





URI: [dismech:slot/subtype_frequency](https://w3id.org/monarch-initiative/dismech/slot/subtype_frequency)
Alias: subtype_frequency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subtype](../classes/Subtype.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | NONE&nbsp;or&nbsp;<br />[FrequencyEnum](../enums/FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](../types/FrequencyQuantity.md) |
| Domain Of | [Subtype](../classes/Subtype.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'FrequencyEnum'})
- AnonymousSlotExpression({'range': 'FrequencyQuantity'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:subtype_frequency |
| native | dismech:subtype_frequency |




## LinkML Source

<details>
```yaml
name: subtype_frequency
description: Frequency of this subtype among all cases of the parent disease (e.g.,
  '60-70%', '~15%'). Distinct from phenotype frequency.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: subtype_frequency
domain_of:
- Subtype
any_of:
- range: FrequencyEnum
- range: FrequencyQuantity

```
</details>