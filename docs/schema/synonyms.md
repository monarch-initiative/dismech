

# Slot: synonyms 



URI: [dismech:synonyms](https://w3id.org/monarch-initiative/dismech/synonyms)
Alias: synonyms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [Disease](Disease.md) |  |  no  |
| [Variant](Variant.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True





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