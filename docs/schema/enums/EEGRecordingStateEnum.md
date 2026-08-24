# Enum: EEGRecordingStateEnum 




_Behavioural state or activation procedure under which an EEG finding is recorded, since many findings are state- or provocation-dependent._



URI: [dismech:enum/EEGRecordingStateEnum](https://w3id.org/monarch-initiative/dismech/enum/EEGRecordingStateEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| AWAKE | None | Recorded during wakefulness |
| ASLEEP | None | Recorded during sleep (findings may be sleep-activated) |
| DROWSY | None | Recorded during drowsiness / transition to sleep |
| SLEEP_DEPRIVED | None | Recorded after sleep deprivation (a seizure-activation procedure) |
| PHOTIC_STIMULATION | None | Recorded during intermittent photic stimulation |
| HYPERVENTILATION | None | Recorded during hyperventilation activation |




## Slots

| Name | Description |
| ---  | --- |
| [recording_state](../slots/recording_state.md) | Behavioural state or activation procedure under which an EEG finding is recor... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: EEGRecordingStateEnum
description: Behavioural state or activation procedure under which an EEG finding
  is recorded, since many findings are state- or provocation-dependent.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  AWAKE:
    text: AWAKE
    description: Recorded during wakefulness
  ASLEEP:
    text: ASLEEP
    description: Recorded during sleep (findings may be sleep-activated)
  DROWSY:
    text: DROWSY
    description: Recorded during drowsiness / transition to sleep
  SLEEP_DEPRIVED:
    text: SLEEP_DEPRIVED
    description: Recorded after sleep deprivation (a seizure-activation procedure)
  PHOTIC_STIMULATION:
    text: PHOTIC_STIMULATION
    description: Recorded during intermittent photic stimulation
  HYPERVENTILATION:
    text: HYPERVENTILATION
    description: Recorded during hyperventilation activation

```
</details>