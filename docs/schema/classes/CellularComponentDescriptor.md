

# Class: CellularComponentDescriptor 


_A descriptor for cellular components, bindable to GO cellular component_





URI: [dismech:class/CellularComponentDescriptor](https://w3id.org/monarch-initiative/dismech/class/CellularComponentDescriptor)





```mermaid
 classDiagram
    class CellularComponentDescriptor
    click CellularComponentDescriptor href "../../classes/CellularComponentDescriptor/"
      Descriptor <|-- CellularComponentDescriptor
        click Descriptor href "../../classes/Descriptor/"
      
      CellularComponentDescriptor : clinical_course
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" ClinicalCourseEnum : clinical_course
        click ClinicalCourseEnum href "../../enums/ClinicalCourseEnum/"
    

        
      CellularComponentDescriptor : description
        
      CellularComponentDescriptor : laterality
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../../enums/LateralityEnum/"
    

        
      CellularComponentDescriptor : located_in
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../../classes/AnatomicalEntityDescriptor/"
    

        
      CellularComponentDescriptor : modifier
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../../enums/ModifierEnum/"
    

        
      CellularComponentDescriptor : onset
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" OnsetDescriptor : onset
        click OnsetDescriptor href "../../classes/OnsetDescriptor/"
    

        
      CellularComponentDescriptor : preferred_term
        
      CellularComponentDescriptor : qualifiers
        
          
    
        
        
        CellularComponentDescriptor --> "*" Qualifier : qualifiers
        click Qualifier href "../../classes/Qualifier/"
    

        
      CellularComponentDescriptor : severity
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" Any : severity
        click Any href "../../classes/Any/"
    

        
      CellularComponentDescriptor : spatial_extent
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" SpatialExtentEnum : spatial_extent
        click SpatialExtentEnum href "../../enums/SpatialExtentEnum/"
    

        
      CellularComponentDescriptor : temporality
        
          
    
        
        
        CellularComponentDescriptor --> "0..1" TemporalityEnum : temporality
        click TemporalityEnum href "../../enums/TemporalityEnum/"
    

        
      CellularComponentDescriptor : term
        
          
    
        
        
        CellularComponentDescriptor --> "0..1 _recommended_" Term : term
        click Term href "../../classes/Term/"
    

        
      
```





## Inheritance
* [Descriptor](../classes/Descriptor.md)
    * **CellularComponentDescriptor**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [preferred_term](../slots/preferred_term.md) | 1 <br/> [String](../types/String.md) | The preferred human-readable term for this descriptor | [Descriptor](../classes/Descriptor.md) |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) | A description of the descriptor | [Descriptor](../classes/Descriptor.md) |
