# Enum: TemporalityEnum 




_Temporal qualifiers for descriptor post-composition_



URI: [dismech:enum/TemporalityEnum](https://w3id.org/monarch-initiative/dismech/enum/TemporalityEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ACUTE | HP:0011009 | Acute manifestation or episode | Title: Acute<br>|
| TRANSIENT | HP:0025153 | Transient manifestation | Title: Transient<br>|
| SUBACUTE | HP:0011011 | Subacute manifestation or episode | Title: Subacute<br>|
| CHRONIC | HP:0011010 | Chronic or persistent over time | Title: Chronic<br>|
| RECURRENT | HP:0031796 | Repeated episodes separated by symptom-free intervals | Title: Recurrent<br>|
| DIURNAL | HP:0025302 | Manifestation occurring during the day | Title: Diurnal<br>|
| NOCTURNAL | HP:0025301 | Manifestation occurring at night | Title: Nocturnal<br>|
| PROLONGED | HP:0025297 | Manifestation lasting longer than typical | Title: Prolonged<br>|




## Slots

| Name | Description |
| ---  | --- |
| [temporality](../slots/temporality.md) | Temporal qualifier for this descriptor (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: TemporalityEnum
description: Temporal qualifiers for descriptor post-composition
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ACUTE:
    text: ACUTE
    description: Acute manifestation or episode
    meaning: HP:0011009
    title: Acute
  TRANSIENT:
    text: TRANSIENT
    description: Transient manifestation
    meaning: HP:0025153
    title: Transient
  SUBACUTE:
    text: SUBACUTE
    description: Subacute manifestation or episode
    meaning: HP:0011011
    title: Subacute
  CHRONIC:
    text: CHRONIC
    description: Chronic or persistent over time
    meaning: HP:0011010
    title: Chronic
  RECURRENT:
    text: RECURRENT
    description: Repeated episodes separated by symptom-free intervals
    meaning: HP:0031796
    title: Recurrent
  DIURNAL:
    text: DIURNAL
    description: Manifestation occurring during the day
    meaning: HP:0025302
    title: Diurnal
  NOCTURNAL:
    text: NOCTURNAL
    description: Manifestation occurring at night
    meaning: HP:0025301
    title: Nocturnal
  PROLONGED:
    text: PROLONGED
    description: Manifestation lasting longer than typical
    meaning: HP:0025297
    title: Prolonged

```
</details>