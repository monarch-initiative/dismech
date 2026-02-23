

# Slot: diagnosis_term 


_The MAXO term for this diagnostic procedure_





URI: [dismech:diagnosis_term](https://w3id.org/monarch-initiative/dismech/diagnosis_term)
Alias: diagnosis_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Diagnosis](Diagnosis.md) |  |  no  |






## Properties

* Range: [TreatmentDescriptor](TreatmentDescriptor.md)




## Comments

* MAXO includes diagnostic procedures under medical actions
* Use qualifiers with UBERON terms to specify anatomical location (e.g., right heart catheterization)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:diagnosis_term |
| native | dismech:diagnosis_term |




## LinkML Source

<details>
```yaml
name: diagnosis_term
description: The MAXO term for this diagnostic procedure
comments:
- MAXO includes diagnostic procedures under medical actions
- Use qualifiers with UBERON terms to specify anatomical location (e.g., right heart
  catheterization)
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: diagnosis_term
domain_of:
- Diagnosis
range: TreatmentDescriptor
inlined: true

```
</details>