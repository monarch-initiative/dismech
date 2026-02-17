
# Class: Variant



URI: [dismech:Variant](https://w3id.org/monarch-initiative/dismech/Variant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[FunctionalEffect]<functional_effects%200..*-++[Variant&#124;name:string;description:string%20%3F;synonyms:string%20*;identifiers:uriorcurie%20*;sequence_length:integer%20%3F;clinical_significance:ClinicalSignificanceEnum%20%3F;type:string%20%3F],[EvidenceItem]<evidence%200..*-++[Variant],[GeneDescriptor]<gene%200..1-++[Variant],[Genetic]++-%20variants%200..*>[Variant],[Disease]++-%20variants%200..*>[Variant],[Genetic],[GeneDescriptor],[FunctionalEffect],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[FunctionalEffect]<functional_effects%200..*-++[Variant&#124;name:string;description:string%20%3F;synonyms:string%20*;identifiers:uriorcurie%20*;sequence_length:integer%20%3F;clinical_significance:ClinicalSignificanceEnum%20%3F;type:string%20%3F],[EvidenceItem]<evidence%200..*-++[Variant],[GeneDescriptor]<gene%200..1-++[Variant],[Genetic]++-%20variants%200..*>[Variant],[Disease]++-%20variants%200..*>[Variant],[Genetic],[GeneDescriptor],[FunctionalEffect],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[variants](variants.md)*  <sub>0..\*</sub>  **[Variant](Variant.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [gene](gene.md)  <sub>0..1</sub>
     * Range: [GeneDescriptor](GeneDescriptor.md)
     * Example: {preferred_term: MEFV} None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [functional_effects](functional_effects.md)  <sub>0..\*</sub>
     * Range: [FunctionalEffect](FunctionalEffect.md)
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['CYFRA 21-1'] None
 * [identifiers](identifiers.md)  <sub>0..\*</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [sequence_length](sequence_length.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [clinical_significance](clinical_significance.md)  <sub>0..1</sub>
     * Range: [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
