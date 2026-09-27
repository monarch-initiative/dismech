

# Slot: modality 


_The in-vivo imaging modality by which a finding is detected_





URI: [dismech:slot/modality](https://w3id.org/monarch-initiative/dismech/slot/modality)
Alias: modality

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImagingFinding](../classes/ImagingFinding.md) | A finding detected by in-vivo medical imaging (MRI, CT, PET, ultrasound, etc |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImagingModalityEnum](../enums/ImagingModalityEnum.md) |
| Domain Of | [ImagingFinding](../classes/ImagingFinding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:modality |
| native | dismech:modality |




## LinkML Source

<details>
```yaml
name: modality
description: The in-vivo imaging modality by which a finding is detected
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: modality
domain_of:
- ImagingFinding
range: ImagingModalityEnum

```
</details>