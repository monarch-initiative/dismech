# Enum: ClinicalTrialStatusEnum 




_Clinical trial recruitment and status categories per ClinicalTrials.gov_



URI: [dismech:ClinicalTrialStatusEnum](https://w3id.org/monarch-initiative/dismech/ClinicalTrialStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| RECRUITING | None | Currently enrolling participants |
| NOT_RECRUITING | None | Not currently enrolling but may in the future |
| ACTIVE_NOT_RECRUITING | None | Actively recruiting previously enrolled participants (closed to new enrollmen... |
| COMPLETED | None | Trial data collection and analysis completed |
| ENROLLING_BY_INVITATION | None | Enrollment restricted to invited participants only |
| SUSPENDED | None | Temporarily halted pending review or administrative action |
| TERMINATED | None | Stopped before completion, may include safety or efficacy concerns |
| WITHDRAWN | None | Closed before enrollment began (never enrolled participants) |
| UNKNOWN | None | Status unknown or not provided |




## Slots

| Name | Description |
| ---  | --- |
| [status](status.md) | Recruitment or trial status (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ClinicalTrialStatusEnum
description: Clinical trial recruitment and status categories per ClinicalTrials.gov
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  RECRUITING:
    text: RECRUITING
    description: Currently enrolling participants
  NOT_RECRUITING:
    text: NOT_RECRUITING
    description: Not currently enrolling but may in the future
  ACTIVE_NOT_RECRUITING:
    text: ACTIVE_NOT_RECRUITING
    description: Actively recruiting previously enrolled participants (closed to new
      enrollment)
  COMPLETED:
    text: COMPLETED
    description: Trial data collection and analysis completed
  ENROLLING_BY_INVITATION:
    text: ENROLLING_BY_INVITATION
    description: Enrollment restricted to invited participants only
  SUSPENDED:
    text: SUSPENDED
    description: Temporarily halted pending review or administrative action
  TERMINATED:
    text: TERMINATED
    description: Stopped before completion, may include safety or efficacy concerns
  WITHDRAWN:
    text: WITHDRAWN
    description: Closed before enrollment began (never enrolled participants)
  UNKNOWN:
    text: UNKNOWN
    description: Status unknown or not provided

```
</details>