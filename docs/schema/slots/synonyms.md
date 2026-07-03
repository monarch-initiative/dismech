

# Slot: synonyms 



URI: [dismech:slot/synonyms](https://w3id.org/monarch-initiative/dismech/slot/synonyms)
Alias: synonyms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](../classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Pathophysiology](../classes/Pathophysiology.md), [Biochemical](../classes/Biochemical.md), [Environmental](../classes/Environmental.md), [Disease](../classes/Disease.md), [Variant](../classes/Variant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| ['CYFRA 21-1'] |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:synonyms |
| native | dismech:synonyms |




## LinkML Source

<details>
```yaml
name: synonyms
examples:
- value: '[''CYFRA 21-1'']'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: synonyms
domain_of:
- Pathophysiology
- Biochemical
- Environmental
- Disease
- Variant
range: string
multivalued: true

```
</details>