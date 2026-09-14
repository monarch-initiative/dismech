# Enum: ModuleCollectionTypeEnum 




_The organizing principle for a curated collection of mechanism modules. Collections are navigation and framework records, not mechanism modules themselves and not disease groupings._



URI: [dismech:enum/ModuleCollectionTypeEnum](https://w3id.org/monarch-initiative/dismech/enum/ModuleCollectionTypeEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PUBLISHED_FRAMEWORK | None | A named framework or model defined in the scientific literature, such as the ... | Title: Published framework<br>|
| MECHANISTIC_FAMILY | None | Modules sharing a broad mechanistic pattern or process family | Title: Mechanistic family<br>|
| BIOLOGICAL_SYSTEM | None | Modules organized by the biological system or compartment involved | Title: Biological system<br>|
| PATHOLOGICAL_OUTCOME | None | Modules organized by a shared class of pathological outcome | Title: Pathological outcome<br>|
| THERAPEUTIC_STRATEGY | None | Modules organized by a shared intervention or therapeutic strategy | Title: Therapeutic strategy<br>|
| OTHER | None | A module-collection basis not covered by the other values | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [collection_type](../slots/collection_type.md) | The organizing principle represented by a ModuleCollection |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ModuleCollectionTypeEnum
description: The organizing principle for a curated collection of mechanism modules.
  Collections are navigation and framework records, not mechanism modules themselves
  and not disease groupings.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PUBLISHED_FRAMEWORK:
    text: PUBLISHED_FRAMEWORK
    description: A named framework or model defined in the scientific literature,
      such as the Hallmarks of Aging.
    title: Published framework
  MECHANISTIC_FAMILY:
    text: MECHANISTIC_FAMILY
    description: Modules sharing a broad mechanistic pattern or process family.
    title: Mechanistic family
  BIOLOGICAL_SYSTEM:
    text: BIOLOGICAL_SYSTEM
    description: Modules organized by the biological system or compartment involved.
    title: Biological system
  PATHOLOGICAL_OUTCOME:
    text: PATHOLOGICAL_OUTCOME
    description: Modules organized by a shared class of pathological outcome.
    title: Pathological outcome
  THERAPEUTIC_STRATEGY:
    text: THERAPEUTIC_STRATEGY
    description: Modules organized by a shared intervention or therapeutic strategy.
    title: Therapeutic strategy
  OTHER:
    text: OTHER
    description: A module-collection basis not covered by the other values.
    title: Other

```
</details>