

# Slot: role 



URI: [dismech:slot/role](https://w3id.org/monarch-initiative/dismech/slot/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [HostDescriptor](../classes/HostDescriptor.md) | A descriptor for hosts in an infectious agent life cycle |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [HostDescriptor](../classes/HostDescriptor.md), [Pathophysiology](../classes/Pathophysiology.md), [Stage](../classes/Stage.md), [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









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