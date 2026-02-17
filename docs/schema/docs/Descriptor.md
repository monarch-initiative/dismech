
# Class: Descriptor

Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.

URI: [dismech:Descriptor](https://w3id.org/monarch-initiative/dismech/Descriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[TreatmentDescriptor],[Term],[SampleTypeDescriptor],[Qualifier],[PhenotypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EnvironmentDescriptor],[DiseaseDescriptor],[Qualifier]<qualifiers%200..*-++[Descriptor&#124;preferred_term:string;description:string%20%3F;modifier:ModifierEnum%20%3F;laterality:LateralityEnum%20%3F],[AnatomicalEntityDescriptor]<located_in%200..1-++[Descriptor],[Term]<term%200..1-++[Descriptor],[Biochemical]++-%20biomarker_term%200..1>[Descriptor],[Qualifier]++-%20predicate%200..1>[Descriptor],[Qualifier]++-%20value%200..1>[Descriptor],[Descriptor]^-[TriggerDescriptor],[Descriptor]^-[TreatmentDescriptor],[Descriptor]^-[SampleTypeDescriptor],[Descriptor]^-[PhenotypeDescriptor],[Descriptor]^-[OrganismDescriptor],[Descriptor]^-[GeneDescriptor],[Descriptor]^-[ExposureDescriptor],[Descriptor]^-[EnvironmentDescriptor],[Descriptor]^-[DiseaseDescriptor],[Descriptor]^-[ChemicalEntityDescriptor],[Descriptor]^-[CellularComponentDescriptor],[Descriptor]^-[CellTypeDescriptor],[Descriptor]^-[BiologicalProcessDescriptor],[Descriptor]^-[AssayDescriptor],[Descriptor]^-[AnatomicalEntityDescriptor],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[BiologicalProcessDescriptor],[Biochemical],[AssayDescriptor],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[TriggerDescriptor],[TreatmentDescriptor],[Term],[SampleTypeDescriptor],[Qualifier],[PhenotypeDescriptor],[OrganismDescriptor],[GeneDescriptor],[ExposureDescriptor],[EnvironmentDescriptor],[DiseaseDescriptor],[Qualifier]<qualifiers%200..*-++[Descriptor&#124;preferred_term:string;description:string%20%3F;modifier:ModifierEnum%20%3F;laterality:LateralityEnum%20%3F],[AnatomicalEntityDescriptor]<located_in%200..1-++[Descriptor],[Term]<term%200..1-++[Descriptor],[Biochemical]++-%20biomarker_term%200..1>[Descriptor],[Qualifier]++-%20predicate%200..1>[Descriptor],[Qualifier]++-%20value%200..1>[Descriptor],[Descriptor]^-[TriggerDescriptor],[Descriptor]^-[TreatmentDescriptor],[Descriptor]^-[SampleTypeDescriptor],[Descriptor]^-[PhenotypeDescriptor],[Descriptor]^-[OrganismDescriptor],[Descriptor]^-[GeneDescriptor],[Descriptor]^-[ExposureDescriptor],[Descriptor]^-[EnvironmentDescriptor],[Descriptor]^-[DiseaseDescriptor],[Descriptor]^-[ChemicalEntityDescriptor],[Descriptor]^-[CellularComponentDescriptor],[Descriptor]^-[CellTypeDescriptor],[Descriptor]^-[BiologicalProcessDescriptor],[Descriptor]^-[AssayDescriptor],[Descriptor]^-[AnatomicalEntityDescriptor],[ChemicalEntityDescriptor],[CellularComponentDescriptor],[CellTypeDescriptor],[BiologicalProcessDescriptor],[Biochemical],[AssayDescriptor],[AnatomicalEntityDescriptor])

## Children

 * [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md) - A descriptor for anatomical locations, bindable to UBERON
 * [AssayDescriptor](AssayDescriptor.md) - A descriptor for assays, bindable to OBI
 * [BiologicalProcessDescriptor](BiologicalProcessDescriptor.md) - A descriptor for biological processes, bindable to Gene Ontology (GO)
 * [CellTypeDescriptor](CellTypeDescriptor.md) - A descriptor for cell types, bindable to Cell Ontology (CL)
 * [CellularComponentDescriptor](CellularComponentDescriptor.md) - A descriptor for cellular components, bindable to GO cellular component
 * [ChemicalEntityDescriptor](ChemicalEntityDescriptor.md) - A descriptor for chemical entities, bindable to CHEBI
 * [DiseaseDescriptor](DiseaseDescriptor.md) - A descriptor for the focal disease, bindable to MONDO
 * [EnvironmentDescriptor](EnvironmentDescriptor.md) - A descriptor for environmental contexts/settings, bindable to ENVO
 * [ExposureDescriptor](ExposureDescriptor.md) - A descriptor for exposure events, bindable to ECTO or XCO
 * [GeneDescriptor](GeneDescriptor.md) - A descriptor for genes, bindable to HGNC or other gene databases
 * [OrganismDescriptor](OrganismDescriptor.md) - A descriptor for organisms, bindable to NCBITaxon
 * [PhenotypeDescriptor](PhenotypeDescriptor.md) - A descriptor for phenotypes, bindable to Human Phenotype Ontology (HP)
 * [SampleTypeDescriptor](SampleTypeDescriptor.md) - A descriptor for biological sample types (tissue and/or cell type)
 * [TreatmentDescriptor](TreatmentDescriptor.md) - A descriptor for treatments/medical actions, bindable to Medical Action Ontology (MAXO)
 * [TriggerDescriptor](TriggerDescriptor.md) - A descriptor for triggers/causes

## Referenced by Class

 *  **None** *[biomarker_term](biomarker_term.md)*  <sub>0..1</sub>  **[Descriptor](Descriptor.md)**
 *  **None** *[predicate](predicate.md)*  <sub>0..1</sub>  **[Descriptor](Descriptor.md)**
 *  **None** *[value](value.md)*  <sub>0..1</sub>  **[Descriptor](Descriptor.md)**

## Attributes


### Own

 * [preferred_term](preferred_term.md)  <sub>1..1</sub>
     * Description: The preferred human-readable term for this descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞description](Descriptor_description.md)  <sub>0..1</sub>
     * Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
     * Range: [String](types/String.md)
 * [term](term.md)  <sub>0..1</sub>
     * Description: Optional structured ontology term reference
     * Range: [Term](Term.md)
 * [modifier](modifier.md)  <sub>0..1</sub>
     * Description: Directional or qualitative modifier for a descriptor (e.g., increased, decreased, abnormal)
     * Range: [ModifierEnum](ModifierEnum.md)
 * [located_in](located_in.md)  <sub>0..1</sub>
     * Description: Anatomical location where this entity/process occurs or procedure is performed
     * Range: [AnatomicalEntityDescriptor](AnatomicalEntityDescriptor.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Description: Laterality qualifier (left, right, or bilateral)
     * Range: [LateralityEnum](LateralityEnum.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: List of predicate-value pairs for formal post-composition. Allows OWL-like expressivity with controlled predicates (e.g., RO relations) and values.
     * Range: [Qualifier](Qualifier.md)
