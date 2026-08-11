# Enum: ClinicalCourseEnum 




_Clinical course qualifiers for descriptor post-composition_



URI: [dismech:enum/ClinicalCourseEnum](https://w3id.org/monarch-initiative/dismech/enum/ClinicalCourseEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PROGRESSIVE | HP:0003676 | Worsening over time | Title: Progressive<br>|
| STABLE | HP:0031915 | Not varying in severity or amount over time | Title: Stable<br>|




## Slots

| Name | Description |
| ---  | --- |
| [clinical_course](../slots/clinical_course.md) | Clinical course qualifier for this descriptor (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalCourseEnum
description: Clinical course qualifiers for descriptor post-composition
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PROGRESSIVE:
    text: PROGRESSIVE
    description: Worsening over time
    meaning: HP:0003676
    title: Progressive
  STABLE:
    text: STABLE
    description: Not varying in severity or amount over time
    meaning: HP:0031915
    title: Stable

```
</details>