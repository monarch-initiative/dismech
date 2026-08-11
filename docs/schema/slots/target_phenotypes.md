

# Slot: target_phenotypes 


_Phenotypes that this treatment or trial addresses or targets_





URI: [dismech:slot/target_phenotypes](https://w3id.org/monarch-initiative/dismech/slot/target_phenotypes)
Alias: target_phenotypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) |
| Domain Of | [ClinicalTrial](../classes/ClinicalTrial.md), [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Should reference phenotype names defined in the same disease's phenotypes list
* Enables linking treatments/trials to the symptoms/manifestations they aim to manage
* Each phenotype can include ontology term references (HP)
* Use only for THERAPEUTIC actions; non-therapeutic actions need a future dedicated observation/screening link instead of treatment-style target links



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
- Use only for THERAPEUTIC actions; non-therapeutic actions need a future dedicated
  observation/screening link instead of treatment-style target links
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