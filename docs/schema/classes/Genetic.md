

# Class: Genetic 



URI: [dismech:class/Genetic](https://w3id.org/monarch-initiative/dismech/class/Genetic)





```mermaid
 classDiagram
    class Genetic
    click Genetic href "../../classes/Genetic/"
      Genetic : association
        
      Genetic : evidence
        
          
    
        
        
        Genetic --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      Genetic : examples
        
      Genetic : features
        
      Genetic : frequency
        
          
    
        
        
        Genetic --> "0..1" Any : frequency
        click Any href "../../classes/Any/"
    

        
      Genetic : gene_term
        
          
    
        
        
        Genetic --> "0..1" GeneDescriptor : gene_term
        click GeneDescriptor href "../../classes/GeneDescriptor/"
    

        
      Genetic : inheritance
        
          
    
        
        
        Genetic --> "*" Inheritance : inheritance
        click Inheritance href "../../classes/Inheritance/"
    

        
      Genetic : name
        
      Genetic : notes
        
      Genetic : presence
        
      Genetic : relationship_type
        
          
    
        
        
        Genetic --> "0..1" GeneDiseaseRelationshipEnum : relationship_type
        click GeneDiseaseRelationshipEnum href "../../enums/GeneDiseaseRelationshipEnum/"
    

        
      Genetic : review_notes
        
      Genetic : subtype
        
      Genetic : variant_origin
        
          
    
        
        
        Genetic --> "0..1" VariantOriginEnum : variant_origin
        click VariantOriginEnum href "../../enums/VariantOriginEnum/"
    

        
      Genetic : variants
        
          
    
        
        
        Genetic --> "*" Variant : variants
        click Variant href "../../classes/Variant/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [gene_term](../slots/gene_term.md) | 0..1 <br/> [GeneDescriptor](../classes/GeneDescriptor.md) | The HGNC term for this gene | direct |
| [presence](../slots/presence.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [association](../slots/association.md) | 0..1 <br/> [String](../types/String.md) | Free-text descriptor of how the gene is associated with the disease | direct |
| [relationship_type](../slots/relationship_type.md) | 0..1 <br/> [GeneDiseaseRelationshipEnum](../enums/GeneDiseaseRelationshipEnum.md) | Controlled-vocabulary classification of the gene-disease relationship (e | direct |
| [variant_origin](../slots/variant_origin.md) | 0..1 <br/> [VariantOriginEnum](../enums/VariantOriginEnum.md) | The origin of disease-associated variation in this gene (germline, somatic, d... | direct |
| [review_notes](../slots/review_notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [subtype](../slots/subtype.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [frequency](../slots/frequency.md) | 0..1 <br/> [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[FrequencyEnum](../enums/FrequencyEnum.md)&nbsp;or&nbsp;<br />[FrequencyQuantity](../types/FrequencyQuantity.md) |  | direct |
| [inheritance](../slots/inheritance.md) | * <br/> [Inheritance](../classes/Inheritance.md) |  | direct |
| [variants](../slots/variants.md) | * <br/> [Variant](../classes/Variant.md) |  | direct |
| [features](../slots/features.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [examples](../slots/examples.md) | * <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Disease](../classes/Disease.md) | [genetic](../slots/genetic.md) | range | [Genetic](../classes/Genetic.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:Genetic |
| native | dismech:Genetic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Genetic
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- gene_term
- presence
- evidence
- association
- relationship_type
- variant_origin
- review_notes
- subtype
- frequency
- inheritance
- variants
- features
- notes
- examples

```
</details>

### Induced

<details>
```yaml
name: Genetic
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
    owner: Genetic
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
  gene_term:
    name: gene_term
    description: The HGNC term for this gene
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: gene_term
    owner: Genetic
    domain_of:
    - Genetic
    range: GeneDescriptor
    inlined: true
  presence:
    name: presence
    examples:
    - value: Positive
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: presence
    owner: Genetic
    domain_of:
    - Biochemical
    - Genetic
    - Environmental
    - Diagnosis
    range: string
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: Genetic
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
  association:
    name: association
    description: Free-text descriptor of how the gene is associated with the disease.
      For a controlled vocabulary, also set `relationship_type`.
    examples:
    - value: Susceptibility
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: association
    owner: Genetic
    domain_of:
    - Genetic
    range: string
  relationship_type:
    name: relationship_type
    description: Controlled-vocabulary classification of the gene-disease relationship
      (e.g., causative, risk factor, modifier, somatic driver). Use this in addition
      to the free-text `association` slot when possible.
    examples:
    - value: RISK_FACTOR
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: relationship_type
    owner: Genetic
    domain_of:
    - Genetic
    range: GeneDiseaseRelationshipEnum
  variant_origin:
    name: variant_origin
    description: The origin of disease-associated variation in this gene (germline,
      somatic, de novo, or both). Bound to GENO allele origin terms.
    examples:
    - value: SOMATIC
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: variant_origin
    owner: Genetic
    domain_of:
    - GeneticContext
    - Genetic
    range: VariantOriginEnum
  review_notes:
    name: review_notes
    examples:
    - value: Added an additional clinically relevant subtype.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: review_notes
    owner: Genetic
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
  subtype:
    name: subtype
    examples:
    - value: Eyelid Myoclonia with Absences
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: subtype
    owner: Genetic
    domain_of:
    - PhenotypeContext
    - Prevalence
    - ProgressionInfo
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - Genetic
    range: string
  frequency:
    name: frequency
    examples:
    - value: Occasional
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: frequency
    owner: Genetic
    domain_of:
    - PhenotypeContext
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - Genetic
    range: Any
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
    owner: Genetic
    domain_of:
    - Subtype
    - Genetic
    - Disease
    range: Inheritance
    multivalued: true
    inlined: true
    inlined_as_list: true
  variants:
    name: variants
    comments:
    - can currently be used at gene or disease level, TODO - decide the best level
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: variants
    owner: Genetic
    domain_of:
    - Genetic
    - Disease
    range: Variant
    multivalued: true
    inlined: true
    inlined_as_list: true
  features:
    name: features
    examples:
    - value: DNA virus from the Orthopoxvirus genus
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: features
    owner: Genetic
    domain_of:
    - Genetic
    range: string
  notes:
    name: notes
    examples:
    - value: Contagious stage where symptoms appear and the bacteria can be spread
        to others.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: notes
    owner: Genetic
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
    - Discussion
    - Grouping
    - GroupingCriteria
    - GroupingMember
    - DifferentiatingMechanism
    range: string
  examples:
    name: examples
    examples:
    - value: '[''Kaposi Sarcoma'']'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: examples
    owner: Genetic
    domain_of:
    - Pathophysiology
    - Genetic
    - Environmental
    - Stage
    - Treatment
    range: string
    multivalued: true

```
</details>