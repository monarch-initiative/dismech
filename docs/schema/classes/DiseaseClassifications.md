

# Class: DiseaseClassifications 


_Container for all classification assignments for a disease_





URI: [dismech:class/DiseaseClassifications](https://w3id.org/monarch-initiative/dismech/class/DiseaseClassifications)





```mermaid
 classDiagram
    class DiseaseClassifications
    click DiseaseClassifications href "../../classes/DiseaseClassifications/"
      DiseaseClassifications : channelopathy_category
        
          
    
        
        
        DiseaseClassifications --> "0..1" ChannelopathyAssignment : channelopathy_category
        click ChannelopathyAssignment href "../../classes/ChannelopathyAssignment/"
    

        
      DiseaseClassifications : harrisons_chapter
        
          
    
        
        
        DiseaseClassifications --> "*" HarrisonsChapterAssignment : harrisons_chapter
        click HarrisonsChapterAssignment href "../../classes/HarrisonsChapterAssignment/"
    

        
      DiseaseClassifications : icdo_morphology
        
          
    
        
        
        DiseaseClassifications --> "0..1" ICDOMorphologyAssignment : icdo_morphology
        click ICDOMorphologyAssignment href "../../classes/ICDOMorphologyAssignment/"
    

        
      DiseaseClassifications : iuis_category
        
          
    
        
        
        DiseaseClassifications --> "0..1" IUISAssignment : iuis_category
        click IUISAssignment href "../../classes/IUISAssignment/"
    

        
      DiseaseClassifications : lysosomal_storage_category
        
          
    
        
        
        DiseaseClassifications --> "0..1" LysosomalStorageAssignment : lysosomal_storage_category
        click LysosomalStorageAssignment href "../../classes/LysosomalStorageAssignment/"
    

        
      DiseaseClassifications : mechanistic_category
        
          
    
        
        
        DiseaseClassifications --> "*" MechanisticNosologyAssignment : mechanistic_category
        click MechanisticNosologyAssignment href "../../classes/MechanisticNosologyAssignment/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [icdo_morphology](../slots/icdo_morphology.md) | 0..1 <br/> [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification (for neoplastic diseases) | direct |
| [harrisons_chapter](../slots/harrisons_chapter.md) | * <br/> [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification | direct |
| [lysosomal_storage_category](../slots/lysosomal_storage_category.md) | 0..1 <br/> [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification | direct |
| [mechanistic_category](../slots/mechanistic_category.md) | * <br/> [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification | direct |
| [iuis_category](../slots/iuis_category.md) | 0..1 <br/> [IUISAssignment](../classes/IUISAssignment.md) | IUIS primary immunodeficiency classification | direct |
| [channelopathy_category](../slots/channelopathy_category.md) | 0..1 <br/> [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) | Channelopathy organ system classification | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Disease](../classes/Disease.md) | [classifications](../slots/classifications.md) | range | [DiseaseClassifications](../classes/DiseaseClassifications.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:DiseaseClassifications |
| native | dismech:DiseaseClassifications |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiseaseClassifications
description: Container for all classification assignments for a disease
from_schema: https://w3id.org/monarch-initiative/dismech
slots:
- icdo_morphology
- harrisons_chapter
- lysosomal_storage_category
- mechanistic_category
- iuis_category
- channelopathy_category

```
</details>

### Induced

<details>
```yaml
name: DiseaseClassifications
description: Container for all classification assignments for a disease
from_schema: https://w3id.org/monarch-initiative/dismech
attributes:
  icdo_morphology:
    name: icdo_morphology
    description: ICD-O morphology classification (for neoplastic diseases)
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: icdo_morphology
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: ICDOMorphologyAssignment
    inlined: true
  harrisons_chapter:
    name: harrisons_chapter
    description: Harrison's internal medicine chapter classification
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: harrisons_chapter
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: HarrisonsChapterAssignment
    multivalued: true
    inlined: true
  lysosomal_storage_category:
    name: lysosomal_storage_category
    description: Lysosomal storage disease biochemical classification
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: lysosomal_storage_category
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: LysosomalStorageAssignment
    inlined: true
  mechanistic_category:
    name: mechanistic_category
    description: Mechanistic/pathway-based disease classification
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: mechanistic_category
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: MechanisticNosologyAssignment
    multivalued: true
    inlined: true
  iuis_category:
    name: iuis_category
    description: IUIS primary immunodeficiency classification
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: iuis_category
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: IUISAssignment
    inlined: true
  channelopathy_category:
    name: channelopathy_category
    description: Channelopathy organ system classification
    from_schema: https://w3id.org/monarch-initiative/dismech
    rank: 1000
    alias: channelopathy_category
    owner: DiseaseClassifications
    domain_of:
    - DiseaseClassifications
    range: ChannelopathyAssignment
    inlined: true

```
</details>