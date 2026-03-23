

# Slot: dataset_identifier 


_Native identifier for this variable in the source dataset or model (e.g., SBML species ID, database column name, COBRA reaction ID). When the parent context already specifies the dataset (e.g., a ComputationalModel with model_id), this field gives the local name within that dataset._





URI: [dismech:slot/dataset_identifier](https://w3id.org/monarch-initiative/dismech/slot/dataset_identifier)
Alias: dataset_identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelVariable](../classes/ModelVariable.md) | A variable in a computational model, identified by a human-readable name, wit... |  no  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| ECCPhos |
| Qbone |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:dataset_identifier |
| native | dismech:dataset_identifier |




## LinkML Source

<details>
```yaml
name: dataset_identifier
description: Native identifier for this variable in the source dataset or model (e.g.,
  SBML species ID, database column name, COBRA reaction ID). When the parent context
  already specifies the dataset (e.g., a ComputationalModel with model_id), this field
  gives the local name within that dataset.
examples:
- value: ECCPhos
- value: Qbone
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: dataset_identifier
domain_of:
- ModelVariable
range: string

```
</details>