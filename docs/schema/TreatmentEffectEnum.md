# Enum: TreatmentEffectEnum 




_How a treatment affects a pathophysiology mechanism node_



URI: [dismech:TreatmentEffectEnum](https://w3id.org/monarch-initiative/dismech/TreatmentEffectEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| INHIBITS | None | Blocks or decreases the mechanism (e |
| ACTIVATES | None | Promotes or increases the mechanism (e |
| MODULATES | None | Alters the mechanism without clear unidirectional effect |
| BYPASSES | None | Works around the disrupted mechanism via an alternative pathway |
| RESTORES | None | Restores normal function of a disrupted mechanism (e |




## Slots

| Name | Description |
| ---  | --- |
| [treatment_effect](treatment_effect.md) | How the treatment affects the targeted mechanism |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: TreatmentEffectEnum
description: How a treatment affects a pathophysiology mechanism node
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  INHIBITS:
    text: INHIBITS
    description: Blocks or decreases the mechanism (e.g., TKI inhibiting constitutive
      kinase activity)
  ACTIVATES:
    text: ACTIVATES
    description: Promotes or increases the mechanism (e.g., enzyme replacement restoring
      a deficient pathway)
  MODULATES:
    text: MODULATES
    description: Alters the mechanism without clear unidirectional effect
  BYPASSES:
    text: BYPASSES
    description: Works around the disrupted mechanism via an alternative pathway
  RESTORES:
    text: RESTORES
    description: Restores normal function of a disrupted mechanism (e.g., gene therapy,
      enzyme replacement)

```
</details>