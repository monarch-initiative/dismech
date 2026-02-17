
# Class: ExposureDescriptor

A descriptor for exposure events, bindable to ECTO or XCO

URI: [dismech:ExposureDescriptor](https://w3id.org/monarch-initiative/dismech/ExposureDescriptor)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[ExposureDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[Environmental]++-%20exposure_term%200..1>[ExposureDescriptor],[Dataset]++-%20exposures%200..*>[ExposureDescriptor],[Descriptor]^-[ExposureDescriptor],[Environmental],[Descriptor],[Dataset],[AnatomicalEntityDescriptor])](https://yuml.me/diagram/nofunky;dir:TB/class/[Term],[Qualifier],[Term]<term%200..1-++[ExposureDescriptor&#124;preferred_term(i):string;description(i):string%20%3F;modifier(i):ModifierEnum%20%3F;laterality(i):LateralityEnum%20%3F],[Environmental]++-%20exposure_term%200..1>[ExposureDescriptor],[Dataset]++-%20exposures%200..*>[ExposureDescriptor],[Descriptor]^-[ExposureDescriptor],[Environmental],[Descriptor],[Dataset],[AnatomicalEntityDescriptor])

## Parents

 *  is_a: [Descriptor](Descriptor.md) - Base class for structured descriptors that allow a preferred term, optional description, optional ontology term binding, and post-composition via modifier, located_in, and laterality slots.

## Referenced by Class

 *  **None** *[exposure_term](exposure_term.md)*  <sub>0..1</sub>  **[ExposureDescriptor](ExposureDescriptor.md)**
 *  **None** *[exposures](exposures.md)*  <sub>0..\*</sub>  **[ExposureDescriptor](ExposureDescriptor.md)**

## Attributes


### Own

 * [ExposureDescriptor➞term](ExposureDescriptor_term.md)  <sub>0..1</sub>
     * Description: Optional ECTO/XCO exposure term reference
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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | Use ECTO (Environmental Conditions, Treatments, and Exposures Ontology) for general exposures |
|  | | Use XCO (Experimental Conditions Ontology) for experimental exposure conditions |
