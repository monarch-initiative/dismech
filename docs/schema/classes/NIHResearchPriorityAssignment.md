

# Class: NIHResearchPriorityAssignment 


_NIH Highlighted Topics funding-priority assignment. A secondary, grant-strategy tag (not a disease nosology) recording which NIH highlighted funding topic the disease is relevant to. Use ``notes`` to explain the relevance and ``evidence`` where a specific claim backs it._





URI: [dismech:class/NIHResearchPriorityAssignment](https://w3id.org/monarch-initiative/dismech/class/NIHResearchPriorityAssignment)





```mermaid
 classDiagram
    class NIHResearchPriorityAssignment
    click NIHResearchPriorityAssignment href "../../classes/NIHResearchPriorityAssignment/"
      ClassificationAssignment <|-- NIHResearchPriorityAssignment
        click ClassificationAssignment href "../../classes/ClassificationAssignment/"
      
      NIHResearchPriorityAssignment : classification_value
        
          
    
        
        
        NIHResearchPriorityAssignment --> "1" NIHResearchPriorityEnum : classification_value
        click NIHResearchPriorityEnum href "../../enums/NIHResearchPriorityEnum/"
    

        
      NIHResearchPriorityAssignment : evidence
        
          
    
        
        
        NIHResearchPriorityAssignment --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      NIHResearchPriorityAssignment : notes
        
      
```





## Inheritance
* [ClassificationAssignment](../classes/ClassificationAssignment.md)
    * **NIHResearchPriorityAssignment**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [classification_value](../slots/classification_value.md) | 1 <br/> [NIHResearchPriorityEnum](../enums/NIHResearchPriorityEnum.md) | The classification value assigned | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | [ClassificationAssignment](../classes/ClassificationAssignment.md) |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | [ClassificationAssignment](../classes/ClassificationAssignment.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseClassifications](../classes/DiseaseClassifications.md) | [nih_research_priority](../slots/nih_research_priority.md) | range | [NIHResearchPriorityAssignment](../classes/NIHResearchPriorityAssignment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:NIHResearchPriorityAssignment |
| native | dismech:NIHResearchPriorityAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NIHResearchPriorityAssignment
description: NIH Highlighted Topics funding-priority assignment. A secondary, grant-strategy
  tag (not a disease nosology) recording which NIH highlighted funding topic the disease
  is relevant to. Use ``notes`` to explain the relevance and ``evidence`` where a
  specific claim backs it.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slots:
- classification_value
slot_usage:
  classification_value:
    name: classification_value
    range: NIHResearchPriorityEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: NIHResearchPriorityAssignment
description: NIH Highlighted Topics funding-priority assignment. A secondary, grant-strategy
  tag (not a disease nosology) recording which NIH highlighted funding topic the disease
  is relevant to. Use ``notes`` to explain the relevance and ``evidence`` where a
  specific claim backs it.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slot_usage:
  classification_value:
    name: classification_value
    range: NIHResearchPriorityEnum
    required: true
attributes:
  classification_value:
    name: classification_value
    description: The classification value assigned
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: classification_value
    owner: NIHResearchPriorityAssignment
    domain_of:
    - ICDOMorphologyAssignment
    - HarrisonsChapterAssignment
    - LysosomalStorageAssignment
    - MechanisticNosologyAssignment
    - IUISAssignment
    - ChannelopathyAssignment
    - ICIMDAssignment
    - ISDSNosologyAssignment
    - NIHResearchPriorityAssignment
    range: NIHResearchPriorityEnum
    required: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: NIHResearchPriorityAssignment
    domain_of:
    - PhenotypeContext
    - Dataset
    - ExperimentalModel
    - Experiment
    - ExperimentalPerturbation
    - ExperimentalReadout
    - ExperimentalControl
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
    - ModelMechanismLink
    - BiomarkerReadout
    - PhenotypeReadout
    - ReferenceRange
    - SurrogateEndpoint
    - ExternalAssertion
    - Finding
    - Prevalence
    - GeneCaseFraction
    - ProgressionInfo
    - ClinicalBurden
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - ImagingFinding
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
    - AlgorithmValidationStatus
    - CriteriaSet
    - AssociationSignal
    - AssociationStatistics
    - ComorbidityHypothesis
    - UpstreamConditionHypothesis
    - MechanisticHypothesis
    - Discussion
    - GroupingCriteria
    - GroupingMember
    - DifferentiatingMechanism
    range: EvidenceItem
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    examples:
    - value: Contagious stage where symptoms appear and the bacteria can be spread
        to others.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: notes
    owner: NIHResearchPriorityAssignment
    domain_of:
    - GeneticContext
    - OnsetDescriptor
    - PhenotypeContext
    - Dataset
    - ExperimentalModel
    - Experiment
    - ExperimentalPerturbation
    - ExperimentalReadout
    - ExperimentalControl
    - ClinicalTrial
    - ComputationalModel
    - ModelVariable
    - DifferentialDiagnosis
    - ReferenceRange
    - SurrogateEndpoint
    - SurrogateEndpointCollection
    - ExternalAssertion
    - TrackedIssue
    - Prevalence
    - GeneCaseFraction
    - ProgressionInfo
    - ClinicalBurden
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - ImagingFinding
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
    - Discussion
    - Grouping
    - GroupingCriteria
    - GroupingMember
    - DifferentiatingMechanism
    range: string

```
</details>