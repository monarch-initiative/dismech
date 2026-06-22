

# Slot: target_transcript 


_The specific transcript, pre-mRNA element, or sequence motif targeted by an antisense oligonucleotide (e.g., a RefSeq/Ensembl transcript ID, "SMN2 ISS-N1", or "APOB mRNA")._





URI: [dismech:slot/target_transcript](https://w3id.org/monarch-initiative/dismech/slot/target_transcript)
Alias: target_transcript

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AntisenseOligonucleotideDetail](../classes/AntisenseOligonucleotideDetail.md) | Structured attributes specific to an antisense oligonucleotide (ASO) treatmen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AntisenseOligonucleotideDetail](../classes/AntisenseOligonucleotideDetail.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dismech:target_transcript |
| native | dismech:target_transcript |




## LinkML Source

<details>
```yaml
name: target_transcript
description: The specific transcript, pre-mRNA element, or sequence motif targeted
  by an antisense oligonucleotide (e.g., a RefSeq/Ensembl transcript ID, "SMN2 ISS-N1",
  or "APOB mRNA").
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
alias: target_transcript
domain_of:
- AntisenseOligonucleotideDetail
range: string

```
</details>