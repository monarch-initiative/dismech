

# Slot: name 



URI: [dismech:slot/name](https://w3id.org/monarch-initiative/dismech/slot/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](../classes/Assay.md) |  |  no  |
| [Disease](../classes/Disease.md) |  |  yes  |
| [ModelingConsideration](../classes/ModelingConsideration.md) |  |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [Diagnosis](../classes/Diagnosis.md) |  |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [CriteriaSet](../classes/CriteriaSet.md) | A named criteria grouping within a definition |  yes  |
| [Mechanism](../classes/Mechanism.md) |  |  no  |
| [Transmission](../classes/Transmission.md) |  |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [ModelVariable](../classes/ModelVariable.md) | A variable in a computational model, identified by a human-readable name, wit... |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [InfectiousAgent](../classes/InfectiousAgent.md) |  |  no  |
| [Definition](../classes/Definition.md) | A diagnostic or phenotype definition for the disease |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [Inheritance](../classes/Inheritance.md) |  |  no  |
| [Variant](../classes/Variant.md) |  |  no  |
| [EpidemiologyInfo](../classes/EpidemiologyInfo.md) |  |  no  |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  yes  |
| [SeverityTier](../classes/SeverityTier.md) | A threshold-severity pair defining one tier in a severity scale |  yes  |






## Properties

* Range: [String](../types/String.md)

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
- ModelVariable
- SeverityTier
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