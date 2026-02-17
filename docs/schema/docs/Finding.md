
# Class: Finding

A key finding or claim extracted from a publication

URI: [dismech:Finding](https://w3id.org/monarch-initiative/dismech/Finding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PublicationReference]++-%20findings%200..*>[Finding&#124;statement:string;supporting_text:string%20%3F],[PublicationReference])](https://yuml.me/diagram/nofunky;dir:TB/class/[PublicationReference]++-%20findings%200..*>[Finding&#124;statement:string;supporting_text:string%20%3F],[PublicationReference])

## Referenced by Class

 *  **None** *[findings](findings.md)*  <sub>0..\*</sub>  **[Finding](Finding.md)**

## Attributes


### Own

 * [statement](statement.md)  <sub>1..1</sub>
     * Description: A key finding or claim from the publication
     * Range: [String](types/String.md)
 * [supporting_text](supporting_text.md)  <sub>0..1</sub>
     * Description: Exact excerpt/quote from the publication supporting the statement
     * Range: [String](types/String.md)
