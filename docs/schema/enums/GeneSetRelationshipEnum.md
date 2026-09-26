# Enum: GeneSetRelationshipEnum 




_How an external gene set (e.g. an MSigDB/KEGG pathway, a cell-type signature, or an expression-perturbation signature) relates to a disease entry. Records the semantics of a curated disease<->gene-set link so the link is auditable and the right kind of alignment can be applied._



URI: [dismech:enum/GeneSetRelationshipEnum](https://w3id.org/monarch-initiative/dismech/enum/GeneSetRelationshipEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| CANONICAL_PATHWAY | None | A curated pathway gene set representing the disease's canonical mechanism (e |
| CELL_TYPE_SIGNATURE | None | A marker gene set for a cell type relevant to the disease |
| PERTURBATION_SIGNATURE | None | An up/down expression signature from a perturbation or contrast (e |
| DISEASE_SIGNATURE | None | A differential-expression signature derived from the disease itself |
| OTHER | None | A related gene set that does not fit the categories above |













## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: GeneSetRelationshipEnum
description: How an external gene set (e.g. an MSigDB/KEGG pathway, a cell-type signature,
  or an expression-perturbation signature) relates to a disease entry. Records the
  semantics of a curated disease<->gene-set link so the link is auditable and the
  right kind of alignment can be applied.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  CANONICAL_PATHWAY:
    text: CANONICAL_PATHWAY
    description: A curated pathway gene set representing the disease's canonical mechanism
      (e.g. KEGG_ASTHMA for asthma). The primary target for BP alignment against the
      pathograph.
  CELL_TYPE_SIGNATURE:
    text: CELL_TYPE_SIGNATURE
    description: A marker gene set for a cell type relevant to the disease.
  PERTURBATION_SIGNATURE:
    text: PERTURBATION_SIGNATURE
    description: An up/down expression signature from a perturbation or contrast (e.g.
      drug response, knockout) relevant to the disease.
  DISEASE_SIGNATURE:
    text: DISEASE_SIGNATURE
    description: A differential-expression signature derived from the disease itself.
  OTHER:
    text: OTHER
    description: A related gene set that does not fit the categories above.

```
</details>