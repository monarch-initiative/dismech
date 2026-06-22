

# Slot: classification_value 


_The classification value assigned_





URI: [dismech:slot/classification_value](https://w3id.org/monarch-initiative/dismech/slot/classification_value)
Alias: classification_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  yes  |
| [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  yes  |
| [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  yes  |
| [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  yes  |
| [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  yes  |
| [IUISAssignment](../classes/IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md), [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md), [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md), [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md), [IUISAssignment](../classes/IUISAssignment.md), [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










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