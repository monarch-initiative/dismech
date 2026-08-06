# Enum: PrevalenceClassEnum 




_Coarse, always-fillable band for disease occurrence — the population-rate analog of the HPO-style FrequencyEnum used for phenotype frequency. The numeric bands are the Orphanet prevalence classes (so the ~7% of records already quoting Orphanet map directly and the ICEES/ORPHA structured sources stay aligned); the qualitative tiers cover records that report only prose ("rare", "common") with no numeric estimate. When a numeric estimate exists, also populate rate_per_100000 (or rate_low/rate_high); the band is the queryable summary, the rate carries the precision._



URI: [dismech:enum/PrevalenceClassEnum](https://w3id.org/monarch-initiative/dismech/enum/PrevalenceClassEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| ABOVE_1_IN_1000 | None | More than 1 in 1,000 (more than 100 per 100,000) | Title: >1 / 1,000<br>|
| BAND_1_5_PER_10000 | None | 1 to 9 per 10,000 (10-99 per 100,000) | Title: 1-9 / 10,000<br>|
| BAND_1_9_PER_100000 | None | 1 to 9 per 100,000 | Title: 1-9 / 100,000<br>|
| BAND_1_9_PER_1000000 | None | 1 to 9 per 1,000,000 (0 | Title: 1-9 / 1,000,000<br>|
| BELOW_1_IN_1000000 | None | Fewer than 1 in 1,000,000 (less than 0 | Title: <1 / 1,000,000<br>|
| COMMON | None | Qualitative tier for disorders described as common/endemic with no numeric es... | Title: Common<br>|
| RARE | None | Qualitative tier for disorders described as "rare" in the source without a nu... | Title: Rare<br>|
| ULTRA_RARE | None | Qualitative tier for disorders described as ultra-rare / only a handful of re... | Title: Ultra-rare<br>|
| NOT_YET_DOCUMENTED | None | Source states prevalence is not yet documented | Title: Not yet documented<br>|
| UNKNOWN | None | Prevalence is unknown or not stated | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [prevalence_class](../slots/prevalence_class.md) | Coarse occurrence band (Orphanet prevalence class or qualitative tier) — the ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: PrevalenceClassEnum
description: Coarse, always-fillable band for disease occurrence — the population-rate
  analog of the HPO-style FrequencyEnum used for phenotype frequency. The numeric
  bands are the Orphanet prevalence classes (so the ~7% of records already quoting
  Orphanet map directly and the ICEES/ORPHA structured sources stay aligned); the
  qualitative tiers cover records that report only prose ("rare", "common") with no
  numeric estimate. When a numeric estimate exists, also populate rate_per_100000
  (or rate_low/rate_high); the band is the queryable summary, the rate carries the
  precision.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ABOVE_1_IN_1000:
    text: ABOVE_1_IN_1000
    description: More than 1 in 1,000 (more than 100 per 100,000). Orphanet class.
    title: '>1 / 1,000'
  BAND_1_5_PER_10000:
    text: BAND_1_5_PER_10000
    description: 1 to 9 per 10,000 (10-99 per 100,000). Combines the Orphanet 1-5
      and 6-9 per 10,000 classes into one decade-spanning band, matching the other
      per-decade bands and the _band_from_rate() boundaries.
    title: 1-9 / 10,000
  BAND_1_9_PER_100000:
    text: BAND_1_9_PER_100000
    description: 1 to 9 per 100,000. Orphanet class.
    title: 1-9 / 100,000
  BAND_1_9_PER_1000000:
    text: BAND_1_9_PER_1000000
    description: 1 to 9 per 1,000,000 (0.1-0.9 per 100,000). Orphanet class.
    title: 1-9 / 1,000,000
  BELOW_1_IN_1000000:
    text: BELOW_1_IN_1000000
    description: Fewer than 1 in 1,000,000 (less than 0.1 per 100,000). Orphanet class.
    title: <1 / 1,000,000
  COMMON:
    text: COMMON
    description: Qualitative tier for disorders described as common/endemic with no
      numeric estimate captured. Roughly corresponds to the >1/1,000 region but asserted
      only qualitatively.
    title: Common
  RARE:
    text: RARE
    description: Qualitative tier for disorders described as "rare" in the source
      without a numeric estimate (the EU rare-disease threshold is <1 in 2,000).
    title: Rare
  ULTRA_RARE:
    text: ULTRA_RARE
    description: Qualitative tier for disorders described as ultra-rare / only a handful
      of reported cases, with no population rate available. Often paired with measure_type
      CASES_IN_LITERATURE.
    title: Ultra-rare
  NOT_YET_DOCUMENTED:
    text: NOT_YET_DOCUMENTED
    description: Source states prevalence is not yet documented. Orphanet class.
    title: Not yet documented
    aliases:
    - Not yet documented
  UNKNOWN:
    text: UNKNOWN
    description: Prevalence is unknown or not stated.
    title: Unknown

```
</details>