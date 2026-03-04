

# Class: SampleTypeDescriptor 


_A descriptor for biological sample types (tissue and/or cell type)_





URI: [dismech:SampleTypeDescriptor](https://w3id.org/monarch-initiative/dismech/SampleTypeDescriptor)





```mermaid
 classDiagram
    class SampleTypeDescriptor
    click SampleTypeDescriptor href "../SampleTypeDescriptor/"
      Descriptor <|-- SampleTypeDescriptor
        click Descriptor href "../Descriptor/"
      
      SampleTypeDescriptor : cell_type_term
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" CellTypeDescriptor : cell_type_term
        click CellTypeDescriptor href "../CellTypeDescriptor/"
    

        
      SampleTypeDescriptor : description
        
      SampleTypeDescriptor : laterality
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../LateralityEnum/"
    

        
      SampleTypeDescriptor : located_in
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../AnatomicalEntityDescriptor/"
    

        
      SampleTypeDescriptor : modifier
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../ModifierEnum/"
    

        
      SampleTypeDescriptor : preferred_term
        
      SampleTypeDescriptor : qualifiers
        
          
    
        
        
        SampleTypeDescriptor --> "*" Qualifier : qualifiers
        click Qualifier href "../Qualifier/"
    

        
      SampleTypeDescriptor : term
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" Term : term
        click Term href "../Term/"
    

        
      SampleTypeDescriptor : tissue_term
        
          
    
        
        
        SampleTypeDescriptor --> "0..1" AnatomicalEntityDescriptor : tissue_term
        click AnatomicalEntityDescriptor href "../AnatomicalEntityDescriptor/"
    

        
      
```





## Inheritance
* [Descriptor](Descriptor.md)
    * **SampleTypeDescriptor**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [tissue_term](tissue_term.md) | 0..1 <br/> [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | UBERON term for the tissue | direct |
| [cell_type_term](cell_type_term.md) | 0..1 <br/> [CellTypeDescriptor](CellTypeDescriptor.md) | CL term for the cell type | direct |
| [preferred_term](preferred_term.md) | 1 <br/> [String](String.md) | The preferred human-readable term for this descriptor | [Descriptor](Descriptor.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A description of the descriptor | [Descriptor](Descriptor.md) |
| [term](term.md) | 0..1 _recommended_ <br/> [Term](Term.md) | Optional structured ontology term reference | [Descriptor](Descriptor.md) |
| [modifier](modifier.md) | 0..1 <br/> [ModifierEnum](ModifierEnum.md) | Directional or qualitative modifier for a descriptor (e | [Descriptor](Descriptor.md) |
| [located_in](located_in.md) | 0..1 <br/> [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) | Anatomical location where this entity/process occurs or procedure is performe... | [Descriptor](Descriptor.md) |
| [laterality](laterality.md) | 0..1 <br/> [LateralityEnum](LateralityEnum.md) | Laterality qualifier (left, right, or bilateral) | [Descriptor](Descriptor.md) |
| [qualifiers](qualifiers.md) | * <br/> [Qualifier](Qualifier.md) | List of predicate-value pairs for formal post-composition | [Descriptor](Descriptor.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [sample_types](sample_types.md) | range | [SampleTypeDescriptor](SampleTypeDescriptor.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:SampleTypeDescriptor |
| native | dismech:SampleTypeDescriptor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SampleTypeDescriptor
description: A descriptor for biological sample types (tissue and/or cell type)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slots:
- tissue_term
- cell_type_term

```
</details>

### Induced

<details>
```yaml
name: SampleTypeDescriptor
description: A descriptor for biological sample types (tissue and/or cell type)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
attributes:
  tissue_term:
    name: tissue_term
    description: UBERON term for the tissue
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: tissue_term
    owner: SampleTypeDescriptor
    domain_of:
    - SampleTypeDescriptor
    range: AnatomicalEntityDescriptor
    inlined: true
  cell_type_term:
    name: cell_type_term
    description: CL term for the cell type
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: cell_type_term
    owner: SampleTypeDescriptor
    domain_of:
    - SampleTypeDescriptor
    range: CellTypeDescriptor
    inlined: true
  preferred_term:
    name: preferred_term
    description: The preferred human-readable term for this descriptor
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: preferred_term
    owner: SampleTypeDescriptor
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
    owner: SampleTypeDescriptor
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
    description: Optional structured ontology term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: SampleTypeDescriptor
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
    owner: SampleTypeDescriptor
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
    owner: SampleTypeDescriptor
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
    owner: SampleTypeDescriptor
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
    owner: SampleTypeDescriptor
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>