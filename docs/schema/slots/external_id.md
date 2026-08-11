

# Slot: external_id 


_Identifier used by the external resource (e.g., CCID:009009, CA2573049045)_





URI: [dismech:slot/external_id](https://w3id.org/monarch-initiative/dismech/slot/external_id)
Alias: external_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExternalAssertion](../classes/ExternalAssertion.md) | An externally curated assertion or registry record relevant to a disease or v... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExternalAssertion](../classes/ExternalAssertion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:external_id |
| native | dismech:external_id |




## LinkML Source

<details>
```yaml
name: external_id
description: Identifier used by the external resource (e.g., CCID:009009, CA2573049045)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: external_id
domain_of:
- ExternalAssertion
range: string

```
</details>