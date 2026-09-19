

# Slot: imaging_findings 


_In-vivo imaging findings (radiologic, nuclear-medicine, or ultrasound) that reflect disease pathophysiology or define diagnostic criteria. The macroscopic / in-vivo counterpart of the histopathology slot._





URI: [dismech:slot/imaging_findings](https://w3id.org/monarch-initiative/dismech/slot/imaging_findings)
Alias: imaging_findings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](../classes/Disease.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImagingFinding](../classes/ImagingFinding.md) |
| Domain Of | [Disease](../classes/Disease.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Separate from phenotypes - names the modality plus the imaging appearance, even when the abnormality is also curated as an HP phenotype
* Not for acquisition protocol, per-patient reads, or diagnostic decision support (see the imaging-scope design decision)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:imaging_findings |
| native | dismech:imaging_findings |




## LinkML Source

<details>
```yaml
name: imaging_findings
description: In-vivo imaging findings (radiologic, nuclear-medicine, or ultrasound)
  that reflect disease pathophysiology or define diagnostic criteria. The macroscopic
  / in-vivo counterpart of the histopathology slot.
comments:
- Separate from phenotypes - names the modality plus the imaging appearance, even
  when the abnormality is also curated as an HP phenotype
- Not for acquisition protocol, per-patient reads, or diagnostic decision support
  (see the imaging-scope design decision)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: imaging_findings
domain_of:
- Disease
range: ImagingFinding
recommended: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>