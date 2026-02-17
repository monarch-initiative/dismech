
# Class: DiseaseDescriptor

A descriptor for the focal disease, bindable to MONDO

URI: [dismech:DiseaseDescriptor](https://w3id.org/monarch-initiative/dismech/DiseaseDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[DiseaseDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[DifferentialDiagnosis]++-%20disease_term%200..1>[DiseaseDescriptor],[Disease]++-%20disease_term%200..1>[DiseaseDescriptor],[Subtype]++-%20subtype_term%200..1>[DiseaseDescriptor],[Descriptor]^-[DiseaseDescriptor],[Subtype],[Disease],[DifferentialDiagnosis],[Descriptor],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[DiseaseDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[DifferentialDiagnosis]++-%20disease_term%200..1>[DiseaseDescriptor],[Disease]++-%20disease_term%200..1>[DiseaseDescriptor],[Subtype]++-%20subtype_term%200..1>[DiseaseDescriptor],[Descriptor]^-[DiseaseDescriptor],[Subtype],[Disease],[DifferentialDiagnosis],[Descriptor],[AnatomicalEntityDescriptor])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.

## Referenced by Class

 *  **None** *[disease_term](disease_term.md)*  <sub>0..1</sub>  **[DiseaseDescriptor](DiseaseDescriptor.md)**
 *  **None** *[subtype_term](subtype_term.md)*  <sub>0..1</sub>  **[DiseaseDescriptor](DiseaseDescriptor.md)**

## Attributes


### Own

 * [DiseaseDescriptor➞term](DiseaseDescriptor_term.md)  <sub>0..1</sub>
     * Description: Optional MONDO disease term reference
     * Range: [Term](Term.md)

### Inherited from Descriptor:

 * [preferred_term](preferred_term.md)  <sub>1..1</sub>
     * Description: The preferred human-readable term for this descriptor
     * Range: [String](types/String.md)
 * [Descriptor➞description](Descriptor_description.md)  <sub>0..1</sub>
     * Description: A description of the descriptor. This may typically be redundant with the `term` object, but the description is more human-readable and may be used to communicate nuances not captured by the rigid standardization of the term object.
     * Range: [String](types/String.md)
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
