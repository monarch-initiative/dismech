
# Class: CurationEvent

A single curation event in the audit trail

URI: [dismech:CurationEvent](https://w3id.org/monarch-initiative/dismech/CurationEvent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Disease]++-%20curation_history%200..*>[CurationEvent&#124;curation_timestamp:datetime;curation_model:string%20%3F;curation_action:CurationActionEnum%20%3F;curation_description:string%20%3F],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Disease]++-%20curation_history%200..*>[CurationEvent&#124;curation_timestamp:datetime;curation_model:string%20%3F;curation_action:CurationActionEnum%20%3F;curation_description:string%20%3F],[Disease])

## Referenced by Class

 *  **None** *[curation_history](curation_history.md)*  <sub>0..\*</sub>  **[CurationEvent](CurationEvent.md)**

## Attributes


### Own

 * [CurationEvent➞curation_timestamp](CurationEvent_curation_timestamp.md)  <sub>1..1</sub>
     * Description: ISO 8601 timestamp of the curation event
     * Range: [Datetime](types/Datetime.md)
 * [curation_model](curation_model.md)  <sub>0..1</sub>
     * Description: Model identifier used for curation (e.g., claude-opus-4-5-20251101)
     * Range: [String](types/String.md)
 * [curation_action](curation_action.md)  <sub>0..1</sub>
     * Description: Type of curation action performed
     * Range: [CurationActionEnum](CurationActionEnum.md)
 * [curation_description](curation_description.md)  <sub>0..1</sub>
     * Description: Human-readable description of changes made
     * Range: [String](types/String.md)
