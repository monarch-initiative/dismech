

# Slot: notes 



URI: [dismech:notes](https://w3id.org/monarch-initiative/dismech/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LysosomalStorageAssignment](LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  no  |
| [ClassificationAssignment](ClassificationAssignment.md) | Base class for classification assignments with evidence |  no  |
| [MechanisticNosologyAssignment](MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  no  |
| [GeneticContext](GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [Disease](Disease.md) |  |  no  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [OnsetDescriptor](OnsetDescriptor.md) | Structured description of age of onset |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |  no  |
| [ChannelopathyAssignment](ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  no  |
| [ICDOMorphologyAssignment](ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  yes  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [Diagnosis](Diagnosis.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  no  |
| [IUISAssignment](IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  no  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [Prevalence](Prevalence.md) |  |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [Transmission](Transmission.md) |  |  no  |
| [MappingConsistency](MappingConsistency.md) | Consistency assertion for a mapping relative to another source |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [AssociationMetric](AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [HarrisonsChapterAssignment](HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [MechanisticHypothesis](MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [AssociationStatistics](AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |
| [Genetic](Genetic.md) |  |  no  |






## Properties

* Range: [String](String.md)





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