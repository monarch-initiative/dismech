

# Slot: subtypes 


_Names of subtypes (foreign keys to this disease's `has_subtypes[].name`) associated with a phenotype, biochemical finding, pathophysiology node, or other subtyped entry. Use this multivalued form when an item is characteristic of more than one subtype with overlapping features. For single-subtype associations, the scalar `subtype` slot may still be used._





URI: [dismech:slot/subtypes](https://w3id.org/monarch-initiative/dismech/slot/subtypes)
Alias: subtypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md), [Phenotype](../classes/Phenotype.md), [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| ['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4'] |
| ['Type 1', 'Type 2'] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:subtypes |
| native | dismech:subtypes |




## LinkML Source

<details>
```yaml
name: subtypes
description: Names of subtypes (foreign keys to this disease's `has_subtypes[].name`)
  associated with a phenotype, biochemical finding, pathophysiology node, or other
  subtyped entry. Use this multivalued form when an item is characteristic of more
  than one subtype with overlapping features. For single-subtype associations, the
  scalar `subtype` slot may still be used.
examples:
- value: '[''DENV-1'', ''DENV-2'', ''DENV-3'', ''DENV-4'']'
- value: '[''Type 1'', ''Type 2'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: subtypes
domain_of:
- Pathophysiology
- Phenotype
- Biochemical
range: string
multivalued: true

```
</details>