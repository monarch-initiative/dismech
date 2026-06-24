

# Slot: therapeutic_modality 


_Broad therapeutic platform/modality of a treatment (e.g., small molecule, monoclonal antibody, antisense oligonucleotide, gene therapy). Complements treatment_term (the MAXO action) and therapeutic_agent (the specific drug) by classifying the kind of therapeutic, enabling cross-disease queries by platform. Prefer this enum-backed slot over the free-text role slot for modality._





URI: [dismech:slot/therapeutic_modality](https://w3id.org/monarch-initiative/dismech/slot/therapeutic_modality)
Alias: therapeutic_modality

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](../classes/Treatment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TherapeuticModalityEnum](../enums/TherapeuticModalityEnum.md) |
| Domain Of | [Treatment](../classes/Treatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:therapeutic_modality |
| native | dismech:therapeutic_modality |




## LinkML Source

<details>
```yaml
name: therapeutic_modality
description: Broad therapeutic platform/modality of a treatment (e.g., small molecule,
  monoclonal antibody, antisense oligonucleotide, gene therapy). Complements treatment_term
  (the MAXO action) and therapeutic_agent (the specific drug) by classifying the kind
  of therapeutic, enabling cross-disease queries by platform. Prefer this enum-backed
  slot over the free-text role slot for modality.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: therapeutic_modality
domain_of:
- Treatment
range: TherapeuticModalityEnum

```
</details>