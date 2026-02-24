# Enum: CurationStatusEnum 




_Curation workflow status for an association_



URI: [dismech:CurationStatusEnum](https://w3id.org/monarch-initiative/dismech/CurationStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CANDIDATE | None | Prioritized for curation |
| IN_PROGRESS | None | Curation in progress |
| CURATED | None | Curated with literature-backed evidence |
| DEFERRED | None | Deferred or deprioritized |




## Slots

| Name | Description |
| ---  | --- |
| [curation_status](curation_status.md) | Curation workflow status |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: CurationStatusEnum
description: Curation workflow status for an association
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CANDIDATE:
    text: CANDIDATE
    description: Prioritized for curation
  IN_PROGRESS:
    text: IN_PROGRESS
    description: Curation in progress
  CURATED:
    text: CURATED
    description: Curated with literature-backed evidence
  DEFERRED:
    text: DEFERRED
    description: Deferred or deprioritized

```
</details>