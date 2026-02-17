
# Class: Dataset

A reference to a publicly available omics or phenotype dataset

URI: [dismech:Dataset](https://w3id.org/monarch-initiative/dismech/Dataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleTypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[Dataset&#124;accession:uriorcurie;title:string%20%3F;description:string%20%3F;data_type:DatasetTypeEnum%20%3F;sample_count:integer%20%3F;conditions:string%20*;platform:string%20%3F;publication:PMID%20%3F;notes:string%20%3F],[GeneDescriptor]<genes%200..*-++[Dataset],[ExposureDescriptor]<exposures%200..*-++[Dataset],[SampleTypeDescriptor]<sample_types%200..*-++[Dataset],[OrganismDescriptor]<organism%200..1-++[Dataset],[Disease]++-%20datasets%200..*>[Dataset],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[SampleTypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[Dataset&#124;accession:uriorcurie;title:string%20%3F;description:string%20%3F;data_type:DatasetTypeEnum%20%3F;sample_count:integer%20%3F;conditions:string%20*;platform:string%20%3F;publication:PMID%20%3F;notes:string%20%3F],[GeneDescriptor]<genes%200..*-++[Dataset],[ExposureDescriptor]<exposures%200..*-++[Dataset],[SampleTypeDescriptor]<sample_types%200..*-++[Dataset],[OrganismDescriptor]<organism%200..1-++[Dataset],[Disease]++-%20datasets%200..*>[Dataset],[Disease])

## Referenced by Class

 *  **None** *[datasets](datasets.md)*  <sub>0..\*</sub>  **[Dataset](Dataset.md)**

## Attributes


### Own

 * [accession](accession.md)  <sub>1..1</sub>
     * Description: Dataset accession identifier as a CURIE (e.g., geo:GSE67472)
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [title](title.md)  <sub>0..1</sub>
     * Description: Title of the publication
     * Range: [String](types/String.md)
 * [Dataset➞description](Dataset_description.md)  <sub>0..1</sub>
     * Description: A description of the dataset. This may typically be redundant with the `title` slot, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the title slot.
     * Range: [String](types/String.md)
 * [organism](organism.md)  <sub>0..1</sub>
     * Description: The organism from which samples were derived
     * Range: [OrganismDescriptor](OrganismDescriptor.md)
 * [data_type](data_type.md)  <sub>0..1</sub>
     * Description: The type of omics or other data in the dataset
     * Range: [DatasetTypeEnum](DatasetTypeEnum.md)
 * [sample_types](sample_types.md)  <sub>0..\*</sub>
     * Description: Types of biological samples in the dataset
     * Range: [SampleTypeDescriptor](SampleTypeDescriptor.md)
 * [sample_count](sample_count.md)  <sub>0..1</sub>
     * Description: Total number of samples in the dataset
     * Range: [Integer](types/Integer.md)
 * [conditions](conditions.md)  <sub>0..\*</sub>
     * Description: Experimental conditions or disease states represented
     * Range: [String](types/String.md)
 * [exposures](exposures.md)  <sub>0..\*</sub>
     * Description: Environmental exposures studied in the dataset
     * Range: [ExposureDescriptor](ExposureDescriptor.md)
 * [genes](genes.md)  <sub>0..\*</sub>
     * Range: [GeneDescriptor](GeneDescriptor.md)
     * Example: [{preferred_term: HLA-DQ2}, {preferred_term: INS}] None
 * [platform](platform.md)  <sub>0..1</sub>
     * Description: Sequencing or array platform used
     * Range: [String](types/String.md)
 * [publication](publication.md)  <sub>0..1</sub>
     * Description: Associated publication (PMID)
     * Range: [PMID](types/PMID.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Supports GEO, ArrayExpress, SRA, dbGaP, GTEx, ENCODE, phenopacket-store, and other repositories |
