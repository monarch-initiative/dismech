

# Slot: classification_value 


_The classification value assigned_





URI: [dismech:classification_value](https://w3id.org/monarch-initiative/dismech/classification_value)
Alias: classification_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IUISAssignment](IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  yes  |
| [LysosomalStorageAssignment](LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  yes  |
| [HarrisonsChapterAssignment](HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  yes  |
| [ChannelopathyAssignment](ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  yes  |
| [ICDOMorphologyAssignment](ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  yes  |
| [MechanisticNosologyAssignment](MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  yes  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:classification_value |
| native | dismech:classification_value |




## LinkML Source

<details>
```yaml
name: classification_value
description: The classification value assigned
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: classification_value
domain_of:
- ICDOMorphologyAssignment
- HarrisonsChapterAssignment
- LysosomalStorageAssignment
- MechanisticNosologyAssignment
- IUISAssignment
- ChannelopathyAssignment
range: string

```
</details>