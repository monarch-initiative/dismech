

# Class: CriteriaSet 


_A named criteria grouping within a definition_





URI: [dismech:CriteriaSet](https://w3id.org/monarch-initiative/dismech/CriteriaSet)





```mermaid
 classDiagram
    class CriteriaSet
    click CriteriaSet href "../CriteriaSet/"
      CriteriaSet : additional_requirements
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : additional_requirements
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : core_clinical_characteristics
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : core_clinical_characteristics
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : description
        
      CriteriaSet : evidence
        
          
    
        
        
        CriteriaSet --> "*" EvidenceItem : evidence
        click EvidenceItem href "../EvidenceItem/"
    

        
      CriteriaSet : exclusion_criteria
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : exclusion_criteria
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : imaging_requirements
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : imaging_requirements
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : inclusion_criteria
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : inclusion_criteria
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : laboratory_requirements
        
          
    
        
        
        CriteriaSet --> "*" CriteriaItem : laboratory_requirements
        click CriteriaItem href "../CriteriaItem/"
    

        
      CriteriaSet : minimum_required
        
      CriteriaSet : name
        
      CriteriaSet : notes
        
      CriteriaSet : scope
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [scope](scope.md) | 0..1 <br/> [String](String.md) | Scope or population for which the definition applies (e | direct |
| [minimum_required](minimum_required.md) | 0..1 <br/> [Integer](Integer.md) | Minimum number of criteria required in this criteria set | direct |
| [core_clinical_characteristics](core_clinical_characteristics.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Core clinical characteristics used in a criteria set | direct |
| [inclusion_criteria](inclusion_criteria.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Inclusion criteria for a definition or criteria set | direct |
| [exclusion_criteria](exclusion_criteria.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Exclusion criteria for a definition or criteria set | direct |
| [imaging_requirements](imaging_requirements.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Imaging requirements used in a criteria set | direct |
| [laboratory_requirements](laboratory_requirements.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Laboratory or serologic requirements used in a criteria set | direct |
| [additional_requirements](additional_requirements.md) | * <br/> [CriteriaItem](CriteriaItem.md) | Additional requirements used in a criteria set | direct |
| [evidence](evidence.md) | * _recommended_ <br/> [EvidenceItem](EvidenceItem.md) |  | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Definition](Definition.md) | [criteria_sets](criteria_sets.md) | range | [CriteriaSet](CriteriaSet.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:CriteriaSet |
| native | dismech:CriteriaSet |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriteriaSet
description: A named criteria grouping within a definition
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- description
- scope
- minimum_required
- core_clinical_characteristics
- inclusion_criteria
- exclusion_criteria
- imaging_requirements
- laboratory_requirements
- additional_requirements
- evidence
- notes
slot_usage:
  name:
    name: name
    required: true

```
</details>

### Induced

<details>
```yaml
name: CriteriaSet
description: A named criteria grouping within a definition
from_schema: https://w3id.org/monarch-initiative/dismech
slot_usage:
  name:
    name: name
    required: true
attributes:
  name:
    name: name
    examples:
    - value: Adolescent Nephronophthisis
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    identifier: true
    alias: name
    owner: CriteriaSet
    domain_of:
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
    - Subtype
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
    range: string
    required: true
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: CriteriaSet
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
  scope:
    name: scope
    description: Scope or population for which the definition applies (e.g., adults,
      pediatrics)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: scope
    owner: CriteriaSet
    domain_of:
    - Definition
    - CriteriaSet
    range: string
  minimum_required:
    name: minimum_required
    description: Minimum number of criteria required in this criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: minimum_required
    owner: CriteriaSet
    domain_of:
    - CriteriaSet
    range: integer
  core_clinical_characteristics:
    name: core_clinical_characteristics
    description: Core clinical characteristics used in a criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: core_clinical_characteristics
    owner: CriteriaSet
    domain_of:
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  inclusion_criteria:
    name: inclusion_criteria
    description: Inclusion criteria for a definition or criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: inclusion_criteria
    owner: CriteriaSet
    domain_of:
    - Definition
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  exclusion_criteria:
    name: exclusion_criteria
    description: Exclusion criteria for a definition or criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: exclusion_criteria
    owner: CriteriaSet
    domain_of:
    - Definition
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  imaging_requirements:
    name: imaging_requirements
    description: Imaging requirements used in a criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: imaging_requirements
    owner: CriteriaSet
    domain_of:
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  laboratory_requirements:
    name: laboratory_requirements
    description: Laboratory or serologic requirements used in a criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: laboratory_requirements
    owner: CriteriaSet
    domain_of:
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  additional_requirements:
    name: additional_requirements
    description: Additional requirements used in a criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: additional_requirements
    owner: CriteriaSet
    domain_of:
    - CriteriaSet
    range: CriteriaItem
    multivalued: true
    inlined: true
    inlined_as_list: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: CriteriaSet
    domain_of:
    - PhenotypeContext
    - Dataset
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
    - Subtype
    - CausalEdge
    - TreatmentMechanismTarget
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
    owner: CriteriaSet
    domain_of:
    - GeneticContext
    - OnsetDescriptor
    - PhenotypeContext
    - Dataset
    - ClinicalTrial
    - ComputationalModel
    - DifferentialDiagnosis
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
    range: string

```
</details>