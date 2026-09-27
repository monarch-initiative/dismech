# Enum: DefinitionDerivationBasisEnum 




_The epistemic grounding of a definition / phenotype algorithm, orthogonal to definition_type. Records where the definition comes from and how well established it is, so a mechanism-predicated case-finding query is not conflated with a consensus- or gold-standard-validated one. When the basis is a hypothesis, the definition should attaches_to the pathophysiology node(s)/edge(s) it is predicated on, so the basis can be cross-checked against those edges' hypothesis_groups._



URI: [dismech:enum/DefinitionDerivationBasisEnum](https://w3id.org/monarch-initiative/dismech/enum/DefinitionDerivationBasisEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ESTABLISHED_CRITERIA | None | Published consensus criteria or a validated computable phenotype (e |
| MECHANISTIC_HYPOTHESIS | None | Predicated on a specific, not-yet-proven disease mechanism hypothesis; member... |
| MODEL_SYSTEM_EXTRAPOLATION | None | Extrapolated from an animal or in-vitro model result not yet demonstrated in ... |




## Slots

| Name | Description |
| ---  | --- |
| [derivation_basis](../slots/derivation_basis.md) | Epistemic grounding of a definition, orthogonal to definition_type: establish... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DefinitionDerivationBasisEnum
description: The epistemic grounding of a definition / phenotype algorithm, orthogonal
  to definition_type. Records where the definition comes from and how well established
  it is, so a mechanism-predicated case-finding query is not conflated with a consensus-
  or gold-standard-validated one. When the basis is a hypothesis, the definition should
  attaches_to the pathophysiology node(s)/edge(s) it is predicated on, so the basis
  can be cross-checked against those edges' hypothesis_groups.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  ESTABLISHED_CRITERIA:
    text: ESTABLISHED_CRITERIA
    description: Published consensus criteria or a validated computable phenotype
      (e.g. an OHDSI Phenotype Library cohort). The implicit default for existing
      definitions.
  MECHANISTIC_HYPOTHESIS:
    text: MECHANISTIC_HYPOTHESIS
    description: Predicated on a specific, not-yet-proven disease mechanism hypothesis;
      membership is contingent on that hypothesis holding.
  MODEL_SYSTEM_EXTRAPOLATION:
    text: MODEL_SYSTEM_EXTRAPOLATION
    description: Extrapolated from an animal or in-vitro model result not yet demonstrated
      in humans.

```
</details>