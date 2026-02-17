
# Class: EvidenceItem



URI: [dismech:EvidenceItem](https://w3id.org/monarch-initiative/dismech/EvidenceItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]++-%20evidence%200..*>[EvidenceItem&#124;reference:PMID%20%3F;supports:EvidenceItemSupportEnum%20%3F;snippet:string%20%3F;explanation:string%20%3F],[ComputationalModel]++-%20evidence%200..*>[EvidenceItem],[DifferentialDiagnosis]++-%20evidence%200..*>[EvidenceItem],[Subtype]++-%20evidence%200..*>[EvidenceItem],[CausalEdge]++-%20evidence%200..*>[EvidenceItem],[Prevalence]++-%20evidence%200..*>[EvidenceItem],[ProgressionInfo]++-%20evidence%200..*>[EvidenceItem],[EpidemiologyInfo]++-%20evidence%200..*>[EvidenceItem],[Pathophysiology]++-%20evidence%200..*>[EvidenceItem],[Phenotype]++-%20evidence%200..*>[EvidenceItem],[Biochemical]++-%20evidence%200..*>[EvidenceItem],[Genetic]++-%20evidence%200..*>[EvidenceItem],[Environmental]++-%20evidence%200..*>[EvidenceItem],[Stage]++-%20evidence%200..*>[EvidenceItem],[AnimalModel]++-%20evidence%200..*>[EvidenceItem],[Treatment]++-%20evidence%200..*>[EvidenceItem],[InfectiousAgent]++-%20evidence%200..*>[EvidenceItem],[Transmission]++-%20evidence%200..*>[EvidenceItem],[Diagnosis]++-%20evidence%200..*>[EvidenceItem],[Inheritance]++-%20evidence%200..*>[EvidenceItem],[Variant]++-%20evidence%200..*>[EvidenceItem],[ModelingConsideration]++-%20evidence%200..*>[EvidenceItem],[Variant],[Treatment],[Transmission],[Subtype],[Stage],[ProgressionInfo],[Prevalence],[Phenotype],[Pathophysiology],[ModelingConsideration],[Inheritance],[InfectiousAgent],[Genetic],[EpidemiologyInfo],[Environmental],[DifferentialDiagnosis],[Diagnosis],[Dataset],[ComputationalModel],[CausalEdge],[Biochemical],[AnimalModel])](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]++-%20evidence%200..*>[EvidenceItem&#124;reference:PMID%20%3F;supports:EvidenceItemSupportEnum%20%3F;snippet:string%20%3F;explanation:string%20%3F],[ComputationalModel]++-%20evidence%200..*>[EvidenceItem],[DifferentialDiagnosis]++-%20evidence%200..*>[EvidenceItem],[Subtype]++-%20evidence%200..*>[EvidenceItem],[CausalEdge]++-%20evidence%200..*>[EvidenceItem],[Prevalence]++-%20evidence%200..*>[EvidenceItem],[ProgressionInfo]++-%20evidence%200..*>[EvidenceItem],[EpidemiologyInfo]++-%20evidence%200..*>[EvidenceItem],[Pathophysiology]++-%20evidence%200..*>[EvidenceItem],[Phenotype]++-%20evidence%200..*>[EvidenceItem],[Biochemical]++-%20evidence%200..*>[EvidenceItem],[Genetic]++-%20evidence%200..*>[EvidenceItem],[Environmental]++-%20evidence%200..*>[EvidenceItem],[Stage]++-%20evidence%200..*>[EvidenceItem],[AnimalModel]++-%20evidence%200..*>[EvidenceItem],[Treatment]++-%20evidence%200..*>[EvidenceItem],[InfectiousAgent]++-%20evidence%200..*>[EvidenceItem],[Transmission]++-%20evidence%200..*>[EvidenceItem],[Diagnosis]++-%20evidence%200..*>[EvidenceItem],[Inheritance]++-%20evidence%200..*>[EvidenceItem],[Variant]++-%20evidence%200..*>[EvidenceItem],[ModelingConsideration]++-%20evidence%200..*>[EvidenceItem],[Variant],[Treatment],[Transmission],[Subtype],[Stage],[ProgressionInfo],[Prevalence],[Phenotype],[Pathophysiology],[ModelingConsideration],[Inheritance],[InfectiousAgent],[Genetic],[EpidemiologyInfo],[Environmental],[DifferentialDiagnosis],[Diagnosis],[Dataset],[ComputationalModel],[CausalEdge],[Biochemical],[AnimalModel])

## Referenced by Class

 *  **None** *[evidence](evidence.md)*  <sub>0..\*</sub>  **[EvidenceItem](EvidenceItem.md)**

## Attributes


### Own

 * [reference](reference.md)  <sub>0..1</sub>
     * Description: The authoritative reference (publication) for this evidence item
     * Range: [PMID](types/PMID.md)
     * Example: PMID:35533128 None
 * [supports](supports.md)  <sub>0..1</sub>
     * Range: [EvidenceItemSupportEnum](EvidenceItemSupportEnum.md)
     * Example: SUPPORT None
 * [snippet](snippet.md)  <sub>0..1</sub>
     * Description: An exact excerpt/quote from the referenced publication that supports or refutes the claim
     * Range: [String](types/String.md)
     * Example: At the moment there is no healing therapy, so early kidney transplant is a fundamental tool to improve prognosis. None
 * [explanation](explanation.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: There is no curative treatment for nephronophthisis, indicating that supportive care, including symptomatic treatment and monitoring, is currently applied to manage associated complications. None
