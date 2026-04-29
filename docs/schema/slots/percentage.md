

# Slot: percentage 



URI: [dismech:slot/percentage](https://w3id.org/monarch-initiative/dismech/slot/percentage)
Alias: percentage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

* Range: [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[Float](../types/Float.md)&nbsp;or&nbsp;<br />[Integer](../types/Integer.md)&nbsp;or&nbsp;<br />[String](../types/String.md)





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