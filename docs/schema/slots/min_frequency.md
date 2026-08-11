

# Slot: min_frequency 


_Minimum phenotype frequency threshold for a HAS_PHENOTYPE criterion; members must exhibit the phenotype at this frequency band or higher._





URI: [dismech:slot/min_frequency](https://w3id.org/monarch-initiative/dismech/slot/min_frequency)
Alias: min_frequency

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LogicalCriterion](../classes/LogicalCriterion.md) | A node in a nested boolean membership-criteria expression |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FrequencyEnum](../enums/FrequencyEnum.md) |
| Domain Of | [LogicalCriterion](../classes/LogicalCriterion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:min_frequency |
| native | dismech:min_frequency |




## LinkML Source

<details>
```yaml
name: min_frequency
description: Minimum phenotype frequency threshold for a HAS_PHENOTYPE criterion;
  members must exhibit the phenotype at this frequency band or higher.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: min_frequency
domain_of:
- LogicalCriterion
range: FrequencyEnum

```
</details>