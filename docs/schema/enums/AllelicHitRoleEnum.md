# Enum: AllelicHitRoleEnum 




_Role of a genetic alteration in a multi-hit disease mechanism. This is intentionally separate from variant origin, event type, and functional impact so two-hit models can be represented compositionally._



URI: [dismech:enum/AllelicHitRoleEnum](https://w3id.org/monarch-initiative/dismech/enum/AllelicHitRoleEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| FIRST_HIT | None | Initial alteration that creates a predisposed or partially disabled state, ty... | Title: First hit<br>|
| SECOND_HIT | None | Additional alteration that completes functional inactivation or activation in... | Title: Second hit<br>|
| BIALLELIC_INACTIVATION | None | Combined state in which both alleles of a gene are functionally inactivated | Title: Biallelic inactivation<br>|
| COOPERATING_HIT | None | Alteration that cooperates with another primary alteration without necessaril... | Title: Cooperating hit<br>|
| UNKNOWN | None | The hit role has not been determined | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [allelic_hit_role](../slots/allelic_hit_role.md) | Role of the alteration in a multi-hit mechanism, such as first hit, second hi... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AllelicHitRoleEnum
description: Role of a genetic alteration in a multi-hit disease mechanism. This is
  intentionally separate from variant origin, event type, and functional impact so
  two-hit models can be represented compositionally.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  FIRST_HIT:
    text: FIRST_HIT
    description: Initial alteration that creates a predisposed or partially disabled
      state, typically a germline alteration in tumor-suppressor syndromes.
    title: First hit
  SECOND_HIT:
    text: SECOND_HIT
    description: Additional alteration that completes functional inactivation or activation
      in the relevant disease tissue or clone.
    title: Second hit
  BIALLELIC_INACTIVATION:
    text: BIALLELIC_INACTIVATION
    description: Combined state in which both alleles of a gene are functionally inactivated.
    title: Biallelic inactivation
  COOPERATING_HIT:
    text: COOPERATING_HIT
    description: Alteration that cooperates with another primary alteration without
      necessarily being ordered as the first or second hit.
    title: Cooperating hit
  UNKNOWN:
    text: UNKNOWN
    description: The hit role has not been determined.
    title: Unknown

```
</details>