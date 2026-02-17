
# Class: Term

A structured reference to an ontology term

URI: [dismech:Term](https://w3id.org/monarch-initiative/dismech/Term)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[TreatmentDescriptor],[AnatomicalEntityDescriptor]++-%20term%200..1>[Term&#124;id:uriorcurie;label:string%20%3F],[AssayDescriptor]++-%20term%200..1>[Term],[BiologicalProcessDescriptor]++-%20term%200..1>[Term],[CellTypeDescriptor]++-%20term%200..1>[Term],[CellularComponentDescriptor]++-%20term%200..1>[Term],[ChemicalEntityDescriptor]++-%20term%200..1>[Term],[DiseaseDescriptor]++-%20term%200..1>[Term],[EnvironmentDescriptor]++-%20term%200..1>[Term],[ExposureDescriptor]++-%20term%200..1>[Term],[GeneDescriptor]++-%20term%200..1>[Term],[OrganismDescriptor]++-%20term%200..1>[Term],[PhenotypeDescriptor]++-%20term%200..1>[Term],[TreatmentDescriptor]++-%20term%200..1>[Term],[TriggerDescriptor]++-%20term%200..1>[Term],[Descriptor]++-%20term%200..1>[Term],[PhenotypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EnvironmentDescriptor],[DiseaseDescriptor],[Descriptor],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[BiologicalProcessDescriptor],[AssayDescriptor],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[TreatmentDescriptor],[AnatomicalEntityDescriptor]++-%20term%200..1>[Term&#124;id:uriorcurie;label:string%20%3F],[AssayDescriptor]++-%20term%200..1>[Term],[BiologicalProcessDescriptor]++-%20term%200..1>[Term],[CellTypeDescriptor]++-%20term%200..1>[Term],[CellularComponentDescriptor]++-%20term%200..1>[Term],[ChemicalEntityDescriptor]++-%20term%200..1>[Term],[DiseaseDescriptor]++-%20term%200..1>[Term],[EnvironmentDescriptor]++-%20term%200..1>[Term],[ExposureDescriptor]++-%20term%200..1>[Term],[GeneDescriptor]++-%20term%200..1>[Term],[OrganismDescriptor]++-%20term%200..1>[Term],[PhenotypeDescriptor]++-%20term%200..1>[Term],[TreatmentDescriptor]++-%20term%200..1>[Term],[TriggerDescriptor]++-%20term%200..1>[Term],[Descriptor]++-%20term%200..1>[Term],[PhenotypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EnvironmentDescriptor],[DiseaseDescriptor],[Descriptor],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[BiologicalProcessDescriptor],[AssayDescriptor],[AnatomicalEntityDescriptor])

## Referenced by Class

 *  **[AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md)** *[AnatomicalEntityDescriptor➞term](AnatomicalEntityDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[AssayDescriptor](AssayDescriptor.md)** *[AssayDescriptor➞term](AssayDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[BiologicalProcessDescriptor](BiologicalProcessDescriptor.md)** *[BiologicalProcessDescriptor➞term](BiologicalProcessDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[CellTypeDescriptor](CellTypeDescriptor.md)** *[CellTypeDescriptor➞term](CellTypeDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[CellularComponentDescriptor](CellularComponentDescriptor.md)** *[CellularComponentDescriptor➞term](CellularComponentDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[ChemicalEntityDescriptor](ChemicalEntityDescriptor.md)** *[ChemicalEntityDescriptor➞term](ChemicalEntityDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[DiseaseDescriptor](DiseaseDescriptor.md)** *[DiseaseDescriptor➞term](DiseaseDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[EnvironmentDescriptor](EnvironmentDescriptor.md)** *[EnvironmentDescriptor➞term](EnvironmentDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[ExposureDescriptor](ExposureDescriptor.md)** *[ExposureDescriptor➞term](ExposureDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[GeneDescriptor](GeneDescriptor.md)** *[GeneDescriptor➞term](GeneDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[OrganismDescriptor](OrganismDescriptor.md)** *[OrganismDescriptor➞term](OrganismDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[PhenotypeDescriptor](PhenotypeDescriptor.md)** *[PhenotypeDescriptor➞term](PhenotypeDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[TreatmentDescriptor](TreatmentDescriptor.md)** *[TreatmentDescriptor➞term](TreatmentDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **[TriggerDescriptor](TriggerDescriptor.md)** *[TriggerDescriptor➞term](TriggerDescriptor_term.md)*  <sub>0..1</sub>  **[Term](Term.md)**
 *  **None** *[term](term.md)*  <sub>0..1</sub>  **[Term](Term.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: Ontology term identifier (CURIE)
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [label](label.md)  <sub>0..1</sub>
     * Description: Human-readable label for the ontology term
     * Range: [String](types/String.md)
