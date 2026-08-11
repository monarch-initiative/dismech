

# Slot: external_assertions 


_External curated assertions or registry records relevant to this entity_





URI: [dismech:slot/external_assertions](https://w3id.org/monarch-initiative/dismech/slot/external_assertions)
Alias: external_assertions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Variant](../classes/Variant.md) | A genetic variant associated with a disease, including coding and non-coding ... |  no  |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ExternalAssertion](../classes/ExternalAssertion.md) |
| Domain Of | [Disease](../classes/Disease.md), [Variant](../classes/Variant.md) |

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
| self | dismech:external_assertions |
| native | dismech:external_assertions |




## LinkML Source

<details>
```yaml
name: external_assertions
description: External curated assertions or registry records relevant to this entity
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: external_assertions
domain_of:
- Disease
- Variant
range: ExternalAssertion
multivalued: true
inlined: true
inlined_as_list: true

```
</details>