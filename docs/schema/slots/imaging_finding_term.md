

# Slot: imaging_finding_term 


_Ontology term for an imaging finding (from the NCIT Imaging Finding branch or HP)_





URI: [dismech:slot/imaging_finding_term](https://w3id.org/monarch-initiative/dismech/slot/imaging_finding_term)
Alias: imaging_finding_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImagingFinding](../classes/ImagingFinding.md) | A finding detected by in-vivo medical imaging (MRI, CT, PET, ultrasound, etc |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ImagingFindingDescriptor](../classes/ImagingFindingDescriptor.md) |
| Domain Of | [ImagingFinding](../classes/ImagingFinding.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## Comments

* Use NCIT Imaging Finding terms (C176708 / C199145) or HP imaging-observable phenotypes (atrophy, white-matter lesions, hyperintensity)



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:imaging_finding_term |
| native | dismech:imaging_finding_term |




## LinkML Source

<details>
```yaml
name: imaging_finding_term
description: Ontology term for an imaging finding (from the NCIT Imaging Finding branch
  or HP)
comments:
- Use NCIT Imaging Finding terms (C176708 / C199145) or HP imaging-observable phenotypes
  (atrophy, white-matter lesions, hyperintensity)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: imaging_finding_term
domain_of:
- ImagingFinding
range: ImagingFindingDescriptor
inlined: true

```
</details>