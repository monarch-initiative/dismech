

# Class: Qualifier  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_A predicate-value pair for formal post-composition. Allows OWL-like expressivity with controlled predicates and values, both as full Descriptors._





URI: [dismech:class/Qualifier](https://w3id.org/monarch-initiative/dismech/class/Qualifier)





```mermaid
 classDiagram
    class Qualifier
    click Qualifier href "../../classes/Qualifier/"
      Qualifier : predicate
        
          
    
        
        
        Qualifier --> "0..1" Descriptor : predicate
        click Descriptor href "../../classes/Descriptor/"
    

        
      Qualifier : value
        
          
    
        
        
        Qualifier --> "0..1" Descriptor : value
        click Descriptor href "../../classes/Descriptor/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [predicate](../slots/predicate.md) | 0..1 <br/> [Descriptor](../classes/Descriptor.md) | The relationship/predicate in a qualifier (e | direct |
| [value](../slots/value.md) | 0..1 <br/> [Descriptor](../classes/Descriptor.md) | The value/filler in a qualifier | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Descriptor](../classes/Descriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [CellTypeDescriptor](../classes/CellTypeDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [BiologicalProcessDescriptor](../classes/BiologicalProcessDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [AnatomicalEntityDescriptor](../classes/AnatomicalEntityDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [GeneDescriptor](../classes/GeneDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [CellularComponentDescriptor](../classes/CellularComponentDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [ProteinComplexDescriptor](../classes/ProteinComplexDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [AssayDescriptor](../classes/AssayDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [TriggerDescriptor](../classes/TriggerDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [DiseaseDescriptor](../classes/DiseaseDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [BiomarkerDescriptor](../classes/BiomarkerDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [GeneProductDescriptor](../classes/GeneProductDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [HistopathologyFindingDescriptor](../classes/HistopathologyFindingDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [LifeCycleStageDescriptor](../classes/LifeCycleStageDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [PhenotypeDescriptor](../classes/PhenotypeDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [InheritanceDescriptor](../classes/InheritanceDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [RegimenDescriptor](../classes/RegimenDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [ExposureDescriptor](../classes/ExposureDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [EnvironmentDescriptor](../classes/EnvironmentDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [OrganismDescriptor](../classes/OrganismDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [HostDescriptor](../classes/HostDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [SampleTypeDescriptor](../classes/SampleTypeDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [ModelVariableDescriptor](../classes/ModelVariableDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [CriteriaItem](../classes/CriteriaItem.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |
| [ConditionDescriptor](../classes/ConditionDescriptor.md) | [qualifiers](../slots/qualifiers.md) | range | [Qualifier](../classes/Qualifier.md) |







## Comments

* DEPRECATED - prefer explicit slots (located_in, laterality) for better constraints
* Use for formal semantic relationships like "has_input some X"
* Both predicate and value are Descriptors, allowing recursive composition
* Predicate typically uses RO (Relation Ontology) terms

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:Qualifier |
| native | dismech:Qualifier |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Qualifier
description: A predicate-value pair for formal post-composition. Allows OWL-like expressivity
  with controlled predicates and values, both as full Descriptors.
deprecated: Use explicit slots like located_in and laterality on Descriptor instead
comments:
- DEPRECATED - prefer explicit slots (located_in, laterality) for better constraints
- Use for formal semantic relationships like "has_input some X"
- Both predicate and value are Descriptors, allowing recursive composition
- Predicate typically uses RO (Relation Ontology) terms
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- predicate
- value

```
</details>

### Induced

<details>
```yaml
name: Qualifier
description: A predicate-value pair for formal post-composition. Allows OWL-like expressivity
  with controlled predicates and values, both as full Descriptors.
deprecated: Use explicit slots like located_in and laterality on Descriptor instead
comments:
- DEPRECATED - prefer explicit slots (located_in, laterality) for better constraints
- Use for formal semantic relationships like "has_input some X"
- Both predicate and value are Descriptors, allowing recursive composition
- Predicate typically uses RO (Relation Ontology) terms
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  predicate:
    name: predicate
    description: The relationship/predicate in a qualifier (e.g., RO:0002233 'has
      input')
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: predicate
    owner: Qualifier
    domain_of:
    - Qualifier
    range: Descriptor
    inlined: true
  value:
    name: value
    description: The value/filler in a qualifier
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: value
    owner: Qualifier
    domain_of:
    - Qualifier
    range: Descriptor
    inlined: true

```
</details>