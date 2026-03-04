# Enum: DefinitionTypeEnum 




_The type of definition or criteria set_



URI: [dismech:DefinitionTypeEnum](https://w3id.org/monarch-initiative/dismech/DefinitionTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| DIAGNOSTIC_CRITERIA | None | Published diagnostic criteria (clinical/serologic/imaging) |
| PHENOTYPE_ALGORITHM | None | Algorithmic phenotype definition (e |
| CASE_DEFINITION | None | Case definition for surveillance or reporting |
| OTHER | None | Other definition type |




## Slots

| Name | Description |
| ---  | --- |
| [definition_type](definition_type.md) | The type of definition or criteria set |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DefinitionTypeEnum
description: The type of definition or criteria set
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  DIAGNOSTIC_CRITERIA:
    text: DIAGNOSTIC_CRITERIA
    description: Published diagnostic criteria (clinical/serologic/imaging)
  PHENOTYPE_ALGORITHM:
    text: PHENOTYPE_ALGORITHM
    description: Algorithmic phenotype definition (e.g., PheKB-style)
  CASE_DEFINITION:
    text: CASE_DEFINITION
    description: Case definition for surveillance or reporting
  OTHER:
    text: OTHER
    description: Other definition type

```
</details>