

# Slot: evidence 



URI: [dismech:slot/evidence](https://w3id.org/monarch-initiative/dismech/slot/evidence)
Alias: evidence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ModelingConsideration](../classes/ModelingConsideration.md) |  |  no  |
| [TreatmentMechanismTarget](../classes/TreatmentMechanismTarget.md) | Links a treatment to a specific pathophysiology mechanism node it targets |  yes  |
| [Stage](../classes/Stage.md) |  |  no  |
| [Prevalence](../classes/Prevalence.md) |  |  no  |
| [Subtype](../classes/Subtype.md) |  |  no  |
| [AgentLifeCycle](../classes/AgentLifeCycle.md) |  |  no  |
| [ClinicalTrial](../classes/ClinicalTrial.md) | A clinical trial relevant to treatment or research of a disease |  yes  |
| [Treatment](../classes/Treatment.md) |  |  no  |
| [Diagnosis](../classes/Diagnosis.md) |  |  no  |
| [MechanisticHypothesis](../classes/MechanisticHypothesis.md) | Disease-level hypothesis metadata used to organize downstream causal edges in... |  no  |
| [AgentLifeCycleStage](../classes/AgentLifeCycleStage.md) |  |  no  |
| [AssociationSignal](../classes/AssociationSignal.md) | An association signal from EHR, registry, or computational sources, optionall... |  no  |
| [ClassificationAssignment](../classes/ClassificationAssignment.md) | Base class for classification assignments with evidence |  no  |
| [CriteriaSet](../classes/CriteriaSet.md) | A named criteria grouping within a definition |  no  |
| [ComorbidityHypothesis](../classes/ComorbidityHypothesis.md) | Mechanistic hypothesis for a comorbidity association, with rich text and embe... |  no  |
| [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  no  |
| [Transmission](../classes/Transmission.md) |  |  no  |
| [UpstreamConditionHypothesis](../classes/UpstreamConditionHypothesis.md) | Hypothesized upstream condition that may explain both A and B |  no  |
| [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  no  |
| [Phenotype](../classes/Phenotype.md) |  |  no  |
| [ProgressionInfo](../classes/ProgressionInfo.md) |  |  no  |
| [Environmental](../classes/Environmental.md) | An environmental factor, exposure, or context relevant to disease |  no  |
| [DifferentialDiagnosis](../classes/DifferentialDiagnosis.md) | A disease or condition that presents similarly to the focal disease and must ... |  no  |
| [Finding](../classes/Finding.md) | A key finding or claim extracted from a source (publication or dataset) |  no  |
| [AssociationStatistics](../classes/AssociationStatistics.md) | Statistical summary with evidence for an association signal |  no  |
| [InfectiousAgent](../classes/InfectiousAgent.md) |  |  no  |
| [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  no  |
| [Definition](../classes/Definition.md) | A diagnostic or phenotype definition for the disease |  no  |
| [PhenotypeContext](../classes/PhenotypeContext.md) | A context-specific annotation qualifying how a phenotype manifests under part... |  yes  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |
| [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  no  |
| [Dataset](../classes/Dataset.md) | A reference to a publicly available omics or phenotype dataset |  no  |
| [Genetic](../classes/Genetic.md) |  |  no  |
| [Pathophysiology](../classes/Pathophysiology.md) |  |  no  |
| [IUISAssignment](../classes/IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  no  |
| [Inheritance](../classes/Inheritance.md) |  |  no  |
| [Variant](../classes/Variant.md) |  |  no  |
| [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  no  |
| [AnimalModel](../classes/AnimalModel.md) |  |  no  |
| [EpidemiologyInfo](../classes/EpidemiologyInfo.md) |  |  no  |
| [CausalEdge](../classes/CausalEdge.md) | A reference to a downstream effect or consequence in a causal relationship |  yes  |
| [ComputationalModel](../classes/ComputationalModel.md) | A computational or in-silico model relevant to understanding disease mechanis... |  no  |
| [HistopathologyFinding](../classes/HistopathologyFinding.md) | A histopathologic finding from microscopic examination of tissue |  no  |






## Properties

* Range: [EvidenceItem](../classes/EvidenceItem.md)

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