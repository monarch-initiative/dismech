# Enum: MechanisticNosologyEnum 




_Classification of diseases by molecular mechanism or affected cellular system. Tag diseases with their primary mechanistic category._



URI: [dismech:enum/MechanisticNosologyEnum](https://w3id.org/monarch-initiative/dismech/enum/MechanisticNosologyEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| RASopathy | MONDO:0021060 | RAS/MAPK signaling pathway disorders (Noonan, Costello, CFC, NF1) |
| ciliopathy | MONDO:0005308 | Primary cilia structure/function disorders (PKD, Bardet-Biedl, Joubert) |
| laminopathy | MONDO:0021106 | Nuclear lamina disorders (EDMD, progeria, lipodystrophy) |
| collagenopathy | MONDO:0004603 | Collagen synthesis/structure disorders (OI, EDS, Alport) |
| mitochondrial disease | MONDO:0044970 | Mitochondrial function/genome disorders (MELAS, MERRF, Leigh) |
| amyloidopathy | None | Amyloid protein aggregation disorders (Alzheimer's, CAA, hereditary cerebral ... |
| tauopathy | MONDO:0005574 | Tau protein aggregation disorders (Alzheimer's, PSP, CBD) |
| synucleinopathy | MONDO:0000510 | Alpha-synuclein aggregation disorders (Parkinson's, DLB, MSA) |




## Slots

| Name | Description |
| ---  | --- |
| [classification_value](../slots/classification_value.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: MechanisticNosologyEnum
description: Classification of diseases by molecular mechanism or affected cellular
  system. Tag diseases with their primary mechanistic category.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  RASopathy:
    text: RASopathy
    description: RAS/MAPK signaling pathway disorders (Noonan, Costello, CFC, NF1)
    meaning: MONDO:0021060
  ciliopathy:
    text: ciliopathy
    description: Primary cilia structure/function disorders (PKD, Bardet-Biedl, Joubert)
    meaning: MONDO:0005308
  laminopathy:
    text: laminopathy
    description: Nuclear lamina disorders (EDMD, progeria, lipodystrophy)
    meaning: MONDO:0021106
  collagenopathy:
    text: collagenopathy
    description: Collagen synthesis/structure disorders (OI, EDS, Alport)
    meaning: MONDO:0004603
  mitochondrial disease:
    text: mitochondrial disease
    description: Mitochondrial function/genome disorders (MELAS, MERRF, Leigh)
    meaning: MONDO:0044970
  amyloidopathy:
    text: amyloidopathy
    description: Amyloid protein aggregation disorders (Alzheimer's, CAA, hereditary
      cerebral amyloid angiopathy)
  tauopathy:
    text: tauopathy
    description: Tau protein aggregation disorders (Alzheimer's, PSP, CBD)
    meaning: MONDO:0005574
  synucleinopathy:
    text: synucleinopathy
    description: Alpha-synuclein aggregation disorders (Parkinson's, DLB, MSA)
    meaning: MONDO:0000510

```
</details>