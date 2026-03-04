

# Class: IUISAssignment 


_IUIS primary immunodeficiency classification assignment_





URI: [dismech:IUISAssignment](https://w3id.org/monarch-initiative/dismech/IUISAssignment)





```mermaid
 classDiagram
    class IUISAssignment
    click IUISAssignment href "../IUISAssignment/"
      ClassificationAssignment <|-- IUISAssignment
        click ClassificationAssignment href "../ClassificationAssignment/"
      
      IUISAssignment : classification_value
        
          
    
        
        
        IUISAssignment --> "1" IUISCategoryEnum : classification_value
        click IUISCategoryEnum href "../IUISCategoryEnum/"
    

        
      IUISAssignment : evidence
        
          
    
        
        
        IUISAssignment --> "*" EvidenceItem : evidence
        click EvidenceItem href "../EvidenceItem/"
    

        
      IUISAssignment : notes
        
      
```





## Inheritance
* [ClassificationAssignment](ClassificationAssignment.md)
    * **IUISAssignment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [classification_value](classification_value.md) | 1 <br/> [IUISCategoryEnum](IUISCategoryEnum.md) | The classification value assigned | direct |
| [evidence](evidence.md) | * _recommended_ <br/> [EvidenceItem](EvidenceItem.md) |  | [ClassificationAssignment](ClassificationAssignment.md) |
| [notes](notes.md) | 0..1 <br/> [String](String.md) |  | [ClassificationAssignment](ClassificationAssignment.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseClassifications](DiseaseClassifications.md) | [iuis_category](iuis_category.md) | range | [IUISAssignment](IUISAssignment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:IUISAssignment |
| native | dismech:IUISAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IUISAssignment
description: IUIS primary immunodeficiency classification assignment
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slots:
- classification_value
slot_usage:
  classification_value:
    name: classification_value
    range: IUISCategoryEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: IUISAssignment
description: IUIS primary immunodeficiency classification assignment
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slot_usage:
  classification_value:
    name: classification_value
    range: IUISCategoryEnum
    required: true
attributes:
  classification_value:
    name: classification_value
    description: The classification value assigned
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: classification_value
    owner: IUISAssignment
    domain_of:
    - ICDOMorphologyAssignment
    - HarrisonsChapterAssignment
    - LysosomalStorageAssignment
    - MechanisticNosologyAssignment
    - IUISAssignment
    - ChannelopathyAssignment
    range: IUISCategoryEnum
    required: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: IUISAssignment
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
    owner: IUISAssignment
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