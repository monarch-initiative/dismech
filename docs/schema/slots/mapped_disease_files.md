

# Slot: mapped_disease_files 


_Relative paths of dismech disease YAML files mapped or candidate-mapped to this FDA row_





URI: [dismech:slot/mapped_disease_files](https://w3id.org/monarch-initiative/dismech/slot/mapped_disease_files)
Alias: mapped_disease_files

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SurrogateEndpoint](../classes/SurrogateEndpoint.md) | A regulatory surrogate endpoint assertion curated from FDA's surrogate endpoi... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [SurrogateEndpoint](../classes/SurrogateEndpoint.md) |

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
| self | dismech:mapped_disease_files |
| native | dismech:mapped_disease_files |




## LinkML Source

<details>
```yaml
name: mapped_disease_files
description: Relative paths of dismech disease YAML files mapped or candidate-mapped
  to this FDA row
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: mapped_disease_files
domain_of:
- SurrogateEndpoint
range: string
multivalued: true

```
</details>