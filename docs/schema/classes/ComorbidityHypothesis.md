

# Class: ComorbidityHypothesis 


_Mechanistic hypothesis for a comorbidity association, with rich text and embedded evidence plus atomic pathophysiology elements._





URI: [dismech:class/ComorbidityHypothesis](https://w3id.org/monarch-initiative/dismech/class/ComorbidityHypothesis)





```mermaid
 classDiagram
    class ComorbidityHypothesis
    click ComorbidityHypothesis href "../../classes/ComorbidityHypothesis/"
      ComorbidityHypothesis : description
        
      ComorbidityHypothesis : evidence
        
          
    
        
        
        ComorbidityHypothesis --> "* _recommended_" EvidenceItem : evidence
        click EvidenceItem href "../../classes/EvidenceItem/"
    

        
      ComorbidityHypothesis : pathophysiology
        
          
    
        
        
        ComorbidityHypothesis --> "*" Pathophysiology : pathophysiology
        click Pathophysiology href "../../classes/Pathophysiology/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [evidence](../slots/evidence.md) | * _recommended_ <br/> [EvidenceItem](../classes/EvidenceItem.md) |  | direct |
| [pathophysiology](../slots/pathophysiology.md) | * <br/> [Pathophysiology](../classes/Pathophysiology.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComorbidityAssociation](../classes/ComorbidityAssociation.md) | [hypotheses](../slots/hypotheses.md) | range | [ComorbidityHypothesis](../classes/ComorbidityHypothesis.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ComorbidityHypothesis |
| native | dismech:ComorbidityHypothesis |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ComorbidityHypothesis
description: Mechanistic hypothesis for a comorbidity association, with rich text
  and embedded evidence plus atomic pathophysiology elements.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- description
- evidence
- pathophysiology

```
</details>

### Induced

<details>
```yaml
name: ComorbidityHypothesis
description: Mechanistic hypothesis for a comorbidity association, with rich text
  and embedded evidence plus atomic pathophysiology elements.
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: ComorbidityHypothesis
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
  evidence:
    name: evidence
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: ComorbidityHypothesis
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
  pathophysiology:
    name: pathophysiology
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: pathophysiology
    owner: ComorbidityHypothesis
    domain_of:
    - Disease
    - Stage
    - ComorbidityHypothesis
    range: Pathophysiology
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>