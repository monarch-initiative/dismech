

# Class: ISDSNosologyAssignment 


_ISDS Nosology group assignment for a genetic skeletal disorder, per the Nosology of Genetic Skeletal Disorders (2023 revision, 11th edition; Unger et al., PMID:36779427), which supersedes the 2019 revision (PMID:31633310). Record the provenance — which revision, the group number/name, and the listed disorder name where it differs from the dismech entry name — in ``notes``. Assignments may legitimately cite either revision while the 2019-derived backfill is being re-verified against the 2023 table; the ``notes`` must say which one._





URI: [dismech:class/ISDSNosologyAssignment](https://w3id.org/monarch-initiative/dismech/class/ISDSNosologyAssignment)





```mermaid
 classDiagram
    class ISDSNosologyAssignment
    click ISDSNosologyAssignment href "../../classes/ISDSNosologyAssignment/"
      ClassificationAssignment <|-- ISDSNosologyAssignment
        click ClassificationAssignment href "../../classes/ClassificationAssignment/"
      
      ISDSNosologyAssignment : classification_value
        
          
    
        
        
        ISDSNosologyAssignment --> "1" ISDSNosologyGroupEnum : classification_value
        click ISDSNosologyGroupEnum href "../../enums/ISDSNosologyGroupEnum/"
    

        
      ISDSNosologyAssignment : evidence
        
          
    
        
        
        ISDSNosologyAssignment --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      ISDSNosologyAssignment : notes
        
      
```





## Inheritance
* [ClassificationAssignment](../classes/ClassificationAssignment.md)
    * **ISDSNosologyAssignment**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [classification_value](../slots/classification_value.md) | 1 <br/> [ISDSNosologyGroupEnum](../enums/ISDSNosologyGroupEnum.md) | The classification value assigned | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | [ClassificationAssignment](../classes/ClassificationAssignment.md) |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | [ClassificationAssignment](../classes/ClassificationAssignment.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseClassifications](../classes/DiseaseClassifications.md) | [isds_skeletal_category](../slots/isds_skeletal_category.md) | range | [ISDSNosologyAssignment](../classes/ISDSNosologyAssignment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ISDSNosologyAssignment |
| native | dismech:ISDSNosologyAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ISDSNosologyAssignment
description: ISDS Nosology group assignment for a genetic skeletal disorder, per the
  Nosology of Genetic Skeletal Disorders (2023 revision, 11th edition; Unger et al.,
  PMID:36779427), which supersedes the 2019 revision (PMID:31633310). Record the provenance
  — which revision, the group number/name, and the listed disorder name where it differs
  from the dismech entry name — in ``notes``. Assignments may legitimately cite either
  revision while the 2019-derived backfill is being re-verified against the 2023 table;
  the ``notes`` must say which one.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slots:
- classification_value
slot_usage:
  classification_value:
    name: classification_value
    range: ISDSNosologyGroupEnum
    required: true

```
</details>

### Induced

<details>
```yaml
name: ISDSNosologyAssignment
description: ISDS Nosology group assignment for a genetic skeletal disorder, per the
  Nosology of Genetic Skeletal Disorders (2023 revision, 11th edition; Unger et al.,
  PMID:36779427), which supersedes the 2019 revision (PMID:31633310). Record the provenance
  — which revision, the group number/name, and the listed disorder name where it differs
  from the dismech entry name — in ``notes``. Assignments may legitimately cite either
  revision while the 2019-derived backfill is being re-verified against the 2023 table;
  the ``notes`` must say which one.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: ClassificationAssignment
slot_usage:
  classification_value:
    name: classification_value
    range: ISDSNosologyGroupEnum
    required: true
attributes:
  classification_value:
    name: classification_value
    description: The classification value assigned
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: classification_value
    owner: ISDSNosologyAssignment
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
    range: ISDSNosologyGroupEnum
    required: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: ISDSNosologyAssignment
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
    owner: ISDSNosologyAssignment
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