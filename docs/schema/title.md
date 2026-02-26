

# Slot: title 


_Title of the publication_





URI: [dismech:title](https://w3id.org/monarch-initiative/dismech/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [PublicationReference](PublicationReference.md) | A reference to a publication with associated findings |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:title |
| native | dismech:title |




## LinkML Source

<details>
```yaml
name: title
implements:
- linkml:title
description: Title of the publication
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: title
domain_of:
- Dataset
- PublicationReference
range: string

```
</details>