

# Slot: assays 



URI: [dismech:assays](https://w3id.org/monarch-initiative/dismech/assays)
Alias: assays

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Biochemical](Biochemical.md) |  |  no  |






## Properties

* Range: [AssayDescriptor](AssayDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: Elevated Blood Glucose}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:assays |
| native | dismech:assays |




## LinkML Source

<details>
```yaml
name: assays
examples:
- value: '[{preferred_term: Elevated Blood Glucose}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: assays
domain_of:
- Pathophysiology
- Biochemical
range: AssayDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>