

# Class: CriteriaItem 


_A criterion element (clinical feature, test result, imaging requirement)_





URI: [dismech:CriteriaItem](https://w3id.org/monarch-initiative/dismech/CriteriaItem)





```mermaid
 classDiagram
    class CriteriaItem
    click CriteriaItem href "../CriteriaItem/"
      Descriptor <|-- CriteriaItem
        click Descriptor href "../Descriptor/"
      
      CriteriaItem : description
        
      CriteriaItem : laterality
        
          
    
        
        
        CriteriaItem --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../LateralityEnum/"
    

        
      CriteriaItem : located_in
        
          
    
        
        
        CriteriaItem --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../AnatomicalEntityDescriptor/"
    

        
      CriteriaItem : modifier
        
          
    
        
        
        CriteriaItem --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../ModifierEnum/"
    

        
      CriteriaItem : preferred_term
        
      CriteriaItem : qualifiers
        
          
    
        
        
        CriteriaItem --> "*" Qualifier : qualifiers
        click Qualifier href "../Qualifier/"
    

        
      CriteriaItem : term
        
          
    
        
        
        CriteriaItem --> "0..1" Term : term
        click Term href "../Term/"
    

        
      
```





## Inheritance
* [Descriptor](Descriptor.md)
    * **CriteriaItem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
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
| [Definition](Definition.md) | [inclusion_criteria](inclusion_criteria.md) | range | [CriteriaItem](CriteriaItem.md) |
| [Definition](Definition.md) | [exclusion_criteria](exclusion_criteria.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [core_clinical_characteristics](core_clinical_characteristics.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [inclusion_criteria](inclusion_criteria.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [exclusion_criteria](exclusion_criteria.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [imaging_requirements](imaging_requirements.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [laboratory_requirements](laboratory_requirements.md) | range | [CriteriaItem](CriteriaItem.md) |
| [CriteriaSet](CriteriaSet.md) | [additional_requirements](additional_requirements.md) | range | [CriteriaItem](CriteriaItem.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:CriteriaItem |
| native | dismech:CriteriaItem |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriteriaItem
description: A criterion element (clinical feature, test result, imaging requirement)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor

```
</details>

### Induced

<details>
```yaml
name: CriteriaItem
description: A criterion element (clinical feature, test result, imaging requirement)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
attributes:
  preferred_term:
    name: preferred_term
    description: The preferred human-readable term for this descriptor
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: preferred_term
    owner: CriteriaItem
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
    owner: CriteriaItem
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
    owner: CriteriaItem
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
    owner: CriteriaItem
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
    owner: CriteriaItem
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
    owner: CriteriaItem
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
    owner: CriteriaItem
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>