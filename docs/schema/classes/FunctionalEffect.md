

# Class: FunctionalEffect 



URI: [dismech:class/FunctionalEffect](https://w3id.org/monarch-initiative/dismech/class/FunctionalEffect)





```mermaid
 classDiagram
    class FunctionalEffect
    click FunctionalEffect href "../../classes/FunctionalEffect/"
      FunctionalEffect : description
        
      FunctionalEffect : function
        
      FunctionalEffect : type
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [function](../slots/function.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [type](../slots/type.md) | 0..1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Variant](../classes/Variant.md) | [functional_effects](../slots/functional_effects.md) | range | [FunctionalEffect](../classes/FunctionalEffect.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:FunctionalEffect |
| native | dismech:FunctionalEffect |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FunctionalEffect
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- function
- description
- type

```
</details>

### Induced

<details>
```yaml
name: FunctionalEffect
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  function:
    name: function
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: function
    owner: FunctionalEffect
    domain_of:
    - FunctionalEffect
    range: string
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: FunctionalEffect
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
  type:
    name: type
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: type
    owner: FunctionalEffect
    domain_of:
    - Variant
    - FunctionalEffect
    range: string

```
</details>