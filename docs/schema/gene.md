

# Slot: gene 



URI: [dismech:gene](https://w3id.org/monarch-initiative/dismech/gene)
Alias: gene

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [GeneticContext](GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [Variant](Variant.md) |  |  no  |






## Properties

* Range: [GeneDescriptor](GeneDescriptor.md)





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