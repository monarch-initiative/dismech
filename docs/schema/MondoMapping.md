

# Class: MondoMapping 


_MONDO disease ontology mapping_





URI: [dismech:MondoMapping](https://w3id.org/monarch-initiative/dismech/MondoMapping)





```mermaid
 classDiagram
    class MondoMapping
    click MondoMapping href "../MondoMapping/"
      TermMapping <|-- MondoMapping
        click TermMapping href "../TermMapping/"
      
      MondoMapping : consistency
        
          
    
        
        
        MondoMapping --> "*" MappingConsistency : consistency
        click MappingConsistency href "../MappingConsistency/"
    

        
      MondoMapping : mapping_justification
        
      MondoMapping : mapping_predicate
        
      MondoMapping : mapping_source
        
      MondoMapping : notes
        
      MondoMapping : term
        
          
    
        
        
        MondoMapping --> "1" Term : term
        click Term href "../Term/"
    

        
      
```





## Inheritance
* [TermMapping](TermMapping.md)
    * **MondoMapping**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [term](term.md) | 1 _recommended_ <br/> [Term](Term.md) | Optional structured ontology term reference | [TermMapping](TermMapping.md) |
| [mapping_predicate](mapping_predicate.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Relationship between this disease and the mapped term (e | [TermMapping](TermMapping.md) |
| [mapping_source](mapping_source.md) | 0..1 <br/> [String](String.md) | Source of the mapping (e | [TermMapping](TermMapping.md) |
| [mapping_justification](mapping_justification.md) | 0..1 <br/> [String](String.md) | Brief rationale or justification for the mapping | [TermMapping](TermMapping.md) |
| [consistency](consistency.md) | * <br/> [MappingConsistency](MappingConsistency.md) | Consistency assertions for this mapping against other sources | [TermMapping](TermMapping.md) |
| [notes](notes.md) | 0..1 <br/> [String](String.md) |  | [TermMapping](TermMapping.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseMappings](DiseaseMappings.md) | [mondo_mappings](mondo_mappings.md) | range | [MondoMapping](MondoMapping.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:MondoMapping |
| native | dismech:MondoMapping |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MondoMapping
description: MONDO disease ontology mapping
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: TermMapping
slot_usage:
  term:
    name: term
    bindings:
    - range: DiseaseTerm
      obligation_level: REQUIRED
      binds_value_of: id

```
</details>

### Induced

<details>
```yaml
name: MondoMapping
description: MONDO disease ontology mapping
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: TermMapping
slot_usage:
  term:
    name: term
    bindings:
    - range: DiseaseTerm
      obligation_level: REQUIRED
      binds_value_of: id
attributes:
  term:
    name: term
    description: Optional structured ontology term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: MondoMapping
    domain_of:
    - Descriptor
    - TermMapping
    - ConditionDescriptor
    - GOEnrichmentTerm
    range: Term
    bindings:
    - range: DiseaseTerm
      obligation_level: REQUIRED
      binds_value_of: id
    required: true
    recommended: true
    inlined: true
  mapping_predicate:
    name: mapping_predicate
    description: Relationship between this disease and the mapped term (e.g., skos:exactMatch)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mapping_predicate
    owner: MondoMapping
    domain_of:
    - TermMapping
    range: uriorcurie
    required: true
  mapping_source:
    name: mapping_source
    description: Source of the mapping (e.g., MONDO, ICD-10-CM, manual curation)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mapping_source
    owner: MondoMapping
    domain_of:
    - TermMapping
    range: string
  mapping_justification:
    name: mapping_justification
    description: Brief rationale or justification for the mapping
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mapping_justification
    owner: MondoMapping
    domain_of:
    - TermMapping
    range: string
  consistency:
    name: consistency
    description: Consistency assertions for this mapping against other sources
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: consistency
    owner: MondoMapping
    domain_of:
    - TermMapping
    range: MappingConsistency
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
    owner: MondoMapping
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