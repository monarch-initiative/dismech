# Enum: IctalStateEnum 




_Timing of an electrophysiologic finding relative to a seizure or paroxysmal event - the axis a flat HP phenotype term cannot express._



URI: [dismech:enum/IctalStateEnum](https://w3id.org/monarch-initiative/dismech/enum/IctalStateEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ICTAL | None | Recorded during a seizure / paroxysmal event |
| INTERICTAL | None | Recorded between events, in the baseline state |
| POSTICTAL | None | Recorded in the period immediately following an event |




## Slots

| Name | Description |
| ---  | --- |
| [ictal_state](../slots/ictal_state.md) | Timing of an electrophysiologic finding relative to a seizure/paroxysmal even... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: IctalStateEnum
description: Timing of an electrophysiologic finding relative to a seizure or paroxysmal
  event - the axis a flat HP phenotype term cannot express.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ICTAL:
    text: ICTAL
    description: Recorded during a seizure / paroxysmal event
  INTERICTAL:
    text: INTERICTAL
    description: Recorded between events, in the baseline state
  POSTICTAL:
    text: POSTICTAL
    description: Recorded in the period immediately following an event

```
</details>