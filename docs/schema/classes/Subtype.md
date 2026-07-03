

# Class: Subtype 



URI: [dismech:class/Subtype](https://w3id.org/monarch-initiative/dismech/class/Subtype)





```mermaid
 classDiagram
    class Subtype
    click Subtype href "../../classes/Subtype/"
      Subtype : children
        
      Subtype : classification
        
      Subtype : description
        
      Subtype : display_name
        
      Subtype : evidence
        
          
    
        
        
        Subtype --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      Subtype : genes
        
          
    
        
        
        Subtype --> "*" GeneDescriptor : genes
        click GeneDescriptor href "../../classes/GeneDescriptor/"
    

        
      Subtype : geography
        
          
    
        
        
        Subtype --> "*" GeographyTerm : geography
        click GeographyTerm href "../../enums/GeographyTerm/"
    

        
      Subtype : inheritance
        
          
    
        
        
        Subtype --> "*" Inheritance : inheritance
        click Inheritance href "../../classes/Inheritance/"
    

        
      Subtype : locations
        
          
    
        
        
        Subtype --> "*" AnatomicalEntityDescriptor : locations
        click AnatomicalEntityDescriptor href "../../classes/AnatomicalEntityDescriptor/"
    

        
      Subtype : mappings
        
          
    
        
        
        Subtype --> "0..1" DiseaseMappings : mappings
        click DiseaseMappings href "../../classes/DiseaseMappings/"
    

        
      Subtype : name
        
      Subtype : review_notes
        
      Subtype : subtype_frequency
        
      Subtype : subtype_term
        
          
    
        
        
        Subtype --> "0..1" SubtypeDescriptor : subtype_term
        click SubtypeDescriptor href "../../classes/SubtypeDescriptor/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [display_name](../slots/display_name.md) | 0..1 <br/> [String](../types/String.md) | Human-readable display name for a subtype, used when the name (which serves a... | direct |
| [subtype_term](../slots/subtype_term.md) | 0..1 <br/> [SubtypeDescriptor](../classes/SubtypeDescriptor.md) | The ontology term grounding this subtype or cancer facet value | direct |
| [mappings](../slots/mappings.md) | 0..1 <br/> [DiseaseMappings](../classes/DiseaseMappings.md) | External identifier mappings for this disease or subtype (SSSOM-inspired) | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [review_notes](../slots/review_notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [locations](../slots/locations.md) | * <br/> [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) |  | direct |
| [geography](../slots/geography.md) | * <br/> [GeographyTerm](../enums/GeographyTerm.md) |  | direct |
| [classification](../slots/classification.md) | 0..1 <br/> [String](../types/String.md) | Classification scheme this subtype belongs to (e | direct |
| [children](../slots/children.md) | * <br/> [String](../types/String.md) | Names of other subtypes in this list that are members/children of this groupi... | direct |
| [genes](../slots/genes.md) | * <br/> [GeneDescriptor](../classes/GeneDescriptor.md) |  | direct |
| [subtype_frequency](../slots/subtype_frequency.md) | 0..1 <br/> [String](../types/String.md)&nbsp;or&nbsp;<br />[FrequencyEnum](../enums/FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](../types/FrequencyQuantity.md) | Frequency of this subtype among all cases of the parent disease (e | direct |
| [inheritance](../slots/inheritance.md) | * <br/> [Inheritance](../classes/Inheritance.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Disease](../classes/Disease.md) | [has_subtypes](../slots/has_subtypes.md) | range | [Subtype](../classes/Subtype.md) |
| [InfectiousAgent](../classes/InfectiousAgent.md) | [has_subtypes](../slots/has_subtypes.md) | range | [Subtype](../classes/Subtype.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:Subtype |
| native | dismech:Subtype |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Subtype
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- display_name
- subtype_term
- mappings
- description
- evidence
- review_notes
- locations
- geography
- classification
- children
- genes
- subtype_frequency
- inheritance

```
</details>

### Induced

<details>
```yaml
name: Subtype
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  name:
    name: name
    examples:
    - value: Adolescent Nephronophthisis
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    identifier: true
    alias: name
    owner: Subtype
    domain_of:
    - ExperimentalModel
    - Experiment
    - ExperimentalPerturbation
    - ExperimentalReadout
    - ExperimentalControl
    - ClinicalTrial
    - ComputationalModel
    - ModelVariable
    - SeverityTier
    - DifferentialDiagnosis
    - Subtype
    - ReferenceRangeBand
    - SurrogateEndpointCollection
    - ExternalAssertion
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - Genetic
    - Environmental
    - Disease
    - Stage
    - AgentLifeCycleStage
    - Treatment
    - InfectiousAgent
    - Transmission
    - Assay
    - Diagnosis
    - Inheritance
    - Variant
    - Mechanism
    - ModelingConsideration
    - Definition
    - CriteriaSet
    - ComorbidityAssociation
    - Grouping
    range: string
    required: true
  display_name:
    name: display_name
    description: Human-readable display name for a subtype, used when the name (which
      serves as the FK target) is too terse for comfortable display. Optional; when
      absent, renderers should fall back to name.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: display_name
    owner: Subtype
    domain_of:
    - Subtype
    - Grouping
    - GroupingMember
    range: string
  subtype_term:
    name: subtype_term
    description: The ontology term grounding this subtype or cancer facet value. Prefer
      MONDO when available; use NCIT for oncology-specific subtype refinement when
      needed.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: subtype_term
    owner: Subtype
    domain_of:
    - Subtype
    range: SubtypeDescriptor
    inlined: true
  mappings:
    name: mappings
    description: External identifier mappings for this disease or subtype (SSSOM-inspired)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mappings
    owner: Subtype
    domain_of:
    - Subtype
    - Disease
    - Grouping
    range: DiseaseMappings
    inlined: true
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: Subtype
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
    - ModelMechanismLink
    - BiomarkerReadout
    - SurrogateEndpointCollection
    - ProteinStructure
    - ExternalAssertion
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - HistopathologyFinding
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
    range: string
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: Subtype
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
    - ReferenceRange
    - SurrogateEndpoint
    - ExternalAssertion
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
    - Discussion
    - GroupingCriteria
    - GroupingMember
    - DifferentiatingMechanism
    range: EvidenceItem
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  review_notes:
    name: review_notes
    examples:
    - value: Added an additional clinically relevant subtype.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: review_notes
    owner: Subtype
    domain_of:
    - ClinicalTrial
    - Subtype
    - ProgressionInfo
    - Phenotype
    - Genetic
    - Environmental
    - Disease
    - Stage
    - AgentLifeCycle
    - AgentLifeCycleStage
    - Treatment
    range: string
  locations:
    name: locations
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: locations
    owner: Subtype
    domain_of:
    - Subtype
    - Pathophysiology
    range: AnatomicalEntityDescriptor
    multivalued: true
    inlined: true
    inlined_as_list: true
  geography:
    name: geography
    examples:
    - value: '[''Philippines'']'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: geography
    owner: Subtype
    domain_of:
    - Subtype
    range: GeographyTerm
    multivalued: true
  classification:
    name: classification
    description: Classification scheme this subtype belongs to (e.g., 'complementation_group',
      'pathway_tier', 'histological', 'molecular', 'clinical_phenotype').
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: classification
    owner: Subtype
    domain_of:
    - Subtype
    - LogicalCriterion
    range: string
  children:
    name: children
    description: Names of other subtypes in this list that are members/children of
      this grouping subtype. Used to express cross-scheme relationships (e.g., a pathway_tier
      subtype grouping complementation_group subtypes).
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: children
    owner: Subtype
    domain_of:
    - Subtype
    range: string
    multivalued: true
  genes:
    name: genes
    examples:
    - value: '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: genes
    owner: Subtype
    domain_of:
    - GeneticContext
    - Dataset
    - ExperimentalPerturbation
    - Subtype
    - Pathophysiology
    - AnimalModel
    range: GeneDescriptor
    multivalued: true
    inlined: true
    inlined_as_list: true
  subtype_frequency:
    name: subtype_frequency
    description: Frequency of this subtype among all cases of the parent disease (e.g.,
      '60-70%', '~15%'). Distinct from phenotype frequency.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: subtype_frequency
    owner: Subtype
    domain_of:
    - Subtype
    any_of:
    - range: FrequencyEnum
    - range: FrequencyQuantity
  inheritance:
    name: inheritance
    examples:
    - value: Autosomal Dominant
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: inheritance
    owner: Subtype
    domain_of:
    - Subtype
    - Genetic
    - Disease
    range: Inheritance
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>