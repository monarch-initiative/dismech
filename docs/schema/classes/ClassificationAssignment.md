

# Class: ClassificationAssignment 


_Base class for classification assignments with evidence_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [dismech:class/ClassificationAssignment](https://w3id.org/monarch-initiative/dismech/class/ClassificationAssignment)





```mermaid
 classDiagram
    class ClassificationAssignment
    click ClassificationAssignment href "../../classes/ClassificationAssignment/"
      ClassificationAssignment <|-- ICDOMorphologyAssignment
        click ICDOMorphologyAssignment href "../../classes/ICDOMorphologyAssignment/"
      ClassificationAssignment <|-- HarrisonsChapterAssignment
        click HarrisonsChapterAssignment href "../../classes/HarrisonsChapterAssignment/"
      ClassificationAssignment <|-- LysosomalStorageAssignment
        click LysosomalStorageAssignment href "../../classes/LysosomalStorageAssignment/"
      ClassificationAssignment <|-- MechanisticNosologyAssignment
        click MechanisticNosologyAssignment href "../../classes/MechanisticNosologyAssignment/"
      ClassificationAssignment <|-- IUISAssignment
        click IUISAssignment href "../../classes/IUISAssignment/"
      ClassificationAssignment <|-- ChannelopathyAssignment
        click ChannelopathyAssignment href "../../classes/ChannelopathyAssignment/"
      
      ClassificationAssignment : evidence
        
          
    
        
        
        ClassificationAssignment --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      ClassificationAssignment : notes
        
      
```





## Inheritance
* **ClassificationAssignment**
    * [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md)
    * [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md)
    * [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md)
    * [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md)
    * [IUISAssignment](../classes/IUISAssignment.md)
    * [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ClassificationAssignment |
| native | dismech:ClassificationAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClassificationAssignment
description: Base class for classification assignments with evidence
from_schema: https://w3id.org/monarch-initiative/dismech
abstract: true
slots:
- evidence
- notes

```
</details>

### Induced

<details>
```yaml
name: ClassificationAssignment
description: Base class for classification assignments with evidence
from_schema: https://w3id.org/monarch-initiative/dismech
abstract: true
attributes:
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: ClassificationAssignment
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
  notes:
    name: notes
    examples:
    - value: Contagious stage where symptoms appear and the bacteria can be spread
        to others.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: notes
    owner: ClassificationAssignment
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