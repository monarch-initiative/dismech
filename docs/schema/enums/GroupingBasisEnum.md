# Enum: GroupingBasisEnum 




_The axis (or axes) on which a disease Grouping is drawn. A grouping assembles already-distinct Disease entries into an explicit union; this enum records WHY they belong together, supporting an audit of the grouping boundary. Multivalued — a grouping may rest on more than one basis (e.g., the mucopolysaccharidoses are grouped on both a shared mechanism and a shared gene/enzyme family)._



URI: [dismech:enum/GroupingBasisEnum](https://w3id.org/monarch-initiative/dismech/enum/GroupingBasisEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| SHARED_MECHANISM | None | Members converge on a common pathophysiological mechanism or final-common-pat... | Title: Shared mechanism<br>|
| SHARED_GENE_FAMILY | None | Members are caused by variants in the same gene, gene family, or functionally... | Title: Shared gene family<br>|
| SHARED_PATHWAY | None | Members perturb the same biological pathway or process | Title: Shared pathway<br>|
| SHARED_PHENOTYPE | None | Members share a defining clinical phenotype or phenotypic spectrum | Title: Shared phenotype<br>|
| SHARED_TREATMENT_RESPONSE | None | Members are grouped by a shared therapeutic vulnerability or response to a co... | Title: Shared treatment response<br>|
| CLINICAL_CONVENTION | None | Members are grouped by established clinical or nosological convention rather ... | Title: Clinical convention<br>|
| OTHER | None | A grouping basis that does not fit the categories above | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [grouping_basis](../slots/grouping_basis.md) | The axis or axes on which this grouping is drawn (records why the members bel... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: GroupingBasisEnum
description: The axis (or axes) on which a disease Grouping is drawn. A grouping assembles
  already-distinct Disease entries into an explicit union; this enum records WHY they
  belong together, supporting an audit of the grouping boundary. Multivalued — a grouping
  may rest on more than one basis (e.g., the mucopolysaccharidoses are grouped on
  both a shared mechanism and a shared gene/enzyme family).
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  SHARED_MECHANISM:
    text: SHARED_MECHANISM
    description: Members converge on a common pathophysiological mechanism or final-common-pathway
      (often a shared mechanism module).
    title: Shared mechanism
  SHARED_GENE_FAMILY:
    text: SHARED_GENE_FAMILY
    description: Members are caused by variants in the same gene, gene family, or
      functionally related set of genes/enzymes.
    title: Shared gene family
  SHARED_PATHWAY:
    text: SHARED_PATHWAY
    description: Members perturb the same biological pathway or process.
    title: Shared pathway
  SHARED_PHENOTYPE:
    text: SHARED_PHENOTYPE
    description: Members share a defining clinical phenotype or phenotypic spectrum.
    title: Shared phenotype
  SHARED_TREATMENT_RESPONSE:
    text: SHARED_TREATMENT_RESPONSE
    description: Members are grouped by a shared therapeutic vulnerability or response
      to a common class of treatment.
    title: Shared treatment response
  CLINICAL_CONVENTION:
    text: CLINICAL_CONVENTION
    description: Members are grouped by established clinical or nosological convention
      rather than a single mechanistic axis.
    title: Clinical convention
  OTHER:
    text: OTHER
    description: A grouping basis that does not fit the categories above.
    title: Other

```
</details>