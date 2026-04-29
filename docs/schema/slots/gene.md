

# Slot: gene 



URI: [dismech:slot/gene](https://w3id.org/monarch-initiative/dismech/slot/gene)
Alias: gene

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Variant](../classes/Variant.md) |  |  no  |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |






## Properties

* Range: [GeneDescriptor](../classes/GeneDescriptor.md)





## Examples

| Value |
| --- |
| {preferred_term: MEFV} |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:gene |
| native | dismech:gene |




## LinkML Source

<details>
```yaml
name: gene
examples:
- value: '{preferred_term: MEFV}'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: gene
domain_of:
- GeneticContext
- Pathophysiology
- Variant
range: GeneDescriptor
inlined: true

```
</details>