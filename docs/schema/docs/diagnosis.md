
# Class: Diagnosis



URI: [dismech:Diagnosis](https://w3id.org/monarch-initiative/dismech/Diagnosis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[Diagnosis&#124;name:string;presence:string%20%3F;notes:string%20%3F;results:string%20%3F;markers:string%20%3F;description:string%20%3F],[TreatmentDescriptor]<diagnosis_term%200..1-++[Diagnosis],[Disease]++-%20diagnosis%200..*>[Diagnosis],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentDescriptor],[EvidenceItem],[EvidenceItem]<evidence%200..*-++[Diagnosis&#124;name:string;presence:string%20%3F;notes:string%20%3F;results:string%20%3F;markers:string%20%3F;description:string%20%3F],[TreatmentDescriptor]<diagnosis_term%200..1-++[Diagnosis],[Disease]++-%20diagnosis%200..*>[Diagnosis],[Disease])

## Referenced by Class

 *  **None** *[diagnosis](diagnosis.md)*  <sub>0..\*</sub>  **[Diagnosis](Diagnosis.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [diagnosis_term](diagnosis_term.md)  <sub>0..1</sub>
     * Description: The MAXO term for this diagnostic procedure
     * Range: [TreatmentDescriptor](TreatmentDescriptor.md)
 * [presence](presence.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Positive None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [results](results.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Identifies MEFV mutations None
 * [markers](markers.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: CRP, ESR, SAA None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
