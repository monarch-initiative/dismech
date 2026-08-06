

# Slot: reports_on 


_Links an investigation-readout phenotype (e.g. an abnormal electrophysiology or clinical-test finding such as HP:0000512 Abnormal electroretinogram) to the pathograph node whose underlying state it measures or reflects. The target is a named pathophysiology or phenotype node in the same disease file. These are observational readout links, not causal disease-progression edges, so they let an otherwise-disconnected test-result phenotype attach to the mechanism it reports on without asserting that the mechanism "causes" the test result._





URI: [dismech:slot/reports_on](https://w3id.org/monarch-initiative/dismech/slot/reports_on)
Alias: reports_on

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Phenotype](../classes/Phenotype.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhenotypeReadout](../classes/PhenotypeReadout.md) |
| Domain Of | [Phenotype](../classes/Phenotype.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |








## Comments

* Use on investigation/test-result phenotypes (electrophysiology, functional testing, laboratory findings) that report on an underlying mechanism rather than participating causally
* Target names should match a pathophysiology or phenotype entry name in the same disease file
* Rendered as a dashed observational edge (mechanism -.-> readout), like biomarker readouts



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:reports_on |
| native | dismech:reports_on |




## LinkML Source

<details>
```yaml
name: reports_on
description: Links an investigation-readout phenotype (e.g. an abnormal electrophysiology
  or clinical-test finding such as HP:0000512 Abnormal electroretinogram) to the pathograph
  node whose underlying state it measures or reflects. The target is a named pathophysiology
  or phenotype node in the same disease file. These are observational readout links,
  not causal disease-progression edges, so they let an otherwise-disconnected test-result
  phenotype attach to the mechanism it reports on without asserting that the mechanism
  "causes" the test result.
comments:
- Use on investigation/test-result phenotypes (electrophysiology, functional testing,
  laboratory findings) that report on an underlying mechanism rather than participating
  causally
- Target names should match a pathophysiology or phenotype entry name in the same
  disease file
- Rendered as a dashed observational edge (mechanism -.-> readout), like biomarker
  readouts
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: reports_on
domain_of:
- Phenotype
range: PhenotypeReadout
multivalued: true
inlined: true
inlined_as_list: true

```
</details>