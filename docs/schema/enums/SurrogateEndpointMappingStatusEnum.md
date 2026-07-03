# Enum: SurrogateEndpointMappingStatusEnum 




_Status of mapping an FDA disease/use row to dismech disease entries_



URI: [dismech:enum/SurrogateEndpointMappingStatusEnum](https://w3id.org/monarch-initiative/dismech/enum/SurrogateEndpointMappingStatusEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| EXACT_DISMECH_MATCH | None | FDA disease/use maps directly to an existing dismech disease entry | Title: Exact dismech match<br>|
| CURATED_DISMECH_MAPPING | None | Mapping was manually curated despite non-identical labels | Title: Curated dismech mapping<br>|
| CANDIDATE_DISMECH_MAPPING | None | Row mentions a disease represented in dismech but the FDA disease/use row is ... | Title: Candidate dismech mapping<br>|
| NEEDS_CURATION | None | No dismech disease mapping has been assigned yet | Title: Needs curation<br>|
| NOT_DISEASE_SPECIFIC | None | FDA row is a use, vaccine, or broad product context rather than a directly ma... | Title: Not disease specific<br>|




## Slots

| Name | Description |
| ---  | --- |
| [mapping_status](../slots/mapping_status.md) | Status of mapping the FDA disease/use row to dismech disease entries |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SurrogateEndpointMappingStatusEnum
description: Status of mapping an FDA disease/use row to dismech disease entries
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  EXACT_DISMECH_MATCH:
    text: EXACT_DISMECH_MATCH
    description: FDA disease/use maps directly to an existing dismech disease entry
    title: Exact dismech match
  CURATED_DISMECH_MAPPING:
    text: CURATED_DISMECH_MAPPING
    description: Mapping was manually curated despite non-identical labels
    title: Curated dismech mapping
  CANDIDATE_DISMECH_MAPPING:
    text: CANDIDATE_DISMECH_MAPPING
    description: Row mentions a disease represented in dismech but the FDA disease/use
      row is broader, multi-condition, or otherwise requires review
    title: Candidate dismech mapping
  NEEDS_CURATION:
    text: NEEDS_CURATION
    description: No dismech disease mapping has been assigned yet
    title: Needs curation
  NOT_DISEASE_SPECIFIC:
    text: NOT_DISEASE_SPECIFIC
    description: FDA row is a use, vaccine, or broad product context rather than a
      directly mappable disease entry
    title: Not disease specific

```
</details>