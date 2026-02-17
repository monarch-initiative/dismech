
# Class: DifferentialDiagnosis

A disease or condition that presents similarly to the focal disease and must be differentiated

URI: [dismech:DifferentialDiagnosis](https://w3id.org/monarch-initiative/dismech/DifferentialDiagnosis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Phenotype],[EvidenceItem],[DiseaseDescriptor],[DiseaseDescriptor]<disease_term%200..1-++[DifferentialDiagnosis&#124;name:string;description:string%20%3F;distinguishing_features:string%20*;notes:string%20%3F],[EvidenceItem]<evidence%200..*-++[DifferentialDiagnosis],[Phenotype]<phenotypes%200..*-++[DifferentialDiagnosis],[Disease]++-%20differential_diagnoses%200..*>[DifferentialDiagnosis],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Phenotype],[EvidenceItem],[DiseaseDescriptor],[DiseaseDescriptor]<disease_term%200..1-++[DifferentialDiagnosis&#124;name:string;description:string%20%3F;distinguishing_features:string%20*;notes:string%20%3F],[EvidenceItem]<evidence%200..*-++[DifferentialDiagnosis],[Phenotype]<phenotypes%200..*-++[DifferentialDiagnosis],[Disease]++-%20differential_diagnoses%200..*>[DifferentialDiagnosis],[Disease])

## Referenced by Class

 *  **None** *[differential_diagnoses](differential_diagnoses.md)*  <sub>0..\*</sub>  **[DifferentialDiagnosis](DifferentialDiagnosis.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [DifferentialDiagnosis➞description](DifferentialDiagnosis_description.md)  <sub>0..1</sub>
     * Description: Clinical or mechanistic overlaps, shared presentations, and diagnostic considerations with the focal disease
     * Range: [String](types/String.md)
 * [phenotypes](phenotypes.md)  <sub>0..\*</sub>
     * Range: [Phenotype](Phenotype.md)
 * [DifferentialDiagnosis➞distinguishing_features](DifferentialDiagnosis_distinguishing_features.md)  <sub>0..\*</sub>
     * Description: Key clinical, laboratory, imaging, or epidemiological features that help differentiate this condition from the focal disease
     * Range: [String](types/String.md)
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [DifferentialDiagnosis➞notes](DifferentialDiagnosis_notes.md)  <sub>0..1</sub>
     * Description: Additional clinical notes or management considerations
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [disease_term](disease_term.md)  <sub>0..1</sub>
     * Description: The MONDO disease term for this disease
     * Range: [DiseaseDescriptor](DiseaseDescriptor.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Documents diseases/conditions with overlapping clinical presentations |
|  | | Includes distinguishing features to help differentiate from the focal disease |
|  | | Essential for clinical diagnostic accuracy |
