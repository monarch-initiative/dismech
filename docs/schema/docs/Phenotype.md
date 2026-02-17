
# Class: Phenotype



URI: [dismech:Phenotype](https://w3id.org/monarch-initiative/dismech/Phenotype)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypeDescriptor],[EvidenceItem]<evidence%200..*-++[Phenotype&#124;category:string%20%3F;name:string;description:string%20%3F;diagnostic:boolean%20%3F;context:string%20%3F;review_notes:string%20%3F;severity:string%20%3F;notes:string%20%3F;subtype:string%20%3F],[CausalEdge]<sequelae%200..*-++[Phenotype],[Any]<frequency%200..1-++[Phenotype],[PhenotypeDescriptor]<phenotype_term%200..1-++[Phenotype],[DifferentialDiagnosis]++-%20phenotypes%200..*>[Phenotype],[Disease]++-%20phenotypes%200..*>[Phenotype],[EvidenceItem],[Disease],[DifferentialDiagnosis],[CausalEdge],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypeDescriptor],[EvidenceItem]<evidence%200..*-++[Phenotype&#124;category:string%20%3F;name:string;description:string%20%3F;diagnostic:boolean%20%3F;context:string%20%3F;review_notes:string%20%3F;severity:string%20%3F;notes:string%20%3F;subtype:string%20%3F],[CausalEdge]<sequelae%200..*-++[Phenotype],[Any]<frequency%200..1-++[Phenotype],[PhenotypeDescriptor]<phenotype_term%200..1-++[Phenotype],[DifferentialDiagnosis]++-%20phenotypes%200..*>[Phenotype],[Disease]++-%20phenotypes%200..*>[Phenotype],[EvidenceItem],[Disease],[DifferentialDiagnosis],[CausalEdge],[Any])

## Referenced by Class

 *  **None** *[phenotypes](phenotypes.md)*  <sub>0..\*</sub>  **[Phenotype](Phenotype.md)**

## Attributes


### Own

 * [category](category.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Hematologic None
 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [phenotype_term](phenotype_term.md)  <sub>0..1</sub>
     * Description: The HP term for this phenotype
     * Range: [PhenotypeDescriptor](PhenotypeDescriptor.md)
 * [frequency](frequency.md)  <sub>0..1</sub>
     * Range: [Any](Any.md)
     * Example: Occasional None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [diagnostic](diagnostic.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [sequelae](sequelae.md)  <sub>0..\*</sub>
     * Range: [CausalEdge](CausalEdge.md)
     * Example: [{target: Diabetic Ketoacidosis}, {target: Chronic Complications}] None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [context](context.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Pregnancy None
 * [review_notes](review_notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Added an additional clinically relevant subtype. None
 * [severity](severity.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Severe None
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [subtype](subtype.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Eyelid Myoclonia with Absences None
