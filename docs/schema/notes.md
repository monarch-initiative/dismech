

# Slot: notes 



URI: [dismech:notes](https://w3id.org/monarch-initiative/dismech/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Biochemical](Biochemical.md) |  |  no  |
| [MechanisticNosologyAssignment](MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  no  |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [ICD10CMMapping](ICD10CMMapping.md) | ICD-10-CM diagnosis code mapping |  no  |
| [LysosomalStorageAssignment](LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  no  |
| [ClassificationAssignment](ClassificationAssignment.md) | Base class for classification assignments with evidence |  no  |
| [ComorbidityAssociation](ComorbidityAssociation.md) | An association between two conditions, including directionality, evidence, an... |  no  |
| [MondoMapping](MondoMapping.md) | MONDO disease ontology mapping |  no  |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [TermMapping](TermMapping.md) | Mapping from this disease entry to an external term or code |  no  |
| [Genetic](Genetic.md) |  |  no  |
| [AssociationStatistics](AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |
| [OnsetDescriptor](OnsetDescriptor.md) | Structured description of age of onset |  no  |
| [AssociationMetric](AssociationMetric.md) | Quantitative association metric and its uncertainty |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  no  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [Diagnosis](Diagnosis.md) |  |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  no  |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  no  |
| [Disease](Disease.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [GeneticContext](GeneticContext.md) | A structured description of a genetic context that modifies phenotype frequen... |  no  |
| [Stage](Stage.md) |  |  no  |
| [MappingConsistency](MappingConsistency.md) | Consistency assertion for a mapping relative to another source |  no  |
| [HarrisonsChapterAssignment](HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |
| [Prevalence](Prevalence.md) |  |  no  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  yes  |
| [ICDOMorphologyAssignment](ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [ICD11FMapping](ICD11FMapping.md) | ICD-11 Foundation diagnosis code mapping |  no  |
| [ChannelopathyAssignment](ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [Transmission](Transmission.md) |  |  no  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [IUISAssignment](IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [MechanisticHypothesis](MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  no  |






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