

# Slot: target_mechanisms 


_Pathophysiology mechanism nodes that this treatment targets or modulates. Links a treatment to specific steps in the disease's causal graph, enabling inference about which downstream phenotypes should respond to therapy._





URI: [dismech:target_mechanisms](https://w3id.org/monarch-initiative/dismech/target_mechanisms)
Alias: target_mechanisms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Treatment](Treatment.md) |  |  no  |






## Properties

* Range: [TreatmentMechanismTarget](TreatmentMechanismTarget.md)

* Multivalued: True




## Comments

* Target names should match pathophysiology entry names in the same disease file
* Complements target_phenotypes by explaining WHERE in the causal chain the drug acts
* Analogous to DrugMechDB paths but anchored to dismech pathophysiology nodes

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:target_mechanisms |
| native | dismech:target_mechanisms |




## LinkML Source

<details>
```yaml
name: target_mechanisms
description: Pathophysiology mechanism nodes that this treatment targets or modulates.
  Links a treatment to specific steps in the disease's causal graph, enabling inference
  about which downstream phenotypes should respond to therapy.
comments:
- Target names should match pathophysiology entry names in the same disease file
- Complements target_phenotypes by explaining WHERE in the causal chain the drug acts
- Analogous to DrugMechDB paths but anchored to dismech pathophysiology nodes
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: target_mechanisms
domain_of:
- Treatment
range: TreatmentMechanismTarget
multivalued: true
inlined: true
inlined_as_list: true

```
</details>