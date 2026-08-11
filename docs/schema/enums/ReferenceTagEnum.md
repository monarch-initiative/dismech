# Enum: ReferenceTagEnum 




_Controlled vocabulary for tagging top-level references by authoritative source type. Enables queries like "which disorders lack a GeneReviews citation?"_



URI: [dismech:enum/ReferenceTagEnum](https://w3id.org/monarch-initiative/dismech/enum/ReferenceTagEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| GeneReviews | None | Reference is a GeneReviews article published in the NCBI Bookshelf (https://w... | Title: GeneReviews<br>|




## Slots

| Name | Description |
| ---  | --- |
| [tags](../slots/tags.md) | Authoritative-source tags for a reference (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: ReferenceTagEnum
description: Controlled vocabulary for tagging top-level references by authoritative
  source type. Enables queries like "which disorders lack a GeneReviews citation?"
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  GeneReviews:
    text: GeneReviews
    description: Reference is a GeneReviews article published in the NCBI Bookshelf
      (https://www.ncbi.nlm.nih.gov/books/NBK1116/). GeneReviews are expert-authored,
      peer-reviewed summaries updated on a rolling basis; they are the gold-standard
      narrative resource for rare Mendelian disease phenotyping and management.
    title: GeneReviews

```
</details>