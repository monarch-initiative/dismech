# Enum: CriteriaSemanticsEnum 




_The logical direction relating a grouping's membership criteria to its members, mirroring the OWL necessary/sufficient/equivalent distinction. This determines what tooling may infer: NECESSARY criteria can only be used to AUDIT listed members (member => criteria); SUFFICIENT criteria can be used to CLASSIFY non-members as candidates (criteria => member); NECESSARY_AND_SUFFICIENT criteria do both (member <=> criteria)._



URI: [dismech:enum/CriteriaSemanticsEnum](https://w3id.org/monarch-initiative/dismech/enum/CriteriaSemanticsEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| NECESSARY | None | Every member satisfies these criteria, but satisfying them does not by itself... | Title: Necessary (member => criteria)<br>|
| SUFFICIENT | None | Any disorder satisfying these criteria is a member | Title: Sufficient (criteria => member)<br>|
| NECESSARY_AND_SUFFICIENT | None | These criteria define the grouping: a disorder is a member if and only if it ... | Title: Necessary and sufficient (member <=> criteria)<br>|




## Slots

| Name | Description |
| ---  | --- |
| [criteria_semantics](../slots/criteria_semantics.md) | The logical relationship between this criteria block and grouping membership ... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: CriteriaSemanticsEnum
description: 'The logical direction relating a grouping''s membership criteria to
  its members, mirroring the OWL necessary/sufficient/equivalent distinction. This
  determines what tooling may infer: NECESSARY criteria can only be used to AUDIT
  listed members (member => criteria); SUFFICIENT criteria can be used to CLASSIFY
  non-members as candidates (criteria => member); NECESSARY_AND_SUFFICIENT criteria
  do both (member <=> criteria).'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  NECESSARY:
    text: NECESSARY
    description: Every member satisfies these criteria, but satisfying them does not
      by itself establish membership. Used to audit members for violations.
    title: Necessary (member => criteria)
  SUFFICIENT:
    text: SUFFICIENT
    description: Any disorder satisfying these criteria is a member. Used to classify
      non-members as candidate members.
    title: Sufficient (criteria => member)
  NECESSARY_AND_SUFFICIENT:
    text: NECESSARY_AND_SUFFICIENT
    description: 'These criteria define the grouping: a disorder is a member if and
      only if it satisfies them. Supports both auditing and classification.'
    title: Necessary and sufficient (member <=> criteria)

```
</details>