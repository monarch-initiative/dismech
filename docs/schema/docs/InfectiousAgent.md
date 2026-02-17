
# Class: InfectiousAgent



URI: [dismech:InfectiousAgent](https://w3id.org/monarch-initiative/dismech/InfectiousAgent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subtype],[Subtype]<has_subtypes%200..*-++[InfectiousAgent&#124;name:string;description:string%20%3F],[EvidenceItem]<evidence%200..*-++[InfectiousAgent],[Disease]++-%20infectious_agent%200..*>[InfectiousAgent],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subtype],[Subtype]<has_subtypes%200..*-++[InfectiousAgent&#124;name:string;description:string%20%3F],[EvidenceItem]<evidence%200..*-++[InfectiousAgent],[Disease]++-%20infectious_agent%200..*>[InfectiousAgent],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[infectious_agent](infectious_agent.md)*  <sub>0..\*</sub>  **[InfectiousAgent](InfectiousAgent.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has_subtypes](has_subtypes.md)  <sub>0..\*</sub>
     * Range: [Subtype](Subtype.md)
