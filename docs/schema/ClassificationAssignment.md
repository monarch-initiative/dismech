

# Class: ClassificationAssignment 


_Base class for classification assignments with evidence_




* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [dismech:ClassificationAssignment](https://w3id.org/monarch-initiative/dismech/ClassificationAssignment)





```mermaid
 classDiagram
    class ClassificationAssignment
    click ClassificationAssignment href "../ClassificationAssignment/"
      ClassificationAssignment <|-- ICDOMorphologyAssignment
        click ICDOMorphologyAssignment href "../ICDOMorphologyAssignment/"
      ClassificationAssignment <|-- HarrisonsChapterAssignment
        click HarrisonsChapterAssignment href "../HarrisonsChapterAssignment/"
      ClassificationAssignment <|-- LysosomalStorageAssignment
        click LysosomalStorageAssignment href "../LysosomalStorageAssignment/"
      ClassificationAssignment <|-- MechanisticNosologyAssignment
        click MechanisticNosologyAssignment href "../MechanisticNosologyAssignment/"
      ClassificationAssignment <|-- IUISAssignment
        click IUISAssignment href "../IUISAssignment/"
      ClassificationAssignment <|-- ChannelopathyAssignment
        click ChannelopathyAssignment href "../ChannelopathyAssignment/"
      
      ClassificationAssignment : evidence
        
          
    
        
        
        ClassificationAssignment --> "*" EvidenceItem : evidence
        click EvidenceItem href "../EvidenceItem/"
    

        
      ClassificationAssignment : notes
        
      
```





## Inheritance
* **ClassificationAssignment**
    * [ICDOMorphologyAssignment](ICDOMorphologyAssignment.md)
    * [HarrisonsChapterAssignment](HarrisonsChapterAssignment.md)
    * [LysosomalStorageAssignment](LysosomalStorageAssignment.md)
    * [MechanisticNosologyAssignment](MechanisticNosologyAssignment.md)
    * [IUISAssignment](IUISAssignment.md)
    * [ChannelopathyAssignment](ChannelopathyAssignment.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [evidence](evidence.md) | * _recommended_ <br/> [EvidenceItem](EvidenceItem.md) |  | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) |  | direct |










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