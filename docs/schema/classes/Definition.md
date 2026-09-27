

# Class: Definition 


_A diagnostic or phenotype definition for the disease_





URI: [dismech:class/Definition](https://w3id.org/monarch-initiative/dismech/class/Definition)





```mermaid
 classDiagram
    class Definition
    click Definition href "../../classes/Definition/"
      Definition : attaches_to
        
      Definition : criteria_sets
        
          
    
        
        
        Definition --> "*" CriteriaSet : criteria_sets
        click CriteriaSet href "../../classes/CriteriaSet/"
    

        
      Definition : definition_type
        
          
    
        
        
        Definition --> "1" DefinitionTypeEnum : definition_type
        click DefinitionTypeEnum href "../../enums/DefinitionTypeEnum/"
    

        
      Definition : derivation_basis
        
          
    
        
        
        Definition --> "0..1" DefinitionDerivationBasisEnum : derivation_basis
        click DefinitionDerivationBasisEnum href "../../enums/DefinitionDerivationBasisEnum/"
    

        
      Definition : description
        
      Definition : evidence
        
          
    
        
        
        Definition --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      Definition : exclusion_criteria
        
          
    
        
        
        Definition --> "*" CriteriaItem : exclusion_criteria
        click CriteriaItem href "../../classes/CriteriaItem/"
    

        
      Definition : inclusion_criteria
        
          
    
        
        
        Definition --> "*" CriteriaItem : inclusion_criteria
        click CriteriaItem href "../../classes/CriteriaItem/"
    

        
      Definition : name
        
      Definition : notes
        
      Definition : scope
        
      Definition : validation_status
        
          
    
        
        
        Definition --> "0..1" AlgorithmValidationStatus : validation_status
        click AlgorithmValidationStatus href "../../classes/AlgorithmValidationStatus/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [definition_type](../slots/definition_type.md) | 1 <br/> [DefinitionTypeEnum](../enums/DefinitionTypeEnum.md) | The type of definition or criteria set | direct |
| [derivation_basis](../slots/derivation_basis.md) | 0..1 <br/> [DefinitionDerivationBasisEnum](../enums/DefinitionDerivationBasisEnum.md) | Epistemic grounding of a definition, orthogonal to definition_type: establish... | direct |
| [validation_status](../slots/validation_status.md) | 0..1 <br/> [AlgorithmValidationStatus](../classes/AlgorithmValidationStatus.md) | Structured validation maturity of a phenotype algorithm / computable case def... | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [scope](../slots/scope.md) | 0..1 <br/> [String](../types/String.md) | Scope or population for which the definition applies (e | direct |
| [attaches_to](../slots/attaches_to.md) | * <br/> [String](../types/String.md) | For a hypothesis-based definition, the pathophysiology node(s)/edge(s) this a... | direct |
| [criteria_sets](../slots/criteria_sets.md) | * <br/> [CriteriaSet](../classes/CriteriaSet.md) | Named criteria groupings within a definition | direct |
| [inclusion_criteria](../slots/inclusion_criteria.md) | * <br/> [CriteriaItem](../classes/CriteriaItem.md) | Inclusion criteria for a definition or criteria set | direct |
| [exclusion_criteria](../slots/exclusion_criteria.md) | * <br/> [CriteriaItem](../classes/CriteriaItem.md) | Exclusion criteria for a definition or criteria set | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [notes](../slots/notes.md) | 0..1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Disease](../classes/Disease.md) | [definitions](../slots/definitions.md) | range | [Definition](../classes/Definition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:Definition |
| native | dismech:Definition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Definition
description: A diagnostic or phenotype definition for the disease
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- definition_type
- derivation_basis
- validation_status
- description
- scope
- attaches_to
- criteria_sets
- inclusion_criteria
- exclusion_criteria
- evidence
- notes
slot_usage:
  name:
    name: name
    required: true
  definition_type:
    name: definition_type
    required: true
  attaches_to:
    name: attaches_to
    description: For a hypothesis-based definition, the pathophysiology node(s)/edge(s)
      this algorithm is predicated on, using the `[<file>:]<kind>#<name>` hash-anchor
      grammar (e.g. `pathophysiology#Fever-triggered CaV1.2 activation`). Lets the
      hypothesis basis be inferred from those edges' `hypothesis_groups` rather than
      duplicated as a standalone id.

```
</details>

### Induced

<details>
```yaml
name: Definition
description: A diagnostic or phenotype definition for the disease
from_schema: https://w3id.org/monarch-initiative/dismech
slot_usage:
  name:
    name: name
    required: true
  definition_type:
    name: definition_type
    required: true
  attaches_to:
    name: attaches_to
    description: For a hypothesis-based definition, the pathophysiology node(s)/edge(s)
      this algorithm is predicated on, using the `[<file>:]<kind>#<name>` hash-anchor
      grammar (e.g. `pathophysiology#Fever-triggered CaV1.2 activation`). Lets the
      hypothesis basis be inferred from those edges' `hypothesis_groups` rather than
      duplicated as a standalone id.
attributes:
  name:
    name: name
    examples:
    - value: Adolescent Nephronophthisis
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    identifier: true
    alias: name
    owner: Definition
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
    - ImagingFinding
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
  definition_type:
    name: definition_type
    description: The type of definition or criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: definition_type
    owner: Definition
    domain_of:
    - Definition
    range: DefinitionTypeEnum
    required: true
  derivation_basis:
    name: derivation_basis
    description: 'Epistemic grounding of a definition, orthogonal to definition_type:
      established criteria vs. a mechanistic hypothesis vs. model-system extrapolation.
      When MECHANISTIC_HYPOTHESIS, the definition should `attaches_to` the pathophysiology
      node(s)/edge(s) it is predicated on, so the hypothesis basis can be inferred
      from those edges'' `hypothesis_groups`.'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: derivation_basis
    owner: Definition
    domain_of:
    - Definition
    range: DefinitionDerivationBasisEnum
  validation_status:
    name: validation_status
    description: Structured validation maturity of a phenotype algorithm / computable
      case definition (a graded status plus a free-text rationale and optional citing
      evidence).
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: validation_status
    owner: Definition
    domain_of:
    - Definition
    range: AlgorithmValidationStatus
    inlined: true
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: Definition
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
    - PhenotypeReadout
    - SurrogateEndpointCollection
    - ProteinStructure
    - ExternalAssertion
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - HistopathologyFinding
    - ImagingFinding
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
  scope:
    name: scope
    description: Scope or population for which the definition applies (e.g., adults,
      pediatrics)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: scope
    owner: Definition
    domain_of:
    - Definition
    - CriteriaSet
    range: string
  attaches_to:
    name: attaches_to
    description: For a hypothesis-based definition, the pathophysiology node(s)/edge(s)
      this algorithm is predicated on, using the `[<file>:]<kind>#<name>` hash-anchor
      grammar (e.g. `pathophysiology#Fever-triggered CaV1.2 activation`). Lets the
      hypothesis basis be inferred from those edges' `hypothesis_groups` rather than
      duplicated as a standalone id.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: attaches_to
    owner: Definition
    domain_of:
    - Definition
    - Discussion
    range: string
    multivalued: true
  criteria_sets:
    name: criteria_sets
    description: Named criteria groupings within a definition
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: criteria_sets
    owner: Definition
    domain_of:
    - Definition
    range: CriteriaSet
    multivalued: true
    inlined: true
    inlined_as_list: true
  inclusion_criteria:
    name: inclusion_criteria
    description: Inclusion criteria for a definition or criteria set
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: inclusion_criteria
    owner: Definition
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
    owner: Definition
    domain_of:
    - Definition
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
    owner: Definition
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
    - PhenotypeReadout
    - ReferenceRange
    - SurrogateEndpoint
    - ExternalAssertion
    - Finding
    - Prevalence
    - GeneCaseFraction
    - ProgressionInfo
    - ClinicalBurden
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - ImagingFinding
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
    - AlgorithmValidationStatus
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
  notes:
    name: notes
    examples:
    - value: Contagious stage where symptoms appear and the bacteria can be spread
        to others.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: notes
    owner: Definition
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
    - GeneCaseFraction
    - ProgressionInfo
    - ClinicalBurden
    - EpidemiologyInfo
    - Pathophysiology
    - Phenotype
    - Biochemical
    - HistopathologyFinding
    - ImagingFinding
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

```
</details>