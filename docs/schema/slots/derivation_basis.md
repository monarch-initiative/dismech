

# Slot: derivation_basis 


_Epistemic grounding of a definition, orthogonal to definition_type: established criteria vs. a mechanistic hypothesis vs. model-system extrapolation. When MECHANISTIC_HYPOTHESIS, the definition should `attaches_to` the pathophysiology node(s)/edge(s) it is predicated on, so the hypothesis basis can be inferred from those edges' `hypothesis_groups`._





URI: [dismech:slot/derivation_basis](https://w3id.org/monarch-initiative/dismech/slot/derivation_basis)
Alias: derivation_basis

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Definition](../classes/Definition.md) | A diagnostic or phenotype definition for the disease |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DefinitionDerivationBasisEnum](../enums/DefinitionDerivationBasisEnum.md) |
| Domain Of | [Definition](../classes/Definition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:derivation_basis |
| native | dismech:derivation_basis |




## LinkML Source

<details>
```yaml
name: derivation_basis
description: 'Epistemic grounding of a definition, orthogonal to definition_type:
  established criteria vs. a mechanistic hypothesis vs. model-system extrapolation.
  When MECHANISTIC_HYPOTHESIS, the definition should `attaches_to` the pathophysiology
  node(s)/edge(s) it is predicated on, so the hypothesis basis can be inferred from
  those edges'' `hypothesis_groups`.'
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: derivation_basis
domain_of:
- Definition
range: DefinitionDerivationBasisEnum

```
</details>