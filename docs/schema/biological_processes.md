

# Slot: biological_processes 



URI: [dismech:biological_processes](https://w3id.org/monarch-initiative/dismech/biological_processes)
Alias: biological_processes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |






## Properties

* Range: [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{preferred_term: TNF-alpha Production}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:biological_processes |
| native | dismech:biological_processes |




## LinkML Source

<details>
```yaml
name: biological_processes
examples:
- value: '[{preferred_term: TNF-alpha Production}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: biological_processes
domain_of:
- Pathophysiology
range: BiologicalProcessDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>