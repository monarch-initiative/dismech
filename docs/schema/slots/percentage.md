

# Slot: percentage  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 



URI: [dismech:slot/percentage](https://w3id.org/monarch-initiative/dismech/slot/percentage)
Alias: percentage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[Integer](../types/Integer.md)&nbsp;or&nbsp;<br />[Float](../types/Float.md)&nbsp;or&nbsp;<br />[String](../types/String.md) |
| Domain Of | [Prevalence](../classes/Prevalence.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'float'})
- AnonymousSlotExpression({'range': 'integer'})
- AnonymousSlotExpression({'description': 'for ranges', 'range': 'string'})

</details>










## Examples

| Value |
| --- |
| 0.1 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:percentage |
| native | dismech:percentage |




## LinkML Source

<details>
```yaml
name: percentage
deprecated: 'Overloaded free-text/Any field that conflated measure type, rate, unit,
  and qualitative bands in incompatible notations. Superseded by the structured prevalence
  slots: measure_type, prevalence_class, and rate_per_100000 (with rate_low/rate_high
  for ranges). Retained read-only during migration; do not populate on new records.'
examples:
- value: '0.1'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: percentage
domain_of:
- Prevalence
range: Any
any_of:
- range: float
- range: integer
- description: for ranges
  range: string

```
</details>