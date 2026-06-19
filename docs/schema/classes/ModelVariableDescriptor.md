

# Class: ModelVariableDescriptor 


_A descriptor mapping a model variable to an ontology term (LOINC, CHEBI, HP, etc.). When the mapped term is an HP phenotype, optional threshold fields specify when the variable value activates that phenotype and at what severity._





URI: [dismech:class/ModelVariableDescriptor](https://w3id.org/monarch-initiative/dismech/class/ModelVariableDescriptor)





```mermaid
 classDiagram
    class ModelVariableDescriptor
    click ModelVariableDescriptor href "../../classes/ModelVariableDescriptor/"
      Descriptor <|-- ModelVariableDescriptor
        click Descriptor href "../../classes/Descriptor/"
      
      ModelVariableDescriptor : clinical_course
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" ClinicalCourseEnum : clinical_course
        click ClinicalCourseEnum href "../../enums/ClinicalCourseEnum/"
    

        
      ModelVariableDescriptor : description
        
      ModelVariableDescriptor : laterality
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../../enums/LateralityEnum/"
    

        
      ModelVariableDescriptor : located_in
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../../classes/AnatomicalEntityDescriptor/"
    

        
      ModelVariableDescriptor : modifier
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../../enums/ModifierEnum/"
    

        
      ModelVariableDescriptor : onset
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" OnsetDescriptor : onset
        click OnsetDescriptor href "../../classes/OnsetDescriptor/"
    

        
      ModelVariableDescriptor : preferred_term
        
      ModelVariableDescriptor : qualifiers
        
          
    
        
        
        ModelVariableDescriptor --> "*" Qualifier : qualifiers
        click Qualifier href "../../classes/Qualifier/"
    

        
      ModelVariableDescriptor : severity
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" Any : severity
        click Any href "../../classes/Any/"
    

        
      ModelVariableDescriptor : severity_scale
        
          
    
        
        
        ModelVariableDescriptor --> "*" SeverityTier : severity_scale
        click SeverityTier href "../../classes/SeverityTier/"
    

        
      ModelVariableDescriptor : spatial_extent
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" SpatialExtentEnum : spatial_extent
        click SpatialExtentEnum href "../../enums/SpatialExtentEnum/"
    

        
      ModelVariableDescriptor : temporality
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" TemporalityEnum : temporality
        click TemporalityEnum href "../../enums/TemporalityEnum/"
    

        
      ModelVariableDescriptor : term
        
          
    
        
        
        ModelVariableDescriptor --> "0..1 _recommended_" Term : term
        click Term href "../../classes/Term/"
    

        
      ModelVariableDescriptor : threshold
        
      ModelVariableDescriptor : threshold_direction
        
          
    
        
        
        ModelVariableDescriptor --> "0..1" ThresholdDirectionEnum : threshold_direction
        click ThresholdDirectionEnum href "../../enums/ThresholdDirectionEnum/"
    

        
      
```





## Inheritance
* [Descriptor](../classes/Descriptor.md)
    * **ModelVariableDescriptor**


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [threshold](../slots/threshold.md) | 0..1 <br/> [Float](../types/Float.md) | Value at which the mapped phenotype activates | direct |
| [threshold_direction](../slots/threshold_direction.md) | 0..1 <br/> [ThresholdDirectionEnum](../enums/ThresholdDirectionEnum.md) | Whether the phenotype activates above or below the threshold | direct |
| [severity_scale](../slots/severity_scale.md) | * <br/> [SeverityTier](../classes/SeverityTier.md) | Ordered severity tiers for graded phenotype activation | direct |
| [preferred_term](../slots/preferred_term.md) | 1 <br/> [String](../types/String.md) | The preferred human-readable term for this descriptor | [Descriptor](../classes/Descriptor.md) |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) | A description of the descriptor | [Descriptor](../classes/Descriptor.md) |
| [term](../slots/term.md) | 0..1 _recommended_ <br/> [Term](../classes/Term.md) | Ontology term reference (LOINC code, CHEBI term, HP term, etc | [Descriptor](../classes/Descriptor.md) |
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
| [ModelVariable](../classes/ModelVariable.md) | [mappings_list](../slots/mappings_list.md) | range | [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) |
| [Biochemical](../classes/Biochemical.md) | [mappings_list](../slots/mappings_list.md) | range | [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ModelVariableDescriptor |
| native | dismech:ModelVariableDescriptor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ModelVariableDescriptor
description: A descriptor mapping a model variable to an ontology term (LOINC, CHEBI,
  HP, etc.). When the mapped term is an HP phenotype, optional threshold fields specify
  when the variable value activates that phenotype and at what severity.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slots:
- threshold
- threshold_direction
- severity_scale
slot_usage:
  term:
    name: term
    description: Ontology term reference (LOINC code, CHEBI term, HP term, etc.)
  threshold:
    name: threshold
    description: Value at which the mapped phenotype activates
  threshold_direction:
    name: threshold_direction
    description: Whether the phenotype activates above or below the threshold
  severity_scale:
    name: severity_scale
    description: Ordered severity tiers for graded phenotype activation

```
</details>

### Induced

<details>
```yaml
name: ModelVariableDescriptor
description: A descriptor mapping a model variable to an ontology term (LOINC, CHEBI,
  HP, etc.). When the mapped term is an HP phenotype, optional threshold fields specify
  when the variable value activates that phenotype and at what severity.
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Ontology term reference (LOINC code, CHEBI term, HP term, etc.)
  threshold:
    name: threshold
    description: Value at which the mapped phenotype activates
  threshold_direction:
    name: threshold_direction
    description: Whether the phenotype activates above or below the threshold
  severity_scale:
    name: severity_scale
    description: Ordered severity tiers for graded phenotype activation
attributes:
  threshold:
    name: threshold
    description: Value at which the mapped phenotype activates
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: threshold
    owner: ModelVariableDescriptor
    domain_of:
    - SeverityTier
    - ModelVariableDescriptor
    range: float
  threshold_direction:
    name: threshold_direction
    description: Whether the phenotype activates above or below the threshold
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: threshold_direction
    owner: ModelVariableDescriptor
    domain_of:
    - ModelVariableDescriptor
    range: ThresholdDirectionEnum
  severity_scale:
    name: severity_scale
    description: Ordered severity tiers for graded phenotype activation
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: severity_scale
    owner: ModelVariableDescriptor
    domain_of:
    - ModelVariableDescriptor
    range: SeverityTier
    multivalued: true
    inlined: true
    inlined_as_list: true
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    description: Ontology term reference (LOINC code, CHEBI term, HP term, etc.)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: ModelVariableDescriptor
    domain_of:
    - Descriptor
    - TermMapping
    - ConditionDescriptor
    - GOEnrichmentTerm
    range: Term
    recommended: true
    inlined: true
  modifier:
    name: modifier
    description: Directional or qualitative modifier for a descriptor (e.g., increased,
      decreased, abnormal)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: modifier
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
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
    owner: ModelVariableDescriptor
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>