
# Class: ModelingConsideration



URI: [dismech:ModelingConsideration](https://w3id.org/monarch-initiative/dismech/ModelingConsideration)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[ModelingConsideration&#124;name:string;description:string%20%3F],[Disease]++-%20modeling_considerations%200..*>[ModelingConsideration],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[ModelingConsideration&#124;name:string;description:string%20%3F],[Disease]++-%20modeling_considerations%200..*>[ModelingConsideration],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[modeling_considerations](modeling_considerations.md)*  <sub>0..\*</sub>  **[ModelingConsideration](ModelingConsideration.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
