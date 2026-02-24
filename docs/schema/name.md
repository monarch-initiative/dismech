

# Slot: name 



URI: [dismech:name](https://w3id.org/monarch-initiative/dismech/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Biochemical](Biochemical.md) |  |  no  |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [InfectiousAgent](InfectiousAgent.md) |  |  no  |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  yes  |
| [Genetic](Genetic.md) |  |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  yes  |
| [ModelingConsideration](ModelingConsideration.md) |  |  no  |
| [Diagnosis](Diagnosis.md) |  |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [Disease](Disease.md) |  |  yes  |
| [Phenotype](Phenotype.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [Assay](Assay.md) |  |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [Inheritance](Inheritance.md) |  |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [Variant](Variant.md) |  |  no  |
| [Mechanism](Mechanism.md) |  |  no  |
| [Transmission](Transmission.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Subtype](Subtype.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |






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