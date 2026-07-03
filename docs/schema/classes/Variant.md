

# Class: Variant 


_A genetic variant associated with a disease, including coding and non-coding regulatory variants. For regulatory variants, use regulatory_category to classify the variant's impact on gene expression (LOE/mLOE/GOE per Cheng et al. 2024)._





URI: [dismech:class/Variant](https://w3id.org/monarch-initiative/dismech/class/Variant)





```mermaid
 classDiagram
    class Variant
    click Variant href "../../classes/Variant/"
      Variant : clinical_significance
        
          
    
        
        
        Variant --> "0..1" ClinicalSignificanceEnum : clinical_significance
        click ClinicalSignificanceEnum href "../../enums/ClinicalSignificanceEnum/"
    

        
      Variant : description
        
      Variant : evidence
        
          
    
        
        
        Variant --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      Variant : external_assertions
        
          
    
        
        
        Variant --> "*" ExternalAssertion : external_assertions
        click ExternalAssertion href "../../classes/ExternalAssertion/"
    

        
      Variant : functional_effects
        
          
    
        
        
        Variant --> "*" FunctionalEffect : functional_effects
        click FunctionalEffect href "../../classes/FunctionalEffect/"
    

        
      Variant : gene
        
          
    
        
        
        Variant --> "0..1" GeneDescriptor : gene
        click GeneDescriptor href "../../classes/GeneDescriptor/"
    

        
      Variant : identifiers
        
      Variant : name
        
      Variant : regulatory_category
        
          
    
        
        
        Variant --> "0..1" RegulatoryVariantCategoryEnum : regulatory_category
        click RegulatoryVariantCategoryEnum href "../../enums/RegulatoryVariantCategoryEnum/"
    

        
      Variant : sequence_length
        
      Variant : synonyms
        
      Variant : type
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [gene](../slots/gene.md) | 0..1 <br/> [GeneDescriptor](../classes/GeneDescriptor.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [functional_effects](../slots/functional_effects.md) | * <br/> [FunctionalEffect](../classes/FunctionalEffect.md) |  | direct |
| [synonyms](../slots/synonyms.md) | * <br/> [String](../types/String.md) |  | direct |
| [identifiers](../slots/identifiers.md) | * <br/> [Uriorcurie](../types/Uriorcurie.md) |  | direct |
| [external_assertions](../slots/external_assertions.md) | * <br/> [ExternalAssertion](../classes/ExternalAssertion.md) | External curated assertions or registry records relevant to this entity | direct |
| [sequence_length](../slots/sequence_length.md) | 0..1 <br/> [Integer](../types/Integer.md) |  | direct |
| [clinical_significance](../slots/clinical_significance.md) | 0..1 <br/> [ClinicalSignificanceEnum](../enums/ClinicalSignificanceEnum.md) |  | direct |
| [type](../slots/type.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [regulatory_category](../slots/regulatory_category.md) | 0..1 <br/> [RegulatoryVariantCategoryEnum](../enums/RegulatoryVariantCategoryEnum.md) | Functional classification of a variant's impact on gene expression, using the... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Genetic](../classes/Genetic.md) | [variants](../slots/variants.md) | range | [Variant](../classes/Variant.md) |
| [Disease](../classes/Disease.md) | [variants](../slots/variants.md) | range | [Variant](../classes/Variant.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:Variant |
| native | dismech:Variant |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Variant
description: A genetic variant associated with a disease, including coding and non-coding
  regulatory variants. For regulatory variants, use regulatory_category to classify
  the variant's impact on gene expression (LOE/mLOE/GOE per Cheng et al. 2024).
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- description
- gene
- evidence
- functional_effects
- synonyms
- identifiers
- external_assertions
- sequence_length
- clinical_significance
- type
- regulatory_category

```
</details>

### Induced

<details>
```yaml
name: Variant
description: A genetic variant associated with a disease, including coding and non-coding
  regulatory variants. For regulatory variants, use regulatory_category to classify
  the variant's impact on gene expression (LOE/mLOE/GOE per Cheng et al. 2024).
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
    owner: Variant
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
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: Variant
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
  gene:
    name: gene
    examples:
    - value: '{preferred_term: MEFV}'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: gene
    owner: Variant
    domain_of:
    - GeneticContext
    - ExperimentalPerturbation
    - Pathophysiology
    - Variant
    - LogicalCriterion
    - DifferentiatingMechanism
    range: GeneDescriptor
    inlined: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: Variant
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
  functional_effects:
    name: functional_effects
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: functional_effects
    owner: Variant
    domain_of:
    - Variant
    range: FunctionalEffect
    multivalued: true
    inlined: true
    inlined_as_list: true
  synonyms:
    name: synonyms
    examples:
    - value: '[''CYFRA 21-1'']'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: synonyms
    owner: Variant
    domain_of:
    - Pathophysiology
    - Biochemical
    - Environmental
    - Disease
    - Variant
    range: string
    multivalued: true
  identifiers:
    name: identifiers
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: identifiers
    owner: Variant
    domain_of:
    - Variant
    range: uriorcurie
    multivalued: true
  external_assertions:
    name: external_assertions
    description: External curated assertions or registry records relevant to this
      entity
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: external_assertions
    owner: Variant
    domain_of:
    - Disease
    - Variant
    range: ExternalAssertion
    multivalued: true
    inlined: true
    inlined_as_list: true
  sequence_length:
    name: sequence_length
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: sequence_length
    owner: Variant
    domain_of:
    - Variant
    range: integer
  clinical_significance:
    name: clinical_significance
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: clinical_significance
    owner: Variant
    domain_of:
    - Variant
    range: ClinicalSignificanceEnum
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: type
    owner: Variant
    domain_of:
    - Variant
    - FunctionalEffect
    range: string
  regulatory_category:
    name: regulatory_category
    description: Functional classification of a variant's impact on gene expression,
      using the LOE/mLOE/GOE framework (Cheng et al. 2024, PMID:38436667) or traditional
      coding categories (LOF/GOF/DN).
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: regulatory_category
    owner: Variant
    domain_of:
    - Variant
    - FunctionalEffect
    range: RegulatoryVariantCategoryEnum

```
</details>