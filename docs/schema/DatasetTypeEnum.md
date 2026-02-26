# Enum: DatasetTypeEnum 




_Type of dataset or data resource_



URI: [dismech:DatasetTypeEnum](https://w3id.org/monarch-initiative/dismech/DatasetTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MICROARRAY | None | Gene expression microarray |
| BULK_RNA_SEQ | None | Bulk RNA sequencing |
| SINGLE_CELL_RNA_SEQ | None | Single-cell RNA sequencing |
| SPATIAL_TRANSCRIPTOMICS | None | Spatially resolved transcriptomics |
| METHYLATION | None | DNA methylation profiling |
| CHIP_SEQ | None | Chromatin immunoprecipitation sequencing |
| ATAC_SEQ | None | Assay for transposase-accessible chromatin sequencing |
| PROTEOMICS | None | Protein expression profiling |
| METABOLOMICS | None | Metabolite profiling |
| GWAS | None | Genome-wide association study |
| WGS | None | Whole genome sequencing |
| WES | None | Whole exome sequencing |
| PHENOPACKETS | None | GA4GH Phenopacket collection (case-level phenotype data) |
| VARIANT_DATABASE | None | Curated genetic variant collection |




## Slots

| Name | Description |
| ---  | --- |
| [data_type](data_type.md) | The type of omics or other data in the dataset |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/dismech






## LinkML Source

<details>
```yaml
name: DatasetTypeEnum
description: Type of dataset or data resource
from_schema: https://w3id.org/monarch-initiative/dismech
rank: 1000
permissible_values:
  MICROARRAY:
    text: MICROARRAY
    description: Gene expression microarray
  BULK_RNA_SEQ:
    text: BULK_RNA_SEQ
    description: Bulk RNA sequencing
  SINGLE_CELL_RNA_SEQ:
    text: SINGLE_CELL_RNA_SEQ
    description: Single-cell RNA sequencing
  SPATIAL_TRANSCRIPTOMICS:
    text: SPATIAL_TRANSCRIPTOMICS
    description: Spatially resolved transcriptomics
  METHYLATION:
    text: METHYLATION
    description: DNA methylation profiling
  CHIP_SEQ:
    text: CHIP_SEQ
    description: Chromatin immunoprecipitation sequencing
  ATAC_SEQ:
    text: ATAC_SEQ
    description: Assay for transposase-accessible chromatin sequencing
  PROTEOMICS:
    text: PROTEOMICS
    description: Protein expression profiling
  METABOLOMICS:
    text: METABOLOMICS
    description: Metabolite profiling
  GWAS:
    text: GWAS
    description: Genome-wide association study
  WGS:
    text: WGS
    description: Whole genome sequencing
  WES:
    text: WES
    description: Whole exome sequencing
  PHENOPACKETS:
    text: PHENOPACKETS
    description: GA4GH Phenopacket collection (case-level phenotype data)
  VARIANT_DATABASE:
    text: VARIANT_DATABASE
    description: Curated genetic variant collection

```
</details>