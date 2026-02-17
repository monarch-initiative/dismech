
# Class: Stage



URI: [dismech:Stage](https://w3id.org/monarch-initiative/dismech/Stage)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Stage]<substages%200..*-++[Stage&#124;name:string;description:string%20%3F;notes:string%20%3F;context:string%20%3F;review_notes:string%20%3F;role:string%20%3F;examples:string%20*],[Pathophysiology]<pathophysiology%200..*-++[Stage],[EvidenceItem]<evidence%200..*-++[Stage],[Disease]++-%20stages%200..*>[Stage],[Pathophysiology],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Stage]<substages%200..*-++[Stage&#124;name:string;description:string%20%3F;notes:string%20%3F;context:string%20%3F;review_notes:string%20%3F;role:string%20%3F;examples:string%20*],[Pathophysiology]<pathophysiology%200..*-++[Stage],[EvidenceItem]<evidence%200..*-++[Stage],[Disease]++-%20stages%200..*>[Stage],[Pathophysiology],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[stages](stages.md)*  <sub>0..\*</sub>  **[Stage](Stage.md)**
 *  **None** *[substages](substages.md)*  <sub>0..\*</sub>  **[Stage](Stage.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
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
 * [examples](examples.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Kaposi Sarcoma'] None
 * [pathophysiology](pathophysiology.md)  <sub>0..\*</sub>
     * Range: [Pathophysiology](Pathophysiology.md)
 * [substages](substages.md)  <sub>0..\*</sub>
     * Range: [Stage](Stage.md)
