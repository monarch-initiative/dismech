

# Slot: accession 


_Dataset accession identifier as a CURIE (e.g., geo:GSE67472)_





URI: [dismech:accession](https://w3id.org/monarch-initiative/dismech/accession)
Alias: accession

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:accession |
| native | dismech:accession |




## LinkML Source

<details>
```yaml
name: accession
implements:
- linkml:authoritative_reference
description: Dataset accession identifier as a CURIE (e.g., geo:GSE67472)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
identifier: true
alias: accession
domain_of:
- Dataset
range: uriorcurie
required: true

```
</details>