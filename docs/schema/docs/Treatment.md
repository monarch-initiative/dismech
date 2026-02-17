
# Class: Treatment



URI: [dismech:Treatment](https://w3id.org/monarch-initiative/dismech/Treatment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentDescriptor],[Mechanism]<mechanism%200..*-++[Treatment&#124;name:string;description:string%20%3F;target_phenotypes:string%20*;notes:string%20%3F;context:string%20%3F;review_notes:string%20%3F;role:string%20%3F;examples:string%20*],[EvidenceItem]<evidence%200..*-++[Treatment],[TreatmentDescriptor]<treatment_term%200..1-++[Treatment],[Disease]++-%20treatments%200..*>[Treatment],[Mechanism],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentDescriptor],[Mechanism]<mechanism%200..*-++[Treatment&#124;name:string;description:string%20%3F;target_phenotypes:string%20*;notes:string%20%3F;context:string%20%3F;review_notes:string%20%3F;role:string%20%3F;examples:string%20*],[EvidenceItem]<evidence%200..*-++[Treatment],[TreatmentDescriptor]<treatment_term%200..1-++[Treatment],[Disease]++-%20treatments%200..*>[Treatment],[Mechanism],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[treatments](treatments.md)*  <sub>0..\*</sub>  **[Treatment](Treatment.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [treatment_term](treatment_term.md)  <sub>0..1</sub>
     * Description: The MAXO term for this treatment/medical action
     * Range: [TreatmentDescriptor](TreatmentDescriptor.md)
 * [target_phenotypes](target_phenotypes.md)  <sub>0..\*</sub>
     * Description: Names of phenotypes that this treatment addresses or targets
     * Range: [String](types/String.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [context](context.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Pregnancy None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [role](role.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Primary None
 * [mechanism](mechanism.md)  <sub>0..\*</sub>
     * Range: [Mechanism](Mechanism.md)
 * [examples](examples.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Kaposi Sarcoma'] None
