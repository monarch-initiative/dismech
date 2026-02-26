

# Class: UpstreamConditionHypothesis 


_Hypothesized upstream condition that may explain both A and B._





URI: [dismech:UpstreamConditionHypothesis](https://w3id.org/monarch-initiative/dismech/UpstreamConditionHypothesis)





```mermaid
 classDiagram
    class UpstreamConditionHypothesis
    click UpstreamConditionHypothesis href "../UpstreamConditionHypothesis/"
      UpstreamConditionHypothesis : description
        
      UpstreamConditionHypothesis : evidence
        
          
    
        
        
        UpstreamConditionHypothesis --> "*" EvidenceItem : evidence
        click EvidenceItem href "../EvidenceItem/"
    

        
      UpstreamConditionHypothesis : upstream_disorder
        
          
    
        
        
        UpstreamConditionHypothesis --> "0..1" ConditionDescriptor : upstream_disorder
        click ConditionDescriptor href "../ConditionDescriptor/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [upstream_disorder](upstream_disorder.md) | 0..1 <br/> [ConditionDescriptor](ConditionDescriptor.md) | Upstream disorder referenced in a hypothesis | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [evidence](evidence.md) | * _recommended_ <br/> [EvidenceItem](EvidenceItem.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComorbidityAssociation](ComorbidityAssociation.md) | [shared_upstream_hypotheses](shared_upstream_hypotheses.md) | range | [UpstreamConditionHypothesis](UpstreamConditionHypothesis.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:UpstreamConditionHypothesis |
| native | dismech:UpstreamConditionHypothesis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: UpstreamConditionHypothesis
description: Hypothesized upstream condition that may explain both A and B.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- upstream_disorder
- description
- evidence

```
</details>

### Induced

<details>
```yaml
name: UpstreamConditionHypothesis
description: Hypothesized upstream condition that may explain both A and B.
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  upstream_disorder:
    name: upstream_disorder
    description: Upstream disorder referenced in a hypothesis
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: upstream_disorder
    owner: UpstreamConditionHypothesis
    domain_of:
    - UpstreamConditionHypothesis
    range: ConditionDescriptor
    inlined: true
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: UpstreamConditionHypothesis
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
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: UpstreamConditionHypothesis
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

```
</details>