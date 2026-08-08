

# Slot: classification_value 


_The classification value assigned_





URI: [dismech:slot/classification_value](https://w3id.org/monarch-initiative/dismech/slot/classification_value)
Alias: classification_value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md) | Mechanistic/pathway-based disease classification assignment |  yes  |
| [ISDSNosologyAssignment](../classes/ISDSNosologyAssignment.md) | ISDS Nosology group assignment for a genetic skeletal disorder, per the Nosol... |  yes  |
| [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md) | ICD-O morphology classification assignment for neoplastic diseases |  yes  |
| [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md) | Channelopathy organ system classification assignment |  yes  |
| [IUISAssignment](../classes/IUISAssignment.md) | IUIS primary immunodeficiency classification assignment |  yes  |
| [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md) | Harrison's internal medicine chapter classification assignment |  yes  |
| [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md) | Lysosomal storage disease biochemical classification assignment |  yes  |
| [ICIMDAssignment](../classes/ICIMDAssignment.md) | ICIMD category/group classification assignment for inherited metabolic disord... |  yes  |
| [NIHResearchPriorityAssignment](../classes/NIHResearchPriorityAssignment.md) | NIH Highlighted Topics funding-priority assignment |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ICDOMorphologyAssignment](../classes/ICDOMorphologyAssignment.md), [HarrisonsChapterAssignment](../classes/HarrisonsChapterAssignment.md), [LysosomalStorageAssignment](../classes/LysosomalStorageAssignment.md), [MechanisticNosologyAssignment](../classes/MechanisticNosologyAssignment.md), [IUISAssignment](../classes/IUISAssignment.md), [ChannelopathyAssignment](../classes/ChannelopathyAssignment.md), [ICIMDAssignment](../classes/ICIMDAssignment.md), [ISDSNosologyAssignment](../classes/ISDSNosologyAssignment.md), [NIHResearchPriorityAssignment](../classes/NIHResearchPriorityAssignment.md) |

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
- ICIMDAssignment
- ISDSNosologyAssignment
- NIHResearchPriorityAssignment
range: string

```
</details>