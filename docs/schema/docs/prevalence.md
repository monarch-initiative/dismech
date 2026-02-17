
# Class: Prevalence



URI: [dismech:Prevalence](https://w3id.org/monarch-initiative/dismech/Prevalence)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[Prevalence&#124;subtype:string%20%3F;population:string%20%3F;notes:string%20%3F],[Any]<percentage%200..1-++[Prevalence],[Disease]++-%20prevalence%200..*>[Prevalence],[EvidenceItem],[Disease],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[Prevalence&#124;subtype:string%20%3F;population:string%20%3F;notes:string%20%3F],[Any]<percentage%200..1-++[Prevalence],[Disease]++-%20prevalence%200..*>[Prevalence],[EvidenceItem],[Disease],[Any])

## Referenced by Class

 *  **None** *[prevalence](prevalence.md)*  <sub>0..\*</sub>  **[Prevalence](Prevalence.md)**

## Attributes


### Own

 * [subtype](subtype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Eyelid Myoclonia with Absences None
 * [population](population.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Global None
 * [percentage](percentage.md)  <sub>0..1</sub>
     * Range: [Any](Any.md)
     * Example: 0.1 None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
