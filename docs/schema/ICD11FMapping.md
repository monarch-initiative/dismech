

# Class: ICD11FMapping 


_ICD-11 Foundation diagnosis code mapping_





URI: [dismech:ICD11FMapping](https://w3id.org/monarch-initiative/dismech/ICD11FMapping)





```mermaid
 classDiagram
    class ICD11FMapping
    click ICD11FMapping href "../ICD11FMapping/"
      TermMapping <|-- ICD11FMapping
        click TermMapping href "../TermMapping/"
      
      ICD11FMapping : consistency
        
          
    
        
        
        ICD11FMapping --> "*" MappingConsistency : consistency
        click MappingConsistency href "../MappingConsistency/"
    

        
      ICD11FMapping : mapping_justification
        
      ICD11FMapping : mapping_predicate
        
      ICD11FMapping : mapping_source
        
      ICD11FMapping : notes
        
      ICD11FMapping : term
        
          
    
        
        
        ICD11FMapping --> "1" Term : term
        click Term href "../Term/"
    

        
      
```





## Inheritance
* [TermMapping](TermMapping.md)
    * **ICD11FMapping**



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
| [DiseaseMappings](DiseaseMappings.md) | [icd11f_mappings](icd11f_mappings.md) | range | [ICD11FMapping](ICD11FMapping.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:ICD11FMapping |
| native | dismech:ICD11FMapping |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ICD11FMapping
description: ICD-11 Foundation diagnosis code mapping
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: TermMapping
slot_usage:
  term:
    name: term
    bindings:
    - range: ICD11FTerm
      obligation_level: REQUIRED
      binds_value_of: id

```
</details>

### Induced

<details>
```yaml
name: ICD11FMapping
description: ICD-11 Foundation diagnosis code mapping
from_schema: https://w3id.org/monarch-initiative/dismech
is_a: TermMapping
slot_usage:
  term:
    name: term
    bindings:
    - range: ICD11FTerm
      obligation_level: REQUIRED
      binds_value_of: id
attributes:
  term:
    name: term
    description: Optional structured ontology term reference
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: term
    owner: ICD11FMapping
    domain_of:
    - Descriptor
    - TermMapping
    - ConditionDescriptor
    - GOEnrichmentTerm
    range: Term
    bindings:
    - range: ICD11FTerm
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
    owner: ICD11FMapping
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
    owner: ICD11FMapping
    domain_of:
    - TermMapping
    range: string
  mapping_justification:
    name: mapping_justification
    description: Brief rationale or justification for the mapping
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mapping_justification
    owner: ICD11FMapping
    domain_of:
    - TermMapping
    range: string
  consistency:
    name: consistency
    description: Consistency assertions for this mapping against other sources
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: consistency
    owner: ICD11FMapping
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
    owner: ICD11FMapping
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