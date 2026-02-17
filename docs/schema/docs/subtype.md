
# Class: Subtype



URI: [dismech:Subtype](https://w3id.org/monarch-initiative/dismech/Subtype)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AnatomicalEntityDescriptor]<locations%200..*-++[Subtype&#124;name:string;description:string%20%3F;review_notes:string%20%3F;geography:GeographyTerm%20*],[EvidenceItem]<evidence%200..*-++[Subtype],[DiseaseDescriptor]<subtype_term%200..1-++[Subtype],[Disease]++-%20has_subtypes%200..*>[Subtype],[InfectiousAgent]++-%20has_subtypes%200..*>[Subtype],[InfectiousAgent],[EvidenceItem],[DiseaseDescriptor],[Disease],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[AnatomicalEntityDescriptor]<locations%200..*-++[Subtype&#124;name:string;description:string%20%3F;review_notes:string%20%3F;geography:GeographyTerm%20*],[EvidenceItem]<evidence%200..*-++[Subtype],[DiseaseDescriptor]<subtype_term%200..1-++[Subtype],[Disease]++-%20has_subtypes%200..*>[Subtype],[InfectiousAgent]++-%20has_subtypes%200..*>[Subtype],[InfectiousAgent],[EvidenceItem],[DiseaseDescriptor],[Disease],[AnatomicalEntityDescriptor])

## Referenced by Class

 *  **None** *[has_subtypes](has_subtypes.md)*  <sub>0..\*</sub>  **[Subtype](Subtype.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [subtype_term](subtype_term.md)  <sub>0..1</sub>
     * Description: The MONDO term for a disease subtype
     * Range: [DiseaseDescriptor](DiseaseDescriptor.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [locations](locations.md)  <sub>0..\*</sub>
     * Range: [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md)
 * [geography](geography.md)  <sub>0..\*</sub>
     * Range: [GeographyTerm](GeographyTerm.md)
     * Example: ['Philippines'] None
