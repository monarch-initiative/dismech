

# Slot: relationship 


_Controlled relationship between a biomarker and the pathograph node it reports on_





URI: [dismech:slot/relationship](https://w3id.org/monarch-initiative/dismech/slot/relationship)
Alias: relationship

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomarkerReadout](../classes/BiomarkerReadout.md) | Links a biochemical biomarker to a pathograph node that it measures, reflects... |  yes  |
| [GeneSetAssociation](../classes/GeneSetAssociation.md) | A curated link between this disease and an external gene set, referenced by i... |  no  |
| [PhenotypeReadout](../classes/PhenotypeReadout.md) | Links an investigation-readout phenotype (an abnormal electrophysiology, func... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomarkerReadoutRelationshipEnum](../enums/BiomarkerReadoutRelationshipEnum.md) |
| Domain Of | [GeneSetAssociation](../classes/GeneSetAssociation.md), [BiomarkerReadout](../classes/BiomarkerReadout.md), [PhenotypeReadout](../classes/PhenotypeReadout.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:relationship |
| native | dismech:relationship |




## LinkML Source

<details>
```yaml
name: relationship
description: Controlled relationship between a biomarker and the pathograph node it
  reports on
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: relationship
domain_of:
- GeneSetAssociation
- BiomarkerReadout
- PhenotypeReadout
range: BiomarkerReadoutRelationshipEnum

```
</details>