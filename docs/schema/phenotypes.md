

# Slot: phenotypes 



URI: [dismech:phenotypes](https://w3id.org/monarch-initiative/dismech/phenotypes)
Alias: phenotypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [Disease](Disease.md) |  |  no  |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |






## Properties

* Range: [Phenotype](Phenotype.md)

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