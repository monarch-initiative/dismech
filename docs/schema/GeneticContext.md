

# Class: GeneticContext 


_A structured description of a genetic context that modifies phenotype frequency, severity, or presentation. Flexible enough to capture single genes, multiple genes, mutation types, zygosity, complementation groups, and complex genotypes. The description slot accommodates contexts that don't fit neatly into the structured fields (e.g., structural variants, complex rearrangements)._





URI: [dismech:GeneticContext](https://w3id.org/monarch-initiative/dismech/GeneticContext)





```mermaid
 classDiagram
    class GeneticContext
    click GeneticContext href "../GeneticContext/"
      GeneticContext : allele_type
        
      GeneticContext : complementation_group
        
      GeneticContext : description
        
      GeneticContext : functional_impact
        
      GeneticContext : gene
        
          
    
        
        
        GeneticContext --> "0..1" GeneDescriptor : gene
        click GeneDescriptor href "../GeneDescriptor/"
    

        
      GeneticContext : genes
        
          
    
        
        
        GeneticContext --> "*" GeneDescriptor : genes
        click GeneDescriptor href "../GeneDescriptor/"
    

        
      GeneticContext : notes
        
      GeneticContext : zygosity
        
          
    
        
        
        GeneticContext --> "0..1" ZygosityEnum : zygosity
        click ZygosityEnum href "../ZygosityEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gene](gene.md) | 0..1 <br/> [GeneDescriptor](GeneDescriptor.md) |  | direct |
| [genes](genes.md) | * <br/> [GeneDescriptor](GeneDescriptor.md) |  | direct |
| [allele_type](allele_type.md) | 0..1 <br/> [String](String.md) | Type of allele or mutation (e | direct |
| [zygosity](zygosity.md) | 0..1 <br/> [ZygosityEnum](ZygosityEnum.md) | Zygosity context | direct |
| [functional_impact](functional_impact.md) | 0..1 <br/> [String](String.md) | Functional consequence of the genetic variant (e | direct |
| [complementation_group](complementation_group.md) | 0..1 <br/> [String](String.md) | Complementation group designation (e | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PhenotypeContext](PhenotypeContext.md) | [genetic_context](genetic_context.md) | range | [GeneticContext](GeneticContext.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:GeneticContext |
| native | dismech:GeneticContext |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneticContext
description: A structured description of a genetic context that modifies phenotype
  frequency, severity, or presentation. Flexible enough to capture single genes, multiple
  genes, mutation types, zygosity, complementation groups, and complex genotypes.
  The description slot accommodates contexts that don't fit neatly into the structured
  fields (e.g., structural variants, complex rearrangements).
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- gene
- genes
- allele_type
- zygosity
- functional_impact
- complementation_group
- description
- notes

```
</details>

### Induced

<details>
```yaml
name: GeneticContext
description: A structured description of a genetic context that modifies phenotype
  frequency, severity, or presentation. Flexible enough to capture single genes, multiple
  genes, mutation types, zygosity, complementation groups, and complex genotypes.
  The description slot accommodates contexts that don't fit neatly into the structured
  fields (e.g., structural variants, complex rearrangements).
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  gene:
    name: gene
    examples:
    - value: '{preferred_term: MEFV}'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: gene
    owner: GeneticContext
    domain_of:
    - GeneticContext
    - Pathophysiology
    - Variant
    range: GeneDescriptor
    inlined: true
  genes:
    name: genes
    examples:
    - value: '[{preferred_term: HLA-DQ2}, {preferred_term: INS}]'
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: genes
    owner: GeneticContext
    domain_of:
    - GeneticContext
    - Dataset
    - Subtype
    - Pathophysiology
    - AnimalModel
    range: GeneDescriptor
    multivalued: true
    inlined: true
    inlined_as_list: true
  allele_type:
    name: allele_type
    description: Type of allele or mutation (e.g., null, missense, splice_site, deletion,
      frameshift, nonsense, hypomorphic, structural_variant). Free text to accommodate
      the diversity of mutation nomenclature.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: allele_type
    owner: GeneticContext
    domain_of:
    - GeneticContext
    range: string
  zygosity:
    name: zygosity
    description: Zygosity context
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: zygosity
    owner: GeneticContext
    domain_of:
    - GeneticContext
    range: ZygosityEnum
  functional_impact:
    name: functional_impact
    description: Functional consequence of the genetic variant (e.g., loss_of_function,
      gain_of_function, dominant_negative).
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: functional_impact
    owner: GeneticContext
    domain_of:
    - GeneticContext
    range: string
  complementation_group:
    name: complementation_group
    description: Complementation group designation (e.g., FA-A, FA-D1, BBS1). Used
      for genetically heterogeneous diseases where subtypes are historically named
      by complementation analysis.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: complementation_group
    owner: GeneticContext
    domain_of:
    - GeneticContext
    range: string
  description:
    name: description
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: description
    owner: GeneticContext
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
  notes:
    name: notes
    examples:
    - value: Contagious stage where symptoms appear and the bacteria can be spread
        to others.
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: notes
    owner: GeneticContext
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