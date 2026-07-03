# Enum: MechanismConfidenceEnum 




_Level of confidence in a pathophysiology mechanism_



URI: [dismech:enum/MechanismConfidenceEnum](https://w3id.org/monarch-initiative/dismech/enum/MechanismConfidenceEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ESTABLISHED | None | Well-established mechanism with strong evidence from multiple independent stu... | Title: Established<br>|
| HYPOTHETICAL | None | Hypothetical mechanism with limited or indirect evidence; plausible but not y... | Title: Hypothetical<br>|
| PROVISIONAL | None | Provisional mechanism under active investigation with emerging but incomplete... | Title: Provisional<br>|




## Slots

| Name | Description |
| ---  | --- |
| [mechanism_confidence](../slots/mechanism_confidence.md) | Level of confidence in this pathophysiology mechanism |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: MechanismConfidenceEnum
description: Level of confidence in a pathophysiology mechanism
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ESTABLISHED:
    text: ESTABLISHED
    description: Well-established mechanism with strong evidence from multiple independent
      studies
    title: Established
  HYPOTHETICAL:
    text: HYPOTHETICAL
    description: Hypothetical mechanism with limited or indirect evidence; plausible
      but not yet validated
    title: Hypothetical
  PROVISIONAL:
    text: PROVISIONAL
    description: Provisional mechanism under active investigation with emerging but
      incomplete evidence
    title: Provisional

```
</details>