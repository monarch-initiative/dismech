

# Class: GOEnrichment 


_GO enrichment results for an association signal._





URI: [dismech:GOEnrichment](https://w3id.org/monarch-initiative/dismech/GOEnrichment)





```mermaid
 classDiagram
    class GOEnrichment
    click GOEnrichment href "../GOEnrichment/"
      GOEnrichment : description
        
      GOEnrichment : go_terms
        
          
    
        
        
        GOEnrichment --> "*" GOEnrichmentTerm : go_terms
        click GOEnrichmentTerm href "../GOEnrichmentTerm/"
    

        
      GOEnrichment : method
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [method](method.md) | 0..1 <br/> [String](String.md) | Method or pipeline name | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [go_terms](go_terms.md) | * <br/> [GOEnrichmentTerm](GOEnrichmentTerm.md) | GO term enrichment results | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [AssociationSignal](AssociationSignal.md) | [go_enrichment](go_enrichment.md) | range | [GOEnrichment](GOEnrichment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:GOEnrichment |
| native | dismech:GOEnrichment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GOEnrichment
description: GO enrichment results for an association signal.
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- method
- description
- go_terms

```
</details>

### Induced

<details>
```yaml
name: GOEnrichment
description: GO enrichment results for an association signal.
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  method:
    name: method
    description: Method or pipeline name
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: method
    owner: GOEnrichment
    domain_of:
    - AssociationSignal
    - GOEnrichment
    range: string
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: GOEnrichment
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
  go_terms:
    name: go_terms
    description: GO term enrichment results
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: go_terms
    owner: GOEnrichment
    domain_of:
    - GOEnrichment
    range: GOEnrichmentTerm
    multivalued: true
    inlined: true
    inlined_as_list: true

```
</details>