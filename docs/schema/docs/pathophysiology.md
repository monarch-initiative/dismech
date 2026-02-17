
# Class: Pathophysiology



URI: [dismech:Pathophysiology](https://w3id.org/monarch-initiative/dismech/Pathophysiology)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[Any]<frequency%200..1-++[Pathophysiology&#124;name:string;description:string%20%3F;examples:string%20*;role:string%20%3F;synonyms:string%20*;consequence:string%20%3F;consequences:string%20*;subtypes:string%20*;mechanisms:string%20*;notes:string%20%3F],[AssayDescriptor]<assays%200..*-++[Pathophysiology],[TriggerDescriptor]<triggers%200..*-++[Pathophysiology],[ChemicalEntityDescriptor]<chemical_entities%200..*-++[Pathophysiology],[CellularComponentDescriptor]<cellular_components%200..*-++[Pathophysiology],[GeneDescriptor]<genes%200..*-++[Pathophysiology],[CausalEdge]<downstream%200..*-++[Pathophysiology],[BiologicalProcessDescriptor]<pathways%200..*-++[Pathophysiology],[GeneDescriptor]<gene%200..1-++[Pathophysiology],[AnatomicalEntityDescriptor]<locations%200..*-++[Pathophysiology],[BiologicalProcessDescriptor]<biological_processes%200..*-++[Pathophysiology],[EvidenceItem]<evidence%200..*-++[Pathophysiology],[CellTypeDescriptor]<cell_types%200..*-++[Pathophysiology],[Disease]++-%20pathophysiology%200..*>[Pathophysiology],[Stage]++-%20pathophysiology%200..*>[Pathophysiology],[Stage],[GeneDescriptor],[EvidenceItem],[Disease],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[CausalEdge],[BiologicalProcessDescriptor],[AssayDescriptor],[Any],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[Any]<frequency%200..1-++[Pathophysiology&#124;name:string;description:string%20%3F;examples:string%20*;role:string%20%3F;synonyms:string%20*;consequence:string%20%3F;consequences:string%20*;subtypes:string%20*;mechanisms:string%20*;notes:string%20%3F],[AssayDescriptor]<assays%200..*-++[Pathophysiology],[TriggerDescriptor]<triggers%200..*-++[Pathophysiology],[ChemicalEntityDescriptor]<chemical_entities%200..*-++[Pathophysiology],[CellularComponentDescriptor]<cellular_components%200..*-++[Pathophysiology],[GeneDescriptor]<genes%200..*-++[Pathophysiology],[CausalEdge]<downstream%200..*-++[Pathophysiology],[BiologicalProcessDescriptor]<pathways%200..*-++[Pathophysiology],[GeneDescriptor]<gene%200..1-++[Pathophysiology],[AnatomicalEntityDescriptor]<locations%200..*-++[Pathophysiology],[BiologicalProcessDescriptor]<biological_processes%200..*-++[Pathophysiology],[EvidenceItem]<evidence%200..*-++[Pathophysiology],[CellTypeDescriptor]<cell_types%200..*-++[Pathophysiology],[Disease]++-%20pathophysiology%200..*>[Pathophysiology],[Stage]++-%20pathophysiology%200..*>[Pathophysiology],[Stage],[GeneDescriptor],[EvidenceItem],[Disease],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[CausalEdge],[BiologicalProcessDescriptor],[AssayDescriptor],[Any],[AnatomicalEntityDescriptor])

## Referenced by Class

 *  **None** *[pathophysiology](pathophysiology.md)*  <sub>0..\*</sub>  **[Pathophysiology](Pathophysiology.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
     * Example: Adolescent Nephronophthisis None
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [cell_types](cell_types.md)  <sub>0..\*</sub>
     * Range: [CellTypeDescriptor](CellTypeDescriptor.md)
     * Example: [{preferred_term: Macrophage}, {preferred_term: T Cell}] None
 * [evidence](evidence.md)  <sub>0..\*</sub>
     * Range: [EvidenceItem](EvidenceItem.md)
 * [biological_processes](biological_processes.md)  <sub>0..\*</sub>
     * Range: [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md)
     * Example: [{preferred_term: TNF-alpha Production}] None
 * [locations](locations.md)  <sub>0..\*</sub>
     * Range: [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md)
 * [examples](examples.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Kaposi Sarcoma'] None
 * [role](role.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Primary None
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['CYFRA 21-1'] None
 * [consequence](consequence.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Leads to abnormal sexual development and bone maturation. None
 * [consequences](consequences.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [gene](gene.md)  <sub>0..1</sub>
     * Range: [GeneDescriptor](GeneDescriptor.md)
     * Example: {preferred_term: MEFV} None
 * [pathways](pathways.md)  <sub>0..\*</sub>
     * Range: [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md)
     * Example: [{preferred_term: Wnt Pathway}] None
 * [downstream](downstream.md)  <sub>0..\*</sub>
     * Range: [CausalEdge](CausalEdge.md)
     * Example: [{target: Tissue Damage}] None
 * [genes](genes.md)  <sub>0..\*</sub>
     * Range: [GeneDescriptor](GeneDescriptor.md)
     * Example: [{preferred_term: HLA-DQ2}, {preferred_term: INS}] None
 * [subtypes](subtypes.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['DENV-1', 'DENV-2', 'DENV-3', 'DENV-4'] None
 * [cellular_components](cellular_components.md)  <sub>0..\*</sub>
     * Range: [CellularComponentDescriptor](CellularComponentDescriptor.md)
     * Example: [{preferred_term: Peroxisome}] None
 * [chemical_entities](chemical_entities.md)  <sub>0..\*</sub>
     * Range: [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md)
     * Example: [{preferred_term: Plasmalogen}] None
 * [triggers](triggers.md)  <sub>0..\*</sub>
     * Range: [TriggerDescriptor](TriggerDescriptor.md)
     * Example: [{preferred_term: Viral Infections}] None
 * [assays](assays.md)  <sub>0..\*</sub>
     * Range: [AssayDescriptor](AssayDescriptor.md)
     * Example: [{preferred_term: Elevated Blood Glucose}] None
 * [mechanisms](mechanisms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: ['Thrombocytopenia', 'Platelet Dysfunction', 'Disseminated Intravascular Coagulation (DIC)'] None
 * [notes](notes.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
     * Example: Contagious stage where symptoms appear and the bacteria can be spread to others. None
 * [frequency](frequency.md)  <sub>0..1</sub>
     * Range: [Any](Any.md)
     * Example: Occasional None
