

# Class: AnatomicalEntityDescriptor 


_A descriptor for anatomical locations, bindable to UBERON_





URI: [dismech:AnatomicalEntityDescriptor](https://w3id.org/monarch-initiative/dismech/AnatomicalEntityDescriptor)





```mermaid
 classDiagram
    class AnatomicalEntityDescriptor
    click AnatomicalEntityDescriptor href "../AnatomicalEntityDescriptor/"
      Descriptor <|-- AnatomicalEntityDescriptor
        click Descriptor href "../Descriptor/"
      
      AnatomicalEntityDescriptor : description
        
      AnatomicalEntityDescriptor : laterality
        
          
    
        
        
        AnatomicalEntityDescriptor --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../LateralityEnum/"
    

        
      AnatomicalEntityDescriptor : located_in
        
          
    
        
        
        AnatomicalEntityDescriptor --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../AnatomicalEntityDescriptor/"
    

        
      AnatomicalEntityDescriptor : modifier
        
          
    
        
        
        AnatomicalEntityDescriptor --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../ModifierEnum/"
    

        
      AnatomicalEntityDescriptor : preferred_term
        
      AnatomicalEntityDescriptor : qualifiers
        
          
    
        
        
        AnatomicalEntityDescriptor --> "*" Qualifier : qualifiers
        click Qualifier href "../Qualifier/"
    

        
      AnatomicalEntityDescriptor : term
        
          
    
        
        
        AnatomicalEntityDescriptor --> "0..1" Term : term
        click Term href "../Term/"
    

        
      
```





## Inheritance
* [Descriptor](Descriptor.md)
    * **AnatomicalEntityDescriptor**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [preferred_term](preferred_term.md) | 1 <br/> [String](String.md) | The preferred human-readable term for this descriptor | [Descriptor](Descriptor.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A description of the descriptor | [Descriptor](Descriptor.md) |
| [term](term.md) | 0..1 _recommended_ <br/> [Term](Term.md) | Optional UBERON anatomical entity term reference | [Descriptor](Descriptor.md) |
| [modifier](modifier.md) | 0..1 <br/> [ModifierEnum](ModifierEnum.md) | Directional or qualitative modifier for a descriptor (e | [Descriptor](Descriptor.md) |
| [located_in](located_in.md) | 0..1 <br/> [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | Anatomical location where this entity/process occurs or procedure is performe... | [Descriptor](Descriptor.md) |
| [laterality](laterality.md) | 0..1 <br/> [LateralityEnum](LateralityEnum.md) | Laterality qualifier (left, right, or bilateral) | [Descriptor](Descriptor.md) |
| [qualifiers](qualifiers.md) | * <br/> [Qualifier](Qualifier.md) | List of predicate-value pairs for formal post-composition | [Descriptor](Descriptor.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Descriptor](Descriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [CellTypeDescriptor](CellTypeDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [GeneDescriptor](GeneDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [CellularComponentDescriptor](CellularComponentDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [ProteinComplexDescriptor](ProteinComplexDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [AssayDescriptor](AssayDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [TriggerDescriptor](TriggerDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [DiseaseDescriptor](DiseaseDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [BiomarkerDescriptor](BiomarkerDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [GeneProductDescriptor](GeneProductDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [HistopathologyFindingDescriptor](HistopathologyFindingDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [LifeCycleStageDescriptor](LifeCycleStageDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [PhenotypeDescriptor](PhenotypeDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [InheritanceDescriptor](InheritanceDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [TreatmentDescriptor](TreatmentDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [RegimenDescriptor](RegimenDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [ExposureDescriptor](ExposureDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [EnvironmentDescriptor](EnvironmentDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [OrganismDescriptor](OrganismDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [HostDescriptor](HostDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | [tissue_term](tissue_term.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [SampleTypeDescriptor](SampleTypeDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [Subtype](Subtype.md) | [locations](locations.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [Pathophysiology](Pathophysiology.md) | [locations](locations.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [CriteriaItem](CriteriaItem.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |
| [ConditionDescriptor](ConditionDescriptor.md) | [located_in](located_in.md) | range | [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:AnatomicalEntityDescriptor |
| native | dismech:AnatomicalEntityDescriptor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnatomicalEntityDescriptor
description: A descriptor for anatomical locations, bindable to UBERON
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Optional UBERON anatomical entity term reference

```
</details>

### Induced

<details>
```yaml
name: AnatomicalEntityDescriptor
description: A descriptor for anatomical locations, bindable to UBERON
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Optional UBERON anatomical entity term reference
attributes:
  preferred_term:
    name: preferred_term
    description: The preferred human-readable term for this descriptor
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: preferred_term
    owner: AnatomicalEntityDescriptor
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
    owner: AnatomicalEntityDescriptor
    domain_of:
    - Descriptor
    - GeneticContext
    - Dataset
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
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
    range: string
    recommended: false
  term:
    name: term
    description: Optional UBERON anatomical entity term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: AnatomicalEntityDescriptor
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
    owner: AnatomicalEntityDescriptor
    domain_of:
    - Descriptor
    range: ModifierEnum
  located_in:
    name: located_in
    description: Anatomical location where this entity/process occurs or procedure
      is performed
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: located_in
    owner: AnatomicalEntityDescriptor
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
    owner: AnatomicalEntityDescriptor
    domain_of:
    - Descriptor
    range: LateralityEnum
  qualifiers:
    name: qualifiers
    description: List of predicate-value pairs for formal post-composition. Allows
      OWL-like expressivity with controlled predicates (e.g., RO relations) and values.
    deprecated: Prefer explicit slots like located_in and laterality instead of generic
      qualifiers
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: qualifiers
    owner: AnatomicalEntityDescriptor
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>