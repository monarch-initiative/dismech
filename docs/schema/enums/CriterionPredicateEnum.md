# Enum: CriterionPredicateEnum 




_The kind of constraint expressed by a leaf node in a membership-criteria expression (LogicalCriterion). The leaf's payload slots are interpreted according to this predicate (e.g., HAS_PHENOTYPE uses phenotype_term and optional min_frequency; HAS_GENE uses gene; CONFORMS_TO_MODULE uses module)._



URI: [dismech:enum/CriterionPredicateEnum](https://w3id.org/monarch-initiative/dismech/enum/CriterionPredicateEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| HAS_PHENOTYPE | None | Members present a given phenotype (phenotype_term), optionally at or above a ... |
| HAS_GENE | None | Members carry causal variants in a given gene (gene) |
| CONFORMS_TO_MODULE | None | Members have a pathophysiology node conforming to a given mechanism module (m... |
| HAS_BIOLOGICAL_PROCESS | None | Members involve a given biological process (biological_processes), optionally... |
| HAS_CLASSIFICATION | None | Members carry a given nosology/classification assignment (classification) |
| HAS_INHERITANCE | None | Members share a mode of inheritance (description carries the value) |
| HAS_MAPPING | None | Members map to a given external term or code namespace (description carries t... |
| OTHER | None | A membership constraint that does not fit the categories above; described in ... |




## Slots

| Name | Description |
| ---  | --- |
| [criterion_predicate](../slots/criterion_predicate.md) | The constraint kind for a leaf node in a membership-criteria expression |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: CriterionPredicateEnum
description: The kind of constraint expressed by a leaf node in a membership-criteria
  expression (LogicalCriterion). The leaf's payload slots are interpreted according
  to this predicate (e.g., HAS_PHENOTYPE uses phenotype_term and optional min_frequency;
  HAS_GENE uses gene; CONFORMS_TO_MODULE uses module).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  HAS_PHENOTYPE:
    text: HAS_PHENOTYPE
    description: Members present a given phenotype (phenotype_term), optionally at
      or above a frequency threshold (min_frequency).
  HAS_GENE:
    text: HAS_GENE
    description: Members carry causal variants in a given gene (gene).
  CONFORMS_TO_MODULE:
    text: CONFORMS_TO_MODULE
    description: Members have a pathophysiology node conforming to a given mechanism
      module (module).
  HAS_BIOLOGICAL_PROCESS:
    text: HAS_BIOLOGICAL_PROCESS
    description: Members involve a given biological process (biological_processes),
      optionally with a directional modifier.
  HAS_CLASSIFICATION:
    text: HAS_CLASSIFICATION
    description: Members carry a given nosology/classification assignment (classification).
  HAS_INHERITANCE:
    text: HAS_INHERITANCE
    description: Members share a mode of inheritance (description carries the value).
  HAS_MAPPING:
    text: HAS_MAPPING
    description: Members map to a given external term or code namespace (description
      carries the value).
  OTHER:
    text: OTHER
    description: A membership constraint that does not fit the categories above; described
      in free text via the description slot.

```
</details>