# Enum: AsoChemistryEnum 




_Backbone / sugar chemistry of an antisense oligonucleotide. Determines nuclease resistance, binding affinity, and whether the ASO supports RNase H recruitment (gapmer designs) or acts purely by steric occupancy._



URI: [dismech:enum/AsoChemistryEnum](https://w3id.org/monarch-initiative/dismech/enum/AsoChemistryEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PHOSPHOROTHIOATE | CHEBI:76674 | Phosphorothioate (PS) backbone modification conferring nuclease resistance; c... | Title: Phosphorothioate backbone<br>|
| PHOSPHORODIAMIDATE_MORPHOLINO | None | Morpholino backbone (PMO); charge-neutral, steric-block/splice-switching chem... | Title: Phosphorodiamidate morpholino (PMO)<br>|
| TWO_PRIME_O_METHYL | None | 2'-O-methyl (2'-OMe) ribose modification | Title: 2'-O-methyl<br>|
| TWO_PRIME_O_METHOXYETHYL | None | 2'-O-methoxyethyl (2'-MOE) ribose modification (e | Title: 2'-O-methoxyethyl (2'-MOE)<br>|
| LOCKED_NUCLEIC_ACID | None | Locked nucleic acid bridged-bicyclic sugar modification | Title: Locked nucleic acid (LNA)<br>|
| CONSTRAINED_ETHYL | None | Constrained ethyl (cEt) bridged sugar modification | Title: Constrained ethyl (cEt)<br>|
| OTHER | None | Chemistry not covered by the above categories ||




## Slots

| Name | Description |
| ---  | --- |
| [aso_chemistry](../slots/aso_chemistry.md) | Backbone / sugar chemistry of an antisense oligonucleotide |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AsoChemistryEnum
description: Backbone / sugar chemistry of an antisense oligonucleotide. Determines
  nuclease resistance, binding affinity, and whether the ASO supports RNase H recruitment
  (gapmer designs) or acts purely by steric occupancy.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PHOSPHOROTHIOATE:
    text: PHOSPHOROTHIOATE
    description: Phosphorothioate (PS) backbone modification conferring nuclease resistance;
      common base chemistry for RNase H ASOs
    meaning: CHEBI:76674
    title: Phosphorothioate backbone
    aliases:
    - phosphorothioate oligonucleotide
  PHOSPHORODIAMIDATE_MORPHOLINO:
    text: PHOSPHORODIAMIDATE_MORPHOLINO
    description: Morpholino backbone (PMO); charge-neutral, steric-block/splice-switching
      chemistry (e.g., eteplirsen, golodirsen)
    title: Phosphorodiamidate morpholino (PMO)
  TWO_PRIME_O_METHYL:
    text: TWO_PRIME_O_METHYL
    description: 2'-O-methyl (2'-OMe) ribose modification
    title: 2'-O-methyl
  TWO_PRIME_O_METHOXYETHYL:
    text: TWO_PRIME_O_METHOXYETHYL
    description: 2'-O-methoxyethyl (2'-MOE) ribose modification (e.g., nusinersen,
      inotersen, eplontersen)
    title: 2'-O-methoxyethyl (2'-MOE)
  LOCKED_NUCLEIC_ACID:
    text: LOCKED_NUCLEIC_ACID
    description: Locked nucleic acid bridged-bicyclic sugar modification
    title: Locked nucleic acid (LNA)
  CONSTRAINED_ETHYL:
    text: CONSTRAINED_ETHYL
    description: Constrained ethyl (cEt) bridged sugar modification
    title: Constrained ethyl (cEt)
  OTHER:
    text: OTHER
    description: Chemistry not covered by the above categories

```
</details>