

# Class: InfectiousAgent 



URI: [dismech:class/InfectiousAgent](https://w3id.org/monarch-initiative/dismech/class/InfectiousAgent)





```mermaid
 classDiagram
    class InfectiousAgent
    click InfectiousAgent href "../../classes/InfectiousAgent/"
      InfectiousAgent : description
        
      InfectiousAgent : evidence
        
          
    
        
        
        InfectiousAgent --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      InfectiousAgent : food_source
        
          
    
        
        
        InfectiousAgent --> "0..1" FoodDescriptor : food_source
        click FoodDescriptor href "../../classes/FoodDescriptor/"
    

        
      InfectiousAgent : has_subtypes
        
          
    
        
        
        InfectiousAgent --> "*" Subtype : has_subtypes
        click Subtype href "../../classes/Subtype/"
    

        
      InfectiousAgent : infectious_agent_term
        
          
    
        
        
        InfectiousAgent --> "0..1" OrganismDescriptor : infectious_agent_term
        click OrganismDescriptor href "../../classes/OrganismDescriptor/"
    

        
      InfectiousAgent : name
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [infectious_agent_term](../slots/infectious_agent_term.md) | 0..1 <br/> [OrganismDescriptor](../classes/OrganismDescriptor.md) | The NCBITaxon term for this infectious agent | direct |
| [food_source](../slots/food_source.md) | 0..1 <br/> [FoodDescriptor](../classes/FoodDescriptor.md) | The FOODON or CHEBI term for a specific food, beverage, nutrient, mineral, or... | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [has_subtypes](../slots/has_subtypes.md) | * <br/> [Subtype](../classes/Subtype.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Disease](../classes/Disease.md) | [infectious_agent](../slots/infectious_agent.md) | range | [InfectiousAgent](../classes/InfectiousAgent.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:InfectiousAgent |
| native | dismech:InfectiousAgent |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InfectiousAgent
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- name
- infectious_agent_term
- food_source
- evidence
- description
- has_subtypes

```
</details>

### Induced

<details>
```yaml
name: InfectiousAgent
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
    owner: InfectiousAgent
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
  infectious_agent_term:
    name: infectious_agent_term
    description: The NCBITaxon term for this infectious agent
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: infectious_agent_term
    owner: InfectiousAgent
    domain_of:
    - InfectiousAgent
    range: OrganismDescriptor
    inlined: true
  food_source:
    name: food_source
    description: The FOODON or CHEBI term for a specific food, beverage, nutrient,
      mineral, or supplement source or vehicle relevant to an exposure
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: food_source
    owner: InfectiousAgent
    domain_of:
    - Environmental
    - InfectiousAgent
    range: FoodDescriptor
    inlined: true
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: InfectiousAgent
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
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: InfectiousAgent
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
  has_subtypes:
    name: has_subtypes
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: has_subtypes
    owner: InfectiousAgent
    domain_of:
    - Disease
    - InfectiousAgent
    range: Subtype
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>