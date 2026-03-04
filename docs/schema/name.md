

# Slot: name 



URI: [dismech:name](https://w3id.org/monarch-initiative/dismech/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) |  |  no  |
| [Subtype](Subtype.md) |  |  no  |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [Disease](Disease.md) |  |  yes  |
| [Mechanism](Mechanism.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [Diagnosis](Diagnosis.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [Variant](Variant.md) |  |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  yes  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [Transmission](Transmission.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [InfectiousAgent](InfectiousAgent.md) |  |  no  |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  yes  |
| [Biochemical](Biochemical.md) |  |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [ModelingConsideration](ModelingConsideration.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [Inheritance](Inheritance.md) |  |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [Genetic](Genetic.md) |  |  no  |






## Properties

* Range: [String](String.md)

* Required: True





## Examples

| Value |
| --- |
| Adolescent Nephronophthisis |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:name |
| native | dismech:name |




## LinkML Source

<details>
```yaml
name: name
examples:
- value: Adolescent Nephronophthisis
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
identifier: true
alias: name
domain_of:
- ClinicalTrial
- ComputationalModel
- DifferentialDiagnosis
- Subtype
- EpidemiologyInfo
- Pathophysiology
- Phenotype
- Biochemical
- HistopathologyFinding
- Genetic
- Environmental
- Disease
- Stage
- AgentLifeCycleStage
- Treatment
- InfectiousAgent
- Transmission
- Assay
- Diagnosis
- Inheritance
- Variant
- Mechanism
- ModelingConsideration
- Definition
- CriteriaSet
- ComorbidityAssociation
range: string
required: true

```
</details>