# Enum: AllelicEventEnum 




_Type of genetic or epigenetic event affecting an allele. Use together with variant_origin, allelic_hit_role, zygosity, and functional impact rather than creating cross-product terms._



URI: [dismech:enum/AllelicEventEnum](https://w3id.org/monarch-initiative/dismech/enum/AllelicEventEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| PATHOGENIC_VARIANT | None | Pathogenic sequence variant or small variant not otherwise specified | Title: Pathogenic variant<br>|
| MISSENSE_VARIANT | None | Sequence variant that changes an amino acid | Title: Missense variant<br>|
| NONSENSE_VARIANT | None | Sequence variant that introduces a premature termination codon | Title: Nonsense variant<br>|
| FRAMESHIFT_VARIANT | None | Insertion or deletion that changes the coding reading frame | Title: Frameshift variant<br>|
| SPLICE_SITE_VARIANT | None | Variant that disrupts or alters RNA splicing | Title: Splice site variant<br>|
| DELETION | None | Sequence or chromosomal deletion event | Title: Deletion<br>|
| COPY_NUMBER_LOSS | None | Loss of DNA copy number affecting the gene or locus | Title: Copy-number loss<br>|
| COPY_NUMBER_GAIN | None | Gain of DNA copy number affecting the gene or locus | Title: Copy-number gain<br>|
| LOSS_OF_HETEROZYGOSITY | None | Loss of the wild-type or alternate allele in a tissue or clone | Title: Loss of heterozygosity<br>|
| PROMOTER_METHYLATION | None | Epigenetic promoter methylation affecting gene expression | Title: Promoter methylation<br>|
| BIALLELIC_INACTIVATION | None | Composite event state in which both alleles are functionally inactivated | Title: Biallelic inactivation<br>|
| UNKNOWN | None | The allelic event type has not been determined | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [allelic_events](../slots/allelic_events.md) | Event types affecting the allele or locus |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: AllelicEventEnum
description: Type of genetic or epigenetic event affecting an allele. Use together
  with variant_origin, allelic_hit_role, zygosity, and functional impact rather than
  creating cross-product terms.
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  PATHOGENIC_VARIANT:
    text: PATHOGENIC_VARIANT
    description: Pathogenic sequence variant or small variant not otherwise specified.
    title: Pathogenic variant
  MISSENSE_VARIANT:
    text: MISSENSE_VARIANT
    description: Sequence variant that changes an amino acid.
    title: Missense variant
  NONSENSE_VARIANT:
    text: NONSENSE_VARIANT
    description: Sequence variant that introduces a premature termination codon.
    title: Nonsense variant
  FRAMESHIFT_VARIANT:
    text: FRAMESHIFT_VARIANT
    description: Insertion or deletion that changes the coding reading frame.
    title: Frameshift variant
  SPLICE_SITE_VARIANT:
    text: SPLICE_SITE_VARIANT
    description: Variant that disrupts or alters RNA splicing.
    title: Splice site variant
  DELETION:
    text: DELETION
    description: Sequence or chromosomal deletion event.
    title: Deletion
  COPY_NUMBER_LOSS:
    text: COPY_NUMBER_LOSS
    description: Loss of DNA copy number affecting the gene or locus.
    title: Copy-number loss
  COPY_NUMBER_GAIN:
    text: COPY_NUMBER_GAIN
    description: Gain of DNA copy number affecting the gene or locus.
    title: Copy-number gain
  LOSS_OF_HETEROZYGOSITY:
    text: LOSS_OF_HETEROZYGOSITY
    description: Loss of the wild-type or alternate allele in a tissue or clone.
    title: Loss of heterozygosity
  PROMOTER_METHYLATION:
    text: PROMOTER_METHYLATION
    description: Epigenetic promoter methylation affecting gene expression.
    title: Promoter methylation
  BIALLELIC_INACTIVATION:
    text: BIALLELIC_INACTIVATION
    description: Composite event state in which both alleles are functionally inactivated.
    title: Biallelic inactivation
  UNKNOWN:
    text: UNKNOWN
    description: The allelic event type has not been determined.
    title: Unknown

```
</details>