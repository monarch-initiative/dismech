

# Slot: therapeutic_agent 


_The drug, chemical, or therapeutic agent used in a treatment. Use when the MAXO term is generic (e.g., pharmacotherapy) but specific drugs are involved._





URI: [dismech:slot/therapeutic_agent](https://w3id.org/monarch-initiative/dismech/slot/therapeutic_agent)
Alias: therapeutic_agent

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TreatmentDescriptor](../classes/TreatmentDescriptor.md) | A descriptor for treatments/medical actions, bindable to MAXO or NCIT clinica... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntityDescriptor](../classes/ChemicalEntityDescriptor.md) |
| Domain Of | [TreatmentDescriptor](../classes/TreatmentDescriptor.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Bind to CHEBI for specific chemicals/drugs
* Can also use NCIT for drug classes when CHEBI term unavailable



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:therapeutic_agent |
| native | dismech:therapeutic_agent |




## LinkML Source

<details>
```yaml
name: therapeutic_agent
description: The drug, chemical, or therapeutic agent used in a treatment. Use when
  the MAXO term is generic (e.g., pharmacotherapy) but specific drugs are involved.
comments:
- Bind to CHEBI for specific chemicals/drugs
- Can also use NCIT for drug classes when CHEBI term unavailable
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: therapeutic_agent
domain_of:
- TreatmentDescriptor
range: ChemicalEntityDescriptor
multivalued: true
inlined: true

```
</details>