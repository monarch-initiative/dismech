# Enum: FrequencyEnum 




_The frequency of an event or phenomenon_



URI: [dismech:enum/FrequencyEnum](https://w3id.org/monarch-initiative/dismech/enum/FrequencyEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| OBLIGATE | HP:0040280 | Present in all cases (100% of patients) | Title: Obligate (100%)<br>|
| VERY_FREQUENT | HP:0040281 | Present in most cases (80-99% of patients) | Title: Very frequent (80-99%)<br>|
| FREQUENT | HP:0040282 | Present in many cases (30-79% of patients) | Title: Frequent (30-79%)<br>|
| OCCASIONAL | HP:0040283 | Present in some cases (5-29% of patients) | Title: Occasional (5-29%)<br>|
| VERY_RARE | HP:0040284 | Present in rare cases (<5% of patients) | Title: Very rare (<5%)<br>|




## Slots

| Name | Description |
| ---  | --- |
| [min_frequency](../slots/min_frequency.md) | Minimum phenotype frequency threshold for a HAS_PHENOTYPE criterion; members ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: FrequencyEnum
description: The frequency of an event or phenomenon
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  OBLIGATE:
    text: OBLIGATE
    description: Present in all cases (100% of patients)
    meaning: HP:0040280
    title: Obligate (100%)
  VERY_FREQUENT:
    text: VERY_FREQUENT
    description: Present in most cases (80-99% of patients)
    meaning: HP:0040281
    title: Very frequent (80-99%)
    aliases:
    - Very frequent
  FREQUENT:
    text: FREQUENT
    description: Present in many cases (30-79% of patients)
    meaning: HP:0040282
    title: Frequent (30-79%)
  OCCASIONAL:
    text: OCCASIONAL
    description: Present in some cases (5-29% of patients)
    meaning: HP:0040283
    title: Occasional (5-29%)
  VERY_RARE:
    text: VERY_RARE
    description: Present in rare cases (<5% of patients)
    meaning: HP:0040284
    title: Very rare (<5%)
    aliases:
    - Very rare

```
</details>