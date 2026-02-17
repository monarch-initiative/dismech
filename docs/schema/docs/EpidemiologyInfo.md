
# Class: EpidemiologyInfo



URI: [dismech:EpidemiologyInfo](https://w3id.org/monarch-initiative/dismech/EpidemiologyInfo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[EpidemiologyInfo&#124;name:string;description:string%20%3F;minimum_value:float%20%3F;maximum_value:float%20%3F;mean_range:string%20%3F;notes:string%20%3F;factors:string%20*;unit:string%20%3F],[Disease]++-%20epidemiology%200..*>[EpidemiologyInfo],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[EpidemiologyInfo&#124;name:string;description:string%20%3F;minimum_value:float%20%3F;maximum_value:float%20%3F;mean_range:string%20%3F;notes:string%20%3F;factors:string%20*;unit:string%20%3F],[Disease]++-%20epidemiology%200..*>[EpidemiologyInfo],[Disease])

## Referenced by Class

 *  **None** *[epidemiology](epidemiology.md)*  <sub>0..\*</sub>  **[EpidemiologyInfo](EpidemiologyInfo.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [minimum_value](minimum_value.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [maximum_value](maximum_value.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [mean_range](mean_range.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [factors](factors.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Genetic', 'Environmental', 'Infectious', 'Autoimmune', 'Metabolic', 'Neoplastic', 'Traumatic', 'Iatrogenic', 'Idiopathic'] None
 * [unit](unit.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: cm None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
