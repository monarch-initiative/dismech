
# Class: Transmission



URI: [dismech:Transmission](https://w3id.org/monarch-initiative/dismech/Transmission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[Transmission&#124;name:string;description:string%20%3F;notes:string%20%3F;effect:string%20%3F],[Disease]++-%20transmission%200..*>[Transmission],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[Transmission&#124;name:string;description:string%20%3F;notes:string%20%3F;effect:string%20%3F],[Disease]++-%20transmission%200..*>[Transmission],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[transmission](transmission.md)*  <sub>0..\*</sub>  **[Transmission](Transmission.md)**

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
 * [effect](effect.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Potential trigger for flare-ups None
