# Enum: CausalLinkTypeEnum 




_Degree of mechanistic directness represented by a causal edge_



URI: [dismech:CausalLinkTypeEnum](https://w3id.org/monarch-initiative/dismech/CausalLinkTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| DIRECT | None | Direct causal influence at the current graph granularity |
| INDIRECT_KNOWN_INTERMEDIATES | None | Indirect relationship where one or more intermediates are known but omitted f... |
| INDIRECT_UNKNOWN_INTERMEDIATES | None | Indirect relationship where at least one required intermediate mechanism is c... |
| UNKNOWN | None | Directness has not yet been determined |




## Slots

| Name | Description |
| ---  | --- |
| [causal_link_type](causal_link_type.md) | Whether this edge is direct or indirect, and whether omitted intermediates ar... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: CausalLinkTypeEnum
description: Degree of mechanistic directness represented by a causal edge
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  DIRECT:
    text: DIRECT
    description: Direct causal influence at the current graph granularity
  INDIRECT_KNOWN_INTERMEDIATES:
    text: INDIRECT_KNOWN_INTERMEDIATES
    description: Indirect relationship where one or more intermediates are known but
      omitted from the graph
  INDIRECT_UNKNOWN_INTERMEDIATES:
    text: INDIRECT_UNKNOWN_INTERMEDIATES
    description: Indirect relationship where at least one required intermediate mechanism
      is currently unknown
  UNKNOWN:
    text: UNKNOWN
    description: Directness has not yet been determined

```
</details>