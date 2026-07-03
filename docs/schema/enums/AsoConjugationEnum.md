# Enum: AsoConjugationEnum 




_Targeting ligand or conjugate attached to an antisense oligonucleotide to direct tissue uptake or improve pharmacokinetics._



URI: [dismech:enum/AsoConjugationEnum](https://w3id.org/monarch-initiative/dismech/enum/AsoConjugationEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| UNCONJUGATED | None | No targeting conjugate (naked ASO) ||
| GALNAC | CHEBI:28037 | Tri-antennary N-acetylgalactosamine conjugate for hepatocyte (ASGR-mediated) ... | Title: GalNAc-conjugated<br>|
| LIPID | None | Lipid or fatty-acid conjugate ||
| PEPTIDE | None | Cell-penetrating or targeting peptide conjugate ||
| ANTIBODY | None | Antibody-oligonucleotide conjugate (AOC) for receptor-targeted delivery ||
| OTHER | None | Conjugate not covered by the above categories ||




## Slots

| Name | Description |
| ---  | --- |
| [conjugation](../slots/conjugation.md) | Targeting ligand or conjugate attached to an antisense oligonucleotide |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AsoConjugationEnum
description: Targeting ligand or conjugate attached to an antisense oligonucleotide
  to direct tissue uptake or improve pharmacokinetics.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  UNCONJUGATED:
    text: UNCONJUGATED
    description: No targeting conjugate (naked ASO)
  GALNAC:
    text: GALNAC
    description: Tri-antennary N-acetylgalactosamine conjugate for hepatocyte (ASGR-mediated)
      uptake (e.g., eplontersen, olezarsen)
    meaning: CHEBI:28037
    title: GalNAc-conjugated
    aliases:
    - N-acetyl-D-galactosamine
  LIPID:
    text: LIPID
    description: Lipid or fatty-acid conjugate
  PEPTIDE:
    text: PEPTIDE
    description: Cell-penetrating or targeting peptide conjugate
  ANTIBODY:
    text: ANTIBODY
    description: Antibody-oligonucleotide conjugate (AOC) for receptor-targeted delivery
  OTHER:
    text: OTHER
    description: Conjugate not covered by the above categories

```
</details>