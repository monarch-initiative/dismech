
# Class: Biochemical



URI: [dismech:Biochemical](https://w3id.org/monarch-initiative/dismech/Biochemical)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[Descriptor],[CellTypeDescriptor],[AssayDescriptor]<assays%200..*-++[Biochemical&#124;name:string;presence:string%20%3F;specificity:string%20%3F;notes:string%20%3F;context:string%20%3F;subtype:string%20%3F;synonyms:string%20*],[CellTypeDescriptor]<cell_types%200..*-++[Biochemical],[Any]<frequency%200..1-++[Biochemical],[EvidenceItem]<evidence%200..*-++[Biochemical],[Descriptor]<biomarker_term%200..1-++[Biochemical],[Disease]++-%20biochemical%200..*>[Biochemical],[Disease],[AssayDescriptor],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[Descriptor],[CellTypeDescriptor],[AssayDescriptor]<assays%200..*-++[Biochemical&#124;name:string;presence:string%20%3F;specificity:string%20%3F;notes:string%20%3F;context:string%20%3F;subtype:string%20%3F;synonyms:string%20*],[CellTypeDescriptor]<cell_types%200..*-++[Biochemical],[Any]<frequency%200..1-++[Biochemical],[EvidenceItem]<evidence%200..*-++[Biochemical],[Descriptor]<biomarker_term%200..1-++[Biochemical],[Disease]++-%20biochemical%200..*>[Biochemical],[Disease],[AssayDescriptor],[Any])

## Referenced by Class

 *  **None** *[biochemical](biochemical.md)*  <sub>0..\*</sub>  **[Biochemical](Biochemical.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [biomarker_term](biomarker_term.md)  <sub>0..1</sub>
     * Description: Ontology term for a biomarker (from NCIT, CHEBI, or LOINC)
     * Range: [Descriptor](Descriptor.md)
 * [presence](presence.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Positive None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [specificity](specificity.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: High None
 * [frequency](frequency.md)  <sub>0..1</sub>
     * Range: [Any](Any.md)
     * Example: Occasional None
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [context](context.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Pregnancy None
 * [subtype](subtype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Eyelid Myoclonia with Absences None
 * [cell_types](cell_types.md)  <sub>0..\*</sub>
     * Range: [CellTypeDescriptor](CellTypeDescriptor.md)
     * Example: [{preferred_term: Macrophage}, {preferred_term: T Cell}] None
 * [assays](assays.md)  <sub>0..\*</sub>
     * Range: [AssayDescriptor](AssayDescriptor.md)
     * Example: [{preferred_term: Elevated Blood Glucose}] None
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['CYFRA 21-1'] None
