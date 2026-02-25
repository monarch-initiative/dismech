

# Slot: target_phenotypes 


_Phenotypes that this treatment or trial addresses or targets_





URI: [dismech:target_phenotypes](https://w3id.org/monarch-initiative/dismech/target_phenotypes)
Alias: target_phenotypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [Treatment](Treatment.md) |  |  no  |






## Properties

* Range: [PhenotypeDescriptor](PhenotypeDescriptor.md)

* Multivalued: True




## Comments

* Should reference phenotype names defined in the same disease's phenotypes list
* Enables linking treatments/trials to the symptoms/manifestations they aim to manage
* Each phenotype can include ontology term references (HP)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:target_phenotypes |
| native | dismech:target_phenotypes |




## LinkML Source

<details>
```yaml
name: target_phenotypes
description: Phenotypes that this treatment or trial addresses or targets
comments:
- Should reference phenotype names defined in the same disease's phenotypes list
- Enables linking treatments/trials to the symptoms/manifestations they aim to manage
- Each phenotype can include ontology term references (HP)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: target_phenotypes
domain_of:
- ClinicalTrial
- Treatment
range: PhenotypeDescriptor
multivalued: true
inlined: true
inlined_as_list: true

```
</details>