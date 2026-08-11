

# Slot: epidemiology 



URI: [dismech:slot/epidemiology](https://w3id.org/monarch-initiative/dismech/slot/epidemiology)
Alias: epidemiology

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EpidemiologyInfo](../classes/EpidemiologyInfo.md) |
| Domain Of | [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| ['Global'] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:epidemiology |
| native | dismech:epidemiology |




## LinkML Source

<details>
```yaml
name: epidemiology
examples:
- value: '[''Global'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: epidemiology
domain_of:
- Disease
range: EpidemiologyInfo
multivalued: true
inlined: true
inlined_as_list: true

```
</details>