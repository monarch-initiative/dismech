

# Class: TreatmentDescriptor 


_A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)_





URI: [dismech:class/TreatmentDescriptor](https://w3id.org/monarch-initiative/dismech/class/TreatmentDescriptor)





```mermaid
 classDiagram
    class TreatmentDescriptor
    click TreatmentDescriptor href "../../classes/TreatmentDescriptor/"
      Descriptor <|-- TreatmentDescriptor
        click Descriptor href "../../classes/Descriptor/"
      
      TreatmentDescriptor : description
        
      TreatmentDescriptor : laterality
        
          
    
        
        
        TreatmentDescriptor --> "0..1" LateralityEnum : laterality
        click LateralityEnum href "../../enums/LateralityEnum/"
    

        
      TreatmentDescriptor : located_in
        
          
    
        
        
        TreatmentDescriptor --> "0..1" AnatomicalEntityDescriptor : located_in
        click AnatomicalEntityDescriptor href "../../classes/AnatomicalEntityDescriptor/"
    

        
      TreatmentDescriptor : modifier
        
          
    
        
        
        TreatmentDescriptor --> "0..1" ModifierEnum : modifier
        click ModifierEnum href "../../enums/ModifierEnum/"
    

        
      TreatmentDescriptor : preferred_term
        
      TreatmentDescriptor : qualifiers
        
          
    
        
        
        TreatmentDescriptor --> "*" Qualifier : qualifiers
        click Qualifier href "../../classes/Qualifier/"
    

        
      TreatmentDescriptor : term
        
          
    
        
        
        TreatmentDescriptor --> "0..1 _recommended_" Term : term
        click Term href "../../classes/Term/"
    

        
      TreatmentDescriptor : therapeutic_agent
        
          
    
        
        
        TreatmentDescriptor --> "*" ChemicalEntityDescriptor : therapeutic_agent
        click ChemicalEntityDescriptor href "../../classes/ChemicalEntityDescriptor/"
    

        
      
```





## Inheritance
* [Descriptor](../classes/Descriptor.md)
    * **TreatmentDescriptor**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [therapeutic_agent](../slots/therapeutic_agent.md) | * <br/> [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) | The drug(s) or chemical agent(s) used in this treatment | direct |
| [preferred_term](../slots/preferred_term.md) | 1 <br/> [String](../types/String.md) | The preferred human-readable term for this descriptor | [Descriptor](../classes/Descriptor.md) |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) | A description of the descriptor | [Descriptor](../classes/Descriptor.md) |
| [term](../slots/term.md) | 0..1 _recommended_ <br/> [Term](../classes/Term.md) | Optional MAXO treatment term reference | [Descriptor](../classes/Descriptor.md) |
| [modifier](../slots/modifier.md) | 0..1 <br/> [ModifierEnum](../enums/ModifierEnum.md) | Directional or qualitative modifier for a descriptor (e | [Descriptor](../classes/Descriptor.md) |
| [located_in](../slots/located_in.md) | 0..1 <br/> [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | Anatomical location where this entity/process occurs or procedure is performe... | [Descriptor](../classes/Descriptor.md) |
| [laterality](../slots/laterality.md) | 0..1 <br/> [LateralityEnum](../enums/LateralityEnum.md) | Laterality qualifier (left, right, or bilateral) | [Descriptor](../classes/Descriptor.md) |
| [qualifiers](../slots/qualifiers.md) | * <br/> [Qualifier](../classes/Qualifier.md) | List of predicate-value pairs for formal post-composition | [Descriptor](../classes/Descriptor.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Treatment](../classes/Treatment.md) | [treatment_term](../slots/treatment_term.md) | range | [TreatmentDescriptor](../classes/TreatmentDescriptor.md) |
| [Diagnosis](../classes/Diagnosis.md) | [diagnosis_term](../slots/diagnosis_term.md) | range | [TreatmentDescriptor](../classes/TreatmentDescriptor.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:TreatmentDescriptor |
| native | dismech:TreatmentDescriptor |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TreatmentDescriptor
description: A descriptor for treatments/medical actions, bindable to Medical Action
  Ontology (MAXO)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slots:
- therapeutic_agent
slot_usage:
  term:
    name: term
    description: Optional MAXO treatment term reference
    bindings:
    - range: TreatmentActionTerm
      obligation_level: REQUIRED
      binds_value_of: id
  therapeutic_agent:
    name: therapeutic_agent
    description: The drug(s) or chemical agent(s) used in this treatment. Use when
      the MAXO term is generic (e.g., pharmacotherapy MAXO:0000058) but specific drugs
      are involved.
    comments:
    - Prefer CHEBI terms for specific drugs (e.g., CHEBI:15365 for aspirin)
    - Use NCIT for drug classes when specific CHEBI term unavailable

```
</details>

### Induced

<details>
```yaml
name: TreatmentDescriptor
description: A descriptor for treatments/medical actions, bindable to Medical Action
  Ontology (MAXO)
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: Descriptor
slot_usage:
  term:
    name: term
    description: Optional MAXO treatment term reference
    bindings:
    - range: TreatmentActionTerm
      obligation_level: REQUIRED
      binds_value_of: id
  therapeutic_agent:
    name: therapeutic_agent
    description: The drug(s) or chemical agent(s) used in this treatment. Use when
      the MAXO term is generic (e.g., pharmacotherapy MAXO:0000058) but specific drugs
      are involved.
    comments:
    - Prefer CHEBI terms for specific drugs (e.g., CHEBI:15365 for aspirin)
    - Use NCIT for drug classes when specific CHEBI term unavailable
attributes:
  therapeutic_agent:
    name: therapeutic_agent
    description: The drug(s) or chemical agent(s) used in this treatment. Use when
      the MAXO term is generic (e.g., pharmacotherapy MAXO:0000058) but specific drugs
      are involved.
    comments:
    - Prefer CHEBI terms for specific drugs (e.g., CHEBI:15365 for aspirin)
    - Use NCIT for drug classes when specific CHEBI term unavailable
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: therapeutic_agent
    owner: TreatmentDescriptor
    domain_of:
    - TreatmentDescriptor
    range: ChemicalEntityDescriptor
    multivalued: true
    inlined: true
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
    owner: TreatmentDescriptor
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
    owner: TreatmentDescriptor
    domain_of:
    - Descriptor
    - GeneticContext
    - Dataset
    - ClinicalTrial
    - ComputationalModel
    - ModelVariable
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
    - ProteinStructure
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
    description: Optional MAXO treatment term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: TreatmentDescriptor
    domain_of:
    - Descriptor
    - TermMapping
    - ConditionDescriptor
    - GOEnrichmentTerm
    range: Term
    bindings:
    - range: TreatmentActionTerm
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
    owner: TreatmentDescriptor
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
    owner: TreatmentDescriptor
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
    owner: TreatmentDescriptor
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
    owner: TreatmentDescriptor
    domain_of:
    - Descriptor
    range: Qualifier
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>