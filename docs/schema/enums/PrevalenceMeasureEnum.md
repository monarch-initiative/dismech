# Enum: PrevalenceMeasureEnum 




_The kind of epidemiological measure a Prevalence record reports. Disease occurrence is reported in several non-interchangeable ways; this enum makes the measure explicit so a point prevalence is never silently compared with an incidence rate or a literature case-count. Mirrors the "type" column of the Orphanet epidemiology table._



URI: [dismech:enum/PrevalenceMeasureEnum](https://w3id.org/monarch-initiative/dismech/enum/PrevalenceMeasureEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| POINT_PREVALENCE | None | Proportion of a population affected at a single point in time | Title: Point prevalence<br>|
| BIRTH_PREVALENCE | None | Proportion of live births (or births) affected; common for congenital disorde... | Title: Prevalence at birth<br>|
| LIFETIME_PREVALENCE | None | Proportion of a population affected at some point during their lifetime | Title: Lifetime prevalence<br>|
| PERIOD_PREVALENCE | None | Proportion of a population affected during a defined interval (e | Title: Period prevalence<br>|
| ANNUAL_INCIDENCE | None | Rate of new cases arising in a population per year (an incidence, not a preva... | Title: Annual incidence<br>|
| CARRIER_FREQUENCY | None | Frequency of heterozygous carriers in a population (not affected individuals) | Title: Carrier frequency<br>|
| CASES_IN_LITERATURE | None | Count of reported cases or families rather than a population rate; used for u... | Title: Cases/families reported in the literature<br>|
| UNKNOWN | None | The measure type is not stated or cannot be determined from the source | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [measure_type](../slots/measure_type.md) | Which epidemiological measure this Prevalence record reports (point prevalenc... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: PrevalenceMeasureEnum
description: The kind of epidemiological measure a Prevalence record reports. Disease
  occurrence is reported in several non-interchangeable ways; this enum makes the
  measure explicit so a point prevalence is never silently compared with an incidence
  rate or a literature case-count. Mirrors the "type" column of the Orphanet epidemiology
  table.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  POINT_PREVALENCE:
    text: POINT_PREVALENCE
    description: Proportion of a population affected at a single point in time.
    title: Point prevalence
  BIRTH_PREVALENCE:
    text: BIRTH_PREVALENCE
    description: Proportion of live births (or births) affected; common for congenital
      disorders.
    title: Prevalence at birth
    aliases:
    - Prevalence at birth
  LIFETIME_PREVALENCE:
    text: LIFETIME_PREVALENCE
    description: Proportion of a population affected at some point during their lifetime.
    title: Lifetime prevalence
  PERIOD_PREVALENCE:
    text: PERIOD_PREVALENCE
    description: Proportion of a population affected during a defined interval (e.g.,
      five-year period prevalence).
    title: Period prevalence
  ANNUAL_INCIDENCE:
    text: ANNUAL_INCIDENCE
    description: Rate of new cases arising in a population per year (an incidence,
      not a prevalence).
    title: Annual incidence
    aliases:
    - Incidence
    - Annual incidence
  CARRIER_FREQUENCY:
    text: CARRIER_FREQUENCY
    description: Frequency of heterozygous carriers in a population (not affected
      individuals).
    title: Carrier frequency
  CASES_IN_LITERATURE:
    text: CASES_IN_LITERATURE
    description: Count of reported cases or families rather than a population rate;
      used for ultra-rare disorders where no denominator-based estimate exists.
    title: Cases/families reported in the literature
    aliases:
    - Cases/families in the literature
  UNKNOWN:
    text: UNKNOWN
    description: The measure type is not stated or cannot be determined from the source.
    title: Unknown

```
</details>