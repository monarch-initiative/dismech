

# Slot: findings 


_Key findings or claims extracted from this source (publication or dataset)_





URI: [dismech:findings](https://w3id.org/monarch-initiative/dismech/findings)
Alias: findings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PublicationReference](PublicationReference.md) | A reference to a publication with associated findings |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |






## Properties

* Range: [Finding](Finding.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:findings |
| native | dismech:findings |




## LinkML Source

<details>
```yaml
name: findings
description: Key findings or claims extracted from this source (publication or dataset)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: findings
domain_of:
- Dataset
- ComputationalModel
- PublicationReference
range: Finding
multivalued: true
inlined: true
inlined_as_list: true

```
</details>