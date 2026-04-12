

# Slot: factors 



URI: [dismech:slot/factors](https://w3id.org/monarch-initiative/dismech/slot/factors)
Alias: factors

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EpidemiologyInfo](../classes/EpidemiologyInfo.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Multivalued: True





## Examples

| Value |
| --- |
| ['Genetic', 'Environmental', 'Infectious', 'Autoimmune', 'Metabolic', 'Neoplastic', 'Traumatic', 'Iatrogenic', 'Idiopathic'] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:factors |
| native | dismech:factors |




## LinkML Source

<details>
```yaml
name: factors
examples:
- value: '[''Genetic'', ''Environmental'', ''Infectious'', ''Autoimmune'', ''Metabolic'',
    ''Neoplastic'', ''Traumatic'', ''Iatrogenic'', ''Idiopathic'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: factors
domain_of:
- EpidemiologyInfo
range: string
multivalued: true

```
</details>