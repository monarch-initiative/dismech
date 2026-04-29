

# Slot: downstream 



URI: [dismech:slot/downstream](https://w3id.org/monarch-initiative/dismech/slot/downstream)
Alias: downstream

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |






## Properties

* Range: [CausalEdge](../classes/CausalEdge.md)

* Multivalued: True





## Examples

| Value |
| --- |
| [{target: Tissue Damage, causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES, hypothesis_groups: [canonical_model]}] |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:downstream |
| native | dismech:downstream |




## LinkML Source

<details>
```yaml
name: downstream
examples:
- value: '[{target: Tissue Damage, causal_link_type: INDIRECT_UNKNOWN_INTERMEDIATES,
    hypothesis_groups: [canonical_model]}]'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: downstream
domain_of:
- Pathophysiology
range: CausalEdge
multivalued: true
inlined: true
inlined_as_list: true

```
</details>