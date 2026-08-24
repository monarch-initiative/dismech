

# Slot: electrophysiology 


_Optional electrophysiologic post-composition sidecar for a phenotype whose phenotype_term is an EEG/EMG/EKG finding (HP:0002353 / HP:0003457 / HP:0003115 subtrees). Carries modality plus the ictal and recording-state axes a flat HP term cannot express. Electrophysiologic findings are HP phenotypes, so they stay in `phenotypes`; this only post-composes them._





URI: [dismech:slot/electrophysiology](https://w3id.org/monarch-initiative/dismech/slot/electrophysiology)
Alias: electrophysiology

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ElectrophysiologyContext](../classes/ElectrophysiologyContext.md) |
| Domain Of | [Phenotype](../classes/Phenotype.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## Comments

* Use on EEG/EMG/EKG phenotypes; leave absent otherwise
* Not for acquisition protocol, per-patient tracings, or decision support



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:electrophysiology |
| native | dismech:electrophysiology |




## LinkML Source

<details>
```yaml
name: electrophysiology
description: Optional electrophysiologic post-composition sidecar for a phenotype
  whose phenotype_term is an EEG/EMG/EKG finding (HP:0002353 / HP:0003457 / HP:0003115
  subtrees). Carries modality plus the ictal and recording-state axes a flat HP term
  cannot express. Electrophysiologic findings are HP phenotypes, so they stay in `phenotypes`;
  this only post-composes them.
comments:
- Use on EEG/EMG/EKG phenotypes; leave absent otherwise
- Not for acquisition protocol, per-patient tracings, or decision support
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: electrophysiology
domain_of:
- Phenotype
range: ElectrophysiologyContext
inlined: true

```
</details>