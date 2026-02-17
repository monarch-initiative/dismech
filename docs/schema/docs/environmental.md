
# Class: Environmental

An environmental factor, exposure, or context relevant to disease

URI: [dismech:Environmental](https://w3id.org/monarch-initiative/dismech/Environmental)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureDescriptor],[EvidenceItem],[EnvironmentDescriptor]<environment_context%200..1-++[Environmental&#124;name:string;presence:string%20%3F;notes:string%20%3F;description:string%20%3F;chemicals:string%20*;synonyms:string%20*;effect:string%20%3F;examples:string%20*;review_notes:string%20%3F],[ExposureDescriptor]<exposure_term%200..1-++[Environmental],[EvidenceItem]<evidence%200..*-++[Environmental],[Disease]++-%20environmental%200..*>[Environmental],[EnvironmentDescriptor],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExposureDescriptor],[EvidenceItem],[EnvironmentDescriptor]<environment_context%200..1-++[Environmental&#124;name:string;presence:string%20%3F;notes:string%20%3F;description:string%20%3F;chemicals:string%20*;synonyms:string%20*;effect:string%20%3F;examples:string%20*;review_notes:string%20%3F],[ExposureDescriptor]<exposure_term%200..1-++[Environmental],[EvidenceItem]<evidence%200..*-++[Environmental],[Disease]++-%20environmental%200..*>[Environmental],[EnvironmentDescriptor],[Disease])

## Referenced by Class

 *  **None** *[environmental](environmental.md)*  <sub>0..\*</sub>  **[Environmental](Environmental.md)**

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
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [chemicals](chemicals.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Phenol'] None
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['CYFRA 21-1'] None
 * [effect](effect.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Potential trigger for flare-ups None
 * [examples](examples.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Kaposi Sarcoma'] None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [exposure_term](exposure_term.md)  <sub>0..1</sub>
     * Description: The ECTO/XCO term for this exposure event
     * Range: [ExposureDescriptor](ExposureDescriptor.md)
 * [environment_context](environment_context.md)  <sub>0..1</sub>
     * Description: The ENVO term for the environmental context/setting
     * Range: [EnvironmentDescriptor](EnvironmentDescriptor.md)
