

# Slot: method 


_Method or pipeline name_





URI: [dismech:method](https://w3id.org/monarch-initiative/dismech/method)
Alias: method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GOEnrichment](GOEnrichment.md) | GO enrichment results for an association signal |  no  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  yes  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:method |
| native | dismech:method |




## LinkML Source

<details>
```yaml
name: method
description: Method or pipeline name
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: method
domain_of:
- AssociationSignal
- GOEnrichment
range: string

```
</details>