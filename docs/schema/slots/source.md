

# Slot: source 


_Source dataset or provenance label_





URI: [dismech:slot/source](https://w3id.org/monarch-initiative/dismech/slot/source)
Alias: source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  yes  |
| [ExternalAssertion](../classes/ExternalAssertion.md) | An externally curated assertion or registry record relevant to a disease or v... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ExternalAssertion](../classes/ExternalAssertion.md), [AssociationSignal](../classes/AssociationSignal.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:source |
| native | dismech:source |




## LinkML Source

<details>
```yaml
name: source
description: Source dataset or provenance label
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: source
domain_of:
- ExternalAssertion
- AssociationSignal
range: string

```
</details>