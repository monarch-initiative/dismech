
# Class: CausalEdge

A reference to a downstream effect or consequence in a causal relationship

URI: [dismech:CausalEdge](https://w3id.org/monarch-initiative/dismech/CausalEdge)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[CausalEdge&#124;target:string;description:string%20%3F],[Pathophysiology]++-%20downstream%200..*>[CausalEdge],[Phenotype]++-%20sequelae%200..*>[CausalEdge],[Phenotype],[Pathophysiology])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem],[EvidenceItem]<evidence%200..*-++[CausalEdge&#124;target:string;description:string%20%3F],[Pathophysiology]++-%20downstream%200..*>[CausalEdge],[Phenotype]++-%20sequelae%200..*>[CausalEdge],[Phenotype],[Pathophysiology])

## Referenced by Class

 *  **None** *[downstream](downstream.md)*  <sub>0..\*</sub>  **[CausalEdge](CausalEdge.md)**
 *  **None** *[sequelae](sequelae.md)*  <sub>0..\*</sub>  **[CausalEdge](CausalEdge.md)**

## Attributes


### Own

 * [target](target.md)  <sub>1..1</sub>
     * Description: The name of the target element in a causal relationship
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
