

# Slot: notes 



URI: [dismech:slot/notes](https://w3id.org/monarch-initiative/dismech/slot/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |
| [ICD10CMMapping](../classes/ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [Stage](../classes/Stage.md) |  |  no  |
| [AssociationMetric](../classes/AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |
| [Prevalence](../classes/Prevalence.md) |  |  no  |
| [ICD11FMapping](../classes/ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [Diagnosis](../classes/Diagnosis.md) |  |  no  |
| [MechanisticHypothesis](../classes/MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [ClassificationAssignment](../classes/ClassificationAssignment.md) | Base class for classification assignments with evidence |  no  |
| [CriteriaSet](../classes/CriteriaSet.md) | A named criteria grouping within a definition |  no  |
| [MappingConsistency](../classes/MappingConsistency.md) | Consistency assertion for a mapping relative to another source |  no  |
| [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  no  |
| [Transmission](../classes/Transmission.md) |  |  no  |
| [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [ModelVariable](../classes/ModelVariable.md) | A variable in a computational model, identified by a human-readable name, wit... |  no  |
| [MondoMapping](../classes/MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  yes  |
| [AssociationStatistics](../classes/AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |
| [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  no  |
| [Definition](../classes/Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [OnsetDescriptor](../classes/OnsetDescriptor.md) | Structured description of age of onset |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [GeneticContext](../classes/GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  no  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [IUISAssignment](../classes/IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  no  |
| [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  no  |
| [EpidemiologyInfo](../classes/EpidemiologyInfo.md) |  |  no  |
| [TermMapping](../classes/TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |






## Properties

* Range: [String](../types/String.md)





## Examples

| Value |
| --- |
| Contagious stage where symptoms appear and the bacteria can be spread to others. |

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:notes |
| native | dismech:notes |




## LinkML Source

<details>
```yaml
name: notes
examples:
- value: Contagious stage where symptoms appear and the bacteria can be spread to
    others.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: notes
domain_of:
- GeneticContext
- OnsetDescriptor
- PhenotypeContext
- Dataset
- ClinicalTrial
- ComputationalModel
- ModelVariable
- DifferentialDiagnosis
- Prevalence
- ProgressionInfo
- EpidemiologyInfo
- Pathophysiology
- Phenotype
- Biochemical
- HistopathologyFinding
- Genetic
- Environmental
- Disease
- Stage
- AgentLifeCycle
- AgentLifeCycleStage
- Treatment
- Transmission
- Diagnosis
- ClassificationAssignment
- Definition
- CriteriaSet
- TermMapping
- MappingConsistency
- ComorbidityAssociation
- AssociationSignal
- AssociationMetric
- AssociationStatistics
- MechanisticHypothesis
range: string

```
</details>