

# Slot: sequelae 



URI: [dismech:slot/sequelae](https://w3id.org/monarch-initiative/dismech/slot/sequelae)
Alias: sequelae

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |






## Properties

* Range: [CausalEdge](../classes/CausalEdge.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{target: Diabetic Ketoacidosis}, {target: Chronic Complications}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:sequelae |
| native | dismech:sequelae |




## LinkML Source

<details>
```yaml
name: sequelae
examples:
- value: '[{target: Diabetic Ketoacidosis}, {target: Chronic Complications}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: sequelae
domain_of:
- Phenotype
range: CausalEdge
multivalued: true
inlined: true
inlined_as_list: true

```
</details>