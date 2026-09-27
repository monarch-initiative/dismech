

# Slot: prevalence_class 


_Coarse occurrence band (Orphanet prevalence class or qualitative tier) — the always-fillable, queryable summary, analogous to phenotype FrequencyEnum._





URI: [dismech:slot/prevalence_class](https://w3id.org/monarch-initiative/dismech/slot/prevalence_class)
Alias: prevalence_class

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Prevalence](../classes/Prevalence.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PrevalenceClassEnum](../enums/PrevalenceClassEnum.md) |
| Domain Of | [Prevalence](../classes/Prevalence.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |









## Examples

| Value |
| --- |
| BAND_1_9_PER_100000 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:prevalence_class |
| native | dismech:prevalence_class |




## LinkML Source

<details>
```yaml
name: prevalence_class
description: Coarse occurrence band (Orphanet prevalence class or qualitative tier)
  — the always-fillable, queryable summary, analogous to phenotype FrequencyEnum.
examples:
- value: BAND_1_9_PER_100000
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: prevalence_class
domain_of:
- Prevalence
range: PrevalenceClassEnum

```
</details>