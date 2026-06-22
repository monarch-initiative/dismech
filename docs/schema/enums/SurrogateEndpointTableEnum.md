# Enum: SurrogateEndpointTableEnum 




_FDA surrogate endpoint table section from which a row was curated_



URI: [dismech:enum/SurrogateEndpointTableEnum](https://w3id.org/monarch-initiative/dismech/enum/SurrogateEndpointTableEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ADULT_NONCANCER | None | Adult Surrogate Endpoints - Non-cancer Related | Title: Adult non-cancer related<br>|
| ADULT_CANCER | None | Adult Surrogate Endpoints - Cancer Related | Title: Adult cancer related<br>|
| PEDIATRIC_NONCANCER | None | Pediatric Surrogate Endpoints - Non-cancer Related | Title: Pediatric non-cancer related<br>|
| PEDIATRIC_CANCER | None | Pediatric Surrogate Endpoints - Cancer Related | Title: Pediatric cancer related<br>|




## Slots

| Name | Description |
| ---  | --- |
| [source_table](../slots/source_table.md) | FDA surrogate endpoint table section from which the row was curated |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: SurrogateEndpointTableEnum
description: FDA surrogate endpoint table section from which a row was curated
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ADULT_NONCANCER:
    text: ADULT_NONCANCER
    description: Adult Surrogate Endpoints - Non-cancer Related
    title: Adult non-cancer related
  ADULT_CANCER:
    text: ADULT_CANCER
    description: Adult Surrogate Endpoints - Cancer Related
    title: Adult cancer related
  PEDIATRIC_NONCANCER:
    text: PEDIATRIC_NONCANCER
    description: Pediatric Surrogate Endpoints - Non-cancer Related
    title: Pediatric non-cancer related
  PEDIATRIC_CANCER:
    text: PEDIATRIC_CANCER
    description: Pediatric Surrogate Endpoints - Cancer Related
    title: Pediatric cancer related

```
</details>