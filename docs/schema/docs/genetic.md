
# Class: Genetic



URI: [dismech:Genetic](https://w3id.org/monarch-initiative/dismech/Genetic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Inheritance],[Variant]<variants%200..*-++[Genetic&#124;name:string;presence:string%20%3F;association:string%20%3F;review_notes:string%20%3F;subtype:string%20%3F;features:string%20%3F;notes:string%20%3F;examples:string%20*],[Inheritance]<inheritance%200..*-++[Genetic],[Any]<frequency%200..1-++[Genetic],[EvidenceItem]<evidence%200..*-++[Genetic],[Disease]++-%20genetic%200..*>[Genetic],[EvidenceItem],[Disease],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variant],[Inheritance],[Variant]<variants%200..*-++[Genetic&#124;name:string;presence:string%20%3F;association:string%20%3F;review_notes:string%20%3F;subtype:string%20%3F;features:string%20%3F;notes:string%20%3F;examples:string%20*],[Inheritance]<inheritance%200..*-++[Genetic],[Any]<frequency%200..1-++[Genetic],[EvidenceItem]<evidence%200..*-++[Genetic],[Disease]++-%20genetic%200..*>[Genetic],[EvidenceItem],[Disease],[Any])

## Referenced by Class

 *  **None** *[genetic](genetic.md)*  <sub>0..\*</sub>  **[Genetic](Genetic.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [presence](presence.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Positive None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [association](association.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Susceptibility None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [subtype](subtype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Eyelid Myoclonia with Absences None
 * [frequency](frequency.md)  <sub>0..1</sub>
     * Range: [Any](Any.md)
     * Example: Occasional None
 * [inheritance](inheritance.md)  <sub>0..\*</sub>
     * Range: [Inheritance](Inheritance.md)
     * Example: Autosomal Dominant None
 * [variants](variants.md)  <sub>0..\*</sub>
     * Range: [Variant](Variant.md)
 * [features](features.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: DNA virus from the Orthopoxvirus genus None
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [examples](examples.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Kaposi Sarcoma'] None
