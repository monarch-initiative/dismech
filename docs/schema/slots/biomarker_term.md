

# Slot: biomarker_term 


_Ontology term for a biomarker (from NCIT)_





URI: [dismech:slot/biomarker_term](https://w3id.org/monarch-initiative/dismech/slot/biomarker_term)
Alias: biomarker_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalReadout](../classes/ExperimentalReadout.md) | A structured readout or outcome measured in an experiment |  no  |
| [Biochemical](../classes/Biochemical.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomarkerDescriptor](../classes/BiomarkerDescriptor.md) |
| Domain Of | [ExperimentalReadout](../classes/ExperimentalReadout.md), [Biochemical](../classes/Biochemical.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## Comments

* Use NCIT terms for biomarkers (proteins, genes, fusion products)
* NCIT:C16342 (Biomarker) is the root class for validation



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:biomarker_term |
| native | dismech:biomarker_term |




## LinkML Source

<details>
```yaml
name: biomarker_term
description: Ontology term for a biomarker (from NCIT)
comments:
- Use NCIT terms for biomarkers (proteins, genes, fusion products)
- NCIT:C16342 (Biomarker) is the root class for validation
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: biomarker_term
domain_of:
- ExperimentalReadout
- Biochemical
range: BiomarkerDescriptor
inlined: true

```
</details>