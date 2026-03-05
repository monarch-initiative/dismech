

# Slot: percentage 



URI: [dismech:percentage](https://w3id.org/monarch-initiative/dismech/percentage)
Alias: percentage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](Prevalence.md) |  |  no  |






## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Float](Float.md)&nbsp;or&nbsp;<br />[Integer](Integer.md)&nbsp;or&nbsp;<br />[String](String.md)





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