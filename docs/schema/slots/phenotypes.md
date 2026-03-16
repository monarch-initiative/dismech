

# Slot: phenotypes 



URI: [dismech:slot/phenotypes](https://w3id.org/monarch-initiative/dismech/slot/phenotypes)
Alias: phenotypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [Disease](../classes/Disease.md) |  |  no  |
| [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |






## Properties

* Range: [Phenotype](../classes/Phenotype.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:phenotypes |
| native | dismech:phenotypes |




## LinkML Source

<details>
```yaml
name: phenotypes
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: phenotypes
domain_of:
- DifferentialDiagnosis
- Disease
- ComorbidityAssociation
range: Phenotype
multivalued: true
inlined: true
inlined_as_list: true

```
</details>