# Enum: CurationActionEnum 




_Simple action types for curation audit trail_



URI: [dismech:CurationActionEnum](https://w3id.org/monarch-initiative/dismech/CurationActionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CREATED | None | Initial file creation |
| EDITED | None | File modification |




## Slots

| Name | Description |
| ---  | --- |
| [curation_action](curation_action.md) | Type of curation action performed |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: CurationActionEnum
description: Simple action types for curation audit trail
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CREATED:
    text: CREATED
    description: Initial file creation
  EDITED:
    text: EDITED
    description: File modification

```
</details>