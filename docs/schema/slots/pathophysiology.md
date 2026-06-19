

# Slot: pathophysiology 



URI: [dismech:slot/pathophysiology](https://w3id.org/monarch-initiative/dismech/slot/pathophysiology)
Alias: pathophysiology

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComorbidityHypothesis](../classes/ComorbidityHypothesis.md) | Mechanistic hypothesis for a comorbidity association, with rich text and embe... |  no  |
| [Disease](../classes/Disease.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Pathophysiology](../classes/Pathophysiology.md) |
| Domain Of | [Disease](../classes/Disease.md), [Stage](../classes/Stage.md), [ComorbidityHypothesis](../classes/ComorbidityHypothesis.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:pathophysiology |
| native | dismech:pathophysiology |




## LinkML Source

<details>
```yaml
name: pathophysiology
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: pathophysiology
domain_of:
- Disease
- Stage
- ComorbidityHypothesis
range: Pathophysiology
multivalued: true
inlined: true
inlined_as_list: true

```
</details>