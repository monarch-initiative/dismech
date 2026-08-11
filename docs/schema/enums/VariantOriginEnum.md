# Enum: VariantOriginEnum 




_The origin of variation in a gene with respect to a disease entry. Bound to GENO allele origin terms._



URI: [dismech:enum/VariantOriginEnum](https://w3id.org/monarch-initiative/dismech/enum/VariantOriginEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| GERMLINE | GENO:0000888 | germline allele origin | Title: Germline<br>|
| SOMATIC | GENO:0000882 | somatic allele origin | Title: Somatic<br>|
| DE_NOVO | GENO:0000880 | de novo allele origin | Title: De novo<br>|
| GERMLINE_AND_SOMATIC | None | The gene is implicated by both germline and somatic variants in the disease (... | Title: Germline and somatic<br>|
| UNKNOWN | GENO:0000881 | unknown allele origin | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [variant_origin](../slots/variant_origin.md) | The origin of disease-associated variation in this gene (germline, somatic, d... |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: VariantOriginEnum
description: The origin of variation in a gene with respect to a disease entry. Bound
  to GENO allele origin terms.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  GERMLINE:
    text: GERMLINE
    description: germline allele origin
    meaning: GENO:0000888
    title: Germline
    notes:
    - Variant present in the germline (inherited or constitutional).
  SOMATIC:
    text: SOMATIC
    description: somatic allele origin
    meaning: GENO:0000882
    title: Somatic
    notes:
    - Variant acquired in somatic tissue after fertilization.
  DE_NOVO:
    text: DE_NOVO
    description: de novo allele origin
    meaning: GENO:0000880
    title: De novo
    notes:
    - Variant arising as a new mutation in the proband, not present in parents.
  GERMLINE_AND_SOMATIC:
    text: GERMLINE_AND_SOMATIC
    description: The gene is implicated by both germline and somatic variants in the
      disease (e.g., tumor suppressors with two-hit mechanisms).
    title: Germline and somatic
  UNKNOWN:
    text: UNKNOWN
    description: unknown allele origin
    meaning: GENO:0000881
    title: Unknown
    notes:
    - Origin of the variant is unspecified or not determined.

```
</details>