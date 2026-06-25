# Enum: AsoMechanismEnum 




_Molecular mechanism of action of an antisense oligonucleotide, following the three core ASO paradigms (RNase H-mediated degradation, splice modulation, and steric blockade) described in Sang et al. 2024 (PMID:38914784)._



URI: [dismech:enum/AsoMechanismEnum](https://w3id.org/monarch-initiative/dismech/enum/AsoMechanismEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| RNASE_H_KNOCKDOWN | GO:0004523 | ASO:RNA heteroduplex recruits RNase H1 to cleave the target mRNA, reducing a ... | Title: RNase H knockdown<br>|
| SPLICE_MODULATION_EXON_SKIPPING | None | ASO occludes a splice site or splicing element to exclude an exon, restoring ... | Title: Splice modulation (exon skipping)<br>|
| SPLICE_MODULATION_EXON_INCLUSION | None | ASO blocks an intronic splicing silencer to promote exon inclusion (e | Title: Splice modulation (exon inclusion)<br>|
| STERIC_BLOCKADE | None | ASO sterically blocks ribosome access or other RNA-protein interactions witho... | Title: Steric translational blockade<br>|
| MIRNA_MODULATION | None | ASO sequesters or inhibits a microRNA (antimiR) or blocks a miRNA binding sit... | Title: miRNA modulation<br>|




## Slots

| Name | Description |
| ---  | --- |
| [aso_mechanism](../slots/aso_mechanism.md) | Molecular mechanism of action of an antisense oligonucleotide |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AsoMechanismEnum
description: Molecular mechanism of action of an antisense oligonucleotide, following
  the three core ASO paradigms (RNase H-mediated degradation, splice modulation, and
  steric blockade) described in Sang et al. 2024 (PMID:38914784).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  RNASE_H_KNOCKDOWN:
    text: RNASE_H_KNOCKDOWN
    description: ASO:RNA heteroduplex recruits RNase H1 to cleave the target mRNA,
      reducing a toxic or gain-of-function protein
    meaning: GO:0004523
    title: RNase H knockdown
    aliases:
    - RNA-DNA hybrid ribonuclease activity
  SPLICE_MODULATION_EXON_SKIPPING:
    text: SPLICE_MODULATION_EXON_SKIPPING
    description: ASO occludes a splice site or splicing element to exclude an exon,
      restoring an in-frame transcript (e.g., DMD exon skipping)
    title: Splice modulation (exon skipping)
  SPLICE_MODULATION_EXON_INCLUSION:
    text: SPLICE_MODULATION_EXON_INCLUSION
    description: ASO blocks an intronic splicing silencer to promote exon inclusion
      (e.g., nusinersen at SMN2 ISS-N1)
    title: Splice modulation (exon inclusion)
  STERIC_BLOCKADE:
    text: STERIC_BLOCKADE
    description: ASO sterically blocks ribosome access or other RNA-protein interactions
      without inducing cleavage (e.g., fomivirsen)
    title: Steric translational blockade
  MIRNA_MODULATION:
    text: MIRNA_MODULATION
    description: ASO sequesters or inhibits a microRNA (antimiR) or blocks a miRNA
      binding site
    title: miRNA modulation

```
</details>