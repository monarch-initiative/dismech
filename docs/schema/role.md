

# Slot: role 



URI: [dismech:role](https://w3id.org/monarch-initiative/dismech/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [HostDescriptor](HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [Stage](Stage.md) |  |  no  |






## Properties

* Range: [String](String.md)





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