| [term](../slots/term.md) | 0..1 _recommended_ <br/> [Term](../classes/Term.md) | Optional GO cellular component term reference | [Descriptor](../classes/Descriptor.md) |
| [modifier](../slots/modifier.md) | 0..1 <br/> [ModifierEnum](../enums/ModifierEnum.md) | Directional or qualitative modifier for a descriptor (e | [Descriptor](../classes/Descriptor.md) |
| [located_in](../slots/located_in.md) | 0..1 <br/> [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | Anatomical location where this entity/process occurs or procedure is performe... | [Descriptor](../classes/Descriptor.md) |
| [laterality](../slots/laterality.md) | 0..1 <br/> [LateralityEnum](../enums/LateralityEnum.md) | Laterality qualifier (left, right, or bilateral) | [Descriptor](../classes/Descriptor.md) |
| [spatial_extent](../slots/spatial_extent.md) | 0..1 <br/> [SpatialExtentEnum](../enums/SpatialExtentEnum.md) | The spatial extent or distribution pattern applicable to this descriptor (e | [Descriptor](../classes/Descriptor.md) |
| [onset](../slots/onset.md) | 0..1 <br/> [OnsetDescriptor](../classes/OnsetDescriptor.md) | Structured age of onset descriptor | [Descriptor](../classes/Descriptor.md) |
| [temporality](../slots/temporality.md) | 0..1 <br/> [TemporalityEnum](../enums/TemporalityEnum.md) | Temporal qualifier for this descriptor (e | [Descriptor](../classes/Descriptor.md) |
| [clinical_course](../slots/clinical_course.md) | 0..1 <br/> [ClinicalCourseEnum](../enums/ClinicalCourseEnum.md) | Clinical course qualifier for this descriptor (e | [Descriptor](../classes/Descriptor.md) |
| [severity](../slots/severity.md) | 0..1 <br/> [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[String](../types/String.md)&nbsp;or&nbsp;<br />[SeverityQualifierEnum](../enums/SeverityQualifierEnum.md) |  | [Descriptor](../classes/Descriptor.md) |
| [qualifiers](../slots/qualifiers.md) | * <br/> [Qualifier](../classes/Qualifier.md) | List of predicate-value pairs for formal post-composition | [Descriptor](../classes/Descriptor.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Pathophysiology](../classes/Pathophysiology.md) | [cellular_components](../slots/cellular_components.md) | range | [CellularComponentDescriptor](../classes/CellularComponentDescriptor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:CellularComponentDescriptor |
| native | dismech:CellularComponentDescriptor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellularComponentDescriptor
description: A descriptor for cellular components, bindable to GO cellular component
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Optional GO cellular component term reference
    bindings:
    - range: CellularComponentTerm
      obligation_level: REQUIRED
      binds_value_of: id

```
</details>

### Induced

<details>
```yaml
name: CellularComponentDescriptor
description: A descriptor for cellular components, bindable to GO cellular component
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Optional GO cellular component term reference
    bindings:
    - range: CellularComponentTerm
      obligation_level: REQUIRED
      binds_value_of: id
attributes:
  preferred_term:
    name: preferred_term
    description: The preferred human-readable term for this descriptor. This may be
      more specific or nuanced than the linked ontology term label when the ontology
      does not fully capture the desired granularity. Note that postcomposition using
      the modifier slot may be appropriate for capturing the semantics of the preferred
      term.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: preferred_term
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    - ConditionDescriptor
    range: string
    required: true
  description:
    name: description
    description: A description of the descriptor. This may typically be redundant
      with the `term` object, but the description is more human-readable and may be
      used to communicate nuances not captured by the rigid standardization of the
      term object.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: CellularComponentDescriptor
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
    recommended: false
  term:
    name: term
    description: Optional GO cellular component term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    - TermMapping
    - ConditionDescriptor
    - GOEnrichmentTerm
    range: Term
    bindings:
    - range: CellularComponentTerm
      obligation_level: REQUIRED
      binds_value_of: id
    recommended: true
    inlined: true
  modifier:
    name: modifier
    description: Directional or qualitative modifier for a descriptor (e.g., increased,
      decreased, abnormal)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: modifier
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    - DifferentiatingMechanism
    range: ModifierEnum
  located_in:
    name: located_in
    description: Anatomical location where this entity/process occurs or procedure
      is performed
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: located_in
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: AnatomicalEntityDescriptor
    inlined: true
  laterality:
    name: laterality
    description: Laterality qualifier (left, right, or bilateral)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: laterality
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: LateralityEnum
  spatial_extent:
    name: spatial_extent
    description: The spatial extent or distribution pattern applicable to this descriptor
      (e.g., focal, diffuse, extensive)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: spatial_extent
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: SpatialExtentEnum
  onset:
    name: onset
    description: Structured age of onset descriptor. Combines an HPO onset category
      with optional quantitative age data (mean, min, max in years) and free-text
      notes.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: onset
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    - PhenotypeContext
    range: OnsetDescriptor
    inlined: true
  temporality:
    name: temporality
    description: Temporal qualifier for this descriptor (e.g., acute, chronic, recurrent)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: temporality
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: TemporalityEnum
  clinical_course:
    name: clinical_course
    description: Clinical course qualifier for this descriptor (e.g., progressive,
      stable)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: clinical_course
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: ClinicalCourseEnum
  severity:
    name: severity
    examples:
    - value: Severe
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: severity
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    - PhenotypeContext
    - ReferenceRangeBand
    - Phenotype
    range: Any
    any_of:
    - range: SeverityQualifierEnum
    - range: string
  qualifiers:
    name: qualifiers
    description: List of predicate-value pairs for formal post-composition. Allows
      OWL-like expressivity with controlled predicates (e.g., RO relations) and values.
    deprecated: Prefer explicit slots like located_in and laterality instead of generic
      qualifiers
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: qualifiers
    owner: CellularComponentDescriptor
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>