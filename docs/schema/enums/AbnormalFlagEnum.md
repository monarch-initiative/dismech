# Enum: AbnormalFlagEnum 




_Categorical interpretation flag for a clinical laboratory result band, aligned with HL7 v2 / LOINC abnormal-flag conventions._



URI: [dismech:enum/AbnormalFlagEnum](https://w3id.org/monarch-initiative/dismech/enum/AbnormalFlagEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| NORMAL | None | Result within the reference interval (HL7 "N") |
| LOW | None | Result below the reference interval (HL7 "L") |
| HIGH | None | Result above the reference interval (HL7 "H") |
| CRITICAL_LOW | None | Critically (panic) low result requiring urgent action (HL7 "LL") |
| CRITICAL_HIGH | None | Critically (panic) high result requiring urgent action (HL7 "HH") |




## Slots

| Name | Description |
| ---  | --- |
| [abnormal_flag](../slots/abnormal_flag.md) | Categorical abnormal-result flag for a reference-range band, following HL7/LO... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AbnormalFlagEnum
description: Categorical interpretation flag for a clinical laboratory result band,
  aligned with HL7 v2 / LOINC abnormal-flag conventions.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  NORMAL:
    text: NORMAL
    description: Result within the reference interval (HL7 "N")
  LOW:
    text: LOW
    description: Result below the reference interval (HL7 "L")
  HIGH:
    text: HIGH
    description: Result above the reference interval (HL7 "H")
  CRITICAL_LOW:
    text: CRITICAL_LOW
    description: Critically (panic) low result requiring urgent action (HL7 "LL")
  CRITICAL_HIGH:
    text: CRITICAL_HIGH
    description: Critically (panic) high result requiring urgent action (HL7 "HH")

```
</details>