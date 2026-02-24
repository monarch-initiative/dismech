

# Slot: associated_phenotypes 



URI: [dismech:associated_phenotypes](https://w3id.org/monarch-initiative/dismech/associated_phenotypes)
Alias: associated_phenotypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnimalModel](AnimalModel.md) |  |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True





## Examples

| Value |
| --- |
| ['Celiac Disease', 'Type 1 Diabetes', 'Autoimmune Thyroid Disease'] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:associated_phenotypes |
| native | dismech:associated_phenotypes |




## LinkML Source

<details>
```yaml
name: associated_phenotypes
examples:
- value: '[''Celiac Disease'', ''Type 1 Diabetes'', ''Autoimmune Thyroid Disease'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: associated_phenotypes
domain_of:
- AnimalModel
range: string
multivalued: true

```
</details>