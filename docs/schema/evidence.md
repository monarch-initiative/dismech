

# Slot: evidence 



URI: [dismech:evidence](https://w3id.org/monarch-initiative/dismech/evidence)
Alias: evidence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LysosomalStorageAssignment](LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  no  |
| [ClassificationAssignment](ClassificationAssignment.md) | Base class for classification assignments with evidence |  no  |
| [Subtype](Subtype.md) |  |  no  |
| [MechanisticNosologyAssignment](MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  no  |
| [AnimalModel](AnimalModel.md) |  |  no  |
| [ComorbidityHypothesis](ComorbidityHypothesis.md) | Mechanistic hypothesis for a comorbidity association, with rich text and embe... |  no  |
| [PhenotypeContext](PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  yes  |
| [Phenotype](Phenotype.md) |  |  no  |
| [AgentLifeCycle](AgentLifeCycle.md) |  |  no  |
| [EpidemiologyInfo](EpidemiologyInfo.md) |  |  no  |
| [ChannelopathyAssignment](ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  no  |
| [ICDOMorphologyAssignment](ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [DifferentialDiagnosis](DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [AssociationSignal](AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [Diagnosis](Diagnosis.md) |  |  no  |
| [Stage](Stage.md) |  |  no  |
| [Variant](Variant.md) |  |  no  |
| [CriteriaSet](CriteriaSet.md) | A named criteria grouping within a definition |  no  |
| [IUISAssignment](IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  no  |
| [CausalEdge](CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  yes  |
| [Prevalence](Prevalence.md) |  |  no  |
| [ProgressionInfo](ProgressionInfo.md) |  |  no  |
| [AgentLifeCycleStage](AgentLifeCycleStage.md) |  |  no  |
| [Transmission](Transmission.md) |  |  no  |
| [TreatmentMechanismTarget](TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  yes  |
| [Environmental](Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [InfectiousAgent](InfectiousAgent.md) |  |  no  |
| [Definition](Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [Biochemical](Biochemical.md) |  |  no  |
| [ComputationalModel](ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [UpstreamConditionHypothesis](UpstreamConditionHypothesis.md) | Hypothesized upstream condition that may explain both A and B |  no  |
| [Pathophysiology](Pathophysiology.md) |  |  no  |
| [ModelingConsideration](ModelingConsideration.md) |  |  no  |
| [HistopathologyFinding](HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |
| [HarrisonsChapterAssignment](HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  no  |
| [Inheritance](Inheritance.md) |  |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [MechanisticHypothesis](MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  no  |
| [Treatment](Treatment.md) |  |  no  |
| [Finding](Finding.md) | A key finding or claim extracted from a source (publication or dataset) |  no  |
| [AssociationStatistics](AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |
| [Genetic](Genetic.md) |  |  no  |






## Properties

* Range: [EvidenceItem](EvidenceItem.md)

* Multivalued: True

* Recommended: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:evidence |
| native | dismech:evidence |




## LinkML Source

<details>
```yaml
name: evidence
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: evidence
domain_of:
- PhenotypeContext
- Dataset
- ClinicalTrial
- ComputationalModel
- DifferentialDiagnosis
- Subtype
- CausalEdge
- TreatmentMechanismTarget
- Finding
- Prevalence
- ProgressionInfo
- EpidemiologyInfo
- Pathophysiology
- Phenotype
- Biochemical
- HistopathologyFinding
- Genetic
- Environmental
- Stage
- AgentLifeCycle
- AgentLifeCycleStage
- AnimalModel
- Treatment
- InfectiousAgent
- Transmission
- Diagnosis
- Inheritance
- Variant
- ModelingConsideration
- ClassificationAssignment
- Definition
- CriteriaSet
- AssociationSignal
- AssociationStatistics
- ComorbidityHypothesis
- UpstreamConditionHypothesis
- MechanisticHypothesis
range: EvidenceItem
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>