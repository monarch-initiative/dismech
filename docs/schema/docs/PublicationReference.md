
# Class: PublicationReference

A reference to a publication with associated findings

URI: [dismech:PublicationReference](https://w3id.org/monarch-initiative/dismech/PublicationReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Finding]<findings%200..*-++[PublicationReference&#124;reference:PMID;title:string%20%3F],[Disease]++-%20references%200..*>[PublicationReference],[Finding],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Finding]<findings%200..*-++[PublicationReference&#124;reference:PMID;title:string%20%3F],[Disease]++-%20references%200..*>[PublicationReference],[Finding],[Disease])

## Referenced by Class

 *  **None** *[references](references.md)*  <sub>0..\*</sub>  **[PublicationReference](PublicationReference.md)**

## Attributes


### Own

 * [PublicationReference➞reference](PublicationReference_reference.md)  <sub>1..1</sub>
     * Description: The authoritative reference (publication) for this evidence item
     * Range: [PMID](types/PMID.md)
     * Example: PMID:35533128 None
 * [title](title.md)  <sub>0..1</sub>
     * Description: Title of the publication
     * Range: [String](types/String.md)
 * [findings](findings.md)  <sub>0..\*</sub>
     * Description: Key findings or claims extracted from this reference
     * Range: [Finding](Finding.md)
