
# Class: AnimalModel



URI: [dismech:AnimalModel](https://w3id.org/monarch-initiative/dismech/AnimalModel)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[AnimalModel&#124;species:string%20%3F;genotype:string%20%3F;background:string%20%3F;category:string%20%3F;alleles:string%20*;description:string%20%3F;associated_phenotypes:string%20*],[GeneDescriptor]<genes%200..*-++[AnimalModel],[Disease]++-%20animal_models%200..*>[AnimalModel],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[AnimalModel&#124;species:string%20%3F;genotype:string%20%3F;background:string%20%3F;category:string%20%3F;alleles:string%20*;description:string%20%3F;associated_phenotypes:string%20*],[GeneDescriptor]<genes%200..*-++[AnimalModel],[Disease]++-%20animal_models%200..*>[AnimalModel],[Disease])

## Referenced by Class

 *  **None** *[animal_models](animal_models.md)*  <sub>0..\*</sub>  **[AnimalModel](AnimalModel.md)**

## Attributes


### Own

 * [species](species.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Human None
 * [genotype](genotype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: HLA-DQ2 None
 * [background](background.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [genes](genes.md)  <sub>0..\*</sub>
     * Range: [GeneDescriptor](GeneDescriptor.md)
     * Example: [{preferred_term: HLA-DQ2}, {preferred_term: INS}] None
 * [category](category.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Hematologic None
 * [alleles](alleles.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [associated_phenotypes](associated_phenotypes.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Celiac Disease', 'Type 1 Diabetes', 'Autoimmune Thyroid Disease'] None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
