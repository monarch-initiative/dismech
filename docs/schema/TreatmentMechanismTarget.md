

# Class: TreatmentMechanismTarget 


_Links a treatment to a specific pathophysiology mechanism node it targets. Enables reasoning about which downstream phenotypes should respond to therapy and why resistance may emerge when the causal chain shifts._





URI: [dismech:TreatmentMechanismTarget](https://w3id.org/monarch-initiative/dismech/TreatmentMechanismTarget)





```mermaid
 classDiagram
    class TreatmentMechanismTarget
    click TreatmentMechanismTarget href "../TreatmentMechanismTarget/"
      TreatmentMechanismTarget : description
        
      TreatmentMechanismTarget : evidence
        
          
    
        
        
        TreatmentMechanismTarget --> "*" EvidenceItem : evidence
        click EvidenceItem href "../EvidenceItem/"
    

        
      TreatmentMechanismTarget : target
        
      TreatmentMechanismTarget : treatment_effect
        
          
    
        
        
        TreatmentMechanismTarget --> "0..1" TreatmentEffectEnum : treatment_effect
        click TreatmentEffectEnum href "../TreatmentEffectEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [target](target.md) | 1 <br/> [String](String.md) | Name of the pathophysiology entry this treatment targets | direct |
| [treatment_effect](treatment_effect.md) | 0..1 <br/> [TreatmentEffectEnum](TreatmentEffectEnum.md) | How the treatment affects the targeted mechanism | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [evidence](evidence.md) | * _recommended_ <br/> [EvidenceItem](EvidenceItem.md) | Evidence that this treatment targets this specific mechanism | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Treatment](Treatment.md) | [target_mechanisms](target_mechanisms.md) | range | [TreatmentMechanismTarget](TreatmentMechanismTarget.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:TreatmentMechanismTarget |
| native | dismech:TreatmentMechanismTarget |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TreatmentMechanismTarget
description: Links a treatment to a specific pathophysiology mechanism node it targets.
  Enables reasoning about which downstream phenotypes should respond to therapy and
  why resistance may emerge when the causal chain shifts.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- target
- treatment_effect
- description
- evidence
slot_usage:
  target:
    name: target
    description: Name of the pathophysiology entry this treatment targets. Must match
      a pathophysiology name in the same disease file.
  evidence:
    name: evidence
    description: Evidence that this treatment targets this specific mechanism

```
</details>

### Induced

<details>
```yaml
name: TreatmentMechanismTarget
description: Links a treatment to a specific pathophysiology mechanism node it targets.
  Enables reasoning about which downstream phenotypes should respond to therapy and
  why resistance may emerge when the causal chain shifts.
from_schema: https://w3id.org/monarch-initiative/dismech
slot_usage:
  target:
    name: target
    description: Name of the pathophysiology entry this treatment targets. Must match
      a pathophysiology name in the same disease file.
  evidence:
    name: evidence
    description: Evidence that this treatment targets this specific mechanism
attributes:
  target:
    name: target
    description: Name of the pathophysiology entry this treatment targets. Must match
      a pathophysiology name in the same disease file.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: target
    owner: TreatmentMechanismTarget
    domain_of:
    - CausalEdge
    - TreatmentMechanismTarget
    range: string
    required: true
  treatment_effect:
    name: treatment_effect
    description: How the treatment affects the targeted mechanism
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: treatment_effect
    owner: TreatmentMechanismTarget
    domain_of:
    - TreatmentMechanismTarget
    range: TreatmentEffectEnum
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: TreatmentMechanismTarget
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
    description: Evidence that this treatment targets this specific mechanism
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: evidence
    owner: TreatmentMechanismTarget
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