# Enum: MappingConsistencyEnum 




_Consistency of a mapping relative to another reference source_



URI: [dismech:MappingConsistencyEnum](https://w3id.org/monarch-initiative/dismech/MappingConsistencyEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CONSISTENT | None | Mapping is consistent with the reference source |
| INCONSISTENT | None | Mapping conflicts with the reference source |
| MISSING | None | Mapping is missing from the reference source |
| UNKNOWN | None | Consistency not assessed or unclear |




## Slots

| Name | Description |
| ---  | --- |
| [consistent](consistent.md) | Consistency status for a mapping relative to a reference source |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: MappingConsistencyEnum
description: Consistency of a mapping relative to another reference source
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CONSISTENT:
    text: CONSISTENT
    description: Mapping is consistent with the reference source
  INCONSISTENT:
    text: INCONSISTENT
    description: Mapping conflicts with the reference source
  MISSING:
    text: MISSING
    description: Mapping is missing from the reference source
  UNKNOWN:
    text: UNKNOWN
    description: Consistency not assessed or unclear

```
</details>