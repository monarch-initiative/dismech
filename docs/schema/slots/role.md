

# Slot: role 



URI: [dismech:slot/role](https://w3id.org/monarch-initiative/dismech/slot/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [HostDescriptor](../classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| Primary |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:role |
| native | dismech:role |




## LinkML Source

<details>
```yaml
name: role
examples:
- value: Primary
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: role
domain_of:
- HostDescriptor
- Pathophysiology
- Stage
- Treatment
range: string

```
</details>