

# Slot: causal_link_type 


_Whether this edge is direct or indirect, and whether omitted intermediates are known_





URI: [dismech:causal_link_type](https://w3id.org/monarch-initiative/dismech/causal_link_type)
Alias: causal_link_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalEdge](CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  yes  |






## Properties

* Range: [CausalLinkTypeEnum](CausalLinkTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:causal_link_type |
| native | dismech:causal_link_type |




## LinkML Source

<details>
```yaml
name: causal_link_type
description: Whether this edge is direct or indirect, and whether omitted intermediates
  are known
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: causal_link_type
domain_of:
- CausalEdge
range: CausalLinkTypeEnum

```
</details>