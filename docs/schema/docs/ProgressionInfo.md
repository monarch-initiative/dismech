
# Class: ProgressionInfo



URI: [dismech:ProgressionInfo](https://w3id.org/monarch-initiative/dismech/ProgressionInfo)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[ProgressionInfo&#124;phase:PhaseTerm%20%3F;subtype:string%20%3F;age_range:string%20%3F;incubation_days:string%20%3F;review_notes:string%20%3F;incubation_years:string%20%3F;notes:string%20%3F;duration_days:string%20%3F;duration:string%20%3F],[Disease]++-%20progression%200..*>[ProgressionInfo],[EvidenceItem],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[EvidenceItem]<evidence%200..*-++[ProgressionInfo&#124;phase:PhaseTerm%20%3F;subtype:string%20%3F;age_range:string%20%3F;incubation_days:string%20%3F;review_notes:string%20%3F;incubation_years:string%20%3F;notes:string%20%3F;duration_days:string%20%3F;duration:string%20%3F],[Disease]++-%20progression%200..*>[ProgressionInfo],[EvidenceItem],[Disease])

## Referenced by Class

 *  **None** *[progression](progression.md)*  <sub>0..\*</sub>  **[ProgressionInfo](ProgressionInfo.md)**

## Attributes


### Own

 * [phase](phase.md)  <sub>0..1</sub>
     * Range: [PhaseTerm](PhaseTerm.md)
     * Example: Active TB None
 * [subtype](subtype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Eyelid Myoclonia with Absences None
 * [age_range](age_range.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Childhood-Adolescence None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [incubation_days](incubation_days.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: 3-14 None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [incubation_years](incubation_years.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: 2-15 None
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [duration_days](duration_days.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: 2-5 None
 * [duration](duration.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Variable None
