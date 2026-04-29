

# Slot: metrics 


_Quantitative association metrics_





URI: [dismech:slot/metrics](https://w3id.org/monarch-initiative/dismech/slot/metrics)
Alias: metrics

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [AssociationStatistics](../classes/AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |






## Properties

* Range: [AssociationMetric](../classes/AssociationMetric.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:metrics |
| native | dismech:metrics |




## LinkML Source

<details>
```yaml
name: metrics
description: Quantitative association metrics
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: metrics
domain_of:
- AssociationSignal
- AssociationStatistics
range: AssociationMetric
multivalued: true
inlined: true
inlined_as_list: true

```
</details>