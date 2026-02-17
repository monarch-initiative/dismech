
# Class: GeneDescriptor

A descriptor for genes, bindable to HGNC or other gene databases

URI: [dismech:GeneDescriptor](https://w3id.org/monarch-initiative/dismech/GeneDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[GeneDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[Pathophysiology]++-%20gene%200..1>[GeneDescriptor],[Variant]++-%20gene%200..1>[GeneDescriptor],[Dataset]++-%20genes%200..*>[GeneDescriptor],[Pathophysiology]++-%20genes%200..*>[GeneDescriptor],[AnimalModel]++-%20genes%200..*>[GeneDescriptor],[ComputationalModel]++-%20perturbations%200..*>[GeneDescriptor],[Descriptor]^-[GeneDescriptor],[Variant],[Pathophysiology],[Descriptor],[Dataset],[ComputationalModel],[AnimalModel],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[GeneDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[Pathophysiology]++-%20gene%200..1>[GeneDescriptor],[Variant]++-%20gene%200..1>[GeneDescriptor],[Dataset]++-%20genes%200..*>[GeneDescriptor],[Pathophysiology]++-%20genes%200..*>[GeneDescriptor],[AnimalModel]++-%20genes%200..*>[GeneDescriptor],[ComputationalModel]++-%20perturbations%200..*>[GeneDescriptor],[Descriptor]^-[GeneDescriptor],[Variant],[Pathophysiology],[Descriptor],[Dataset],[ComputationalModel],[AnimalModel],[AnatomicalEntityDescriptor])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.

## Referenced by Class

 *  **None** *[gene](gene.md)*  <sub>0..1</sub>  **[GeneDescriptor](GeneDescriptor.md)**
 *  **None** *[genes](genes.md)*  <sub>0..\*</sub>  **[GeneDescriptor](GeneDescriptor.md)**
 *  **None** *[perturbations](perturbations.md)*  <sub>0..\*</sub>  **[GeneDescriptor](GeneDescriptor.md)**

## Attributes


### Own

 * [GeneDescriptor➞term](GeneDescriptor_term.md)  <sub>0..1</sub>
     * Description: Optional gene database term reference (e.g., HGNC)
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
