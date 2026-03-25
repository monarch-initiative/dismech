

# Slot: assays 



URI: [dismech:slot/assays](https://w3id.org/monarch-initiative/dismech/slot/assays)
Alias: assays

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

* Range: [AssayDescriptor](../classes/AssayDescriptor.md)

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