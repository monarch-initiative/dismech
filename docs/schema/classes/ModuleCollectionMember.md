

# Class: ModuleCollectionMember 


_A mechanism module included in a ModuleCollection, with optional labels and explanation specific to the source framework._





URI: [dismech:class/ModuleCollectionMember](https://w3id.org/monarch-initiative/dismech/class/ModuleCollectionMember)





```mermaid
 classDiagram
    class ModuleCollectionMember
    click ModuleCollectionMember href "../../classes/ModuleCollectionMember/"
      ModuleCollectionMember : description
        
      ModuleCollectionMember : evidence
        
          
    
        
        
        ModuleCollectionMember --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      ModuleCollectionMember : framework_terms
        
      ModuleCollectionMember : module
        
      ModuleCollectionMember : notes
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [module](../slots/module.md) | 1 <br/> [String](../types/String.md) | Foreign key to a mechanism module filename stem in kb/modules/ | direct |
| [framework_terms](../slots/framework_terms.md) | * <br/> [String](../types/String.md) | One or more labels used by the source framework for the concept represented b... | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ModuleCollection](../classes/ModuleCollection.md) | [module_members](../slots/module_members.md) | range | [ModuleCollectionMember](../classes/ModuleCollectionMember.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ModuleCollectionMember |
| native | dismech:ModuleCollectionMember |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModuleCollectionMember
description: A mechanism module included in a ModuleCollection, with optional labels
  and explanation specific to the source framework.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- module
- framework_terms
- description
- evidence
- notes
slot_usage:
  module:
    name: module
    description: Foreign key to a mechanism module filename stem in kb/modules/. Node
      anchors are not used for collection membership.
    required: true

```
</details>

### Induced

<details>
```yaml
name: ModuleCollectionMember
description: A mechanism module included in a ModuleCollection, with optional labels
  and explanation specific to the source framework.
from_schema: https://w3id.org/monarch-initiative/dismech
slot_usage:
  module:
    name: module
    description: Foreign key to a mechanism module filename stem in kb/modules/. Node
      anchors are not used for collection membership.
    required: true
attributes:
  module:
    name: module
    description: Foreign key to a mechanism module filename stem in kb/modules/. Node
      anchors are not used for collection membership.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: module
    owner: ModuleCollectionMember
    domain_of:
    - LogicalCriterion
    - DifferentiatingMechanism
    - ModuleCollectionMember
    range: string
    required: true
  framework_terms:
    name: framework_terms
    description: One or more labels used by the source framework for the concept represented
      by this module. Multivalued because one module may intentionally combine closely
      coupled framework concepts.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: framework_terms
    owner: ModuleCollectionMember
    domain_of:
    - ModuleCollectionMember
    range: string
    multivalued: true
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: ModuleCollectionMember
    domain_of:
    - Descriptor
    - DietaryModification
    - GeneticContext
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
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
    - EnvironmentalMechanismTarget
    - ModelMechanismLink
    - BiomarkerReadout
    - PhenotypeReadout
    - SurrogateEndpointCollection
    - ProteinStructure
    - ExternalAssertion
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - HistopathologyFinding
    - ImagingFinding
    - Environmental
    - Disease
    - Stage
    - AgentLifeCycle
    - AgentLifeCycleStage
    - AnimalModel
    - Treatment
    - InfectiousAgent
    - Transmission
    - Assay
    - Diagnosis
    - Inheritance
    - Variant
    - FunctionalEffect
    - Mechanism
    - ModelingConsideration
    - Definition
    - CriteriaSet
    - ConditionDescriptor
    - GOEnrichment
    - ComorbidityHypothesis
    - UpstreamConditionHypothesis
    - MechanisticHypothesis
    - Grouping
    - GroupingCriteria
    - LogicalCriterion
    - DifferentiatingMechanism
    - ModuleCollection
    - ModuleCollectionMember
    range: string
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: ModuleCollectionMember
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
    - EnvironmentalMechanismTarget
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
    - ModuleCollection
    - ModuleCollectionMember
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
    owner: ModuleCollectionMember
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
    - AnimalModel
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
    - ModuleCollection
    - ModuleCollectionMember
    range: string

```
</details>